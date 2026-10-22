import SwiftUI
import WebKit

/// Shows one route of the bundled web page (a widget, a problem, the flashcards or the glossary).
/// The page asks the app to open a widget by posting {widget: id} to the "app" message handler.
struct WebPage: UIViewRepresentable {
    let route: String
    var onOpenWidget: (String) -> Void = { _ in }

    func makeCoordinator() -> Coordinator { Coordinator(onOpenWidget: onOpenWidget) }

    func makeUIView(context: Context) -> WKWebView {
        let config = WKWebViewConfiguration()
        config.userContentController.add(context.coordinator, name: "app")
        let view = WKWebView(frame: .zero, configuration: config)
        // Match the page background so there is no white flash before the page draws.
        view.isOpaque = false
        view.backgroundColor = UIColor(named: "PageBackground")
        view.scrollView.backgroundColor = UIColor(named: "PageBackground")
        view.scrollView.contentInsetAdjustmentBehavior = .never
        load(view)
        context.coordinator.route = route
        return view
    }

    func updateUIView(_ view: WKWebView, context: Context) {
        context.coordinator.onOpenWidget = onOpenWidget
        if context.coordinator.route != route {
            context.coordinator.route = route
            load(view)
        }
    }

    static func dismantleUIView(_ view: WKWebView, coordinator: Coordinator) {
        view.configuration.userContentController.removeScriptMessageHandler(forName: "app")
    }

    private func load(_ view: WKWebView) {
        let store = ContentStore.shared
        view.loadFileURL(store.pageURL(route), allowingReadAccessTo: store.webRoot)
    }

    @MainActor
    final class Coordinator: NSObject, WKScriptMessageHandler {
        var onOpenWidget: (String) -> Void
        var route = ""

        init(onOpenWidget: @escaping (String) -> Void) {
            self.onOpenWidget = onOpenWidget
        }

        func userContentController(_ controller: WKUserContentController, didReceive message: WKScriptMessage) {
            guard let body = message.body as? [String: Any], let id = body["widget"] as? String,
                  ContentStore.shared.widgets[id] != nil else { return }
            onOpenWidget(id)
        }
    }
}

struct WidgetLink: Identifiable, Hashable {
    let id: String
}

/// A web route with a title; widgets the page asks for are pushed on the navigation stack.
struct WebScreen: View {
    let title: String
    let route: String
    @State private var widget: WidgetLink?

    var body: some View {
        WebPage(route: route) { widget = WidgetLink(id: $0) }
            .background(Color("PageBackground"))
            .navigationTitle(title)
            .navigationBarTitleDisplayMode(.inline)
            .navigationDestination(item: $widget) { WidgetScreen(id: $0.id) }
    }
}

struct WidgetScreen: View {
    let id: String

    var body: some View {
        WebScreen(title: ContentStore.shared.widgetTitle(id), route: id)
    }
}
