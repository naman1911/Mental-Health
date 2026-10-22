from helpers import D, src, DSM
CARDS = []

# Bipolar I Disorder ----------
CARDS.append({
 "topic_id": "bipolar-i-disorder",
 "official_name": "Bipolar I Disorder",
 "plain_title": "When mood and energy swing to extremes",
 "also_known_as": ["Bipolar 1", "manic depression (older term)"],
 "chapter_id": "bipolar", "card_type": "condition", "icd10cm_code": "F31.x (by current episode)",
 "language_convention": "person-first",
 "language_convention_note": "'A person with bipolar disorder' or 'living with bipolar'. Avoid 'bipolar' as a noun for a person or as an adjective for moodiness.",
 "one_liner": "A condition with periods of extreme high mood and energy (mania), usually with periods of depression too.",
 "in_simple_words": "Bipolar I means a person has had at least one episode of mania: a week or more of unusually high or irritable mood, racing energy, little need for sleep, and decisions that are out of character. Most people also have episodes of depression. Between episodes, mood can be steady for months or years. It is a long-term condition, and it is very treatable.",
 "what_it_can_feel_like": [
  "For a while I felt unstoppable. I barely slept and it all made sense. Then it fell apart.",
  "The crash after a high is the worst part. I'm ashamed of things I did when I wasn't myself.",
  "With the right treatment I've had years of steady. I still get to be me."
 ],
 "common_signs": [
  "Periods of unusually high, excited, or irritable mood lasting days or longer",
  "Needing much less sleep without feeling tired",
  "Racing thoughts, fast talking, jumping between ideas",
  "Risky or out-of-character decisions about money, sex, or plans",
  "Periods of deep depression, low energy, and hopelessness",
  "Sometimes, during a high, beliefs or experiences that aren't real"
 ],
 "myths_vs_facts": [
  {"myth": "Bipolar just means moody.", "fact": "Mood episodes last days to months, not minutes. Everyday ups and downs are not bipolar disorder."},
  {"myth": "People with bipolar disorder are dangerous.", "fact": "People with bipolar disorder are far more likely to be harmed, including by suicide, than to harm anyone else. Stigma is the bigger danger."},
  {"myth": "Treatment will flatten my personality.", "fact": "The goal is steady mood with full feeling. Many people say treatment gave them their real selves back."},
  {"myth": "Mania is fun, so why treat it?", "fact": "Mania can wreck relationships, money, work, and safety, and it is often followed by a severe crash."}
 ],
 "how_common": {
  "plain": "Nearly 3 in 100 US adults have some form of bipolar disorder in a given year. Bipolar I on its own is rarer, affecting under 1 in 100 people worldwide.",
  "figure": "2.8% past-year prevalence of bipolar disorder (all types) among US adults (NCS-R); bipolar I about 0.6% lifetime across 11 countries (WMH survey)",
  "source_ref": "src-nimh-stats",
  "note": "The worldwide bipolar I figure comes from Merikangas et al. 2011; marked for verification."
 },
 "what_helps": {
  "plain_summary": "Bipolar I is usually managed long-term with medication, prescribed and monitored by a doctor, plus talking therapy and self-management. For mania, doctors typically use an antipsychotic. For keeping well, lithium is the best-studied option. Psychoeducation (learning your early warning signs), CBT, family-focused therapy, and keeping regular sleep and daily rhythms all reduce relapses.",
  "evidence_based_options": [
   "Mood stabilizers such as lithium for long-term stability, prescribed and monitored by a doctor with blood tests",
   "Antipsychotic medication for mania, prescribed and monitored by a doctor",
   "Group or individual psychoeducation about bipolar disorder",
   "CBT, family-focused therapy, or interpersonal and social rhythm therapy alongside medication"
  ],
  "self_help_that_supports_care": [
   "Keeping a regular sleep and wake time, even at weekends",
   "Tracking mood, sleep, and energy to catch early signs of an episode",
   "A written crisis plan agreed with your team and someone you trust",
   "Avoiding alcohol and recreational drugs, which can trigger episodes"
  ],
  "guideline_refs": ["src-nice-cg185"]
 },
 "when_to_reach_out": "If you or someone close to you has had a stretch of days with little sleep, racing energy, and out-of-character decisions, or if deep depression follows a high, see a doctor soon. If someone is in danger or losing touch with reality, use the crisis strip now.",
 "is_not": "Bipolar I is not mood swings within a day, and not a reaction to a good or bad week. It is also different from bipolar II, where the highs (hypomania) are milder and depression dominates.",
 "hope_note": "Many people with bipolar I live full, stable lives with the right treatment and support. Early diagnosis and a good team make a real difference.",
 "in_young_people": "Bipolar disorder usually begins in the late teens or twenties. In younger people, highs can look like extreme irritability or energy rather than happiness, and it is often mistaken for ADHD or depression at first.",
 "across_cultures": "How a high is seen varies: in some communities it is read as spiritual, in others as bad behaviour. Family involvement in care is common and valued in many cultures, and most guidelines now encourage it where the person agrees.",
 "sub_sections": [
  {"title": "Other specified and unspecified bipolar disorder", "icd10cm_code": "F31.89 / F31.9", "text": "When mood episodes don't fully match bipolar I or II, for example highs that are too short, clinicians may use these labels. They still deserve treatment."},
  {"title": "Bipolar disorder due to a medical condition or a substance", "icd10cm_code": "F06.33 / F06.34; varies", "text": "Some medicines, drugs, and illnesses can cause mania-like episodes. See the cross-chapter cards for these."}
 ],
 "related_topics": ["bipolar-ii-disorder", "cyclothymic-disorder", "major-depressive-disorder", "understanding-psychosis", "schizoaffective-disorder", "suicidal-thoughts-and-behavior"],
 "glossary_terms": ["mania", "hypomania", "mixed-features", "euthymia", "rapid-cycling", "mood-stabilizer", "antipsychotic", "psychoeducation", "crisis-plan", "insight"],
 "safety": {"sensitivity_level": "elevated", "show_crisis_strip": True,
  "content_notes": ["Raised suicide risk, especially in depressive and mixed episodes; crisis strip required.", "No mention of self-harm methods. Suicide language follows safe-messaging rules."]},
 "visual": {"color_token": "bipolar", "icon": "waves",
  "illustration_prompt": "Soft line illustration of a person standing steady on a small boat on gentle rolling waves, holding a lantern, with a calm horizon ahead. Pastel teal and lavender, hopeful, no storm or lightning.",
  "alt_text": "A person stands steady on a small boat on gentle waves, holding a lantern toward a calm horizon."},
 "communities": ["reddit-r-bipolar", "dbsa-online-support-groups", "reddit-r-bipolarsos", "sane-forums-australia"],
 "sources": [
  DSM("Bipolar and Related Disorders"),
  src("src-nimh-stats", "Bipolar Disorder statistics", "National Institute of Mental Health (NIMH)", "https://www.nimh.nih.gov/health/statistics/bipolar-disorder", seen=True),
  src("src-merikangas-2011", "Prevalence and correlates of bipolar spectrum disorder in the World Mental Health Survey Initiative", "Archives of General Psychiatry (Merikangas et al.)", "https://pubmed.ncbi.nlm.nih.gov/21383262/", 2011, note="PubMed ID from memory; must be confirmed."),
  src("src-nice-cg185", "Bipolar disorder: assessment and management (CG185)", "NICE", "https://www.nice.org.uk/guidance/cg185", 2014, note="Guideline documents seen in search; the recommendations page itself was not opened."),
  src("src-nimh-bipolar", "Bipolar Disorder (health topic)", "National Institute of Mental Health (NIMH)", "https://www.nimh.nih.gov/health/topics/bipolar-disorder")
 ],
 "review": {"last_researched": D, "reading_grade_estimate": 0, "reading_grade_method": "Flesch-Kincaid grade, computed on all reader-facing text",
  "verification_status": "needs_human_review", "needs_clinician_signoff": True,
  "open_questions": ["Confirm NICE CG185 wording on first-line treatment for acute mania (sources conflicted: antipsychotic-first vs mood stabilizer).", "Confirm Merikangas 2011 PubMed link and figures."]}
})

# ---------- remaining bipolar chapter cards ----------
NIMH_BP = src("src-nimh-stats", "Bipolar Disorder statistics", "National Institute of Mental Health (NIMH)", "https://www.nimh.nih.gov/health/statistics/bipolar-disorder", seen=True)
NICE185 = src("src-nice-cg185", "Bipolar disorder: assessment and management (CG185)", "NICE", "https://www.nice.org.uk/guidance/cg185", 2014, note="Not opened; recommendations summarized from secondary sources.")
VIS = lambda prompt, alt: {"color_token": "bipolar", "icon": "waves", "illustration_prompt": prompt, "alt_text": alt}
REV = lambda qs=[], clin=False: {"last_researched": D, "reading_grade_estimate": 0, "reading_grade_method": "Flesch-Kincaid grade, computed on all reader-facing text", "verification_status": "needs_human_review" if clin else "needs_verification", "needs_clinician_signoff": clin, "open_questions": qs}

CARDS.append({
 "topic_id": "bipolar-ii-disorder", "official_name": "Bipolar II Disorder", "plain_title": "Deep lows with milder highs",
 "also_known_as": ["bipolar 2", "bipolar type II"], "chapter_id": "bipolar", "card_type": "condition", "icd10cm_code": "F31.81", "language_convention": "person-first",
 "one_liner": "Episodes of depression plus at least one hypomanic episode: a milder high that doesn't tip into mania.",
 "in_simple_words": "Bipolar II involves the same deep depressions as bipolar I, but the highs are hypomania: several days of unusually high energy, confidence, and productivity, with less need for sleep, without the severe disruption or loss of reality of mania. Because hypomania can feel good, people often only seek help for the depression, so bipolar II is often mistaken for depression alone. That matters, because antidepressants on their own can make things worse. It responds well to the right treatment.",
 "what_it_can_feel_like": ["For a week I'd be brilliant: no sleep, ten projects, charming everyone. Then months in a hole.", "Three doctors treated my depression. The fourth asked about the good weeks. That changed everything.", "Now I know the signs. When I start needing less sleep, I call my team instead of booking flights."],
 "common_signs": ["Repeated episodes of depression, often long and severe", "At least one hypomanic episode: days of high energy, fast thinking, little sleep, big confidence", "Hypomania that's noticeable to others but doesn't wreck life or involve losing touch with reality", "Irritability or restlessness during highs", "Mood that cycles over weeks or months, not within a day"],
 "myths_vs_facts": [
  {"myth": "Bipolar II is 'bipolar lite'.", "fact": "The depressions in bipolar II are just as severe as in bipolar I and often last longer. The suicide risk is comparable. 'Milder' only describes the highs."},
  {"myth": "If I've never been manic, I can't be bipolar.", "fact": "Bipolar II is diagnosed by hypomania, which is milder and easy to miss. Many people with it have never been manic."},
  {"myth": "Antidepressants are the main treatment.", "fact": "Used alone, antidepressants can trigger hypomania or rapid cycling in bipolar II. Mood stabilizers or certain antipsychotics come first, prescribed and monitored by a doctor."}],
 "how_common": {"plain": "Fewer than 1 in 100 people have bipolar II, though many more have milder patterns, and many people with it are misdiagnosed with depression for years.",
  "figure": "Lifetime prevalence about 0.4% worldwide (World Mental Health Survey); all bipolar types combined about 2.8% past-year in US adults", "source_ref": "src-nimh-stats", "note": "Bipolar II-specific figure from Merikangas et al. 2011, needs direct verification."},
 "what_helps": {"plain_summary": "Treatment is long-term and combines medication, prescribed and monitored by a doctor, with psychological support. For bipolar depression, certain mood stabilizers (such as lamotrigine or lithium) and some antipsychotics (such as quetiapine) are used; antidepressants are added only with a mood stabilizer, if at all. Psychoeducation, CBT, and therapy that keeps daily rhythms steady reduce relapses. Tracking mood and sleep lets people and their teams act early.",
  "evidence_based_options": ["Mood stabilizers or specific antipsychotics for bipolar depression and prevention, prescribed and monitored by a doctor", "Psychoeducation, individual or in groups", "CBT, interpersonal and social rhythm therapy, or family-focused therapy", "Mood and sleep tracking with an agreed early-warning plan"],
  "self_help_that_supports_care": ["Keeping sleep regular; lost sleep can tip into hypomania", "Noticing personal early signs: talking faster, spending, big plans", "Avoiding alcohol and drugs", "Peer support with others who have bipolar II"],
  "guideline_refs": ["src-nice-cg185"]},
 "when_to_reach_out": "If you have had depressions and also periods of several days when you needed little sleep and felt unusually energetic or confident, tell a doctor about both, even if the highs felt good. If depression is deepening or you have thoughts of ending your life, use the crisis strip now.",
 "is_not": "Ordinary good weeks, or feeling productive after a depression lifts, are not hypomania. Fast mood changes within hours or a day point to other conditions, such as borderline personality disorder or ADHD, which can also co-occur.",
 "hope_note": "Once bipolar II is recognized, many people describe finally getting the right treatment and years of stability they'd stopped hoping for.",
 "in_young_people": "Bipolar II often starts in the late teens or twenties, usually with depression first. Teens' hypomania can look like irritability, risk-taking, or a sudden burst of confidence. A family history of bipolar disorder is a reason to ask.",
 "across_cultures": "Hypomania is easy to miss in any culture, and especially where high energy and productivity are prized. Families often notice the change before the person does; involving them in assessment, with consent, helps.",
 "related_topics": ["bipolar-i-disorder", "cyclothymic-disorder", "major-depressive-disorder", "borderline-personality-disorder", "adhd", "suicidal-thoughts-and-behavior"],
 "glossary_terms": ["hypomania", "mania", "euthymia", "rapid-cycling", "mood-stabilizer", "antidepressant", "psychoeducation"],
 "safety": {"sensitivity_level": "elevated", "show_crisis_strip": True, "content_notes": ["Suicide risk comparable to bipolar I; crisis strip required."]},
 "visual": VIS("Soft line illustration of a person reading on a balcony at dusk with a mood journal open and a sleep tracker on the table, the sky shifting from gold to deep blue. Pastel teal and lavender.", "A person reads on a balcony at dusk with a mood journal open and a sleep tracker on the table."),
 "communities": ["reddit-r-bipolar", "bipolar-uk-ecommunity", "dbsa-online-support-groups", "reddit-r-bipolarsos"],
 "sources": [DSM("Bipolar and Related Disorders"), NIMH_BP, NICE185, src("src-merikangas-2011", "Prevalence and correlates of bipolar spectrum disorder in the World Mental Health Survey Initiative", "Archives of General Psychiatry (Merikangas et al.)", "https://pubmed.ncbi.nlm.nih.gov/21383262/", 2011, note="PubMed ID from memory; confirm.")],
 "review": REV(["Confirm bipolar II prevalence citation.", "Clinician to check medication wording (lamotrigine, quetiapine) against CG185."], clin=True)})

CARDS.append({
 "topic_id": "cyclothymic-disorder", "official_name": "Cyclothymic Disorder", "plain_title": "Years of ups and downs that never quite reach an episode",
 "also_known_as": ["cyclothymia"], "chapter_id": "bipolar", "card_type": "condition", "icd10cm_code": "F34.0", "language_convention": "person-first",
 "one_liner": "Two years or more of mood swings between mild highs and lows that never meet the bar for full episodes.",
 "in_simple_words": "Cyclothymic disorder is a milder but long-lasting pattern of mood swings: periods of feeling unusually upbeat and energetic, alternating with periods of low mood, for at least two years, without ever reaching a full hypomanic, manic, or depressive episode. The swings are frequent, and stable stretches are short. People often think it's just their temperament. It can affect work and relationships, and some people later develop bipolar disorder, so recognizing it matters. Treatment helps smooth things out.",
 "what_it_can_feel_like": ["Everyone knew me as moody. I never had a stable month, but nothing was ever 'bad enough' to get help.", "I'd commit to things on an up and bail on a down. My friends gave up predicting me.", "Learning it had a name let me plan around it instead of being ambushed."],
 "common_signs": ["Frequent periods of mild highs: energy, confidence, less sleep, talkativeness", "Frequent periods of mild lows: tiredness, low mood, withdrawal", "Going on for two years or more (one year in young people)", "Never free of symptoms for more than two months at a time", "Swings that affect relationships, work, or study"],
 "myths_vs_facts": [
  {"myth": "It's just a moody personality.", "fact": "Cyclothymia is a mood condition with a biological basis, often in families with bipolar disorder. It's not a character flaw."},
  {"myth": "It's too mild to matter.", "fact": "The constant instability takes a real toll, and a significant minority of people go on to develop bipolar I or II."},
  {"myth": "Nothing can be done about it.", "fact": "Psychoeducation, regular routines, and sometimes medication help a lot."}],
 "how_common": {"plain": "Fewer than 1 in 100 people have cyclothymic disorder, though it is probably under-recognized because many never seek help.",
  "figure": "Lifetime prevalence estimated at 0.4%–1% (DSM-5-TR text)", "source_ref": "src-dsm", "note": "Figure from the DSM-5-TR text; needs a primary citation."},
 "what_helps": {"plain_summary": "Understanding the pattern is the first help. Psychoeducation and CBT help people spot their cycles and steady their routines, especially sleep. Mood-stabilizing medication, prescribed and monitored by a doctor, is used for some people, particularly if swings are disruptive or there's a family history of bipolar disorder. Antidepressants alone are used cautiously, as they can worsen cycling.",
  "evidence_based_options": ["Psychoeducation about mood cycling", "CBT and routine-stabilizing approaches", "Mood stabilizers in some cases, prescribed and monitored by a doctor", "Regular review, as the pattern can change over time"],
  "self_help_that_supports_care": ["Mood tracking to see the cycles clearly", "Regular sleep and daily rhythms", "Delaying big decisions made during an up", "Letting close people know the pattern so they can support, not judge"],
  "guideline_refs": ["src-nice-cg185"]},
 "when_to_reach_out": "If your mood has swung between highs and lows for years in a way that disrupts your life, ask a doctor about an assessment. Go sooner if a high becomes a lot bigger than usual, or a low becomes dark.",
 "is_not": "Ordinary mood variation, or mood changes caused by life events, is not cyclothymia. If a full hypomanic or depressive episode occurs, the diagnosis changes to bipolar II; if mania occurs, to bipolar I.",
 "hope_note": "People with cyclothymia learn to ride their cycles rather than be thrown by them, and many find steadier ground with treatment.",
 "in_young_people": "In children and teens, one year of symptoms is enough for the diagnosis. It can look like unpredictable moodiness and is easily mistaken for ADHD or 'just being a teenager'.",
 "related_topics": ["bipolar-ii-disorder", "bipolar-i-disorder", "persistent-depressive-disorder", "borderline-personality-disorder", "adhd"],
 "glossary_terms": ["hypomania", "euthymia", "emotional-lability", "mood-stabilizer", "psychoeducation"],
 "safety": {"sensitivity_level": "standard", "show_crisis_strip": False, "content_notes": ["Site-wide crisis link stays one tap away."]},
 "visual": VIS("Soft line illustration of a person cycling along a gently rolling coastal path, small rises and dips, a calm sea beside them. Pastel teal and sand.", "A person cycles along a gently rolling coastal path beside a calm sea."),
 "communities": ["reddit-r-bipolar", "bipolar-uk-ecommunity", "dbsa-online-support-groups"],
 "sources": [DSM("Bipolar and Related Disorders"), NICE185],
 "review": REV(["Find a primary prevalence source."])})
