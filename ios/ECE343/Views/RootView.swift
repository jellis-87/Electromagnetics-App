import SwiftUI

struct RootView: View {
    var body: some View {
        TabView {
            NavigationStack { TopicsView() }
                .tabItem { Label("Topics", systemImage: "square.grid.2x2") }
            NavigationStack { WidgetsView() }
                .tabItem { Label("Widgets", systemImage: "waveform.path.ecg") }
            NavigationStack { WebScreen(title: "Flashcards", route: "cards") }
                .tabItem { Label("Flashcards", systemImage: "rectangle.on.rectangle.angled") }
            NavigationStack { PracticeListView(topic: nil) }
                .tabItem { Label("Practice", systemImage: "list.bullet.clipboard") }
            NavigationStack { WebScreen(title: "Glossary", route: "glossary") }
                .tabItem { Label("Glossary", systemImage: "character.book.closed") }
        }
    }
}

#Preview {
    RootView()
}
