"""Bundles data/ into preview/data/ so preview/index.html can be served as a static folder.
Run from the repository root after the other builds: python3 -I tools/build_preview.py
Then serve: python3 -m http.server --directory preview 8000  and open http://localhost:8000"""
import json, os
ROOT = os.path.join(os.path.dirname(__file__), "..")
OUT = os.path.join(ROOT, "preview", "data"); os.makedirs(OUT, exist_ok=True)
cards = {f[:-5]: json.load(open(os.path.join(ROOT, "data", "cards", f))) for f in sorted(os.listdir(os.path.join(ROOT, "data", "cards")))}
json.dump(cards, open(os.path.join(OUT, "cards.json"), "w"), ensure_ascii=False)
for f in ("taxonomy", "communities", "crisis-lines", "glossary", "design-tokens"):
    json.dump(json.load(open(os.path.join(ROOT, "data", f"{f}.json"))), open(os.path.join(OUT, f"{f}.json"), "w"), ensure_ascii=False)
print("preview data written:", len(cards), "cards")
