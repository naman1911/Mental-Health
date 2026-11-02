# Mental-Health

Every DSM-5-TR topic explained in plain language (US grade 6–8 target), as card data for a static site, with each card linked to moderated peer communities and crisis lines.

## What is here

| Path | Contents |
|---|---|
| `data/taxonomy.json` | 25 chapters, 153 topics, folded variants, sensitivity levels |
| `data/cards/*.json` | 153 cards, one per topic (schema in `schemas/card.schema.json`) |
| `data/glossary.json` | 305 plain-language terms |
| `data/communities.json` | 143 moderated communities, helplines and resource hubs |
| `data/crisis-lines.json` | 55 crisis and support lines (US, UK, IE, CA, AU, IN) plus global directories |
| `data/design-tokens.json` | Pastel palette per chapter, light and dark, WCAG AA checked |
| `docs/` | Version check, design system, style guide, QA report, sources, exclusion log |
| `schemas/` | JSON Schemas for cards, glossary, communities, crisis lines |
| `tools/` | Python builders that generate and validate every data file (see `tools/README.md`) |
| `site/` | The website: a static single-page app over all of the above, deployed by `.github/workflows/pages.yml` |

## Status

Content is complete for all 153 topics. **Nothing has been verified by opening a source, community or helpline page**: the build environment had no outbound web access, so every entry is marked `needs_verification` with a note on what a reviewer must check. Read `docs/qa-report.md` before publishing anything.

## Build

```
python3 -I tools/build_taxonomy.py
python3 -I tools/glossary/build_glossary.py
python3 -I tools/cards/build_cards.py
python3 -I tools/build_crisis_lines.py
python3 -I tools/build_design_tokens.py
python3 -I tools/build_site.py
python3 -m http.server --directory site 8000
```

Requires Python 3 and `jsonschema`.

## Live site

Pushes to `main` run the Pages workflow and publish `site/`. To turn it on once: repository Settings → Pages → Source: GitHub Actions.
