from helpers import D, src, DSM
CARDS = []
NIMH_MDD = src("src-nimh-mdd", "Major Depression statistics", "National Institute of Mental Health (NIMH)", "https://www.nimh.nih.gov/health/statistics/major-depression", seen=True)
NICE_222 = src("src-nice-ng222", "Depression in adults: treatment and management (NG222)", "NICE", "https://www.nice.org.uk/guidance/ng222", 2022, seen=True, note="Guideline page seen in search; severity-band recommendations summarized from the guideline structure and general knowledge; confirm on the live page.")

CARDS.append({
 "topic_id": "major-depressive-disorder",
 "official_name": "Major Depressive Disorder",
 "plain_title": "When low mood takes over",
 "also_known_as": ["depression", "clinical depression", "MDD", "major depression"],
 "chapter_id": "depressive", "card_type": "condition", "icd10cm_code": "F32.x / F33.x (single / recurrent, by severity)",
 "language_convention": "person-first",
 "language_convention_note": "'A person with depression' or 'living with depression'. 'Depressed' as a passing mood is fine in everyday speech; this card keeps it for the condition.",
 "one_liner": "Weeks or more of low mood or lost interest that drains energy and makes daily life hard.",
 "in_simple_words": "Depression is more than a bad week. For at least two weeks, most of the day, nearly every day, a person feels low, empty, or numb, or stops enjoying things they used to love. Sleep, appetite, energy, concentration, and self-worth often change too. It can happen once or come back in episodes. It is one of the most common health conditions in the world, and most people get better with treatment.",
 "what_it_can_feel_like": [
  "It's not sadness exactly. It's like the colour drained out of everything.",
  "Getting out of bed felt like lifting a car. People thought I was lazy. I was drowning.",
  "The first week the fog lifted, I cried because I'd forgotten what normal felt like."
 ],
 "common_signs": [
  "Feeling low, empty, hopeless, or irritable most of the day, nearly every day",
  "Losing interest or pleasure in almost everything",
  "Sleeping much more or much less than usual",
  "Big changes in appetite or weight",
  "Feeling worthless, guilty, or like a burden",
  "Trouble thinking, concentrating, or making decisions"
 ],
 "myths_vs_facts": [
  {"myth": "Depression is just sadness, and everyone gets sad.", "fact": "Sadness is one feeling that passes. Depression is a whole-body condition that changes sleep, energy, thinking, and hope for weeks or months."},
  {"myth": "People with depression could cheer up if they tried.", "fact": "Depression takes away the energy and motivation needed to 'try'. That's the illness, not the person."},
  {"myth": "Antidepressants change your personality or are addictive.", "fact": "They aren't addictive and don't change who you are. They can have side effects, which is why a doctor monitors them."},
  {"myth": "Talking about suicide makes it more likely.", "fact": "Asking directly and listening without judgement lowers risk and opens the door to help."}
 ],
 "how_common": {
  "plain": "About 1 in 12 US adults had a major depressive episode in the past year. Among teenagers it was about 1 in 5, and nearly 3 in 10 teenage girls.",
  "figure": "8.3% of US adults and 20.1% of adolescents aged 12–17 had a past-year major depressive episode (NSDUH 2021)",
  "source_ref": "src-nimh-mdd",
  "note": "Rates in the UK, Australia, India and worldwide differ by survey; WHO estimates about 5% of adults worldwide have depression. Add verified country figures."
 },
 "what_helps": {
  "plain_summary": "Depression is very treatable. For milder depression, guided self-help, behavioural activation (getting back to meaningful activity step by step), CBT, or exercise programmes are good first options. For more severe depression, a talking therapy combined with an antidepressant, prescribed and monitored by a doctor, works best. If the first treatment doesn't help, there are many more options, so it's worth going back.",
  "evidence_based_options": [
   "Cognitive behavioural therapy (CBT), behavioural activation, or interpersonal therapy",
   "Guided self-help, group therapy, or structured exercise programmes for less severe depression",
   "Antidepressants (SSRIs and others), prescribed and monitored by a doctor, especially for more severe depression",
   "For severe or treatment-resistant depression: combined therapy and medication, and in some cases brain stimulation treatments"
  ],
  "self_help_that_supports_care": [
   "One small activity a day that used to matter, even without the feeling",
   "Keeping a regular wake time and getting daylight in the morning",
   "Telling one person how bad it really is",
   "Cutting back on alcohol, which deepens depression"
  ],
  "guideline_refs": ["src-nice-ng222"]
 },
 "when_to_reach_out": "If low mood or loss of interest has lasted two weeks or more and is affecting daily life, talk to a doctor. If you are having thoughts of ending your life, use the crisis strip now. You don't have to wait until things are unbearable.",
 "is_not": "Grief after a loss, a normal reaction to a hard event, or a few bad days are not depression, although any of them can lead to it. Low mood with periods of high energy may be bipolar disorder, which needs different treatment.",
 "hope_note": "Depression lies about the future. With treatment, most people recover, and many say they came out knowing themselves better.",
 "in_young_people": "Children and teenagers often show depression as irritability, anger, school refusal, or physical complaints rather than sadness. It is common in teens, and talking therapies are the first-line treatment for young people.",
 "across_cultures": "In many cultures depression is felt and described through the body: tiredness, pain, 'heaviness', 'thinking too much'. Some languages have no direct word for it. Stigma can keep people from naming it, so doctors may need to ask about sleep, energy, and interest rather than mood.",
 "sub_sections": [
  {"title": "With seasonal pattern", "text": "Depression that returns at the same time each year, usually in autumn and winter. Light therapy and CBT help."},
  {"title": "With peripartum onset", "text": "Depression starting in pregnancy or soon after birth. See the perinatal depression card."},
  {"title": "With psychotic features", "text": "In severe depression, some people experience beliefs or voices that aren't real, often about guilt or illness. This needs urgent treatment and responds well to it."},
  {"title": "Other specified and unspecified depressive disorder; unspecified mood disorder", "icd10cm_code": "F32.89 / F32.A / F39", "text": "Used when depression is clearly present but doesn't fit the full pattern, for example shorter episodes. Still deserves treatment."}
 ],
 "related_topics": ["persistent-depressive-disorder", "bipolar-i-disorder", "bipolar-ii-disorder", "generalized-anxiety-disorder", "perinatal-depression-and-anxiety", "grief-and-bereavement", "suicidal-thoughts-and-behavior"],
 "glossary_terms": ["anhedonia", "rumination", "cbt", "behavioural-activation", "antidepressant", "ssri", "seasonal-pattern", "suicidal-ideation", "episode", "remission"],
 "safety": {"sensitivity_level": "elevated", "show_crisis_strip": True, "content_notes": ["Suicide risk; crisis strip required.", "No methods; 'died by suicide' language only."]},
 "visual": {"color_token": "depressive", "icon": "sunrise",
  "illustration_prompt": "Soft line illustration of a person opening curtains in the morning, warm light spilling across a bed and a mug on the sill, a small plant beginning to lean toward the window. Pastel peach and soft yellow. No head-in-hands, no rain.",
  "alt_text": "A person opens curtains and morning light spills across a bed, a mug, and a small plant on the windowsill."},
 "communities": ["reddit-r-depression", "dbsa-online-support-groups", "adaa-online-support-group", "mind-side-by-side", "beyondblue-forums"],
 "sources": [DSM("Depressive Disorders"), NIMH_MDD, NICE_222,
  src("src-nimh-depression", "Depression (health topic)", "National Institute of Mental Health (NIMH)", "https://www.nimh.nih.gov/health/topics/depression"),
  src("src-who-depression", "Depressive disorder (depression) fact sheet", "World Health Organization", "https://www.who.int/news-room/fact-sheets/detail/depression")],
 "review": {"last_researched": D, "reading_grade_estimate": 0, "reading_grade_method": "Flesch-Kincaid grade, computed on all reader-facing text", "verification_status": "needs_verification", "needs_clinician_signoff": False,
  "open_questions": ["Confirm NG222 severity-band recommendations on the live page.", "Add UK, AU, India prevalence."]}
})

CARDS.append({
 "topic_id": "persistent-depressive-disorder",
 "official_name": "Persistent Depressive Disorder",
 "plain_title": "The low mood that never quite lifts",
 "also_known_as": ["dysthymia", "PDD", "chronic depression", "'high-functioning' depression (popular term)"],
 "chapter_id": "depressive", "card_type": "condition", "icd10cm_code": "F34.1",
 "language_convention": "person-first",
 "one_liner": "A milder but long-lasting depression, present most days for two years or more.",
 "in_simple_words": "Persistent depressive disorder is depression that runs in the background for years. The mood is low or flat most days, with tiredness, poor sleep or appetite, low self-esteem, and trouble concentrating, but the person often keeps going. Many people assume 'this is just who I am'. It isn't. It is a treatable condition, and treatment can show people a brighter baseline they didn't know existed.",
 "what_it_can_feel_like": [
  "I thought everyone felt this tired and grey all the time. Turns out they don't.",
  "I function. I work. I just never feel good, and I can't remember when I last did.",
  "Treatment didn't make me happy overnight. It made 'okay' possible."
 ],
 "common_signs": [
  "Low or flat mood most days for two years or more",
  "Low energy and tiredness that never fully lifts",
  "Low self-esteem or feeling not good enough",
  "Poor sleep or appetite, or too much of either",
  "Trouble concentrating or making decisions",
  "Feeling hopeless about things ever changing"
 ],
 "myths_vs_facts": [
  {"myth": "It's just my personality. I'm a glass-half-empty person.", "fact": "Long-term low mood often gets mistaken for personality. When it's treated, people are often surprised how different they feel."},
  {"myth": "If you can hold down a job, it isn't real depression.", "fact": "Functioning on the outside while feeling empty inside is exactly what this condition looks like. The pain counts."},
  {"myth": "Mild means it doesn't matter.", "fact": "Years of low mood add up. PDD is linked with as much long-term impact as major depression, and it raises the risk of a major episode on top ('double depression')."}
 ],
 "how_common": {
  "plain": "About 1 or 2 in every 100 US adults have persistent depressive disorder in a given year, and about 1 in 40 at some point in life. Women are affected more often.",
  "figure": "1.5% past-year and 2.5% lifetime prevalence among US adults (NCS-R, 2001–2003)",
  "source_ref": "src-nimh-pdd",
  "note": "Older figures using the DSM-IV 'dysthymia' definition; DSM-5 PDD is broader."
 },
 "what_helps": {
  "plain_summary": "The same treatments that work for major depression work here, and combining a talking therapy with an antidepressant, prescribed and monitored by a doctor, often works better than either alone for long-term depression. Because the pattern has usually lasted years, treatment may take longer and benefits from patience and a plan to prevent slipping back.",
  "evidence_based_options": [
   "CBT, behavioural activation, or interpersonal therapy, often longer-term",
   "Antidepressants, prescribed and monitored by a doctor",
   "Combined therapy and medication for chronic depression",
   "Relapse-prevention work, including mindfulness-based cognitive therapy"
  ],
  "self_help_that_supports_care": [
   "Tracking mood for a few weeks to see the pattern clearly",
   "Scheduling small, pleasant, or meaningful activities, not waiting to feel like it",
   "Regular sleep, movement, and daylight",
   "Peer support with others who know what 'always a bit low' is like"
  ],
  "guideline_refs": ["src-nice-ng222"]
 },
 "when_to_reach_out": "If you've felt low, tired, or empty more days than not for a year or more, and especially if you've started to believe that's just who you are, talk to a doctor or therapist. If things get suddenly worse or you think about not wanting to be here, reach out now.",
 "is_not": "Being an introvert, a realist, or someone who doesn't show much emotion is not depression. The difference is distress and a mood that stays low regardless of what's happening.",
 "hope_note": "People who have lived with low mood for years often say the best part of treatment was discovering what they'd been missing.",
 "in_young_people": "In children and teens the mood can be irritable rather than sad, and only one year is needed for the diagnosis. It is easy to miss because it looks like 'a moody kid'.",
 "related_topics": ["major-depressive-disorder", "cyclothymic-disorder", "generalized-anxiety-disorder", "avoidant-personality-disorder"],
 "glossary_terms": ["high-functioning-depression", "anhedonia", "cbt", "antidepressant", "mindfulness", "acute-vs-chronic", "wellbeing"],
 "safety": {"sensitivity_level": "elevated", "show_crisis_strip": True, "content_notes": ["Suicide risk is raised in chronic depression; crisis strip required."]},
 "visual": {"color_token": "depressive", "icon": "sunrise",
  "illustration_prompt": "Soft line illustration of a person walking a familiar path at dawn as the grey sky slowly warms to peach at the horizon. Pastel grey-blue and peach. Gentle, hopeful, no rain.",
  "alt_text": "A person walks a familiar path at dawn as the grey sky warms to peach at the horizon."},
 "communities": ["reddit-r-depression", "dbsa-online-support-groups", "mind-side-by-side", "adaa-online-support-group"],
 "sources": [DSM("Depressive Disorders"),
  src("src-nimh-pdd", "Persistent Depressive Disorder (Dysthymic Disorder) statistics", "National Institute of Mental Health (NIMH)", "https://www.nimh.nih.gov/health/statistics/persistent-depressive-disorder-dysthymic-disorder", seen=True),
  NICE_222],
 "review": {"last_researched": D, "reading_grade_estimate": 0, "reading_grade_method": "Flesch-Kincaid grade, computed on all reader-facing text", "verification_status": "needs_verification", "needs_clinician_signoff": False,
  "open_questions": ["Add a DSM-5-era prevalence figure if one can be verified."]}
})

CARDS.append({
 "topic_id": "premenstrual-dysphoric-disorder",
 "official_name": "Premenstrual Dysphoric Disorder",
 "plain_title": "When the week before your period wrecks your mood",
 "also_known_as": ["PMDD", "severe PMS (not the same thing)"],
 "chapter_id": "depressive", "card_type": "condition", "icd10cm_code": "F32.81",
 "language_convention": "person-first",
 "language_convention_note": "'A person with PMDD'. The card says 'people who menstruate' as well as 'women', because trans men and nonbinary people can have PMDD.",
 "one_liner": "Severe mood symptoms in the week or so before a period that lift once it starts, cycle after cycle.",
 "in_simple_words": "PMDD is a severe, cyclical mood condition tied to the menstrual cycle. In the days before a period, mood crashes: deep sadness, rage, anxiety, hopelessness, feeling out of control, alongside tiredness, sleep changes, and physical symptoms. Within a few days of bleeding starting, it lifts. It is not 'bad PMS' or weakness. It is thought to be an abnormal brain sensitivity to normal hormone changes, and it is treatable.",
 "what_it_can_feel_like": [
  "For ten days a month I don't recognize myself. Then my period comes and I'm back.",
  "I planned my whole life around the 'bad week' before I knew it had a name.",
  "Tracking it on a calendar was the moment it finally made sense."
 ],
 "common_signs": [
  "Mood swings, sudden sadness, or tearfulness in the week before a period",
  "Intense irritability, anger, or conflict with others",
  "Feeling anxious, on edge, or hopeless",
  "Low energy, trouble concentrating, sleep changes, food cravings",
  "Breast tenderness, bloating, or aches",
  "Symptoms lift within a few days of the period starting"
 ],
 "myths_vs_facts": [
  {"myth": "It's just PMS. Everyone gets it.", "fact": "PMS is common and mild. PMDD is severe enough to disrupt work, relationships, and safety, and it has its own diagnosis."},
  {"myth": "It's a hormone imbalance.", "fact": "Hormone levels are usually normal. The brain responds to normal changes in an unusual way, which is why treatments target the brain or stop the cycle."},
  {"myth": "You just have to put up with it.", "fact": "Several treatments work well, and tracking symptoms for two cycles is the first step to getting them."}
 ],
 "how_common": {
  "plain": "Roughly 3 to 6 in every 100 people who menstruate have PMDD. Many more have milder premenstrual symptoms.",
  "figure": "Estimates range from about 1.8% to 5.8% of menstruating people (APA range cited in a 2024 meta-analysis); IAPMD cites 5.5%",
  "source_ref": "src-iapmd-prev",
  "note": "Estimates vary with method; studies using daily symptom diaries give lower, more accurate figures."
 },
 "what_helps": {
  "plain_summary": "First, track symptoms daily across two cycles so the pattern is clear; a diagnosis needs this. Treatments with good evidence include certain antidepressants (SSRIs), which for PMDD can work within days and are sometimes taken only in the second half of the cycle, and some hormonal contraceptives. CBT helps with coping and mood. All medication is prescribed and monitored by a doctor. For severe cases that don't respond, specialists have further options.",
  "evidence_based_options": [
   "SSRIs, taken continuously or only in the premenstrual phase, prescribed and monitored by a doctor",
   "Certain combined hormonal contraceptives, prescribed and monitored by a doctor",
   "Cognitive behavioural therapy (CBT)",
   "Specialist hormonal treatments for severe, non-responding PMDD"
  ],
  "self_help_that_supports_care": [
   "A daily symptom tracker app or paper chart for at least two cycles",
   "Planning demanding tasks for the better half of the cycle where possible",
   "Regular sleep, exercise, and less alcohol and caffeine in the premenstrual week",
   "Telling the people close to you what the pattern is and what helps"
  ],
  "guideline_refs": ["src-iapmd-prev"]
 },
 "when_to_reach_out": "If mood symptoms before your period are severe, happen most cycles, and affect your life or relationships, see a doctor and bring your symptom tracking. If you have thoughts of ending your life in the premenstrual phase, which happens to many people with PMDD, use the crisis strip now; this phase passes, and help exists.",
 "is_not": "Ordinary PMS, with mild irritability or bloating, is not PMDD. Depression or anxiety that is present all month and gets worse before a period is called 'premenstrual exacerbation' and is treated differently.",
 "hope_note": "People with PMDD often go years without a name for it. Once it's recognized and treated, many get most of their month back.",
 "in_young_people": "PMDD can start with the first periods. Teenagers' symptoms are often dismissed as 'hormonal'. Tracking helps young people and parents see the pattern and get it taken seriously.",
 "across_cultures": "Menstruation is taboo in many communities, which makes PMDD harder to talk about and diagnose. Symptoms may be put down to character or 'nerves'. Culturally sensitive, private conversations with a clinician help.",
 "related_topics": ["major-depressive-disorder", "generalized-anxiety-disorder", "borderline-personality-disorder", "perinatal-depression-and-anxiety"],
 "glossary_terms": ["dysphoria", "emotional-lability", "ssri", "cbt", "suicidal-ideation", "irritability"],
 "safety": {"sensitivity_level": "elevated", "show_crisis_strip": True, "content_notes": ["Suicidal thoughts in the luteal phase are common in PMDD; crisis strip required."]},
 "visual": {"color_token": "depressive", "icon": "sunrise",
  "illustration_prompt": "Soft line illustration of a person marking a wall calendar with coloured dots, a cup of tea beside them, a cat on the chair, calm afternoon light. Pastel rose and peach.",
  "alt_text": "A person marks a wall calendar with coloured dots beside a cup of tea while a cat sits on the chair."},
 "communities": ["iapmd-peer-support", "reddit-r-pmdd"],
 "sources": [DSM("Depressive Disorders"),
  src("src-iapmd-prev", "What is the prevalence of premenstrual disorders?", "International Association for Premenstrual Disorders (IAPMD)", "https://faq.iapmd.org/en/articles/2609618-what-is-the-prevalence-of-premenstrual-disorders", seen=True),
  src("src-oxford-pmdd", "New data shows prevalence of PMDD (2024 meta-analysis)", "University of Oxford, Department of Psychiatry", "https://www.psych.ox.ac.uk/news/new-data-shows-prevalence-of-premenstrual-dysphoric-disorder-pmdd", 2024, seen=True),
  src("src-iapmd-treat", "Treatment options for PMDD", "International Association for Premenstrual Disorders (IAPMD)", "https://iapmd.org/treatment-options", note="Page URL from memory; confirm.")],
 "review": {"last_researched": D, "reading_grade_estimate": 0, "reading_grade_method": "Flesch-Kincaid grade, computed on all reader-facing text", "verification_status": "needs_verification", "needs_clinician_signoff": False,
  "open_questions": ["Confirm IAPMD treatment page URL and current guidance (RCOG/ISPMD) before publishing."]}
})

CARDS.append({
 "topic_id": "disruptive-mood-dysregulation-disorder",
 "official_name": "Disruptive Mood Dysregulation Disorder",
 "plain_title": "When a child's anger is constant and explosive",
 "also_known_as": ["DMDD"],
 "chapter_id": "depressive", "card_type": "condition", "icd10cm_code": "F34.81",
 "language_convention": "person-first",
 "language_convention_note": "'A child with DMDD'. The card speaks to parents and to young people themselves.",
 "one_liner": "A childhood condition of severe, frequent temper outbursts and an irritable or angry mood almost all the time.",
 "in_simple_words": "DMDD is diagnosed in children and young teens who have big, out-of-proportion outbursts several times a week, and who are irritable or angry most of the day in between. It has gone on for a year or more, at home, at school, and with friends. It is not bad parenting or a 'bad kid'. It is a mood condition, and it is treatable. It was added in 2013 partly to stop children being wrongly labelled bipolar.",
 "what_it_can_feel_like": [
  "I don't want to explode. It just happens and then I feel awful.",
  "As a parent, I walked on eggshells every day and blamed myself.",
  "Finding out it had a name meant finding out there was help."
 ],
 "common_signs": [
  "Severe temper outbursts, verbal or physical, three or more times a week",
  "Outbursts far bigger than the situation and than expected for their age",
  "Irritable or angry mood most of the day, nearly every day, between outbursts",
  "Going on for a year or more, in at least two settings",
  "Starts before age 10; diagnosed between ages 6 and 18"
 ],
 "myths_vs_facts": [
  {"myth": "It's just tantrums. They'll grow out of it.", "fact": "Toddler tantrums are normal. DMDD is older children with daily anger and outbursts that disrupt life for a year or more. It needs support, and it responds to it."},
  {"myth": "It's the parents' fault.", "fact": "DMDD has biological roots. Parents often need support and skills, but they didn't cause it."},
  {"myth": "This is childhood bipolar disorder.", "fact": "DMDD was created because most of these children do not go on to have bipolar disorder. They are more likely to have depression or anxiety as adults, which is why early help matters."}
 ],
 "how_common": {
  "plain": "Estimates suggest about 2 to 5 in every 100 children and teenagers may meet the criteria, with boys and younger children affected more often.",
  "figure": "Estimated 2–5% of children and adolescents (DSM-5-TR text estimate; community studies vary widely)",
  "source_ref": "src-dsm",
  "note": "Prevalence figure drawn from the DSM-5-TR's own summary of community studies; marked for verification against a primary study."
 },
 "what_helps": {
  "plain_summary": "Treatment usually starts with therapy for the child and training for parents in responding to outbursts calmly and consistently. CBT helps children learn to notice and manage frustration. Where DMDD overlaps with ADHD, treating the ADHD often helps the mood too. Medication, if used, is prescribed and monitored by a child psychiatrist. School support is part of the plan.",
  "evidence_based_options": [
   "Parent management training and family-based approaches",
   "Cognitive behavioural therapy adapted for children, including skills for frustration",
   "Treating co-occurring ADHD, anxiety, or depression",
   "Medication in some cases, prescribed and monitored by a child and adolescent psychiatrist"
  ],
  "self_help_that_supports_care": [
   "Predictable routines and warnings before transitions",
   "Noticing and praising calm moments, not only reacting to outbursts",
   "A shared plan with school for triggers and calm-down spaces",
   "Support for parents' own wellbeing; this is exhausting"
  ],
  "guideline_refs": ["src-nimh-dmdd"]
 },
 "when_to_reach_out": "If a child's anger and outbursts are far beyond what's typical for their age, happen most weeks, and have gone on for months, ask a doctor for an assessment. Seek urgent help if a child talks about hurting themselves or is a danger to others.",
 "is_not": "Normal tantrums in young children, anger after a specific upset, or defiance mainly aimed at authority figures (which may be oppositional defiant disorder) are not DMDD. Clear episodes of high energy and little sleep would point to bipolar disorder instead.",
 "hope_note": "Children with DMDD can learn to manage frustration, and families can find calm again. Many children's symptoms ease a lot as they grow, especially with support.",
 "in_young_people": "DMDD only applies to young people; it cannot be newly diagnosed after age 18. Teens may describe it as feeling angry 'all the time' and hating that they explode.",
 "related_topics": ["oppositional-defiant-disorder", "adhd", "major-depressive-disorder", "intermittent-explosive-disorder", "bipolar-i-disorder"],
 "glossary_terms": ["irritability", "emotional-dysregulation", "family-therapy", "cbt", "psychiatrist"],
 "safety": {"sensitivity_level": "standard", "show_crisis_strip": False, "content_notes": ["Frame as a condition, never as a 'bad kid'. Site-wide crisis link stays one tap away."]},
 "visual": {"color_token": "depressive", "icon": "sunrise",
  "illustration_prompt": "Soft line illustration of a parent and child sitting together on a step, the child holding a feelings chart, the parent's hand on their shoulder, a kite resting beside them. Pastel peach and sky blue. Calm, not angry.",
  "alt_text": "A parent and child sit together on a step looking at a feelings chart, with a kite resting beside them."},
 "communities": ["dbsa-balanced-mind-parent-network"],
 "sources": [DSM("Depressive Disorders"),
  src("src-nimh-dmdd", "Disruptive Mood Dysregulation Disorder: The Basics", "National Institute of Mental Health (NIMH)", "https://www.nimh.nih.gov/health/publications/disruptive-mood-dysregulation-disorder", note="Well-known NIMH page; not opened."),
  src("src-dbsa-bmpn", "Balanced Mind Parent Network", "Depression and Bipolar Support Alliance", "https://www.dbsalliance.org/balanced-mind-parent-network/", seen=True)],
 "review": {"last_researched": D, "reading_grade_estimate": 0, "reading_grade_method": "Flesch-Kincaid grade, computed on all reader-facing text", "verification_status": "needs_verification", "needs_clinician_signoff": False,
  "open_questions": ["Find a primary prevalence study to replace the DSM text estimate.", "Only one community found; look for a young-person-facing option."]}
})

CARDS.append({
 "topic_id": "perinatal-depression-and-anxiety",
 "official_name": "Perinatal (Peripartum) Depression and Anxiety",
 "plain_title": "Struggling during pregnancy or after a baby",
 "also_known_as": ["postpartum depression", "postnatal depression", "PPD", "PND", "perinatal mood and anxiety disorders (PMADs)"],
 "chapter_id": "depressive", "card_type": "explainer", "icd10cm_code": "n/a (specifier: 'with peripartum onset', applied to depressive or bipolar episodes)",
 "language_convention": "person-first",
 "language_convention_note": "Uses 'parents', 'mothers', and 'birthing parents' so that fathers, partners, and trans and nonbinary parents are included. Partners can also experience perinatal depression.",
 "one_liner": "Depression or anxiety that starts in pregnancy or the first year after birth. Common, nobody's fault, and treatable.",
 "in_simple_words": "Having a baby is supposed to be joyful, which makes it even harder to admit you feel low, anxious, numb, or frightened. Perinatal depression and anxiety affect around one in seven mothers and many partners too. They can bring sadness, constant worry, intrusive scary thoughts about the baby, trouble bonding, guilt, and exhaustion beyond normal tiredness. This is a medical condition, not a failure as a parent, and with help most people recover fully.",
 "what_it_can_feel_like": [
  "Everyone said I'd feel a rush of love. I felt nothing, then terror that I felt nothing.",
  "I had horrible pictures in my head of something happening to her. I thought it meant I was dangerous. It didn't.",
  "My partner got it too. Nobody told us dads could."
 ],
 "common_signs": [
  "Low mood, tearfulness, or numbness lasting more than two weeks",
  "Constant worry about the baby, or panic attacks",
  "Scary unwanted thoughts about harm coming to the baby",
  "Trouble sleeping even when the baby sleeps",
  "Feeling unable to bond, or like a bad parent",
  "Feeling hopeless, or thoughts that the family would be better off without you"
 ],
 "myths_vs_facts": [
  {"myth": "It's just the baby blues.", "fact": "The baby blues last up to two weeks and pass. Perinatal depression lasts longer, feels heavier, and needs support."},
  {"myth": "Scary thoughts about the baby mean I might hurt them.", "fact": "Unwanted intrusive thoughts are very common in new parents and are a sign of anxiety, not intent. They are different from postpartum psychosis, which is rare and shows as confusion and losing touch with reality."},
  {"myth": "If I tell anyone, they'll take my baby away.", "fact": "Perinatal mental health services exist to keep families together. Asking for help is what good parents do."},
  {"myth": "Only mothers get it.", "fact": "Fathers and partners get perinatal depression and anxiety too, especially when the other parent is unwell."}
 ],
 "how_common": {
  "plain": "About 1 in 7 women experience depression during pregnancy or in the year after birth, and about 1 in 10 experience both depression and anxiety. Around 1 in 10 fathers are affected too.",
  "figure": "~1 in 7 (about 14%) perinatal depression (ACOG estimate); ~9% co-occurring anxiety and depression (2025 meta-analysis of 122 studies)",
  "source_ref": "src-jama-perinatal",
  "note": "Partner/father figure (~10%) is widely cited but not verified in this session; marked for verification."
 },
 "what_helps": {
  "plain_summary": "Talking therapies such as CBT and interpersonal therapy are first-line, and many areas have specialist perinatal mental health teams. Antidepressants can be used in pregnancy and while breastfeeding; a doctor will weigh the options with you and monitor treatment. Peer support from other parents who've been through it is powerful. Sleep, practical help, and honest conversations with your partner all matter.",
  "evidence_based_options": [
   "Cognitive behavioural therapy or interpersonal therapy, including online and group versions",
   "Antidepressants, prescribed and monitored by a doctor, with a discussion about pregnancy and breastfeeding",
   "Specialist perinatal mental health services, including mother-and-baby units for severe illness",
   "Peer support groups run by perinatal organizations"
  ],
  "self_help_that_supports_care": [
   "Accepting practical help so you can sleep in longer stretches",
   "Telling your midwife, health visitor, doctor, or a helpline how you really feel",
   "Connecting with other new parents, in person or online",
   "Lowering the bar: a fed baby and a rested parent beat a tidy house"
  ],
  "guideline_refs": ["src-nice-cg192"]
 },
 "when_to_reach_out": "If low mood or anxiety has lasted more than two weeks during pregnancy or after birth, tell your midwife, health visitor, or doctor. Get urgent help, today, if you feel confused, hear or see things others don't, or have thoughts of harming yourself or the baby. Postpartum psychosis is rare, serious, and very treatable.",
 "is_not": "Tiredness, tearfulness, and feeling overwhelmed in the first two weeks are the baby blues and usually pass. Ordinary new-parent worry is not an anxiety disorder unless it takes over.",
 "hope_note": "Perinatal depression and anxiety are among the most treatable mental health conditions. Parents recover, bond, and go on to enjoy their children.",
 "across_cultures": "Postpartum customs differ: in many cultures the first weeks involve rest and family care, which can protect mental health, while in others new mothers are expected to carry on alone. Shame about 'not coping' is a barrier everywhere. Services that involve family and respect customs reach more parents.",
 "related_topics": ["major-depressive-disorder", "generalized-anxiety-disorder", "obsessive-compulsive-disorder", "bipolar-i-disorder", "understanding-psychosis", "premenstrual-dysphoric-disorder"],
 "glossary_terms": ["peripartum-onset", "baby-blues", "postpartum-psychosis", "intrusive-thoughts", "cbt", "ipt", "antidepressant", "mom-rage"],
 "safety": {"sensitivity_level": "elevated", "show_crisis_strip": True, "content_notes": ["Suicide is a leading cause of maternal death in the first year; crisis strip required.", "Intrusive thoughts are described without detail and framed as anxiety.", "Postpartum psychosis is named as an emergency with a clear 'get help today'."]},
 "visual": {"color_token": "depressive", "icon": "sunrise",
  "illustration_prompt": "Soft line illustration of a parent holding a sleeping baby by a window while another adult brings a cup of tea, morning light. Pastel peach and lavender. Warm, no idealized 'glowing mother'.",
  "alt_text": "A parent holds a sleeping baby by a window as another adult brings them a cup of tea in morning light."},
 "communities": ["postpartum-support-international", "reddit-r-postpartum-depression", "dbsa-online-support-groups"],
 "sources": [DSM("Depressive Disorders"),
  src("src-jama-perinatal", "Perinatal depression (JAMA patient page / summary)", "JAMA Network", "https://jamanetwork.com/journals/jama/fullarticle/2841695", seen=True, note="Cites the ~1 in 7 estimate; confirm article title."),
  src("src-psychmed-2025", "Co-occurring perinatal anxiety and depression: meta-analysis of 122 studies", "Psychological Medicine (Cambridge)", "https://www.cambridge.org/core/journals/psychological-medicine", 2025, note="Seen only as a journal issue listing; find the article DOI."),
  src("src-nice-cg192", "Antenatal and postnatal mental health: clinical management and service guidance (CG192)", "NICE", "https://www.nice.org.uk/guidance/cg192", 2014, note="Well-known guideline; not opened."),
  src("src-psi", "Postpartum Support International", "Postpartum Support International", "https://www.postpartum.net/", note="Not opened.")],
 "review": {"last_researched": D, "reading_grade_estimate": 0, "reading_grade_method": "Flesch-Kincaid grade, computed on all reader-facing text", "verification_status": "needs_verification", "needs_clinician_signoff": True,
  "open_questions": ["Verify father/partner prevalence figure.", "Verify PSI helpline number before adding it to the card.", "Clinician check of the medication-in-pregnancy wording."]}
})
