from helpers import D, src, DSM
CARDS = []

# Generalized Anxiety Disorder ----------
CARDS.append({
 "topic_id": "generalized-anxiety-disorder",
 "official_name": "Generalized Anxiety Disorder",
 "plain_title": "When worry won't switch off",
 "also_known_as": ["GAD", "generalised anxiety disorder (UK spelling)"],
 "chapter_id": "anxiety", "card_type": "condition", "icd10cm_code": "F41.1",
 "language_convention": "person-first",
 "language_convention_note": "'A person with GAD' or 'someone who has anxiety'. Most anxiety organizations use person-first language.",
 "one_liner": "Worry that is hard to control, about many everyday things, most days, for months on end.",
 "in_simple_words": "Everyone worries sometimes. With GAD, the worry is bigger than the situation, jumps from topic to topic, and is very hard to turn off even when you know it is 'too much'. It often shows up in the body too: tight muscles, tiredness, poor sleep. It is common, it is not your fault, and it responds well to treatment.",
 "what_it_can_feel_like": [
  "My brain runs 'what if' scenarios all day, and I can't find the off switch.",
  "I'm exhausted but I can't relax. Even good news comes with a new worry.",
  "People say 'stop stressing' as if I haven't tried."
 ],
 "common_signs": [
  "Worrying a lot about everyday things: health, money, family, school, work",
  "Feeling restless, keyed up, or on edge much of the time",
  "Getting tired easily, or finding it hard to concentrate",
  "Tense muscles, headaches, or an upset stomach",
  "Trouble falling or staying asleep because of worry"
 ],
 "myths_vs_facts": [
  {"myth": "It's just being a worrier. Snap out of it.", "fact": "GAD is a recognized health condition. Willpower alone doesn't fix it, but treatment helps most people."},
  {"myth": "If I were stronger, I wouldn't feel like this.", "fact": "Anxiety has nothing to do with strength. It's a stuck alarm system, and it can be reset."},
  {"myth": "Medication is the only answer.", "fact": "Talking therapies, especially CBT, are first-line treatments. Medication is one option among several."}
 ],
 "how_common": {
  "plain": "About 3 in every 100 adults in the US have GAD in a given year, and about 6 in 100 at some point in their lives. Women are affected more often than men.",
  "figure": "2.7% past-year and 5.7% lifetime prevalence among US adults (NCS-R, 2001–2003)",
  "source_ref": "src-nimh-stats",
  "note": "US figures from an older survey; rates in other countries vary. UK and Australian surveys give broadly similar past-year figures, to be added when verified."
 },
 "what_helps": {
  "plain_summary": "Talking therapies, especially CBT (cognitive behavioural therapy, which helps you change the worry habit), help many people. Guided self-help and courses are often the first step. Some people also take an antidepressant, prescribed and monitored by a doctor. Sleep, movement, and cutting back on caffeine and alcohol support recovery.",
  "evidence_based_options": [
   "Cognitive behavioural therapy (CBT), in person or online",
   "Applied relaxation (a structured relaxation training)",
   "Guided self-help or a psychoeducation course as a first step",
   "An SSRI or SNRI antidepressant, prescribed and monitored by a doctor"
  ],
  "self_help_that_supports_care": [
   "A set 'worry time' each day, so worry has a slot instead of the whole day",
   "Slow breathing and grounding exercises when the body is tense",
   "Regular sleep, daily movement, and less caffeine",
   "Writing worries down and sorting them into 'can act on' and 'can't control'"
  ],
  "guideline_refs": ["src-nice-cg113"]
 },
 "when_to_reach_out": "If worry has been getting in the way of sleep, work, school, or relationships for several weeks, it is worth talking to a doctor or therapist. You don't need to be 'bad enough'; early help works best.",
 "is_not": "Feeling anxious before an exam, a date, or a big decision is normal and passes. GAD is ongoing worry about many things that doesn't match the situation and doesn't let up for months. A panic attack is also different: a sudden surge of fear that peaks in minutes.",
 "hope_note": "Most people with GAD feel much better with the right support, and many learn skills that help for life.",
 "in_young_people": "Children and teens with GAD often worry about school, being on time, doing things perfectly, or bad things happening to family. It can look like needing lots of reassurance, stomach aches, or refusing to go to school.",
 "across_cultures": "Anxiety is often felt and described through the body first: headaches, chest tightness, stomach trouble. In many cultures people see a doctor for the physical symptoms long before anyone mentions worry. Both are real and both count.",
 "related_topics": ["panic-disorder", "social-anxiety-disorder", "major-depressive-disorder", "insomnia-disorder", "adjustment-disorders"],
 "glossary_terms": ["rumination", "catastrophizing", "cbt", "ssri", "panic-attack", "stress", "avoidance"],
 "safety": {"sensitivity_level": "standard", "show_crisis_strip": False, "content_notes": ["Site-wide crisis link remains one tap away on every card."]},
 "visual": {"color_token": "anxiety", "icon": "wind",
  "illustration_prompt": "Soft line illustration of a person sitting calmly on a hillside while gentle looping thought-ribbons drift away from their head into an open sky. Pastel blue palette, hopeful, no distress imagery.",
  "alt_text": "A person sits calmly on a hillside as looping ribbons of thought drift away into an open sky."},
 "communities": ["reddit-r-anxiety", "adaa-online-support-group", "anxiety-uk-peer-support-groups", "beyondblue-forums", "sane-forums-australia"],
 "sources": [
  DSM("Anxiety Disorders"),
  src("src-nimh-stats", "Generalized Anxiety Disorder statistics", "National Institute of Mental Health (NIMH)", "https://www.nimh.nih.gov/health/statistics/generalized-anxiety-disorder", seen=True),
  src("src-nice-cg113", "Generalised anxiety disorder and panic disorder in adults: management (CG113)", "NICE", "https://www.nice.org.uk/guidance/cg113", 2011, seen=True, note="Last reviewed by NICE in 2024 per search results."),
  src("src-nhs-gad", "Generalised anxiety disorder in adults", "NHS", "https://www.nhs.uk/mental-health/conditions/generalised-anxiety-disorder/", note="Well-known NHS page; not opened in this session.")
 ],
 "review": {"last_researched": D, "reading_grade_estimate": 0, "reading_grade_method": "Flesch-Kincaid grade, computed on all reader-facing text",
  "verification_status": "needs_verification", "needs_clinician_signoff": False,
  "open_questions": ["Add UK (APMS) and Australian (NSMHWB) prevalence figures once pages can be opened.", "Confirm NICE CG113 step-3 medication wording."]}
})
