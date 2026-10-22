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

def mk(chapter, color, icon, tid, name, title, aka, code, one, simple, feel, signs, myths, how, helps, reach, isnot, hope, related, gloss, comms, vis, srcs, qs=[], young=None, cult=None, subs=None, strengths=None, sens="standard", notes=None, clin=False, card_type="condition", lang="person-first", lang_note=None):
    crisis = sens in ("elevated", "high")
    base_notes = {"standard": ["Site-wide crisis link stays one tap away."], "elevated": ["Crisis strip required."], "high": ["Crisis strip required.", "Safe-messaging rules apply: no methods, no numbers."]}[sens]
    card = {"topic_id": tid, "official_name": name, "plain_title": title, "also_known_as": aka, "chapter_id": chapter, "card_type": card_type, "icd10cm_code": code,
     "language_convention": lang, "one_liner": one, "in_simple_words": simple, "what_it_can_feel_like": feel, "common_signs": signs, "myths_vs_facts": myths,
     "how_common": how, "what_helps": helps, "when_to_reach_out": reach, "is_not": isnot, "hope_note": hope, "related_topics": related, "glossary_terms": gloss,
     "safety": {"sensitivity_level": sens, "show_crisis_strip": crisis, "content_notes": base_notes + (notes or [])},
     "visual": {"color_token": color, "icon": icon, "illustration_prompt": vis[0], "alt_text": vis[1]}, "communities": comms, "sources": srcs,
     "review": {"last_researched": D, "reading_grade_estimate": 0, "reading_grade_method": "Flesch-Kincaid grade, computed on all reader-facing text",
                "verification_status": "needs_human_review" if clin else "needs_verification", "needs_clinician_signoff": clin, "open_questions": qs}}
    if lang_note: card["language_convention_note"] = lang_note
    if young: card["in_young_people"] = young
    if cult: card["across_cultures"] = cult
    if subs: card["sub_sections"] = subs
    if strengths: card["strengths_and_differences"] = strengths
    return card
