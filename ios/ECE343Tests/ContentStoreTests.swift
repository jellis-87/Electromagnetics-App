import XCTest
@testable import ECE343

final class ContentStoreTests: XCTestCase {
    private let store = ContentStore.shared

    func testBundleLoads() {
        XCTAssertFalse(store.availableTopics.isEmpty)
        XCTAssertFalse(store.problems.isEmpty)
        XCTAssertTrue(store.availableTopics.allSatisfy { $0.counts.quiz > 0 })
        XCTAssertTrue(FileManager.default.fileExists(atPath: store.webRoot.appendingPathComponent("index.html").path))
        XCTAssertTrue(FileManager.default.fileExists(atPath: store.webRoot.appendingPathComponent("vendor/mathjax/tex-svg-full.js").path))
    }

    func testEveryTagPointsAtAKnownTopicAndWidget() {
        let ids = Set(store.topics.map(\.id))
        for p in store.problems {
            XCTAssertFalse(p.topics.isEmpty, p.id)
            XCTAssertTrue(Set(p.topics).isSubset(of: ids), p.id)
            XCTAssertFalse(p.titleText.contains("$"), p.id)
        }
        for t in store.topics {
            for w in t.widgets { XCTAssertNotNil(store.widgets[w], "\(t.id) lists unknown widget \(w)") }
        }
    }

    func testPageURLKeepsTheRoute() {
        let url = store.pageURL("practice&id=smith-01")
        XCTAssertEqual(url.lastPathComponent, "index.html")
        XCTAssertEqual(url.fragment, "practice&id=smith-01&embed=1")
    }
}
