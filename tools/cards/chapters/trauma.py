from helpers import D, src, DSM
CARDS = []

# Prolonged Grief Disorder ----------
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

# ---------- remaining trauma chapter cards ----------
NIMH_PTSD = src("src-nimh-ptsd", "Post-Traumatic Stress Disorder (PTSD) statistics", "National Institute of Mental Health (NIMH)", "https://www.nimh.nih.gov/health/statistics/post-traumatic-stress-disorder-ptsd", seen=True)
NICE116 = src("src-nice-ng116", "Post-traumatic stress disorder (NG116)", "NICE", "https://www.nice.org.uk/guidance/ng116", 2018, seen=True, note="Evidence-review documents seen in search; recommendations summarized from those and secondary summaries; confirm on the live page.")
ELEV = lambda notes: {"sensitivity_level": "elevated", "show_crisis_strip": True, "content_notes": notes}
REV = lambda qs=[], clin=False: {"last_researched": D, "reading_grade_estimate": 0, "reading_grade_method": "Flesch-Kincaid grade, computed on all reader-facing text", "verification_status": "needs_human_review" if clin else "needs_verification", "needs_clinician_signoff": clin, "open_questions": qs}

CARDS.append({
 "topic_id": "posttraumatic-stress-disorder", "official_name": "Posttraumatic Stress Disorder", "plain_title": "When the danger is over but your body doesn't know",
 "also_known_as": ["PTSD", "post-traumatic stress disorder", "shell shock (historical)"], "chapter_id": "trauma", "card_type": "condition", "icd10cm_code": "F43.10", "language_convention": "person-first",
 "language_convention_note": "'A person with PTSD' or 'a survivor'. Avoids 'victim'.",
 "one_liner": "After something terrifying, the mind and body stay stuck in danger mode for months: reliving, avoiding, on edge.",
 "in_simple_words": "After a frightening event, such as an assault, accident, disaster, war, or abuse, it's normal to feel shaken for a while. PTSD is when, a month or more later, the event keeps intruding through flashbacks, nightmares, or unwanted memories; you avoid reminders; your mood and beliefs turn dark; and your body stays on high alert. It's a recognized injury, not weakness, and specific therapies work very well.",
 "what_it_can_feel_like": ["A car door slams and I'm back there. Not remembering it. There.", "I stopped going anywhere that might remind me, which turned out to be everywhere.", "Trauma therapy was the hardest thing I've done. The memory is still mine, but it stopped running my life."],
 "common_signs": ["Flashbacks, nightmares, or memories that force their way in", "Avoiding people, places, thoughts, or feelings linked to the event", "Feeling numb, guilty, ashamed, or that the world is unsafe", "Being on constant alert, jumpy, irritable, or unable to sleep", "Trouble concentrating or remembering parts of what happened", "Lasting more than a month and affecting daily life"],
 "myths_vs_facts": [
  {"myth": "PTSD only happens to soldiers.", "fact": "Anyone can develop PTSD after any kind of trauma. Sexual assault, accidents, childbirth, and abuse are among the most common causes."},
  {"myth": "If you were strong you'd get over it.", "fact": "PTSD is a predictable injury to the brain's threat system. Strength has nothing to do with it."},
  {"myth": "Talking about it will make it worse.", "fact": "Avoiding the memory keeps PTSD alive. Trauma-focused therapies work precisely by helping you process it safely."},
  {"myth": "You'll have it forever.", "fact": "Most people improve a great deal with trauma-focused therapy, even decades after the event."}],
 "how_common": {"plain": "About 4 in 100 US adults have PTSD in a given year, and about 7 in 100 at some point in their lives. Women are affected nearly three times as often as men.",
  "figure": "3.6% past-year and 6.8% lifetime prevalence among US adults (5.2% women, 1.8% men past-year), NCS-R", "source_ref": "src-nimh-ptsd"},
 "what_helps": {"plain_summary": "Trauma-focused talking therapies are the first-line treatment: trauma-focused CBT (including cognitive processing therapy and prolonged exposure) and EMDR. They help the brain file the memory as past rather than present. Medication is not first-line; an SSRI or venlafaxine, prescribed and monitored by a doctor, may be used if a person prefers it or therapy isn't enough. Benzodiazepines are not recommended for PTSD.",
  "evidence_based_options": ["Trauma-focused CBT, including cognitive processing therapy and prolonged exposure", "EMDR (eye movement desensitization and reprocessing)", "Trauma-focused CBT adapted for children and young people", "SSRI or venlafaxine antidepressants if preferred or if therapy isn't enough, prescribed and monitored by a doctor"],
  "self_help_that_supports_care": ["Grounding techniques for flashbacks: naming what you can see, hear, and touch now", "Keeping routines, sleep, and movement going", "Reducing alcohol and drugs, which deepen PTSD", "Connecting with other survivors in moderated peer spaces"],
  "guideline_refs": ["src-nice-ng116"]},
 "when_to_reach_out": "If, a month or more after something frightening, you are reliving it, avoiding life, or on constant alert, talk to a doctor or a trauma service. You don't have to describe what happened to ask for help. If you have thoughts of ending your life, use the crisis strip now.",
 "is_not": "Being upset, shaken, or sleepless in the first weeks after a trauma is a normal reaction, and for most people it fades. Symptoms in the first month are called acute stress disorder. Long-term difficulties with emotions, self-worth, and relationships after repeated childhood trauma are called complex PTSD in ICD-11; in DSM-5-TR they are diagnosed as PTSD, often with the dissociative subtype.",
 "hope_note": "PTSD is one of the most treatable serious mental health conditions. The memory stays, but the fear can let go.",
 "in_young_people": "Children may show trauma through play that repeats the event, nightmares without clear content, clinginess, tantrums, bedwetting, or physical complaints. DSM-5-TR has separate criteria for children aged six and under. Trauma-focused CBT with a parent involved is the main treatment.",
 "across_cultures": "Trauma is often expressed through the body or through spiritual language, and some communities have their own words for it. Refugees and people from communities facing violence carry high rates of PTSD and often face the most barriers to care. Treatment works across cultures when it respects how the person understands what happened.",
 "sub_sections": [
  {"title": "Dissociative subtype", "text": "Some people with PTSD also feel detached from themselves or the world much of the time. Therapy is adapted to help them stay present."},
  {"title": "Other specified trauma- and stressor-related disorder", "icd10cm_code": "F43.89", "text": "Used when a stress reaction causes real trouble but doesn't fit PTSD, acute stress, or adjustment disorder patterns, including persistent trauma reactions that fall short of PTSD and some culturally specific reactions."}],
 "related_topics": ["acute-stress-disorder", "adjustment-disorders", "dissociative-identity-disorder", "depersonalization-derealization-disorder", "major-depressive-disorder", "child-abuse-and-neglect", "partner-violence-and-adult-abuse", "crime-disaster-and-legal-problems"],
 "glossary_terms": ["trauma", "flashback", "hypervigilance", "avoidance", "emotional-numbing", "complex-trauma", "cpt-and-pe", "emdr", "grounding", "trigger", "moral-injury"],
 "safety": ELEV(["Raised suicide risk; crisis strip required.", "No graphic descriptions of traumatic events anywhere on the card.", "Link to abuse and violence cards with their helplines."]),
 "visual": {"color_token": "trauma", "icon": "shield", "illustration_prompt": "Soft line illustration of a person sitting on a porch step with a dog, a storm visible far off on the horizon but the sky overhead clear, a warm light in the window behind. Pastel lilac and warm grey. No weapons, no violence.", "alt_text": "A person sits on a porch step with a dog under a clear sky, a storm far off on the horizon, warm light in the window behind."},
 "communities": ["reddit-r-cptsd", "reddit-r-cptsd-nscommunity", "reddit-r-cptsdpartners", "open-arms-australia", "sane-forums-australia"],
 "sources": [DSM("Trauma- and Stressor-Related Disorders"), NIMH_PTSD, NICE116,
  src("src-ncptsd", "National Center for PTSD", "US Department of Veterans Affairs", "https://www.ptsd.va.gov/", note="Not opened; widely known resource hub including family pages."),
  src("src-nhs-ptsd", "Post-traumatic stress disorder (PTSD)", "NHS", "https://www.nhs.uk/mental-health/conditions/post-traumatic-stress-disorder/", note="Not opened.")],
 "review": REV(["No PTSD-specific (rather than C-PTSD) subreddit confirmed; r/ptsd to be checked.", "Add UK and Australian prevalence."])})

CARDS.append({
 "topic_id": "acute-stress-disorder", "official_name": "Acute Stress Disorder", "plain_title": "The first weeks after something terrible",
 "also_known_as": ["ASD (not autism)", "acute stress reaction"], "chapter_id": "trauma", "card_type": "condition", "icd10cm_code": "F43.0", "language_convention": "person-first",
 "one_liner": "A strong stress reaction in the first month after a traumatic event, with reliving, numbness, and being on edge.",
 "in_simple_words": "In the days and weeks right after something frightening, many people feel shaken, numb, unreal, jumpy, or haunted by what happened. When these reactions are strong, last from three days to a month, and get in the way of coping, clinicians call it acute stress disorder. For most people it eases with time, safety, and support. For some it continues into PTSD, which is why early check-ins matter.",
 "what_it_can_feel_like": ["The week after the crash I felt like I was watching my life through glass.", "I couldn't sleep, couldn't stop seeing it, and couldn't explain it to anyone.", "Someone told me it was a normal reaction to an abnormal event. That helped more than anything."],
 "common_signs": ["Intrusive memories, nightmares, or flashbacks of the event", "Feeling numb, dazed, unreal, or detached from your body", "Being unable to remember parts of what happened", "Avoiding reminders, people, or places", "Trouble sleeping, being jumpy, irritable, or unable to concentrate", "Starting within a month of the event and lasting between three days and a month"],
 "myths_vs_facts": [
  {"myth": "Everyone who goes through trauma should have counselling straight away.", "fact": "Single-session 'debriefing' right after trauma doesn't help and can harm. What helps is safety, practical support, and watching for symptoms that persist."},
  {"myth": "If you're falling apart in the first week, you'll definitely get PTSD.", "fact": "Most people with early reactions recover without developing PTSD. Early symptoms are a reason to keep an eye on things, not a sentence."},
  {"myth": "You should be over it in a month.", "fact": "There's no deadline. After a month, if symptoms are still strong, the name changes to PTSD and effective treatment is available."}],
 "how_common": {"plain": "Roughly 1 in 5 people have an acute stress reaction after a trauma, higher after violence from another person and lower after accidents or disasters.",
  "figure": "Meta-analysis of 70 studies: acute stress disorder in about 14% (war-related) to 36% (interpersonal trauma) of trauma survivors", "source_ref": "src-asd-meta", "note": "Rates vary widely with trauma type and measurement method."},
 "what_helps": {"plain_summary": "Safety, practical help, and the support of people you trust come first. Clinicians use 'watchful waiting' with a follow-up within a month. If symptoms are severe, a short course of trauma-focused CBT in the first weeks can prevent PTSD. Routine one-off debriefing sessions are not recommended. Sleep problems may be treated short-term, with any medication prescribed and monitored by a doctor.",
  "evidence_based_options": ["Practical and emotional support, and active monitoring with a follow-up appointment", "Brief trauma-focused CBT for people with severe early symptoms", "Treating sleep problems and pain, which worsen stress reactions", "Not offering single-session psychological debriefing"],
  "self_help_that_supports_care": ["Getting back to routine, food, and sleep as far as possible", "Letting trusted people help with practical tasks", "Talking about it only as much as you want, when you want", "Avoiding alcohol as a way to sleep or numb out"],
  "guideline_refs": ["src-nice-ng116"]},
 "when_to_reach_out": "If reactions in the first weeks are so strong that you can't function, feel unreal most of the time, or can't sleep at all, tell a doctor. If you are thinking about ending your life, get help now. And if symptoms are still strong a month on, ask about trauma-focused therapy.",
 "is_not": "Feeling upset, tearful, or on edge for a few days after a scary event is a normal reaction and not a disorder. Symptoms that last beyond a month are PTSD, not acute stress disorder.",
 "hope_note": "The first weeks are the hardest. Most people find their footing again, and for those who don't, treatment works.",
 "in_young_people": "Children may become clingy, regress (bedwetting, baby talk), act out the event in play, or complain of tummy aches. Calm routines and the presence of trusted adults are the most protective things.",
 "related_topics": ["posttraumatic-stress-disorder", "adjustment-disorders", "depersonalization-derealization-disorder", "crime-disaster-and-legal-problems"],
 "glossary_terms": ["trauma", "dissociation", "emotional-numbing", "hypervigilance", "grounding", "fight-flight-freeze-fawn"],
 "safety": ELEV(["Crisis strip required; refers to abuse and violence helplines.", "No graphic event descriptions."]),
 "visual": {"color_token": "trauma", "icon": "shield", "illustration_prompt": "Soft line illustration of a person wrapped in a blanket on a sofa holding a warm mug, a friend sitting nearby with a hand on the sofa back, a clock on the wall. Pastel lilac and warm grey. Safe, quiet.", "alt_text": "A person wrapped in a blanket on a sofa holds a warm mug while a friend sits close by."},
 "communities": ["reddit-r-cptsd", "open-arms-australia", "sane-forums-australia"],
 "sources": [DSM("Trauma- and Stressor-Related Disorders"), NICE116,
  src("src-asd-meta", "Prevalence of acute stress disorder after trauma: systematic review and meta-analysis (70 studies)", "Journal of Affective Disorders Reports / related meta-analysis (2020)", "https://doaj.org/article/8d1b44219a284ea89a9cec23f48dec26", 2020, seen=True, note="Seen as a DOAJ listing; confirm article and figures.")],
 "review": REV(["Confirm the ASD meta-analysis citation.", "No ASD-specific community exists; broader trauma communities listed."])})

CARDS.append({
 "topic_id": "adjustment-disorders", "official_name": "Adjustment Disorders", "plain_title": "When a life change knocks you off your feet",
 "also_known_as": ["adjustment reaction", "situational depression (popular term)"], "chapter_id": "trauma", "card_type": "condition", "icd10cm_code": "F43.2x (by subtype)", "language_convention": "person-first",
 "one_liner": "Distress after a big life change, like a breakup or job loss, that is stronger than expected and disrupts life.",
 "in_simple_words": "Big changes are stressful. An adjustment disorder is when the reaction to a stressful event or change is stronger than you'd expect and interferes with daily life: low mood, worry, tearfulness, trouble sleeping, or acting out, starting within three months of the change. It is one of the most common diagnoses in primary care and usually eases once the situation settles or the person finds new footing, often with some support.",
 "what_it_can_feel_like": ["After the redundancy I couldn't sleep or think straight. I wasn't 'depressed'. I was knocked sideways.", "The diagnosis itself was the stress. Six months of just getting my head around it.", "A few sessions with a counsellor helped me see the change as something I could handle."],
 "common_signs": ["Low mood, worry, or tearfulness clearly linked to a recent change or stress", "Distress that's bigger than most people would have in that situation", "Trouble sleeping, concentrating, or keeping up with work or school", "In young people, acting out, skipping school, or risky behaviour", "Starting within three months of the event", "Easing within six months once the stress ends"],
 "myths_vs_facts": [
  {"myth": "It's not a 'real' diagnosis, just a label for being upset.", "fact": "It's a recognized condition with real distress and real risk, including of suicide. It's just one that usually resolves."},
  {"myth": "You should be able to cope with life events without help.", "fact": "Some changes are enormous. Getting support early is sensible and shortens recovery."},
  {"myth": "It's the same as depression.", "fact": "It's tied to a specific stress and usually lifts as things settle. If symptoms deepen or last beyond six months, it may be depression or anxiety and treatment changes."}],
 "how_common": {"plain": "Around 3 in 100 people seeing a family doctor meet the criteria, and most of them are never recognized. Rates are much higher among people facing serious illness.",
  "figure": "2.9% prevalence in a primary-care sample of 3,815 patients (Catalonia); general-population estimates 0.3%–2%", "source_ref": "src-adj-prim", "note": "Estimates vary widely by setting and method."},
 "what_helps": {"plain_summary": "Support often makes the difference: talking it through with a counsellor, brief CBT or problem-solving therapy, and practical help with the stressor itself. Many people need only a few sessions. Medication is not usually the main treatment; a doctor may prescribe and monitor short-term help with sleep, or an antidepressant if symptoms become severe or long-lasting.",
  "evidence_based_options": ["Brief counselling, CBT, or problem-solving therapy", "Practical support with the stressor (financial advice, workplace adjustments, medical information)", "Peer support with people facing the same change", "Short-term medication in some cases, prescribed and monitored by a doctor"],
  "self_help_that_supports_care": ["Naming the change and what it took from you", "Keeping sleep, meals, and movement steady", "Leaning on people; this is what they're for", "Giving yourself permission to take longer than you'd like"],
  "guideline_refs": ["src-adj-prim"]},
 "when_to_reach_out": "If a life change has left you struggling to function for weeks, or if you've started thinking you can't go on, talk to a doctor or counsellor. Adjustment disorders carry real suicide risk, so take dark thoughts seriously.",
 "is_not": "Normal stress and sadness after a change that you're still managing isn't a disorder. Grief after a death is its own thing, and PTSD follows events that were life-threatening rather than just stressful.",
 "hope_note": "Adjustment disorders usually pass. Most people find their feet within months, often stronger for having asked for help.",
 "in_young_people": "In children and teens, adjustment disorders often show as behaviour: anger, skipping school, fights, or risky choices after a move, divorce, or loss. Looking for the stress behind the behaviour is the key.",
 "sub_sections": [{"title": "Subtypes", "icd10cm_code": "F43.21–F43.25, F43.20", "text": "With depressed mood, with anxiety, with mixed anxiety and depressed mood, with disturbance of conduct, with mixed disturbance of emotions and conduct, or unspecified. The subtype just describes the main flavour of the reaction."}],
 "related_topics": ["major-depressive-disorder", "generalized-anxiety-disorder", "acute-stress-disorder", "grief-and-bereavement", "school-and-work-problems", "family-and-relationship-problems", "housing-and-money-problems"],
 "glossary_terms": ["stress", "burnout", "nervous-breakdown", "coping-skills", "resilience", "support-group"],
 "safety": ELEV(["Adjustment disorders carry raised suicide risk; crisis strip required."]),
 "visual": {"color_token": "trauma", "icon": "shield", "illustration_prompt": "Soft line illustration of a person standing at a fork in a path with a small suitcase, looking toward the brighter branch, a signpost with blank signs, early morning light. Pastel lilac and gold.", "alt_text": "A person with a small suitcase stands at a fork in a path, looking toward the brighter branch under early morning light."},
 "communities": ["mind-side-by-side", "beyondblue-forums", "adaa-online-support-group"],
 "sources": [DSM("Trauma- and Stressor-Related Disorders"),
  src("src-adj-prim", "Adjustment disorders in primary care: prevalence, recognition and use of services", "British Journal of Psychiatry (Fernández et al.)", "https://www.cambridge.org/core/journals/the-british-journal-of-psychiatry/article/adjustment-disorders-in-primary-care-prevalence-recognition-and-use-of-services/FCFF31580B65EEDE575FC2B689DC731E", 2012, seen=True)],
 "review": REV(["No clinical guideline specific to adjustment disorder found; treatment summary follows general consensus and should be checked by a clinician."])})

CARDS.append({
 "topic_id": "reactive-attachment-disorder", "official_name": "Reactive Attachment Disorder", "plain_title": "When a young child has learned not to seek comfort",
 "also_known_as": ["RAD"], "chapter_id": "trauma", "card_type": "condition", "icd10cm_code": "F94.1", "language_convention": "person-first",
 "language_convention_note": "'A child with RAD'. The card avoids blaming current caregivers, who are often adoptive or foster parents doing their best.",
 "one_liner": "A rare condition in young children who, after severe early neglect, don't seek or accept comfort from caregivers.",
 "in_simple_words": "Babies and toddlers learn to seek comfort from the adults who care for them. When early care has been severely neglectful, as in some institutions or chaotic homes, a few children stop seeking comfort at all. They rarely reach out when upset, don't respond much to soothing, and seem withdrawn, sad, or fearful with caregivers. This is reactive attachment disorder. It is rare, it's caused by what happened to the child, and it improves with stable, patient, loving care.",
 "what_it_can_feel_like": ["When she fell and hurt herself she didn't come to us. She just sat there. That broke my heart.", "He'd flinch from a hug, then stare at the wall. Nobody had ever come when he cried.", "Two years in, she climbed on my lap for comfort for the first time. We both cried."],
 "common_signs": ["Rarely seeking comfort when upset, and not responding to it when offered", "Little joy, few smiles, and limited emotional response to caregivers", "Unexplained sadness, irritability, or fear even during calm moments", "A history of severe neglect, institutional care, or many changes of caregiver", "Visible before age five, in a child at least nine months old"],
 "myths_vs_facts": [
  {"myth": "Any adopted or fostered child has attachment disorder.", "fact": "RAD is rare even among children with hard starts. Most children who've been through neglect do not have it, and many adopted children attach well."},
  {"myth": "Children with RAD are manipulative or future criminals.", "fact": "This myth is harmful and false. RAD is a withdrawn, sad pattern in young children. It has nothing to do with being 'bad'."},
  {"myth": "'Attachment therapies' like holding or rebirthing cure it.", "fact": "Coercive 'attachment therapies' are dangerous and have caused deaths. The treatment is a stable, responsive caregiver and support for the family."}],
 "how_common": {"plain": "RAD is rare. One UK study of children in a deprived area found about 1 in 70; among maltreated toddlers in foster care, rates are much higher.",
  "figure": "1.4% (95% CI 0.94–2.10) in a deprived UK general population sample of 6–8-year-olds; far higher in maltreated foster-care samples", "source_ref": "src-rad-prev", "note": "Population data are sparse."},
 "what_helps": {"plain_summary": "The key treatment is making sure the child has a stable, emotionally available caregiver and helping that caregiver respond sensitively, often through therapies that work with the parent and child together. Many children improve considerably once they have consistent care. Harsh or coercive 'attachment therapies' are not recommended and can be dangerous. Medication is not a treatment for RAD.",
  "evidence_based_options": ["Ensuring a stable, consistent, emotionally available caregiver", "Parent-child therapies that build sensitivity and responsiveness (for example video-feedback approaches)", "Support and training for foster and adoptive parents", "Treating co-occurring problems such as developmental delay or trauma symptoms"],
  "self_help_that_supports_care": ["Predictable routines and the same caregivers day after day", "Responding warmly even when the child doesn't seem to want it", "Looking after your own wellbeing as a carer; this is slow work", "Connecting with other foster and adoptive parents"],
  "guideline_refs": ["src-nice-ng26"]},
 "when_to_reach_out": "If a young child who has had a difficult start rarely seeks comfort, seems withdrawn or fearful with caregivers, and shows little joy, ask a paediatrician or child mental health service for an assessment. Be wary of anyone offering 'attachment therapy' outside mainstream services.",
 "is_not": "Autism can look similar but involves repetitive behaviours and sensory differences and doesn't require a history of neglect. A child who is shy with strangers but seeks comfort from parents does not have RAD. Children who are over-friendly with strangers may have disinhibited social engagement disorder instead.",
 "hope_note": "Children with RAD can learn that comfort is safe. It takes time and steady love, and it happens.",
 "in_young_people": "RAD is diagnosed only in young children and is thought to fade or change form as children grow. Older children with early neglect histories may show different difficulties and need their own assessment.",
 "across_cultures": "What counts as neglect varies by context, and poverty is not neglect. Assessments should look at whether the child had any consistent caregiver, not at whether care matched one culture's norms.",
 "related_topics": ["disinhibited-social-engagement-disorder", "child-abuse-and-neglect", "autism-spectrum-disorder", "posttraumatic-stress-disorder", "family-and-relationship-problems"],
 "glossary_terms": ["attachment", "trauma-informed", "adverse-childhood-experiences", "emotional-neglect"],
 "safety": ELEV(["Involves child neglect; links to child-protection helplines. Crisis strip required.", "Explicitly warns against coercive 'attachment therapies'."]),
 "visual": {"color_token": "trauma", "icon": "shield", "illustration_prompt": "Soft line illustration of a caregiver sitting on the floor at a small distance from a young child who is playing, the adult's hand open and resting, patient, warm light. Pastel lilac and peach.", "alt_text": "A caregiver sits on the floor a little way from a young child who is playing, with an open hand resting patiently."},
 "communities": ["nas-online-community"],
 "sources": [DSM("Trauma- and Stressor-Related Disorders"),
  src("src-rad-prev", "Prevalence of reactive attachment disorder in a deprived population", "British Journal of Psychiatry (Minnis et al.)", "https://www.cambridge.org/core/journals/the-british-journal-of-psychiatry/article/prevalence-of-reactive-attachment-disorder-in-a-deprivedpopulation/A41FDD96BBBF21FBFDCCED5D8B0F762B", 2013, seen=True),
  src("src-nice-ng26", "Children's attachment: attachment in children and young people who are adopted from care, in care or at high risk of going into care (NG26)", "NICE", "https://www.nice.org.uk/guidance/ng26", 2015, note="Not opened; well-known guideline that recommends sensitivity-focused parent interventions and advises against coercive approaches.")],
 "review": REV(["Communities: no RAD-specific group confirmed; the NAS community is a placeholder for a foster/adoptive parent community. Find adoption/fostering peer groups (e.g. Adoption UK) and verify.", "Clinician review of treatment wording."], clin=True)})

CARDS.append({
 "topic_id": "disinhibited-social-engagement-disorder", "official_name": "Disinhibited Social Engagement Disorder", "plain_title": "When a young child is too trusting of strangers",
 "also_known_as": ["DSED", "disinhibited attachment (older term)"], "chapter_id": "trauma", "card_type": "condition", "icd10cm_code": "F94.2", "language_convention": "person-first",
 "one_liner": "A rare pattern after severe early neglect: a young child approaches and goes off with strangers without any wariness.",
 "in_simple_words": "Most toddlers are a bit wary of strangers and check back with a trusted adult. After severe neglect or many changes of caregiver, a few children lose that wariness entirely. They'll climb onto a stranger's lap, wander off with anyone, and never check back. This is disinhibited social engagement disorder. It's caused by what the child went through, not by their character, and the main risk is safety. With stable care and support it improves, though it can take years.",
 "what_it_can_feel_like": ["In the park he'd hold any adult's hand and walk away with them. Terrifying.", "She called the plumber 'Daddy' within five minutes. People thought it was cute. It wasn't.", "Teaching her who's safe took years. Now she checks with me first. That's huge."],
 "common_signs": ["Approaching and interacting with unfamiliar adults with no hesitation", "Over-familiar behaviour, like hugging or sitting on strangers' laps", "Wandering off with unfamiliar adults without checking back", "A history of severe neglect, institutional care, or repeated changes of caregiver", "Visible in children aged at least nine months"],
 "myths_vs_facts": [
  {"myth": "The child is just friendly and outgoing.", "fact": "Friendly children still check with their caregiver and show some caution. DSED is a lack of the normal wariness that keeps children safe."},
  {"myth": "Once the child has a loving home, it goes away quickly.", "fact": "Unlike RAD, DSED can persist for years even in good homes. Patience and supervision are needed."},
  {"myth": "It's the adoptive parents' fault.", "fact": "DSED stems from early neglect before the child reached their current family. Supportive caregivers are the solution, not the cause."}],
 "how_common": {"plain": "DSED is rare in the general population but is seen in a notable minority of children who spent their early years in institutions or very neglectful homes.",
  "figure": "No reliable general-population figure; around 20% in some samples of children raised in institutions", "source_ref": "src-dsm", "note": "Prevalence drawn from DSM-5-TR summary of research on institutionalized children; needs a primary citation."},
 "what_helps": {"plain_summary": "Stable, consistent caregiving is the foundation. Therapies that help parents respond sensitively and teach the child about safe and unsafe people help over time. Practical safety measures, like close supervision in public, matter. Behaviour may improve slowly, so support for parents is important. Medication is not a treatment for DSED.",
  "evidence_based_options": ["A stable, emotionally available caregiver and consistent routines", "Parent-child therapies focused on sensitivity and responsiveness", "Explicit teaching about safe adults and checking back", "Support and respite for foster and adoptive parents"],
  "self_help_that_supports_care": ["Close supervision in public places, planned rather than panicked", "Clear, repeated, kind rules about strangers", "Praise for checking back with you", "Peer support from other adoptive and foster families"],
  "guideline_refs": ["src-nice-ng26"]},
 "when_to_reach_out": "If a young child who has had an unsettled start shows no wariness of strangers and would go off with anyone, ask a paediatrician or child mental health team for an assessment, and ask for support with safety planning now.",
 "is_not": "A sociable, confident child who still checks in with their caregiver does not have DSED. Impulsive, overly familiar behaviour in a child with ADHD and no history of neglect is a different thing.",
 "hope_note": "Children with DSED can learn who is safe and build real bonds. The progress is slow, and it is progress.",
 "in_young_people": "DSED is diagnosed in young children but, unlike RAD, can continue into middle childhood and the teens, sometimes showing as over-familiarity with peers and adults and risky trust. Ongoing support helps.",
 "related_topics": ["reactive-attachment-disorder", "child-abuse-and-neglect", "adhd", "posttraumatic-stress-disorder"],
 "glossary_terms": ["attachment", "trauma-informed", "adverse-childhood-experiences", "impulsivity"],
 "safety": ELEV(["Involves child neglect and child safety; crisis strip and child-protection links required."]),
 "visual": {"color_token": "trauma", "icon": "shield", "illustration_prompt": "Soft line illustration of a child in a playground looking back over their shoulder toward a caregiver who waves from a bench, a safe fenced area, soft light. Pastel lilac and green.", "alt_text": "A child in a fenced playground looks back over their shoulder at a caregiver waving from a bench."},
 "communities": ["nas-online-community"],
 "sources": [DSM("Trauma- and Stressor-Related Disorders"),
  src("src-nice-ng26", "Children's attachment (NG26)", "NICE", "https://www.nice.org.uk/guidance/ng26", 2015, note="Not opened.")],
 "review": REV(["Find a primary prevalence source for institutionalized samples.", "Replace placeholder community with a verified adoption/fostering peer group."], clin=True)})
