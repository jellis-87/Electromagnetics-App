# ECE 343 Electromagnetics Companion

A phone-first companion app for ECE 343 (Intro to Electromagnetics): interactive visualization widgets, calculators, definitions, flashcards and practice problems. iPhone first, then Android. Standalone and offline.

## What's here

| Path | Contents |
| --- | --- |
| `widgets/ece343-widgets.html` | Working prototype of every widget plus the flashcard, practice and glossary viewers. Open it in a browser. |
| `widgets/build.py` | Embeds the JSON content into the prototype page. |
| `content/` | App content as JSON, shared by the iOS and Android builds. |
| `tools/` | Scripts that generate the content and compute every numeric answer. |

### Chapter 3: Transmission lines

Widgets: standing waves, line calculator, Smith chart (Z, Y, ZY), single-stub matching, transients and bounce diagrams, line parameters (coax geometry or R′L′G′C′).

Content: 46 flashcards, 31 glossary terms, 34 practice problems (16 from the course practice sets with worked keys, 18 new).

## Content format

Text fields hold inline TeX in `$...$` and display TeX in `$$...$$`. Answer `label`/`value` and glossary `symbol`/`units` fields are TeX without delimiters. The prototype renders math with MathJax 3 (SVG output); the native apps need a bundled math renderer to stay offline.

Each practice problem has `prompt`, `hints`, `steps`, `answers`, an optional `note` (used where the course key looks wrong), and `widget`, the id of the widget that explores it.

## Regenerating content

```sh
pip install numpy
python3 tools/make_ch03_practice.py
python3 tools/make_ch03_cards.py
python3 widgets/build.py
```

Never hand-edit numbers in `content/*.json`. Change the generator so the steps and answers stay consistent.

## Conventions

- Load at z = 0, source at z = −ℓ, as in the course.
- Lossless lines unless a widget says otherwise.
- Colors follow the NanoVNA trace colors used in the lab.
