D = "2026-10-22"
def src(id, title, publisher, url, year=None, seen=False, note=None):
    d = {"id": id, "title": title, "publisher": publisher, "url": url, "accessed": D,
         "access_method": "seen-in-search-results" if seen else "not-opened",
         "verification_status": "verified" if seen else "needs_verification"}
    if year: d["year"] = year
    if note: d["note"] = note
    return d

DSM = lambda ch: src("src-dsm", f"DSM-5-TR, {ch} chapter", "American Psychiatric Association", "https://www.psychiatry.org/psychiatrists/practice/dsm", 2022, seen=True,
                     note="Chapter structure confirmed; the DSM text itself was not reproduced. Content is written in the project's own words.")
D = "2026-10-22"
NV = "needs_verification"
def c(cid, name, platform, url, ctype, audience, for_, topics, region, members=None, size_note="", notes="", safety="Peer support, not professional advice. Not a crisis service.", has_rules=None, mods=None, crisis=None, reviewer=""):
    return {"community_id": cid, "name": name, "platform": platform, "url": url, "type": ctype, "audience": audience, "for": for_, "topics": topics,
            "region": region, "language": "en", "cost": "free",
            "size": {"members": members, "as_of": D if members else None, "note": size_note},
            "last_activity_seen": None,
            "moderation": {"has_rules": has_rules, "active_mods": mods, "pins_crisis_resources": crisis, "notes": notes},
            "safety_notes": safety, "verification_status": NV, "verified_on": None,
            "reviewer_notes": "NOT OPENED: the build environment blocked outbound web access. URL and details were seen in search-engine results on " + D + ". " + reviewer}
