import SwiftUI

struct RootView: View {
    var body: some View {
        TabView {
            NavigationStack { TopicsView() }
                .tabItem { Label("Topics", systemImage: "square.grid.2x2") }
            NavigationStack { WidgetsView() }
                .tabItem { Label("Widgets", systemImage: "waveform.path.ecg") }
            NavigationStack { StudyView() }
                .tabItem { Label("Study", systemImage: "graduationcap") }
            NavigationStack { WebScreen(title: "Glossary", route: "glossary") }
                .tabItem { Label("Glossary", systemImage: "character.book.closed") }
        }
    }
}

#Preview {
    RootView()
}
