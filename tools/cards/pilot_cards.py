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

CARDS = []

# ---------- 1. Generalized Anxiety Disorder ----------
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

# ---------- 2. Bipolar I Disorder ----------
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

# ---------- 3. Anorexia Nervosa ----------
CARDS.append({
 "topic_id": "anorexia-nervosa",
 "official_name": "Anorexia Nervosa",
 "plain_title": "When fear of food and weight takes over",
 "also_known_as": ["anorexia", "AN"],
 "chapter_id": "eating", "card_type": "condition", "icd10cm_code": "F50.01x / F50.02x (by type, severity, remission)",
 "language_convention": "person-first",
 "language_convention_note": "'A person with anorexia'. Never 'an anorexic'. No weights, BMIs, calories, or food amounts anywhere on this card, following safe-messaging guidance for eating disorders.",
 "one_liner": "A serious illness where eating becomes severely restricted and fear of gaining weight takes over thinking and life.",
 "in_simple_words": "Anorexia nervosa is an illness, not a choice or a diet gone too far. A person eats far less than their body needs, feels intense fear of gaining weight, and sees their body differently from how others see it. It affects the brain, heart, bones, and mood, and it can be life-threatening. It happens to people of every size, gender, age, and background. Full recovery is possible, and getting help early makes it more likely.",
 "what_it_can_feel_like": [
  "Food rules felt like the one thing I could control, until they controlled me.",
  "Everyone said I looked ill. I honestly couldn't see it.",
  "Recovery was the hardest and best thing I've done. The voice got quieter."
 ],
 "common_signs": [
  "Eating much less, skipping meals, or cutting out whole food groups",
  "Intense fear of gaining weight, even when others are worried about health",
  "Seeing your body very differently from how others see it",
  "Thinking about food, weight, or exercise most of the day",
  "Feeling cold, tired, dizzy, or low; periods may stop",
  "Pulling away from meals with friends and family"
 ],
 "myths_vs_facts": [
  {"myth": "You can tell someone has anorexia by looking at them.", "fact": "You can't. People at any size can have anorexia and be seriously unwell. 'Atypical anorexia' is just as dangerous."},
  {"myth": "It's a girls' illness, a phase, or about vanity.", "fact": "It affects boys, men, and people of all genders and ages, and it is a serious mental illness with the highest death rate of any."},
  {"myth": "They just need to eat.", "fact": "Eating is the treatment, and the illness makes it terrifying. Recovery needs skilled, patient support, not pressure or blame."}
 ],
 "how_common": {
  "plain": "Fewer than 1 in 100 US adults have had anorexia nervosa in their lifetime, with women affected about three times as often as men. Many more people have eating disorders that don't fit one label exactly.",
  "figure": "0.6% lifetime prevalence among US adults (0.9% women, 0.3% men), NCS-R 2001–2003",
  "source_ref": "src-nimh-stats",
  "note": "A later US survey (NESARC-III, DSM-5 criteria) found 0.8%. Figures for teens and for other countries to be added when verified."
 },
 "what_helps": {
  "plain_summary": "Treatment works best with a team: a doctor to check physical health, a therapist, and often a dietitian. For teenagers, family-based treatment, where parents help with meals, has the best evidence. For adults, specialist talking therapies for eating disorders are first-line. Medication is never the only treatment. Some people need a hospital stay to get physically safe first.",
  "evidence_based_options": [
   "Family-based treatment (anorexia-focused family therapy) for children and teenagers",
   "Specialist talking therapies for adults: CBT for eating disorders (CBT-ED), MANTRA, or specialist supportive clinical management (SSCM)",
   "Regular physical health monitoring by a doctor",
   "Hospital or day-programme care when physical health or safety requires it"
  ],
  "self_help_that_supports_care": [
   "Telling one trusted person what is happening",
   "Contacting an eating-disorder helpline or online support group",
   "Unfollowing accounts that promote dieting or body comparison",
   "Being patient with yourself: recovery is not a straight line"
  ],
  "guideline_refs": ["src-nice-ng69"]
 },
 "when_to_reach_out": "If food, weight, or exercise rules are taking over your days, if you are frightened of eating, or if someone who cares about you is worried, please talk to a doctor or an eating-disorder helpline now. Don't wait until it 'looks serious'. If you feel faint, have chest pain, or have thoughts of ending your life, get urgent help.",
 "is_not": "Dieting, healthy eating, or being naturally slim are not anorexia. Anorexia is driven by fear and distress, takes over life, and harms health. Avoiding food because of taste, texture, or fear of choking without fear of weight gain is more likely ARFID, a different condition.",
 "hope_note": "People recover fully from anorexia, including after many years. Every step toward eating is a step toward getting your life and mind back.",
 "in_young_people": "Anorexia often starts in the early to mid teens. In children it can show up as 'picky' eating, refusing to eat with family, sudden exercise, or stopping growing. Parents are the most important part of a young person's recovery team.",
 "across_cultures": "Anorexia is found worldwide, and it is often missed in boys, in people of colour, and in people whose bodies don't match the stereotype. In some communities, food refusal is explained through fasting, religion, or 'fussiness' first. Treatment that respects family and food culture works better.",
 "sub_sections": [
  {"title": "Atypical anorexia nervosa", "icd10cm_code": "F50.89 (other specified feeding or eating disorder)", "text": "All the same thoughts, fears, and behaviours, but the person's weight stays in or above the typical range. It is just as serious and needs the same care."},
  {"title": "Restricting and binge-eating/purging types", "icd10cm_code": "F50.01x / F50.02x", "text": "Some people only restrict; others also have episodes of eating a lot or trying to 'undo' eating. Both are anorexia and both are treatable."}
 ],
 "related_topics": ["bulimia-nervosa", "binge-eating-disorder", "avoidant-restrictive-food-intake-disorder", "body-dysmorphic-disorder", "obsessive-compulsive-disorder", "major-depressive-disorder"],
 "glossary_terms": ["restriction", "body-image", "diet-culture", "orthorexia", "family-therapy", "cbt-e", "remission", "relapse", "inpatient"],
 "safety": {"sensitivity_level": "high", "show_crisis_strip": True,
  "content_notes": ["No numbers: no weights, BMI, calories, or amounts of food, anywhere on this card.", "No 'how to' behaviours or descriptions of purging methods.", "Crisis strip required; eating-disorder helplines shown alongside suicide lines.", "Illustration must not show a thin body, scales, measuring tape, or food being refused."]},
 "visual": {"color_token": "eating", "icon": "leaf",
  "illustration_prompt": "Soft line illustration of two people of unspecified body shape sitting at a small kitchen table sharing tea, warm light from a window, a plant on the sill. Pastel sage and peach. No scales, mirrors, food close-ups, or thin bodies.",
  "alt_text": "Two people share tea at a small kitchen table in warm window light, with a plant on the sill."},
 "communities": ["beat-uk-helpline-and-online-groups", "beat-uk-carers-peer-support", "butterfly-foundation-helpline", "reddit-r-eatingdisorders", "reddit-r-fuckeatingdisorders"],
 "sources": [
  DSM("Feeding and Eating Disorders"),
  src("src-nimh-stats", "Eating Disorders statistics", "National Institute of Mental Health (NIMH)", "https://www.nimh.nih.gov/health/statistics/eating-disorders", seen=True),
  src("src-nice-ng69", "Eating disorders: recognition and treatment (NG69)", "NICE", "https://www.nice.org.uk/guidance/ng69", 2017, note="Recommendations seen only via secondary summaries; must be confirmed on the NICE page."),
  src("src-udo-grilo-2018", "Prevalence and correlates of DSM-5-defined eating disorders in a nationally representative sample of U.S. adults", "Biological Psychiatry (Udo & Grilo)", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6097933/", 2018, seen=True),
  src("src-beat-info", "Anorexia nervosa", "Beat (UK)", "https://www.beateatingdisorders.org.uk/get-information-and-support/about-eating-disorders/types/anorexia/")
 ],
 "review": {"last_researched": D, "reading_grade_estimate": 0, "reading_grade_method": "Flesch-Kincaid grade, computed on all reader-facing text",
  "verification_status": "needs_human_review", "needs_clinician_signoff": True,
  "open_questions": ["High-sensitivity card: clinician and lived-experience review required before publication.", "Confirm the 'highest death rate of any mental illness' claim against a current source (commonly cited; often compared with opioid use disorder) or soften it.", "Confirm NICE NG69 adult therapy list on the live page."]}
})

# ---------- 4. Autism Spectrum Disorder ----------
CARDS.append({
 "topic_id": "autism-spectrum-disorder",
 "official_name": "Autism Spectrum Disorder",
 "plain_title": "A different way of experiencing the world",
 "also_known_as": ["autism", "ASD", "Asperger's (older term, no longer used in DSM)"],
 "chapter_id": "neurodevelopmental", "card_type": "condition", "icd10cm_code": "F84.0",
 "language_convention": "identity-first",
 "language_convention_note": "'Autistic person' and 'autistic people', following the stated preference of the Autistic Self Advocacy Network and most autistic adults surveyed. Some families and clinicians prefer 'person with autism'; both appear in this card's sources.",
 "one_liner": "A lifelong difference in how a person communicates, relates to others, senses the world, and handles change.",
 "in_simple_words": "Autism is a neurodevelopmental difference: the brain is wired differently from birth. Autistic people often communicate and socialize in their own way, feel sounds, lights, and textures more or less strongly, prefer routine, and have deep interests. Every autistic person is different, and support needs vary a lot. Autism is not an illness to cure. The DSM calls it a 'disorder' because these differences can make life in a non-autistic world hard without the right support.",
 "what_it_can_feel_like": [
  "Small talk is like a language I never learned, but give me my topic and I can talk for hours.",
  "The supermarket is lights, beeps, and smells all at once. I need my headphones.",
  "Being diagnosed at 35 explained my whole life. I wasn't broken. I was autistic.",
  "Routine isn't boring to me. It's what makes the world safe enough to enjoy."
 ],
 "common_signs": [
  "Finding eye contact, small talk, or reading social cues hard or tiring",
  "Communicating differently: very direct, very literal, or with few or no words",
  "Strong reactions to sounds, lights, textures, or smells",
  "Deep, focused interests and real expertise in them",
  "Needing routine and finding sudden change very hard",
  "Repeated movements like rocking or hand-flapping that help with calm"
 ],
 "myths_vs_facts": [
  {"myth": "Autistic people don't feel empathy or want friends.", "fact": "Most autistic people feel deeply and want connection. They may show it differently, and non-autistic people often misread it."},
  {"myth": "Vaccines cause autism.", "fact": "Large studies in many countries have found no link. Autism is mostly genetic and is present from birth."},
  {"myth": "Autism is a childhood condition, or only affects boys.", "fact": "Autistic children become autistic adults. Girls, women, and nonbinary people are often diagnosed late because they mask more."},
  {"myth": "Autistic people are either geniuses or can't do anything.", "fact": "Autistic people have the full range of abilities. Support needs vary, and many need a lot of support in some areas and none in others."}
 ],
 "how_common": {
  "plain": "In the US, about 1 in every 31 eight-year-olds has been identified as autistic. Rates have risen mainly because of better awareness and wider criteria.",
  "figure": "1 in 31 (3.2%) of 8-year-olds in 2022, CDC ADDM Network, published April 2025",
  "source_ref": "src-cdc-addm",
  "note": "Adult figures are less certain and generally lower because many adults were never assessed. UK and Australian figures to be added once verified."
 },
 "what_helps": {
  "plain_summary": "There is no treatment for autism itself, and none is needed. What helps is support that fits the person: early support for communication and daily skills, adjustments at school and work, sensory tools, and help for things that often come alongside autism like anxiety, sleep problems, or depression. Autistic adults say the most useful things are being understood, accepted, and allowed to be autistic. Medication is not used for autism's core features, only for co-occurring conditions, prescribed and monitored by a doctor.",
  "evidence_based_options": [
   "Early, play-based support for communication and daily living, involving parents (children)",
   "Speech and language therapy and occupational therapy, including sensory strategies",
   "Reasonable adjustments at school and work, such as quiet spaces, written instructions, and predictable routines",
   "Adapted CBT for anxiety or depression when they occur alongside autism"
  ],
  "self_help_that_supports_care": [
   "Connecting with other autistic people online or in person",
   "Sensory tools: noise-cancelling headphones, sunglasses, fidgets, a quiet space",
   "Building routines and planning for transitions and change",
   "Unmasking where it's safe: letting yourself stim, rest, and be direct"
  ],
  "guideline_refs": ["src-nice-cg170", "src-nice-cg142"]
 },
 "when_to_reach_out": "If you recognize yourself or your child here and it's causing struggle at school, work, or in daily life, ask a doctor about an autism assessment. Waits can be long, so ask what support is available in the meantime. Seek help promptly for burnout, depression, or thoughts of self-harm, which are more common in autistic people.",
 "is_not": "Being shy, introverted, or socially awkward is not autism. Autism is lifelong and involves sensory and communication differences together, from early childhood. ADHD, social anxiety, and OCD can look similar in places and often co-occur, which is why assessment matters.",
 "hope_note": "Autistic people are living, working, creating, and leading in every field. The right understanding and adjustments turn 'struggling' into 'thriving'.",
 "strengths_and_differences": "Many autistic people bring deep focus, honesty, pattern-spotting, memory for detail, loyalty, and a strong sense of fairness. These are differences, not deficits. At the same time, some autistic people need substantial daily support, and that need is just as valid. The autism community uses 'support needs' rather than 'high-' or 'low-functioning' labels.",
 "in_young_people": "Signs are often noticed by age two or three: differences in pointing, eye contact, responding to their name, play, and speech. Some children are identified much later, especially girls and children who mask. Early support helps, and so does acceptance at home and school.",
 "across_cultures": "Autism exists in every culture, but what counts as 'typical' social behaviour differs, so signs can be read differently. Diagnosis comes later, on average, for children from minority and lower-income families. Some languages have no word for autism, and stigma can keep families from seeking help.",
 "sub_sections": [
  {"title": "Support levels", "icd10cm_code": "F84.0", "text": "The DSM describes three levels of support need (requiring support, substantial support, or very substantial support), for social communication and for restricted or repetitive behaviours separately. Levels can change over time."},
  {"title": "Co-occurring conditions", "text": "Autism often goes together with ADHD, anxiety, depression, learning differences, epilepsy, sleep problems, and gut issues. Each deserves its own support."}
 ],
 "related_topics": ["adhd", "intellectual-developmental-disorder", "communication-disorders", "social-anxiety-disorder", "obsessive-compulsive-disorder"],
 "glossary_terms": ["stimming", "masking", "meltdown", "shutdown", "sensory-sensitivity", "special-interest", "autistic-burnout", "neurodivergent", "late-diagnosis", "person-first-identity-first"],
 "safety": {"sensitivity_level": "standard", "show_crisis_strip": False,
  "content_notes": ["Autistic people have raised rates of suicidal thoughts; the site-wide crisis link stays one tap away, and the 'when to reach out' text points to it.", "No puzzle-piece imagery; many autistic adults reject it."]},
 "visual": {"color_token": "neurodevelopmental", "icon": "sprout",
  "illustration_prompt": "Soft line illustration of a person wearing headphones happily arranging a collection of shells by colour on a windowsill, with a cat nearby and a calm garden outside. Pastel green and sand. No puzzle pieces.",
  "alt_text": "A person wearing headphones arranges shells by colour on a windowsill while a cat watches, with a garden outside."},
 "communities": ["reddit-r-autism", "reddit-r-autisticadults", "reddit-r-autisminwomen", "nas-online-community"],
 "sources": [
  DSM("Neurodevelopmental Disorders"),
  src("src-cdc-addm", "Prevalence and Early Identification of Autism Spectrum Disorder Among Children Aged 4 and 8 Years, ADDM Network, 2022", "CDC, Morbidity and Mortality Weekly Report", "https://www.cdc.gov/mmwr/volumes/74/ss/ss7402a1.htm", 2025, note="MMWR URL from memory; the 1-in-31 figure was confirmed via multiple news and university summaries. Must be confirmed on cdc.gov."),
  src("src-nice-cg170", "Autism spectrum disorder in under 19s: support and management (CG170)", "NICE", "https://www.nice.org.uk/guidance/cg170", 2013, seen=True),
  src("src-nice-cg142", "Autism spectrum disorder in adults: diagnosis and management (CG142)", "NICE", "https://www.nice.org.uk/guidance/cg142", 2012, seen=True),
  src("src-asan-language", "Identity-First Language", "Autistic Self Advocacy Network", "https://autisticadvocacy.org/about-asan/identity-first-language/"),
  src("src-nimh-autism", "Autism Spectrum Disorder (health topic)", "National Institute of Mental Health (NIMH)", "https://www.nimh.nih.gov/health/topics/autism-spectrum-disorders-asd")
 ],
 "review": {"last_researched": D, "reading_grade_estimate": 0, "reading_grade_method": "Flesch-Kincaid grade, computed on all reader-facing text",
  "verification_status": "needs_verification", "needs_clinician_signoff": False,
  "open_questions": ["Ask autistic reviewers to check tone and the strengths section.", "Confirm CDC MMWR URL.", "Add adult prevalence figure with a verified source."]}
})

# ---------- 5. Prolonged Grief Disorder ----------
CARDS.append({
 "topic_id": "prolonged-grief-disorder",
 "official_name": "Prolonged Grief Disorder",
 "plain_title": "When grief gets stuck",
 "also_known_as": ["PGD", "complicated grief (older term)", "persistent complex bereavement disorder (DSM-5 research term)"],
 "chapter_id": "trauma", "card_type": "condition", "icd10cm_code": "F43.81",
 "language_convention": "person-first",
 "language_convention_note": "'A person with prolonged grief' or 'someone whose grief has become stuck'. The card is careful never to call ordinary grief, however long or deep, a disorder.",
 "one_liner": "Grief is not an illness. For a few people it stays so intense, a year on, that life can't restart.",
 "in_simple_words": "Losing someone you love hurts, often for years, and that is normal. Prolonged grief disorder is different: a year or more after the death, the longing and pain are still as raw as the first weeks, almost every day, and life can't restart. The person may feel part of them died too, or that life has no meaning. It is not weakness or 'grieving wrong'. It is a recognized condition, new in 2022, and specific therapies help.",
 "what_it_can_feel_like": [
  "It's been two years and I still wake up expecting him to be there. Then it hits me all over again.",
  "Everyone else has moved on. I'm still standing at the graveside.",
  "I felt guilty for wanting the pain to ease, as if that meant forgetting her."
 ],
 "common_signs": [
  "Intense longing or constant thoughts of the person, most days, long after the loss",
  "Feeling that part of you died with them, or that life has no meaning now",
  "Deep disbelief that they are really gone",
  "Avoiding places, people, or things that bring reminders, or clinging to them",
  "Feeling numb, cut off from others, or unable to feel joy at all",
  "Struggling to work, care for yourself, or make plans"
 ],
 "myths_vs_facts": [
  {"myth": "This diagnosis means grief is now a mental illness.", "fact": "No. Normal grief, however deep or long, is not a disorder. The diagnosis is for the small group of people whose grief stays unbearably intense and stops life restarting, usually a year or more later."},
  {"myth": "There's a right length of time to grieve.", "fact": "There isn't. Many people grieve deeply for years and are not unwell. What matters is whether grief is slowly becoming livable or stays stuck."},
  {"myth": "Getting help means you didn't love them enough.", "fact": "Getting help honours the relationship. Therapy for prolonged grief is about carrying the person with you while rebuilding a life."}
 ],
 "how_common": {
  "plain": "Research suggests roughly 1 in 10 bereaved adults develop prolonged grief after a death from natural causes. It is more common after sudden, violent, or unexpected deaths, and after losing a child or partner.",
  "figure": "Pooled prevalence 9.8% (95% CI 6.8–14.0) among adults bereaved by non-violent loss, meta-analysis of 14 studies",
  "source_ref": "src-lundorff-2017",
  "note": "This meta-analysis used earlier research criteria, not the DSM-5-TR definition. Estimates using DSM-5-TR criteria may be lower; to be checked."
 },
 "what_helps": {
  "plain_summary": "Most grief does not need treatment, just time, support, and permission to grieve. When grief has become stuck, grief-focused talking therapy has the best evidence. It helps a person face the reality of the loss, stay connected to the person who died in a new way, and slowly re-enter life. Ordinary antidepressants on their own do not treat prolonged grief, though they may help if depression is also present, prescribed and monitored by a doctor.",
  "evidence_based_options": [
   "Grief-focused cognitive behavioural therapy, including gently revisiting the loss",
   "Structured prolonged grief or 'complicated grief' therapy with a trained therapist",
   "Treatment for depression or PTSD if they are also present",
   "Bereavement support groups alongside therapy"
  ],
  "self_help_that_supports_care": [
   "Talking to others who have lost someone, in a bereavement group or online community",
   "Keeping small routines: meals, sleep, a short walk",
   "Finding your own ways to stay connected: letters, rituals, a place to visit",
   "Letting yourself feel moments of ease without guilt"
  ],
  "guideline_refs": ["src-review-2025"]
 },
 "when_to_reach_out": "If it has been a year or more (six months for a child or teenager) and the pain is still as raw as the beginning almost every day, and you can't get back to your life, it is worth talking to a doctor, counsellor, or bereavement service. Reach out sooner if you have thoughts of not wanting to be here; those are common in grief and deserve support now.",
 "is_not": "Grief itself, even years of it with waves of pain on anniversaries and ordinary days, is not a disorder. Depression after a loss is also different: it tends to be about feeling worthless or empty about everything, not mainly about missing the person. The two can overlap, and a professional can help tell them apart.",
 "hope_note": "Grief that has become stuck can become grief you can carry. People who have had this therapy describe finding their person again in memory, not just in pain.",
 "in_young_people": "For children and teenagers, the diagnosis can be considered from six months after the loss rather than twelve. Young people may show stuck grief through anger, risk-taking, school problems, or clinging, rather than visible sadness.",
 "across_cultures": "Every culture has its own mourning customs and timelines, and the DSM says the diagnosis should only be made when grief clearly goes beyond what is expected in the person's own culture and religion. Some traditions keep ongoing bonds with the dead through rituals; that is not a symptom.",
 "sub_sections": [
  {"title": "Ordinary bereavement", "icd10cm_code": "Z63.4", "text": "Clinicians may record 'uncomplicated bereavement' when someone seeks support for normal grief. It is not a diagnosis of illness. See the grief and bereavement card."},
  {"title": "Grief after suicide, overdose, or sudden death", "text": "These losses carry extra shock, guilt, and stigma, and the risk of stuck grief is higher. Specialist support groups exist for people bereaved by suicide."}
 ],
 "related_topics": ["grief-and-bereavement", "major-depressive-disorder", "posttraumatic-stress-disorder", "adjustment-disorders", "suicidal-thoughts-and-behavior"],
 "glossary_terms": ["grief", "anticipatory-grief", "disenfranchised-grief", "suicide-loss-survivor", "cbt", "support-group", "trauma"],
 "safety": {"sensitivity_level": "elevated", "show_crisis_strip": True,
  "content_notes": ["Thoughts of death and 'wanting to join' the person are common in grief; the card names them and points to help without alarm.", "Must not imply there is a correct way or length of time to grieve.", "Crisis strip required."]},
 "visual": {"color_token": "trauma", "icon": "shield",
  "illustration_prompt": "Soft line illustration of a person sitting on a bench under a tree in early spring, holding a photograph gently, with a few new leaves on the branches and soft light. Pastel lilac and warm grey. Tender, not bleak; no rain, no graves.",
  "alt_text": "A person sits on a bench under a tree with a few new spring leaves, gently holding a photograph in soft light."},
 "communities": ["reddit-r-griefsupport", "cruse-bereavement-support", "reddit-r-widowers"],
 "sources": [
  DSM("Trauma- and Stressor-Related Disorders"),
  src("src-apa-pgd", "Prolonged Grief Disorder (DSM-5-TR fact sheet)", "American Psychiatric Association", "https://www.psychiatry.org/File%20Library/Psychiatrists/Practice/DSM/DSM-5-TR/APA-DSM5TR-ProlongedGriefDisorder.pdf", 2022, seen=True, note="Confirms PGD moved to Section II and replaced persistent complex bereavement disorder."),
  src("src-lundorff-2017", "Prevalence of prolonged grief disorder in adult bereavement: A systematic review and meta-analysis", "Journal of Affective Disorders (Lundorff et al.)", "https://pubmed.ncbi.nlm.nih.gov/28167398/", 2017, seen=True),
  src("src-review-2025", "The efficacy of psychotherapeutic interventions for prolonged grief disorder: A systematic review", "PubMed (2025 systematic review of 30 RCTs)", "https://pubmed.ncbi.nlm.nih.gov/40180039/", 2025, seen=True, note="Found grief-focused CBT the most studied and most effective approach."),
  src("src-apa-coding-2022", "DSM-5-TR Update, September 2022 (prolonged grief disorder coding update to F43.81)", "American Psychiatric Association", "https://www.psychiatry.org/getmedia/304e9a98-ca5c-4e04-97d7-30b4756705eb/APA-DSM5TR-Update-September-2022.pdf", 2022, seen=True, note="Heading seen in search; the F43.81 digit must be confirmed in the PDF.")
 ],
 "review": {"last_researched": D, "reading_grade_estimate": 0, "reading_grade_method": "Flesch-Kincaid grade, computed on all reader-facing text",
  "verification_status": "needs_human_review", "needs_clinician_signoff": True,
  "open_questions": ["Flagged for clinician review because of the fine line with normal grief.", "Find a prevalence estimate that uses DSM-5-TR criteria.", "Confirm F43.81 in the APA 2022 coding update PDF."]}
})
