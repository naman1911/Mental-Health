# Build tools

The JSON under `data/` is generated from the Python sources here so that every file validates and cross-references resolve.

```
python3 -I tools/build_taxonomy.py          # writes data/taxonomy.json
python3 -I tools/glossary/build_glossary.py # writes data/glossary.json (checks related_topics against the taxonomy)
python3 -I tools/cards/build_cards.py       # writes data/cards/*.json and data/communities.json
```

Requires `jsonschema` (`pip install jsonschema`). Run from the repository root. Each build script validates against the schemas in `schemas/`, enforces the length rules from the brief, scans for stigmatizing words, and computes a Flesch-Kincaid reading grade for each card.
