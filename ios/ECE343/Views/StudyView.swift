import SwiftUI

/// Flashcards, quizzes and practice problems across every topic. Each topic's own page links to the same tools filtered to that topic.
struct StudyView: View {
    private let store = ContentStore.shared

    var body: some View {
        List {
            Section {
                NavigationLink {
                    WebScreen(title: "Flashcards", route: "cards")
                } label: {
                    StudyRow(title: "Flashcards", detail: "Flip through concepts and equations.", systemImage: "rectangle.on.rectangle.angled")
                }
                NavigationLink {
                    WebScreen(title: "Quiz", route: "quiz")
                } label: {
                    StudyRow(title: "Quiz", detail: "Multiple-choice questions with explanations.", systemImage: "checklist")
                }
                NavigationLink {
                    PracticeListView(topic: nil)
                } label: {
                    StudyRow(title: "Practice problems", detail: "\(store.problems.count) problems with hints and worked steps.", systemImage: "list.bullet.clipboard")
                }
            } footer: {
                Text("To study one topic, open it from the Topics tab.")
            }
        }
        .navigationTitle("Study")
    }
}

struct StudyRow: View {
    let title: String
    let detail: String
    let systemImage: String

    var body: some View {
        Label {
            VStack(alignment: .leading, spacing: 2) {
                Text(title).font(.headline)
                Text(detail).font(.subheadline).foregroundStyle(.secondary)
            }
        } icon: {
            Image(systemName: systemImage)
        }
        .padding(.vertical, 2)
    }
}

#Preview {
    NavigationStack { StudyView() }
}
