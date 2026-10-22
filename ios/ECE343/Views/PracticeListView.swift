import SwiftUI

/// Practice problems for one topic, or for every topic grouped by primary topic.
struct PracticeListView: View {
    let topic: Topic?
    @State private var source = "all"
    private let store = ContentStore.shared

    var body: some View {
        List {
            Section {
                Picker("Source", selection: $source) {
                    Text("All").tag("all")
                    Text("Course").tag("course")
                    Text("New").tag("original")
                }
                .pickerStyle(.segmented)
            }
            if let topic {
                Section { rows(problems(in: topic.id, primaryOnly: false)) }
            } else {
                ForEach(store.availableTopics) { t in
                    let list = problems(in: t.id, primaryOnly: true)
                    if !list.isEmpty {
                        Section(t.title) { rows(list) }
                    }
                }
            }
        }
        .navigationTitle(topic.map { "\($0.title) practice" } ?? "Practice")
        .navigationBarTitleDisplayMode(topic == nil ? .large : .inline)
    }

    private func problems(in id: String, primaryOnly: Bool) -> [Problem] {
        store.problems.filter { p in
            (primaryOnly ? p.topics.first == id : p.topics.contains(id)) && (source == "all" || p.source == source)
        }
    }

    private func rows(_ list: [Problem]) -> some View {
        ForEach(list) { p in
            NavigationLink {
                WebScreen(title: "Problem", route: "practice&id=\(p.id)")
            } label: {
                ProblemRow(problem: p)
            }
        }
    }
}

struct ProblemRow: View {
    let problem: Problem

    var body: some View {
        VStack(alignment: .leading, spacing: 3) {
            Text(problem.titleText)
            HStack(spacing: 6) {
                Text(problem.isCourse ? "Course" : "New")
                    .foregroundStyle(problem.isCourse ? Color.secondary : Color.accentColor)
                Text(String(repeating: "●", count: problem.difficulty) + String(repeating: "○", count: max(0, 3 - problem.difficulty)))
                    .foregroundStyle(.secondary)
                    .accessibilityLabel("Difficulty \(problem.difficulty) of 3")
            }
            .font(.caption)
        }
    }
}
