import json, sys, re, collections
import os, pathlib
ROOT = str(pathlib.Path(__file__).resolve().parents[2])
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from sources import SOURCES
from clinical import CLINICAL
from everyday import EVERYDAY
from treatment import TREATMENT
from rights import RIGHTS

ACCESSED = "2026-10-22"
tax = json.load(open(f"{ROOT}/data/taxonomy.json"))
topic_ids = {t["topic_id"] for c in tax["chapters"] for t in c["topics"]}

groups = [("clinical", CLINICAL), ("everyday", EVERYDAY), ("treatment", TREATMENT), ("rights", RIGHTS)]
all_ids = [r[0] for _, rows in groups for r in rows]
dupes = [i for i, n in collections.Counter(all_ids).items() if n > 1]
assert not dupes, f"duplicate term ids: {dupes}"
id_set = set(all_ids)

def src(key):
    title, pub, url, status = SOURCES[key]
    return {"title": title, "publisher": pub, "url": url, "accessed": ACCESSED,
            "access_method": "seen-in-search-results" if status == "seen" else "not-opened",
            "verification_status": "verified" if status == "seen" else "needs_verification"}

terms = []
problems = []
for group, rows in groups:
    for (tid, term, aka, is_dsm, defn, ex, mis, related, skeys) in rows:
        rel_topics, rel_terms = [], []
        for r in related:
            if r.endswith("-placeholder"):
                r2 = r[:-len("-placeholder")]
                if r2 in id_set: rel_terms.append(r2)
                else: problems.append(f"{tid}: unknown related term {r2}")
            elif r in topic_ids: rel_topics.append(r)
            elif r in id_set: rel_terms.append(r)
            else: problems.append(f"{tid}: unknown related topic {r}")
        for k in skeys:
            assert k in SOURCES, f"{tid}: unknown source {k}"
        d = collections.OrderedDict()
        d["term_id"] = tid; d["term"] = term; d["also_called"] = aka; d["group"] = group
        d["is_dsm_diagnosis"] = is_dsm
        d["plain_definition"] = defn; d["everyday_example"] = ex; d["common_misunderstanding"] = mis
        d["related_topics"] = rel_topics
        if rel_terms: d["related_terms"] = rel_terms
        d["sources"] = [src(k) for k in skeys]
        terms.append(d)

if problems:
    print("\n".join(problems)); sys.exit(1)

# stigma word scan (allowed only in entries that discuss the words themselves)
allowed = {"stigma-words","addiction-pop","suicide-loss-survivor","safe-messaging","narcissist-pop","ocd-as-adjective","bipolar-as-adjective","manipulative-label","lazy-label","attention-seeking","all-in-your-head","snap-out-of-it","main-character-energy","hearing-voices"}
pat = re.compile(r"\b(crazy|psycho|addicts?|suffers?|suffering from|committed suicide|lunatic|retarded|schizo)\b", re.I)
for t in terms:
    if t["term_id"] in allowed: continue
    blob = " ".join([t["term"], t["plain_definition"], t["everyday_example"], t["common_misunderstanding"]] + t["also_called"])
    m = pat.findall(blob)
    if m: print("STIGMA WORD", t["term_id"], m)

out = collections.OrderedDict()
out["generated_on"] = ACCESSED
out["notes"] = ("Plain-language glossary for the Mental-Health project. 'related_topics' are card topic_ids from data/taxonomy.json; 'related_terms' are other glossary term_ids. "
                "Source URLs marked needs_verification were not opened in this session because the build environment blocks outbound web access; they are well-known publisher pages and must be opened and confirmed before publication (see docs/qa-report.md).")
out["groups"] = {"clinical": "Clinical terms people meet", "everyday": "Everyday or popular terms (not DSM diagnoses)", "treatment": "Treatment and care words", "rights": "Rights and access words"}
out["totals"] = {"terms": len(terms), "by_group": dict(collections.Counter(t["group"] for t in terms))}
out["terms"] = terms
json.dump(out, open(f"{ROOT}/data/glossary.json", "w"), indent=2, ensure_ascii=False)
print(json.dumps(out["totals"]))
