import Foundation

/// A course topic. Every card, problem, term and widget belongs to one or more topics.
struct Topic: Codable, Identifiable, Hashable {
    struct Counts: Codable, Hashable {
        let cards: Int
        let problems: Int
        let terms: Int
        let quiz: Int
    }

    let id: String
    let title: String
    let blurb: String
    let widgets: [String]
    let available: Bool
    let counts: Counts
}

struct WidgetInfo: Codable, Hashable {
    let title: String
    let topic: String
}

struct Problem: Codable, Identifiable, Hashable {
    let id: String
    let source: String
    let difficulty: Int
    /// The title with TeX turned into plain text, for native lists.
    let titleText: String
    let topics: [String]

    var isCourse: Bool { source == "course" }
}

/// Loads the content bundle that tools/build_web.py writes to web/www/content.json.
/// The full text (with TeX) is rendered by the web view; native screens only need titles and tags.
final class ContentStore {
    static let shared = ContentStore()

    let webRoot: URL
    let topics: [Topic]
    let widgets: [String: WidgetInfo]
    let problems: [Problem]

    private struct Payload: Decodable {
        let topics: [Topic]
        let widgets: [String: WidgetInfo]
        let problems: [Problem]
    }

    init(bundle: Bundle = .main) {
        guard let root = bundle.url(forResource: "www", withExtension: nil) else {
            fatalError("The web bundle (www/) is missing from the app.")
        }
        do {
            let data = try Data(contentsOf: root.appendingPathComponent("content.json"))
            let payload = try JSONDecoder().decode(Payload.self, from: data)
            webRoot = root
            topics = payload.topics
            widgets = payload.widgets
            problems = payload.problems
        } catch {
            fatalError("Could not read content.json: \(error)")
        }
    }

    var availableTopics: [Topic] { topics.filter(\.available) }

    func topic(_ id: String) -> Topic? { topics.first { $0.id == id } }

    /// Widget ids in topic order, without repeats.
    var widgetOrder: [String] {
        var seen = Set<String>()
        return availableTopics.flatMap(\.widgets).filter { seen.insert($0).inserted }
    }

    func widgetTitle(_ id: String) -> String { widgets[id]?.title ?? id }

    /// The page URL for a route such as "smith" or "practice&id=matching-02".
    /// Embed mode hides the page's own header and tabs, since the app supplies navigation.
    func pageURL(_ route: String) -> URL {
        URL(string: "index.html#\(route)&embed=1", relativeTo: webRoot)!.absoluteURL
    }
}
