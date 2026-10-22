import SwiftUI

/// Every widget, grouped by the topic it belongs to.
struct WidgetsView: View {
    private let store = ContentStore.shared

    var body: some View {
        List {
            ForEach(store.availableTopics) { topic in
                let ids = store.widgetOrder.filter { store.widgets[$0]?.topic == topic.id }
                if !ids.isEmpty {
                    Section(topic.title) {
                        ForEach(ids, id: \.self) { id in
                            NavigationLink(store.widgetTitle(id)) { WidgetScreen(id: id) }
                        }
                    }
                }
            }
        }
        .navigationTitle("Widgets")
    }
}
