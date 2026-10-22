# ECE 343 Electromagnetics Companion

A phone-first companion app for ECE 343 (Intro to Electromagnetics): interactive visualization widgets, calculators, definitions, flashcards and practice problems, organized by topic. iPhone first, then Android. Standalone and offline.

## What's here

| Path | Contents |
| --- | --- |
| `ios/` | The iPhone app (SwiftUI). `project.yml` is the XcodeGen spec; the Xcode project is generated from it. |
| `web/widgets.html` | Every widget plus the flashcard, practice and glossary viewers in one page. Open it in a browser; it is also published as the Widget Bench preview. |
| `web/www/` | The same page packaged for the app: `index.html`, `content.json`, and offline copies of MathJax and the fonts in `vendor/`. Generated; do not edit. |
| `content/` | App content as JSON, shared by the iOS and Android builds. `topics.json` lists the topics; each unit folder holds flashcards, practice problems and glossary terms. |
| `tools/` | Scripts that generate the content, compute every numeric answer, and build the web bundle. |

## Topics

Everything is labeled by topic, not by textbook chapter. Each card, problem and term has a `topics` list; the first entry is its primary topic.

| Topic | Widgets |
| --- | --- |
| Transmission lines | Line calculator, Line parameters |
| Reflection and standing waves | Standing waves, Line calculator |
| Smith chart | Smith chart (Z, Y, ZY) |
| Impedance matching | Stub matching, Smith chart |
| Transients | Bounce diagram |

Fields and phasors, vector calculus, electrostatics, current and conductors, magnetostatics, time-varying fields, plane waves, polarization and reflection at boundaries are listed in `topics.json` as coming later.

Content so far: 46 flashcards, 31 glossary terms, 34 practice problems (16 from the course practice sets with worked keys, 18 new).

## The iPhone app

Native SwiftUI screens handle navigation: Topics, Widgets, Flashcards, Practice and Glossary tabs. Widgets, problem pages, flashcards and the glossary render in a `WKWebView` that loads the bundled `web/www/index.html` with a route in the URL fragment, for example `#smith&embed=1`, `#practice&id=matching-02&embed=1` or `#cards&topic=transients&embed=1`. Embed mode hides the page's own header and tabs. When a page wants to open a widget it posts `{widget: id}` to the `app` message handler and the app pushes that widget.

Building needs a Mac with Xcode 16 or later:

```sh
brew install xcodegen
cd ios
xcodegen generate
open ECE343.xcodeproj
```

Pick an iPhone simulator and run. To run on a real phone, set your team under Signing & Capabilities. CI builds the app and runs the unit tests on a macOS runner for every pull request.

## Content format

Text fields hold inline TeX in `$...$` and display TeX in `$$...$$`. Answer `label`/`value` and glossary `symbol`/`units` fields are TeX without delimiters. Pages render math with MathJax 3 (SVG output), loaded from the bundled copy when offline.

Each practice problem has `prompt`, `hints`, `steps`, `answers`, `topics`, an optional `note` (used where the course key looks wrong), and `widget`, the id of the widget that explores it.

## Regenerating content

```sh
pip install numpy
python3 tools/make_tlines_practice.py
python3 tools/make_tlines_cards.py
python3 tools/build_web.py      # rebuilds web/widgets.html and web/www/
python3 tools/vendor_web.py     # only when updating MathJax or the fonts (needs npm)
```

Never hand-edit numbers in `content/`. Change the generator so the steps and answers stay consistent. CI fails if `web/` is out of date with `content/`.

## Conventions

- Load at z = 0, source at z = −ℓ, as in the course.
- Lossless lines unless a widget says otherwise.
- Colors follow the NanoVNA trace colors used in the lab.

## Licenses

MathJax is Apache-2.0. Archivo, Source Sans 3 and IBM Plex Mono are SIL OFL 1.1. Their license files are in `web/www/vendor/`.
