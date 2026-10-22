import json, sys, collections, re
import os, pathlib
ROOT = str(pathlib.Path(__file__).resolve().parents[2])
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from readability import fk_grade, card_text
import importlib.util, glob, os
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
def load_all(sub, attr):
    out = []
    for f in sorted(glob.glob(str(HERE / sub / "*.py"))):
        spec = importlib.util.spec_from_file_location(f"{sub}_{os.path.basename(f)[:-3]}", f)
        mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
        out += getattr(mod, attr)
    return out
CARDS = load_all("chapters", "CARDS")
COMMUNITIES = load_all("communities", "COMMUNITIES")
import jsonschema

tax = json.load(open(f"{ROOT}/data/taxonomy.json"))
topic_ids = {t["topic_id"]: (c["chapter_id"], t) for c in tax["chapters"] for t in c["topics"]}
gl = json.load(open(f"{ROOT}/data/glossary.json"))
term_ids = {t["term_id"] for t in gl["terms"]}
comm_ids = {c["community_id"] for c in COMMUNITIES}
card_schema = json.load(open(f"{ROOT}/schemas/card.schema.json"))
comm_schema = json.load(open(f"{ROOT}/schemas/community.schema.json"))

STIGMA = re.compile(r"\b(crazy|psycho|addicts?|suffers?|suffering from|committed suicide|lunatic|retarded|schizo|anorexic|an? bipolar)\b", re.I)
problems = []
def words(s): return len(re.findall(r"\S+", s))
# Every card gets at least three communities: general, moderated, multi-region fallbacks are appended
# when a chapter file lists fewer (brief section 4: 3-8 per card). Order is region-balanced US / UK / AU.
FALLBACK = ["nami-connection-and-helpline", "mind-side-by-side", "sane-forums-australia"]
import importlib.util as _ilu
_spec = _ilu.spec_from_file_location("community_links", f"{ROOT}/tools/cards/community_links.py"); _m = _ilu.module_from_spec(_spec); _spec.loader.exec_module(_m)
EXTRA = _m.EXTRA
for card in CARDS:
    tid = card["topic_id"]
    assert tid in topic_ids, tid
    for x in EXTRA.get(tid, []):
        if x not in card["communities"]: card["communities"].append(x)
    for fb in FALLBACK:
        if len(card["communities"]) >= 3: break
        if fb not in card["communities"]: card["communities"].append(fb)
    ch, t = topic_ids[tid]
    if card["chapter_id"] != ch: problems.append(f"{tid}: chapter mismatch")
    if words(card["one_liner"]) > 20: problems.append(f"{tid}: one_liner {words(card['one_liner'])} words")
    if words(card["in_simple_words"]) > 80: problems.append(f"{tid}: in_simple_words {words(card['in_simple_words'])} words")
    for s in card["common_signs"]:
        if words(s) > 15: problems.append(f"{tid}: sign too long: {s}")
    for r in card["related_topics"]:
        if r not in topic_ids: problems.append(f"{tid}: unknown related topic {r}")
    for g in card["glossary_terms"]:
        if g not in term_ids: problems.append(f"{tid}: unknown glossary term {g}")
    for cm in card["communities"]:
        if cm not in comm_ids: problems.append(f"{tid}: unknown community {cm}")
    refs = {s["id"] for s in card["sources"]}
    if card["how_common"]["source_ref"] not in refs: problems.append(f"{tid}: how_common source_ref missing")
    for g in card["what_helps"].get("guideline_refs", []):
        if g not in refs: problems.append(f"{tid}: guideline_ref {g} missing")
    txt = card_text(card)
    m = STIGMA.findall(txt)
    if m: problems.append(f"{tid}: stigma words {m}")
    if card["safety"]["sensitivity_level"] == "high" and re.search(r"\b\d+(\.\d+)?\s*(kg|lb|lbs|pounds|kilos|calories|kcal|bmi)\b", txt, re.I):
        problems.append(f"{tid}: numeric weight/calorie content on high-sensitivity card")
    card["review"]["reading_grade_estimate"] = fk_grade(txt)
    try:
        jsonschema.Draft202012Validator(card_schema).validate(card)
    except jsonschema.ValidationError as e:
        problems.append(f"{tid}: schema: {e.message[:120]} at {list(e.path)}")
    with open(f"{ROOT}/data/cards/{tid}.json", "w") as f:
        json.dump(card, f, indent=2, ensure_ascii=False)

for cm in COMMUNITIES:
    for tp in cm["topics"]:
        if tp not in topic_ids: problems.append(f"community {cm['community_id']}: unknown topic {tp}")
comm_doc = {"generated_on": "2026-10-22",
  "notes": "Community directory. verification_status 'verified' requires every check in section 7.1 of the brief to have been performed by opening the community. In this session the build environment blocked outbound web access, so every entry is 'needs_verification' with reviewer_notes describing what was seen in search results and what remains to be checked.",
  "communities": COMMUNITIES}
jsonschema.Draft202012Validator(comm_schema).validate(comm_doc)
json.dump(comm_doc, open(f"{ROOT}/data/communities.json", "w"), indent=2, ensure_ascii=False)

if problems:
    print("\n".join(problems)); sys.exit(1)
for card in CARDS:
    print(f"{card['topic_id']:<32} grade={card['review']['reading_grade_estimate']:>4}  words(simple)={words(card['in_simple_words'])}  sens={card['safety']['sensitivity_level']}  comms={len(card['communities'])}")
print("communities:", len(COMMUNITIES))
