import SwiftUI

struct TopicsView: View {
    private let store = ContentStore.shared

    var body: some View {
        List {
            Section("Topics") {
                ForEach(store.availableTopics) { topic in
                    NavigationLink(value: topic) { TopicRow(topic: topic) }
                }
            }
            Section("Coming later") {
                ForEach(store.topics.filter { !$0.available }) { topic in
                    TopicRow(topic: topic).foregroundStyle(.secondary)
                }
            }
        }
        .navigationTitle("ECE 343")
        .navigationDestination(for: Topic.self) { TopicDetailView(topic: $0) }
    }
}

struct TopicRow: View {
    let topic: Topic

    var body: some View {
        VStack(alignment: .leading, spacing: 3) {
            Text(topic.title).font(.headline)
            Text(topic.blurb).font(.subheadline).foregroundStyle(.secondary)
            if topic.available {
                Text(summary).font(.caption).foregroundStyle(.tint)
            }
        }
        .padding(.vertical, 2)
    }

    private var summary: String {
        let c = topic.counts
        let widgets = topic.widgets.count
        return "\(widgets) widget\(widgets == 1 ? "" : "s") · \(c.cards) cards · \(c.problems) problems"
    }
}

struct TopicDetailView: View {
    let topic: Topic
    private let store = ContentStore.shared

    var body: some View {
        List {
            Section { Text(topic.blurb) }
            Section("Widgets") {
                ForEach(topic.widgets, id: \.self) { id in
                    NavigationLink(store.widgetTitle(id)) { WidgetScreen(id: id) }
                }
            }
            Section("Study") {
                NavigationLink {
                    WebScreen(title: "Flashcards", route: "cards&topic=\(topic.id)")
                } label: {
                    LabeledContent("Flashcards", value: "\(topic.counts.cards)")
                }
                NavigationLink {
                    PracticeListView(topic: topic)
                } label: {
                    LabeledContent("Practice problems", value: "\(topic.counts.problems)")
                }
                NavigationLink {
                    WebScreen(title: "Glossary", route: "glossary&topic=\(topic.id)")
                } label: {
                    LabeledContent("Glossary", value: "\(topic.counts.terms)")
                }
            }
        }
        .navigationTitle(topic.title)
    }
}
