# Build tools

The JSON under `data/` is generated from the Python sources here so that every file validates and cross-references resolve.

```
python3 -I tools/build_taxonomy.py          # writes data/taxonomy.json
python3 -I tools/glossary/build_glossary.py # writes data/glossary.json (checks related_topics against the taxonomy)
python3 -I tools/cards/build_cards.py       # writes data/cards/*.json and data/communities.json
python3 -I tools/build_crisis_lines.py      # writes data/crisis-lines.json
python3 -I tools/build_design_tokens.py     # writes data/design-tokens.json (WCAG-checked)
python3 -I tools/build_preview.py           # bundles data/ into preview/data/ for the static preview page
```

Requires `jsonschema` (`pip install jsonschema`). Run from the repository root. Each build script validates against the schemas in `schemas/`, enforces the length rules from the brief, scans for stigmatizing words, and computes a Flesch-Kincaid reading grade for each card.

## Preview

`preview/index.html` is a static, dependency-free page that renders every card, the community directory, crisis lines, glossary and design tokens from the bundled JSON. After building, serve the folder (`python3 -m http.server --directory preview 8000`) and open http://localhost:8000. It follows the card anatomy in `docs/design-system.md` and is a working preview, not the production site.
