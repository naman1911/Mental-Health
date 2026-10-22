from helpers import D, src, DSM
CARDS = []

# Anorexia Nervosa ----------
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

# ---------- remaining eating chapter cards ----------
NIMH_ED = src("src-nimh-stats", "Eating Disorders statistics", "National Institute of Mental Health (NIMH)", "https://www.nimh.nih.gov/health/statistics/eating-disorders", seen=True)
NICE69 = src("src-nice-ng69", "Eating disorders: recognition and treatment (NG69)", "NICE", "https://www.nice.org.uk/guidance/ng69", 2017, note="Not opened; recommendations summarized from secondary sources.")
VIS = lambda prompt, alt: {"color_token": "eating", "icon": "leaf", "illustration_prompt": prompt, "alt_text": alt}
HIGH = lambda extra=[]: {"sensitivity_level": "high", "show_crisis_strip": True, "content_notes": ["No numbers: no weights, BMI, calories, or amounts of food.", "No 'how to' behaviours.", "Crisis strip with eating-disorder helplines required."] + extra}
REV = lambda qs=[], clin=True: {"last_researched": D, "reading_grade_estimate": 0, "reading_grade_method": "Flesch-Kincaid grade, computed on all reader-facing text", "verification_status": "needs_human_review" if clin else "needs_verification", "needs_clinician_signoff": clin, "open_questions": qs}

CARDS.append({
 "topic_id": "bulimia-nervosa", "official_name": "Bulimia Nervosa", "plain_title": "Caught in a cycle of bingeing and trying to undo it",
 "also_known_as": ["bulimia", "BN"], "chapter_id": "eating", "card_type": "condition", "icd10cm_code": "F50.2x (by severity, remission)", "language_convention": "person-first",
 "language_convention_note": "'A person with bulimia'. Never 'a bulimic'. No numbers or method detail anywhere on this card.",
 "one_liner": "Repeated episodes of eating a large amount while feeling out of control, followed by harmful attempts to 'undo' it.",
 "in_simple_words": "Bulimia nervosa is a cycle: eating a lot in a short time while feeling unable to stop, then intense guilt and fear of weight gain, then doing something harmful to try to cancel it out. The cycle repeats, often in secret, and self-worth becomes tied to weight and shape. People with bulimia are usually in or above the typical weight range, so it's often invisible from outside. It harms the heart, teeth, and gut, and it is very treatable.",
 "what_it_can_feel_like": ["Nobody knew. I was 'the healthy one'. The bathroom was my secret.", "The binge felt like the only time I wasn't controlling everything. Then the shame hit.", "Guided self-help sounded too simple. It broke the cycle in three months."],
 "common_signs": ["Eating unusually large amounts in a short time, feeling out of control", "Harmful attempts to compensate afterwards, repeated over months", "Secrecy around food, disappearing after meals", "Self-worth driven by weight and body shape", "Swollen cheeks, dental problems, sore throat, tiredness, or dizziness", "Mood swings, shame, and withdrawing from people"],
 "myths_vs_facts": [
  {"myth": "You can tell someone has bulimia by their weight.", "fact": "Most people with bulimia are at a typical weight or above. It is hidden, not visible."},
  {"myth": "It's a way of controlling weight.", "fact": "Compensating does not do what people hope it does, and the cycle usually increases bingeing. It is an illness, not a strategy."},
  {"myth": "It's less serious than anorexia.", "fact": "Bulimia causes serious heart, electrolyte, and dental harm and carries real risk to life. It deserves the same urgency."}],
 "how_common": {"plain": "About 1 in 100 US adults have bulimia nervosa at some point in life, women more often than men, and around 1 in 100 teenagers.",
  "figure": "Lifetime prevalence 1.0% among US adults (NCS-R); 0.9% among adolescents aged 13–18 (NCS-A)", "source_ref": "src-nimh-stats"},
 "what_helps": {"plain_summary": "Specialist talking therapy is the main treatment. For adults, a guided self-help programme based on CBT for eating disorders is often the first step, with full CBT-ED if more is needed. For young people, family therapy focused on bulimia comes first. Some adults also benefit from an antidepressant, prescribed and monitored by a doctor, but medication alone isn't enough. Dental and medical checks are part of care.",
  "evidence_based_options": ["Guided self-help based on CBT for eating disorders (adults)", "CBT for eating disorders (CBT-ED), individual", "Bulimia-focused family therapy for children and young people", "Medical and dental monitoring; an SSRI in some adults, prescribed and monitored by a doctor"],
  "self_help_that_supports_care": ["Regular eating through the day, which cuts the urge to binge", "Telling one person and contacting a helpline", "Delaying the compensating behaviour, even briefly, as a first step", "Muting diet and 'body goals' content"],
  "guideline_refs": ["src-nice-ng69"]},
 "when_to_reach_out": "If you are bingeing and compensating, even occasionally, talk to a doctor or an eating-disorder helpline now; early treatment works best. Get urgent help for chest pain, fainting, or blood when being sick, and if you have thoughts of ending your life.",
 "is_not": "Overeating at a celebration isn't a binge. Bingeing without compensating is binge-eating disorder. Restricting with a low weight, even with bingeing, is anorexia nervosa.",
 "hope_note": "Bulimia has some of the best treatment outcomes of any eating disorder. Many people are free of the cycle within months of starting therapy.",
 "in_young_people": "Bulimia usually begins in the mid to late teens, often after dieting. Parents may notice food disappearing, long bathroom visits, or dental problems. Family-based treatment has the best evidence for young people.",
 "across_cultures": "Bulimia is found in every culture, including where thinness isn't the ideal. Boys, men, and people of colour are under-diagnosed because of stereotypes about who gets eating disorders.",
 "sub_sections": [{"title": "Other specified: low-frequency or limited-duration bulimia; purging disorder", "icd10cm_code": "F50.89", "text": "When the cycle happens less often or has lasted a shorter time, or when a person compensates without bingeing, it is still an eating disorder that needs the same care."}],
 "related_topics": ["binge-eating-disorder", "anorexia-nervosa", "body-dysmorphic-disorder", "major-depressive-disorder", "borderline-personality-disorder", "substance-use-disorders-overview"],
 "glossary_terms": ["binge", "purging", "body-image", "diet-culture", "cbt-e", "family-therapy", "relapse-prevention"],
 "safety": HIGH(),
 "visual": VIS("Soft line illustration of a person setting a small table for a regular meal with a friend, a clock showing midday, plants on the sill. Pastel sage and peach. No food close-ups, no bathroom, no scales.", "A person sets a small table for a midday meal with a friend, plants on the windowsill."),
 "communities": ["beat-uk-helpline-and-online-groups", "butterfly-foundation-helpline", "reddit-r-eatingdisorders", "reddit-r-fuckeatingdisorders", "beat-uk-carers-peer-support"],
 "sources": [DSM("Feeding and Eating Disorders"), NIMH_ED, NICE69],
 "review": REV(["High-sensitivity card: clinician and lived-experience review required."])})

CARDS.append({
 "topic_id": "binge-eating-disorder", "official_name": "Binge-Eating Disorder", "plain_title": "Eating past full, out of control, and alone with the shame",
 "also_known_as": ["BED", "compulsive overeating (older term)"], "chapter_id": "eating", "card_type": "condition", "icd10cm_code": "F50.81x (by severity, remission)", "language_convention": "person-first",
 "language_convention_note": "'A person with binge-eating disorder'. No numbers, no weight talk, no 'how much' descriptions.",
 "one_liner": "Repeated episodes of eating a large amount while feeling out of control, with deep distress, and no compensating afterwards.",
 "in_simple_words": "Binge-eating disorder is the most common eating disorder. A person regularly eats a large amount in a short time, faster than usual, past feeling full, often alone, while feeling unable to stop, and feels disgusted, guilty, or very low afterwards. Unlike bulimia, there's no attempt to 'undo' it. It affects people of all sizes and genders. It isn't greed or lack of willpower; it's a recognized condition closely tied to emotions, dieting, and shame, and it responds well to treatment.",
 "what_it_can_feel_like": ["It wasn't hunger. It was a switch, and then I'd eat until it hurt and hate myself.", "Every diet made it worse. Therapy was the first thing that didn't start with 'eat less'.", "I'd never heard it was a real diagnosis. Finding out was the first relief in twenty years."],
 "common_signs": ["Eating a large amount in a short time, feeling unable to stop", "Eating fast, past full, or when not hungry, often alone out of embarrassment", "Feeling disgusted, depressed, or guilty afterwards", "Happening at least weekly for months", "No regular attempts to compensate afterwards", "Secrecy, shame, and avoiding eating with others"],
 "myths_vs_facts": [
  {"myth": "It's just overeating. Everyone does it.", "fact": "Occasional overeating is normal. Binge-eating disorder means regular episodes with loss of control and real distress. It's a recognized illness."},
  {"myth": "A diet is the solution.", "fact": "Dieting and restriction are among the strongest triggers for bingeing. Treatment focuses on regular eating and the feelings behind bingeing, not on restriction."},
  {"myth": "Only people in larger bodies have it.", "fact": "People of every size have binge-eating disorder. Assuming by size means many people are missed, and many in larger bodies are shamed instead of helped."}],
 "how_common": {"plain": "About 3 in 100 US adults have binge-eating disorder at some point, making it the most common eating disorder. Around 1 or 2 in 100 teenagers are affected.",
  "figure": "Lifetime prevalence 2.8% and past-year 1.2% among US adults (NCS-R); 1.6% lifetime among adolescents (NCS-A)", "source_ref": "src-nimh-stats"},
 "what_helps": {"plain_summary": "Guided self-help based on CBT for eating disorders is the recommended first step for most people and works for many. If more is needed, group or individual CBT for eating disorders follows. Treatment aims at regular, flexible eating, understanding what drives binges, and dismantling shame. Weight loss is not the goal of treatment. Some people also benefit from medication, prescribed and monitored by a doctor, but it isn't first-line.",
  "evidence_based_options": ["Guided self-help based on CBT for eating disorders", "Group CBT-ED, then individual CBT-ED if needed", "Treatment of co-occurring depression, anxiety, or ADHD", "Medication in some cases, prescribed and monitored by a doctor, not as a first step"],
  "self_help_that_supports_care": ["Regular meals and snacks through the day, no skipping", "Noticing the feelings that come before a binge, with curiosity, not blame", "Stepping away from dieting and 'good/bad food' rules", "Support groups where bodies aren't judged"],
  "guideline_refs": ["src-nice-ng69"]},
 "when_to_reach_out": "If you regularly eat in a way that feels out of control and leaves you feeling awful, talk to a doctor or an eating-disorder helpline. Ask for treatment for binge eating, not for weight loss. If you have thoughts of ending your life, use the crisis strip now.",
 "is_not": "Eating a lot at a festival or on a hard day isn't a disorder. Bingeing followed by compensating is bulimia nervosa. Living in a larger body is not, by itself, a sign of any eating disorder.",
 "hope_note": "Binge-eating disorder responds well to treatment, and many people find peace with food for the first time in their lives.",
 "in_young_people": "Binge eating can start in childhood or the teens, often alongside dieting, bullying about weight, or stress. Comments about a young person's body, even well-meant, make it worse. Family support that focuses on feelings and regular meals, not weight, helps.",
 "across_cultures": "Binge-eating disorder is found at similar rates across many countries and ethnic groups, but it is diagnosed far less in some communities because it's hidden or seen as a weight issue rather than a mental health one.",
 "sub_sections": [{"title": "Other specified: low-frequency or limited-duration binge eating; night eating syndrome", "icd10cm_code": "F50.89", "text": "Less frequent bingeing, or a pattern of eating most food at night with distress, still deserves assessment and treatment."}],
 "related_topics": ["bulimia-nervosa", "anorexia-nervosa", "major-depressive-disorder", "adhd", "body-dysmorphic-disorder", "generalized-anxiety-disorder"],
 "glossary_terms": ["binge", "diet-culture", "body-image", "cbt-e", "emotional-dysregulation", "support-group"],
 "safety": HIGH(["Illustration must not show large amounts of food, empty wrappers, or bodies being judged."]),
 "visual": VIS("Soft line illustration of a person on a park bench with a journal, a dog at their feet, a small lunch box closed beside them, autumn leaves. Pastel sage and amber. No food close-ups.", "A person sits on a park bench with a journal and a dog at their feet among autumn leaves."),
 "communities": ["reddit-r-bingeeatingdisorder", "beat-uk-helpline-and-online-groups", "butterfly-foundation-helpline", "reddit-r-eatingdisorders"],
 "sources": [DSM("Feeding and Eating Disorders"), NIMH_ED, NICE69],
 "review": REV(["High-sensitivity card: clinician and lived-experience review required."])})

CARDS.append({
 "topic_id": "avoidant-restrictive-food-intake-disorder", "official_name": "Avoidant/Restrictive Food Intake Disorder", "plain_title": "Eating too little, but not because of weight or shape",
 "also_known_as": ["ARFID", "extreme picky eating (popular term)"], "chapter_id": "eating", "card_type": "condition", "icd10cm_code": "F50.82", "language_convention": "person-first",
 "one_liner": "Eating far too little because of textures, fear of choking, or low interest in food, not because of body image.",
 "in_simple_words": "ARFID is an eating disorder that has nothing to do with wanting to be thin. A person eats far too little, or too few kinds of food, because of sensory issues (textures, smells, colours), fear of something bad happening (choking, vomiting, pain), or little appetite or interest in food. It leads to weight loss or poor growth, nutritional gaps, or big problems with eating socially. It affects children and adults, is common in autistic people, and responds to specialist treatment.",
 "what_it_can_feel_like": ["It's not that I won't eat vegetables. My body reacts to the texture like it's poison.", "After I choked once at nine, I couldn't swallow solid food for a year.", "Everyone called me fussy. ARFID was the first word that didn't make it my fault."],
 "common_signs": ["Eating a very limited range of foods, or very little, over a long time", "Avoidance driven by texture, smell, taste, or appearance", "Fear of choking, vomiting, or pain after a frightening experience", "Little interest in eating, or forgetting to eat", "Weight loss, poor growth, nutritional problems, or needing supplements", "Trouble eating with others, and no fear of weight gain or shape concerns"],
 "myths_vs_facts": [
  {"myth": "It's just picky eating. They'll grow out of it.", "fact": "Ordinary picky eating doesn't harm growth or life. ARFID does, and it often persists without treatment."},
  {"myth": "ARFID is anorexia in disguise.", "fact": "People with ARFID aren't afraid of weight gain and don't have body image concerns. The treatment is different."},
  {"myth": "Forcing or bribing will fix it.", "fact": "Pressure increases fear and avoidance. Gradual, supported exposure to new foods is what works."}],
 "how_common": {"plain": "ARFID is thought to be fairly common, especially in children and in autistic people, but good population figures don't exist yet because the diagnosis is relatively new (2013).",
  "figure": "No reliable general-population estimate; studies in children and young people suggest a few percent, higher in autistic people and in eating-disorder clinics", "source_ref": "src-dsm", "note": "Needs a primary prevalence source once available."},
 "what_helps": {"plain_summary": "Treatment is tailored to the reason for the restriction. For sensory avoidance, gradual, planned exposure to new foods, often with a dietitian and occupational therapist. For fear after choking or vomiting, CBT with graded exposure. For low appetite, structured meals and nutritional support. Children's treatment involves parents closely. Medical monitoring and sometimes supplements or tube feeding keep people safe while progress is made. There is no medication for ARFID itself.",
  "evidence_based_options": ["CBT adapted for ARFID (CBT-AR), with graded food exposure", "Family-based treatment adapted for ARFID in children", "Dietitian and occupational therapy input for sensory and nutritional needs", "Medical monitoring, and nutritional support where needed"],
  "self_help_that_supports_care": ["A 'safe foods' list with no shame attached", "Tiny steps: a new food on the plate, then touched, then tasted", "Separating ARFID from autism sensory needs, with both respected", "Peer support with others who have ARFID, including adults"],
  "guideline_refs": ["src-nice-ng69"]},
 "when_to_reach_out": "If restricted eating is causing weight loss, poor growth, nutritional problems, or stopping someone eating with others, ask a doctor for a referral to an eating-disorder or feeding service and mention ARFID by name. Get urgent help for fainting, severe weakness, or signs of dehydration.",
 "is_not": "Being a picky eater who still grows and eats enough isn't ARFID. Restriction driven by fear of weight gain is anorexia nervosa. Food avoidance caused by a medical condition, allergy, or lack of available food is not ARFID.",
 "hope_note": "People with ARFID expand their safe foods, eat with friends again, and stop living in fear of mealtimes, step by small step.",
 "in_young_people": "ARFID often begins in early childhood and is common in autistic children and children with ADHD. Growth charts flagging a slowdown are often the first clue. Parents are central to treatment and are not to blame.",
 "across_cultures": "ARFID is recognized worldwide but under-diagnosed where 'fussy eating' is seen as behaviour to be disciplined. Safe foods differ by cuisine; treatment should work with the family's food culture.",
 "related_topics": ["anorexia-nervosa", "autism-spectrum-disorder", "specific-phobia", "pica", "obsessive-compulsive-disorder", "generalized-anxiety-disorder"],
 "glossary_terms": ["restriction", "sensory-sensitivity", "interoception", "exposure-therapy", "family-therapy"],
 "safety": HIGH(["Medical risk is described without numbers or weights."]),
 "visual": VIS("Soft line illustration of a child and a dietitian at a table with a 'food ladder' chart, a single new food on a small plate, the child giving a thumbs up. Pastel sage and sky blue. No food close-ups.", "A child and a dietitian sit at a table with a food-ladder chart, the child giving a thumbs up."),
 "communities": ["reddit-r-arfid", "beat-uk-helpline-and-online-groups", "butterfly-foundation-helpline"],
 "sources": [DSM("Feeding and Eating Disorders"), NICE69, src("src-beat-arfid", "ARFID", "Beat (UK)", "https://www.beateatingdisorders.org.uk/get-information-and-support/about-eating-disorders/types/arfid/", note="Not opened.")],
 "review": REV(["Find a prevalence study (for example Kurz et al.).", "Confirm CBT-AR evidence citation."])})

CARDS.append({
 "topic_id": "pica", "official_name": "Pica", "plain_title": "Eating things that aren't food",
 "also_known_as": [], "chapter_id": "eating", "card_type": "condition", "icd10cm_code": "F98.3 (children) / F50.83 (adults)", "language_convention": "person-first",
 "one_liner": "Repeatedly eating non-food substances, like dirt, paper, chalk, or ice, for a month or more, past toddler age.",
 "in_simple_words": "Pica is persistently eating things that aren't food and have no nutritional value: clay, dirt, paper, hair, chalk, paint, ice, and others. Toddlers mouth everything, so pica is only diagnosed from age two. It's most common in children with intellectual disability or autism, and it can also occur in pregnancy and with iron deficiency. The main concerns are safety: poisoning, blockages, infections, and dental damage. Treatment focuses on finding the cause, keeping the person safe, and gentle behavioural approaches.",
 "what_it_can_feel_like": ["I craved ice so badly in pregnancy I was crunching it all day. It turned out my iron was low.", "My son eats paper when he's anxious. The behaviour team helped us see it as a signal, not a problem to punish.", "I was ashamed of eating clay. The doctor just asked what else was going on. That mattered."],
 "common_signs": ["Eating non-food substances regularly for a month or more", "Happening past the age when mouthing is normal (over age two)", "Not part of a cultural or religious practice", "Possible stomach pain, blockages, dental problems, or signs of poisoning", "Often alongside intellectual disability, autism, pregnancy, or iron deficiency"],
 "myths_vs_facts": [
  {"myth": "Pica is just attention-seeking or naughtiness.", "fact": "It's a recognized condition often linked to developmental differences, nutritional deficiencies, stress, or sensory needs. Punishment doesn't help."},
  {"myth": "It's harmless.", "fact": "Depending on what's eaten, pica can cause lead poisoning, blockages, parasites, and tooth damage. Medical checks matter."},
  {"myth": "It only happens in children.", "fact": "Adults have pica too, including during pregnancy and in people with intellectual disabilities."}],
 "how_common": {"plain": "Occasional pica behaviours are not rare, but the disorder itself is uncommon in the general population and much more common in children with autism and intellectual disability.",
  "figure": "About 1% of adults in a German population study reported recurrent pica behaviour; one US study found about 28% of children with both autism and intellectual disability versus under 4% of children generally", "source_ref": "src-pica-prev", "note": "Child figures from a secondary summary of CDC data; needs the primary citation."},
 "what_helps": {"plain_summary": "First, medical assessment: blood tests for iron and other deficiencies, checks for lead or other toxins, and treatment of any blockage. Correcting a deficiency sometimes resolves pica. Then a behavioural approach: working out when and why the eating happens, making the environment safer, offering safe sensory alternatives, and teaching other ways to meet the need. Carers get support and training. Medication is not a treatment for pica itself.",
  "evidence_based_options": ["Medical screening and treatment of deficiencies or poisoning", "Functional behavioural assessment and behaviour support plans", "Environmental safety changes and safe sensory substitutes", "Support and training for parents and carers"],
  "self_help_that_supports_care": ["Keeping risky substances out of reach without turning the home into a fortress", "Offering crunchy or chewy safe foods and chewable items", "Tracking when it happens: time, place, mood", "Telling the dentist and doctor so they can watch for harm"],
  "guideline_refs": ["src-nice-ng11"]},
 "when_to_reach_out": "If a child over two, or an adult, is regularly eating non-food items, see a doctor for blood tests and advice. Get urgent help for severe stomach pain, vomiting, constipation, or if something toxic or sharp has been swallowed.",
 "is_not": "Toddlers mouthing and tasting objects is normal development. Eating clay or other substances as part of a cultural or religious practice isn't a disorder. Craving unusual but edible foods in pregnancy isn't pica.",
 "hope_note": "With the cause found and the environment made safe, pica usually reduces, and families can relax a little.",
 "in_young_people": "Pica is most common in children with developmental disabilities and often appears alongside other sensory behaviours. School and respite settings need to know what the child might eat and how to respond calmly.",
 "across_cultures": "Eating clay or earth (geophagy) is a traditional practice in some parts of Africa, Asia, and the Americas, especially in pregnancy, and the DSM says this is not pica. Assessment should ask about cultural meaning first.",
 "related_topics": ["autism-spectrum-disorder", "intellectual-developmental-disorder", "rumination-disorder", "avoidant-restrictive-food-intake-disorder", "stereotypic-movement-disorder"],
 "glossary_terms": ["sensory-sensitivity", "stimming", "occupational-therapist"],
 "safety": HIGH(["Pica is in the feeding and eating chapter, so the chapter's high-sensitivity rule applies, although body-image content doesn't arise."]),
 "visual": VIS("Soft line illustration of a parent and child in a kitchen choosing from a bowl of crunchy snacks together, a chewable necklace on the child, a doctor's reminder note on the fridge. Pastel sage and peach.", "A parent and child choose crunchy snacks from a bowl in a kitchen, a reminder note on the fridge."),
 "communities": ["nas-online-community"],
 "sources": [DSM("Feeding and Eating Disorders"), src("src-pica-prev", "Prevalence of pica and rumination behaviours in adults and associations with eating disorder and general psychopathology: findings from a population-based study", "Eating and Weight Disorders (PMC9220787)", "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9220787/", 2022, seen=True),
  src("src-nice-ng11", "Challenging behaviour and learning disabilities (NG11)", "NICE", "https://www.nice.org.uk/guidance/ng11", 2015, note="Not opened."),
  src("src-apa-2024-coding", "DSM-5-TR ICD-10-CM coding update, September 2024 (new adult pica code F50.83)", "American Psychiatric Association", "https://www.psychiatry.org/getmedia/172db6ec-8146-4bb4-be2a-49e9c61bcc94/APA-DSM5TR-ICD10CM-Code-Updates-092024.pdf", 2024, seen=True)],
 "review": REV(["Find the primary CDC/autism pica study.", "Replace placeholder community with a verified developmental-disability family group."], clin=False)})

CARDS.append({
 "topic_id": "rumination-disorder", "official_name": "Rumination Disorder", "plain_title": "Bringing food back up and re-chewing it",
 "also_known_as": ["rumination syndrome", "merycism"], "chapter_id": "eating", "card_type": "condition", "icd10cm_code": "F98.21 (children) / F50.84 (adults)", "language_convention": "person-first",
 "one_liner": "Repeatedly bringing swallowed food back up, without nausea, to re-chew, re-swallow, or spit out, for a month or more.",
 "in_simple_words": "Rumination disorder is when swallowed food comes back up into the mouth, easily and without feeling sick, usually soon after eating, and is then chewed again, swallowed again, or spat out. It can happen in infants, in people with intellectual disabilities, and in otherwise healthy children, teens, and adults. It's not deliberate vomiting and not about weight. It's thought to be a learned reflex of the stomach muscles, and it responds well to a simple breathing technique taught by specialists.",
 "what_it_can_feel_like": ["It just comes back up, no effort, no nausea. I thought everyone could do it.", "I avoided eating out for years. Nobody knew why.", "The breathing exercise felt too easy to work. It worked."],
 "common_signs": ["Food coming back up into the mouth soon after meals, without nausea or retching", "Re-chewing, re-swallowing, or spitting out the food", "Going on for a month or more", "Not caused by a stomach condition or another eating disorder", "Weight loss, bad breath, tooth damage, or avoiding social eating"],
 "myths_vs_facts": [
  {"myth": "It's deliberate, like bulimia.", "fact": "Rumination is an involuntary reflex, usually without any wish to lose weight. It's a different condition with a different treatment."},
  {"myth": "It's a stomach disease that needs surgery.", "fact": "Tests are usually normal. The treatment is behavioural, mainly diaphragmatic breathing after meals."},
  {"myth": "Only babies or people with disabilities get it.", "fact": "It occurs in healthy children, teens, and adults too, and is often missed for years."}],
 "how_common": {"plain": "Rumination disorder is uncommon in the general population but is probably under-recognized. It's more common in infants and in people with intellectual disabilities.",
  "figure": "About 0.7% of adults reported recurrent rumination behaviour in a German population study; higher rates in people with intellectual disability", "source_ref": "src-pica-prev"},
 "what_helps": {"plain_summary": "The main treatment is diaphragmatic (belly) breathing, taught by a therapist, dietitian, or gastroenterologist and practised during and after meals; it blocks the muscle reflex that brings food up. Habit reversal approaches and reducing stress around eating help. In infants and people with intellectual disabilities, behavioural approaches and attention to the eating environment are used. Medication is rarely needed. Medical checks rule out reflux and other conditions.",
  "evidence_based_options": ["Diaphragmatic breathing training after meals", "Habit reversal and behavioural approaches", "Medical assessment to rule out reflux or other gut conditions", "Behavioural support and environmental changes for infants and people with intellectual disabilities"],
  "self_help_that_supports_care": ["Practising slow belly breathing for a few minutes after every meal", "Sitting upright after eating", "Keeping a simple diary of when it happens", "Telling the dentist so teeth can be protected"],
  "guideline_refs": ["src-dsm"]},
 "when_to_reach_out": "If food regularly comes back up after meals without nausea, for a month or more, see a doctor. Mention rumination by name; it's often mistaken for reflux or vomiting, and the treatment is different.",
 "is_not": "Reflux (heartburn with acid coming up), vomiting with nausea, or purging driven by fear of weight gain are not rumination disorder. Occasional regurgitation in babies is normal.",
 "hope_note": "Rumination disorder is one of the most treatable conditions in this chapter. Most people improve quickly with the right breathing technique.",
 "in_young_people": "In infants it usually starts between three and twelve months and may resolve. In older children and teens it is often hidden and missed; a tip-off is weight loss or avoiding meals with friends.",
 "related_topics": ["pica", "avoidant-restrictive-food-intake-disorder", "bulimia-nervosa", "intellectual-developmental-disorder", "somatic-symptom-disorder"],
 "glossary_terms": ["habit-reversal-training", "somatic-symptoms"],
 "safety": HIGH(["Chapter-level high-sensitivity rule applies; no body-image content arises."]),
 "visual": VIS("Soft line illustration of a person sitting upright after a meal with one hand on their belly, practising slow breathing, a window open to a garden. Pastel sage and lilac.", "A person sits upright after a meal with a hand on their belly, breathing slowly beside an open window."),
 "communities": ["beat-uk-helpline-and-online-groups"],
 "sources": [DSM("Feeding and Eating Disorders"), src("src-pica-prev", "Prevalence of pica and rumination behaviours in adults (population-based study)", "Eating and Weight Disorders (PMC9220787)", "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9220787/", 2022, seen=True),
  src("src-apa-2024-coding", "DSM-5-TR ICD-10-CM coding update, September 2024 (new adult rumination code F50.84)", "American Psychiatric Association", "https://www.psychiatry.org/getmedia/172db6ec-8146-4bb4-be2a-49e9c61bcc94/APA-DSM5TR-ICD10CM-Code-Updates-092024.pdf", 2024, seen=True)],
 "review": REV(["No rumination-specific community exists; add a gastroenterology patient resource (e.g. IFFGD) after verification."], clin=False)})
