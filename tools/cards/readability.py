import re
def syllables(word):
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w: return 0
    if len(w) <= 3: return 1
    w = re.sub(r"(?:[^laeiouy]es|ed|[^laeiouy]e)$", "", w)
    w = re.sub(r"^y", "", w)
    groups = re.findall(r"[aeiouy]{1,2}", w)
    return max(1, len(groups))
def fk_grade(text):
    sents = [s for s in re.split(r"[.!?]+", text) if s.strip()]
    words = re.findall(r"[A-Za-z][A-Za-z'\-]*", text)
    if not sents or not words: return 0.0
    syl = sum(syllables(w) for w in words)
    return round(0.39 * (len(words) / len(sents)) + 11.8 * (syl / len(words)) - 15.59, 1)
def card_text(card):
    parts = [card["one_liner"], card["in_simple_words"], card["when_to_reach_out"], card["is_not"], card["hope_note"],
             card["what_helps"]["plain_summary"], card["how_common"]["plain"]]
    parts += card["what_it_can_feel_like"] + card["common_signs"]
    parts += [m["myth"] + " " + m["fact"] for m in card["myths_vs_facts"]]
    for k in ("in_young_people", "across_cultures", "strengths_and_differences"):
        if k in card: parts.append(card[k])
    return " ".join(parts)
