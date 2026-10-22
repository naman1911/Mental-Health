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

# ---------- remaining anxiety chapter cards ----------
NIMH = lambda slug, title: src("src-nimh-stats", f"{title} statistics", "National Institute of Mental Health (NIMH)", f"https://www.nimh.nih.gov/health/statistics/{slug}", seen=True)
NICE113 = src("src-nice-cg113", "Generalised anxiety disorder and panic disorder in adults: management (CG113)", "NICE", "https://www.nice.org.uk/guidance/cg113", 2011, seen=True)
NICE159 = src("src-nice-cg159", "Social anxiety disorder: recognition, assessment and treatment (CG159)", "NICE", "https://www.nice.org.uk/guidance/cg159", 2013, seen=True)
NHS_ANX = lambda slug: src("src-nhs", "NHS mental health conditions page", "NHS", f"https://www.nhs.uk/mental-health/conditions/{slug}/", note="Well-known NHS page; not opened.")
STD_SAFETY = {"sensitivity_level": "standard", "show_crisis_strip": False, "content_notes": ["Site-wide crisis link stays one tap away."]}
REV = lambda qs=[], clin=False: {"last_researched": D, "reading_grade_estimate": 0, "reading_grade_method": "Flesch-Kincaid grade, computed on all reader-facing text", "verification_status": "needs_verification", "needs_clinician_signoff": clin, "open_questions": qs}

CARDS.append({
 "topic_id": "panic-disorder", "official_name": "Panic Disorder", "plain_title": "When panic attacks keep coming back",
 "also_known_as": ["panic attacks (the attacks themselves)"], "chapter_id": "anxiety", "card_type": "condition", "icd10cm_code": "F41.0", "language_convention": "person-first",
 "one_liner": "Repeated, unexpected panic attacks, plus ongoing fear of the next one, that change how you live.",
 "in_simple_words": "A panic attack is a sudden wave of intense fear with strong body symptoms: pounding heart, shaking, breathlessness, dizziness, feeling unreal, fear of dying or losing control. It peaks within minutes. Panic disorder is when attacks come out of the blue, again and again, and the person starts living in fear of the next one, often avoiding places or activities. It's frightening but not dangerous, and it's one of the most treatable anxiety conditions.",
 "what_it_can_feel_like": ["I was sure I was having a heart attack. Three ER visits later, they said 'panic'. I didn't believe them.", "The attacks were bad. The fear of the attacks ate my whole life.", "CBT taught me the feelings were a false alarm. Now when one comes, I ride it out."],
 "common_signs": ["Sudden surges of intense fear that peak within minutes", "Racing heart, sweating, trembling, shortness of breath, chest tightness", "Dizziness, chills or hot flushes, numbness, nausea", "Feeling unreal or detached, fear of dying or losing control", "Weeks of worrying about more attacks", "Avoiding places or activities in case an attack happens"],
 "myths_vs_facts": [
  {"myth": "A panic attack can kill you or make you lose your mind.", "fact": "Panic attacks are the body's alarm system firing by mistake. They are intensely unpleasant but not dangerous."},
  {"myth": "You just need to breathe into a paper bag.", "fact": "Slow breathing can help, but the real treatment is learning that the sensations are safe, through CBT."},
  {"myth": "Having had a panic attack means you have panic disorder.", "fact": "Many people have one or two panic attacks in their life. Panic disorder is repeated attacks plus ongoing fear and avoidance."}],
 "how_common": {"plain": "About 3 in 100 US adults have panic disorder in a given year, women more than twice as often as men. Far more people have an occasional panic attack without the disorder.",
  "figure": "2.7% past-year prevalence among US adults (3.8% women, 1.6% men), NCS-R 2001–2003", "source_ref": "src-nimh-stats"},
 "what_helps": {"plain_summary": "CBT for panic disorder is first-line and works well: it teaches what panic is, how to stop fighting the sensations, and how to gradually return to avoided situations. Antidepressants (SSRIs), prescribed and monitored by a doctor, also help. Benzodiazepines are not recommended as a long-term treatment. Cutting back caffeine and getting regular sleep reduce attacks.",
  "evidence_based_options": ["CBT for panic disorder, including interoceptive exposure (safely practising the body sensations)", "Guided self-help based on CBT", "SSRI antidepressants, prescribed and monitored by a doctor", "Gradual return to avoided places and activities"],
  "self_help_that_supports_care": ["Learning the facts about panic, which alone reduces fear", "Slow breathing out, longer than in, during an attack", "Staying in the situation until the wave passes rather than escaping", "Less caffeine, alcohol, and nicotine"],
  "guideline_refs": ["src-nice-cg113"]},
 "when_to_reach_out": "If you've had repeated unexpected panic attacks and are worrying about or avoiding things because of them, see a doctor. A first episode of chest pain should always be checked medically.",
 "is_not": "A single panic attack during a stressful period is not panic disorder. Panic attacks triggered only by a specific fear, like spiders or public speaking, point to a phobia or social anxiety instead.",
 "hope_note": "Panic disorder has one of the best treatment success rates in mental health. Most people who complete CBT get their lives back.",
 "in_young_people": "Panic disorder usually starts in the late teens or twenties but can begin earlier. Teens may describe attacks as 'feeling like I'm dying' and start refusing school or outings.",
 "related_topics": ["agoraphobia", "generalized-anxiety-disorder", "social-anxiety-disorder", "specific-phobia", "depersonalization-derealization-disorder"],
 "glossary_terms": ["panic-attack", "catastrophizing", "avoidance", "exposure-therapy", "cbt", "ssri", "benzodiazepine", "interoception"],
 "safety": STD_SAFETY,
 "visual": {"color_token": "anxiety", "icon": "wind", "illustration_prompt": "Soft line illustration of a person standing on a shoreline as a wave rolls in and gently recedes, feet planted, breathing. Pastel blue and sand. Calm, no distress.", "alt_text": "A person stands calmly on a shoreline as a wave rolls in and gently recedes around their feet."},
 "communities": ["reddit-r-panicattack", "reddit-r-panicdisorder", "adaa-online-support-group", "anxiety-uk-peer-support-groups"],
 "sources": [DSM("Anxiety Disorders"), NIMH("panic-disorder", "Panic Disorder"), NICE113, NHS_ANX("panic-disorder")],
 "review": REV()})

CARDS.append({
 "topic_id": "agoraphobia", "official_name": "Agoraphobia", "plain_title": "When leaving safe places feels impossible",
 "also_known_as": [], "chapter_id": "anxiety", "card_type": "condition", "icd10cm_code": "F40.00", "language_convention": "person-first",
 "one_liner": "Intense fear of places where escape or help might be hard, such as crowds, transport, or being out alone.",
 "in_simple_words": "Agoraphobia is not just 'fear of open spaces'. It's fear and avoidance of situations where you might panic and be unable to get away or get help: buses and trains, queues, shops, crowds, open spaces, or simply being outside the house alone. Many people with agoraphobia have had panic attacks and now avoid wherever one might happen. At its worst, a person's world shrinks to a few rooms. Treatment can open it up again, step by step.",
 "what_it_can_feel_like": ["The supermarket was fine for years. Then one attack in aisle three and I couldn't go back.", "My 'safe zone' got smaller until it was the house, then just the bedroom.", "First trip to the corner shop in two years. I cried in the car park. Good tears."],
 "common_signs": ["Strong fear of two or more: transport, open spaces, enclosed spaces, crowds, being out alone", "Fear that escape would be hard or help unavailable if panic struck", "Avoiding these situations or needing a companion to face them", "Fear out of proportion to any real danger", "Lasting six months or more and limiting daily life"],
 "myths_vs_facts": [
  {"myth": "Agoraphobia means you're afraid of open spaces.", "fact": "It's fear of being stuck somewhere you can't escape or get help, which can include very enclosed places too."},
  {"myth": "People with agoraphobia just like staying home.", "fact": "Most desperately want to go out. The fear, not preference, keeps them in."},
  {"myth": "Once you're housebound, it's permanent.", "fact": "Even severe, long-standing agoraphobia responds to graded exposure. Online and home-based therapy exist for exactly this situation."}],
 "how_common": {"plain": "About 1 in 100 US adults has agoraphobia in a given year. It often begins after panic attacks.",
  "figure": "0.9% past-year prevalence among US adults, NCS-R 2001–2003", "source_ref": "src-nimh-stats"},
 "what_helps": {"plain_summary": "CBT with graded exposure is the main treatment: building a ladder from the easiest feared situation to the hardest and climbing it with support, so the brain learns the places are safe. Where panic attacks are part of it, panic treatment comes too. Antidepressants, prescribed and monitored by a doctor, can help. Therapy can start at home or online if leaving is too hard.",
  "evidence_based_options": ["CBT with graded exposure, in person, at home, or online", "Treatment for panic disorder where present", "SSRI antidepressants, prescribed and monitored by a doctor", "Involving a trusted person as a support in early exposure steps"],
  "self_help_that_supports_care": ["Writing a fear ladder of situations from easiest to hardest", "One small step beyond the current comfort zone, repeated until it feels ordinary", "Not using 'safety behaviours' (like always carrying water) as a crutch forever", "Celebrating every step, however small"],
  "guideline_refs": ["src-nice-cg113"]},
 "when_to_reach_out": "If you are avoiding more and more places, or need someone with you to go out, and it's been going on for months, ask a doctor about CBT. Say if leaving the house for appointments is itself a barrier; services can adapt.",
 "is_not": "Preferring quiet places, or avoiding somewhere after a one-off bad experience, is not agoraphobia. Fear of social judgement points to social anxiety instead.",
 "hope_note": "People who have been housebound for years have recovered. The world comes back one street at a time.",
 "in_young_people": "Agoraphobia usually starts in the late teens or twenties. In teens it can look like refusing school, outings, or public transport after a panic attack.",
 "related_topics": ["panic-disorder", "specific-phobia", "social-anxiety-disorder", "generalized-anxiety-disorder"],
 "glossary_terms": ["avoidance", "exposure-therapy", "panic-attack", "cbt", "ssri"],
 "safety": STD_SAFETY,
 "visual": {"color_token": "anxiety", "icon": "wind", "illustration_prompt": "Soft line illustration of a person stepping out of a front door onto a sunny path, one hand on the door frame, a friend waiting at the gate with a wave. Pastel blue and yellow. Hopeful.", "alt_text": "A person steps out of a front door onto a sunny path while a friend waves from the gate."},
 "communities": ["reddit-r-agoraphobia", "adaa-online-support-group", "anxiety-uk-peer-support-groups"],
 "sources": [DSM("Anxiety Disorders"), NIMH("agoraphobia", "Agoraphobia"), NICE113, NHS_ANX("agoraphobia")],
 "review": REV()})

CARDS.append({
 "topic_id": "social-anxiety-disorder", "official_name": "Social Anxiety Disorder", "plain_title": "When being seen feels dangerous",
 "also_known_as": ["social phobia", "SAD (confusingly, also used for seasonal affective disorder)"], "chapter_id": "anxiety", "card_type": "condition", "icd10cm_code": "F40.10", "language_convention": "person-first",
 "one_liner": "Intense fear of being judged, embarrassed, or rejected in social situations, strong enough to limit life.",
 "in_simple_words": "Everyone feels nervous sometimes about speaking up or meeting new people. Social anxiety disorder is when that fear is so strong and constant that it stops you doing things you want or need to do: talking in class, eating in public, making calls, dating, job interviews. The fear is of being judged and found wanting. The person usually knows it's out of proportion but can't switch it off. It's very common and very treatable.",
 "what_it_can_feel_like": ["I rehearse every sentence before I say it, then replay it for days afterwards.", "People think I'm stuck-up. I'm actually terrified.", "Therapy didn't make me an extrovert. It made the fear small enough to live around."],
 "common_signs": ["Strong fear of situations where you might be watched or judged", "Worrying for days before, and replaying afterwards", "Blushing, shaking, sweating, or a racing heart around people", "Avoiding speaking up, eating in public, phone calls, or meeting new people", "Fear that others will see your anxiety and think less of you", "Lasting six months or more and getting in the way of life"],
 "myths_vs_facts": [
  {"myth": "It's just shyness.", "fact": "Shyness is a normal trait. Social anxiety disorder causes real distress and stops people living the life they want."},
  {"myth": "Pushing people into social situations cures it.", "fact": "Unplanned 'throwing in the deep end' usually makes fear worse. Planned, gradual practice with new ways of thinking is what works."},
  {"myth": "Alcohol helps social anxiety.", "fact": "It takes the edge off for an evening and feeds the anxiety long-term. Many people with social anxiety develop drinking problems this way."}],
 "how_common": {"plain": "About 7 in 100 US adults have social anxiety disorder in a given year. It usually starts in the early teens.",
  "figure": "7.1% past-year prevalence among US adults (8.0% women, 6.1% men), NCS-R 2001–2003", "source_ref": "src-nimh-stats"},
 "what_helps": {"plain_summary": "Individual CBT designed specifically for social anxiety is the first-choice treatment, with strong evidence. It targets the self-focused attention, safety behaviours, and harsh self-judgement that keep the fear going, and includes practising feared situations. Antidepressants (SSRIs), prescribed and monitored by a doctor, are an option if therapy isn't available or isn't enough. Group CBT and parent-supported CBT help young people.",
  "evidence_based_options": ["Individual CBT built for social anxiety disorder", "CBT-based supported self-help as an alternative", "SSRI antidepressants, prescribed and monitored by a doctor", "Group CBT for teenagers; parent-delivered CBT for younger children"],
  "self_help_that_supports_care": ["Shifting attention outward, onto the conversation, not onto yourself", "Dropping one safety behaviour at a time, like avoiding eye contact", "Small planned social experiments, repeated", "Noticing that other people are mostly thinking about themselves"],
  "guideline_refs": ["src-nice-cg159"]},
 "when_to_reach_out": "If fear of being judged is stopping you from school, work, friendships, or everyday tasks, and has for months, talk to a doctor or therapist. You can ask for online or written first contact if phone calls are too hard.",
 "is_not": "Being introverted, reserved, or simply preferring small groups is not a disorder. Nervousness before a performance that doesn't take over life is normal. Fear of all situations with people, from birth, with sensory and communication differences, may point to autism, which can also co-occur.",
 "hope_note": "Social anxiety disorder has excellent treatment outcomes. People who thought they'd never give a talk or go on a date do both.",
 "in_young_people": "Social anxiety usually starts around 13. Teens may refuse school, avoid presentations, or seem rude or withdrawn. Group CBT for teens and parent-supported CBT for children have good evidence. Early treatment prevents years of missed experiences.",
 "across_cultures": "What counts as embarrassing differs by culture. In Japan and Korea, a related pattern called taijin kyofusho centres on fear of offending others rather than embarrassing oneself. In cultures that prize modesty, social anxiety can be mistaken for good manners.",
 "related_topics": ["avoidant-personality-disorder", "generalized-anxiety-disorder", "panic-disorder", "selective-mutism", "autism-spectrum-disorder", "taijin-kyofusho", "alcohol-use-disorder"],
 "glossary_terms": ["shyness-vs-social-anxiety", "avoidance", "cbt", "exposure-therapy", "ssri", "inner-critic", "people-pleasing"],
 "safety": STD_SAFETY,
 "visual": {"color_token": "anxiety", "icon": "wind", "illustration_prompt": "Soft line illustration of a person at a café table mid-conversation with a friend, both relaxed, a spotlight-shaped patch of sunlight on the floor that nobody is looking at. Pastel blue and warm cream.", "alt_text": "Two friends talk at a café table in relaxed poses, with a patch of sunlight on the floor beside them."},
 "communities": ["reddit-r-socialanxiety", "adaa-online-support-group", "anxiety-uk-peer-support-groups", "beyondblue-forums"],
 "sources": [DSM("Anxiety Disorders"), NIMH("social-anxiety-disorder", "Social Anxiety Disorder"), NICE159, NHS_ANX("social-anxiety")],
 "review": REV(["Confirm which SSRIs CG159 names (sources conflicted)."])})

CARDS.append({
 "topic_id": "specific-phobia", "official_name": "Specific Phobia", "plain_title": "When one thing terrifies you out of all proportion",
 "also_known_as": ["phobia", "simple phobia"], "chapter_id": "anxiety", "card_type": "condition", "icd10cm_code": "F40.2xx (by type)", "language_convention": "person-first",
 "one_liner": "Intense, lasting fear of one specific thing or situation, far beyond the real danger, that you avoid or dread.",
 "in_simple_words": "A phobia is a strong fear of a particular thing: animals, heights, flying, needles, blood, vomiting, enclosed spaces, storms. The fear is immediate and out of proportion, and the person goes out of their way to avoid it. Lots of people have fears; it becomes a phobia when it lasts months and limits life, like refusing needed medical care or never visiting family abroad. It's one of the most common and most treatable anxiety conditions.",
 "what_it_can_feel_like": ["I know a spider in the bath can't hurt me. My body doesn't know that.", "I turned down a job because it meant flying. I told everyone it was the money.", "Four sessions of exposure therapy. Thirty years of fear. I still can't believe it."],
 "common_signs": ["Immediate intense fear or panic when facing, or thinking about, the thing", "Avoiding it, or enduring it with great distress", "Fear far bigger than the actual risk", "Lasting six months or more", "Getting in the way of work, health, travel, or relationships"],
 "myths_vs_facts": [
  {"myth": "Phobias are silly and people should just get over them.", "fact": "Phobias are a learned fear response in the brain. Nobody chooses them, and willpower alone rarely shifts them."},
  {"myth": "Treatment means being locked in a room with the thing.", "fact": "Exposure therapy is gradual, planned, and in your control. You never go faster than you agree to."},
  {"myth": "A phobia is just part of who you are.", "fact": "Most specific phobias respond to a short course of exposure therapy, sometimes in a single long session."}],
 "how_common": {"plain": "About 9 in 100 US adults have a specific phobia in a given year, making it the most common anxiety disorder. Women are affected about twice as often.",
  "figure": "9.1% past-year prevalence among US adults (12.2% women, 5.8% men), NCS-R 2001–2003", "source_ref": "src-nimh-stats"},
 "what_helps": {"plain_summary": "Exposure therapy, a form of CBT where you face the feared thing in planned steps until the fear fades, is the treatment with the best evidence, and it often works fast. For blood and needle phobia, a technique called applied tension prevents fainting. Medication is rarely needed. Virtual reality exposure is an option for some phobias, like flying.",
  "evidence_based_options": ["Graded exposure therapy (CBT), sometimes in one extended session", "Applied tension for blood-injection-injury phobia", "Virtual reality exposure where available", "CBT-based self-help for milder phobias"],
  "self_help_that_supports_care": ["Making a step-by-step fear ladder", "Staying with each step until anxiety drops by half, then repeating", "Avoiding reassurance-seeking and escape, which keep fear alive", "Being kind to yourself about how long it has taken to seek help"],
  "guideline_refs": ["src-nhs"]},
 "when_to_reach_out": "If a fear is stopping you doing something that matters, such as getting medical care, travelling, or living where you want, ask a doctor or therapist about exposure therapy. It is short and effective.",
 "is_not": "Disliking something, or sensible caution around real danger, is not a phobia. Fear of many situations because of possible panic is agoraphobia; fear of judgement is social anxiety.",
 "hope_note": "Specific phobias are among the most curable conditions in all of mental health. Help is often a handful of sessions away.",
 "in_young_people": "Fears of the dark, animals, or monsters are a normal part of childhood and usually fade. A phobia in a child is a fear that persists, causes real distress, and interferes with school, sleep, or family life. Children may show it as crying, freezing, or clinging.",
 "sub_sections": [{"title": "Types", "icd10cm_code": "F40.218 / F40.228 / F40.23x / F40.248 / F40.298", "text": "Animal (spiders, dogs); natural environment (heights, storms, water); blood-injection-injury (needles, blood, medical procedures); situational (flying, lifts, enclosed spaces); and other (choking, vomiting, loud sounds, costumed characters). People often have more than one."}],
 "related_topics": ["agoraphobia", "panic-disorder", "social-anxiety-disorder", "generalized-anxiety-disorder"],
 "glossary_terms": ["exposure-therapy", "avoidance", "cbt", "panic-attack"],
 "safety": STD_SAFETY,
 "visual": {"color_token": "anxiety", "icon": "wind", "illustration_prompt": "Soft line illustration of a person climbing a short, sturdy ladder, each rung labelled with a tiny icon, a friend holding the base, blue sky. Pastel blue and mint. No spiders, needles, or threatening imagery.", "alt_text": "A person climbs a short sturdy ladder with a tiny icon on each rung while a friend holds the base."},
 "communities": ["adaa-online-support-group", "anxiety-uk-peer-support-groups", "reddit-r-anxiety"],
 "sources": [DSM("Anxiety Disorders"), NIMH("specific-phobia", "Specific Phobia"), NHS_ANX("phobias")],
 "review": REV(["Find a phobia-specific peer community that passes checks; none confirmed in this session."])})

CARDS.append({
 "topic_id": "separation-anxiety-disorder", "official_name": "Separation Anxiety Disorder", "plain_title": "When being apart feels unbearable",
 "also_known_as": [], "chapter_id": "anxiety", "card_type": "condition", "icd10cm_code": "F93.0", "language_convention": "person-first",
 "one_liner": "Intense, lasting fear of being away from the people you're closest to, beyond what's expected for your age.",
 "in_simple_words": "It's normal for toddlers to cry when a parent leaves. Separation anxiety disorder is when that fear is much stronger, lasts far longer, and shows up past the age when it's expected: a ten-year-old who can't sleep alone or go to school, or an adult who panics when a partner travels. The person fears something terrible will happen to a loved one, or to themselves, while apart. It affects children, teens, and adults, and it responds well to treatment.",
 "what_it_can_feel_like": ["Every school morning was a battle. He wasn't being naughty; he was terrified something would happen to me.", "As an adult I check my partner's location constantly. I hate it, and I can't stop.", "Therapy gave us a plan. Now the goodbyes are short and the days are okay."],
 "common_signs": ["Extreme distress when apart from a parent, partner, or home, or when expecting to be", "Constant worry that harm will come to loved ones, or that something will separate you", "Refusing school, work, or sleepovers; not wanting to sleep alone", "Nightmares about separation", "Headaches or stomach aches when separation is coming", "Lasting at least a month in children or six months in adults"],
 "myths_vs_facts": [
  {"myth": "It's clinginess, and giving in makes it worse.", "fact": "It's real fear. The answer isn't harshness or endless accommodation but a gradual plan, which treatment provides."},
  {"myth": "Only small children get it.", "fact": "Teens and adults have separation anxiety too; adult cases are more common than once thought."},
  {"myth": "Children grow out of it on their own.", "fact": "Some do, but untreated separation anxiety can lead to other anxiety disorders and depression later. Early help is worth it."}],
 "how_common": {"plain": "Around 4 in 100 people have separation anxiety disorder in childhood, and surveys suggest it may be even more common in adults than previously thought.",
  "figure": "Lifetime prevalence 4.1% for childhood-onset and 6.6% for adult cases (NCS-R)", "source_ref": "src-ncsr-sad", "note": "Adult figure from lay interviews without clinical validation; treat as an estimate."},
 "what_helps": {"plain_summary": "CBT is the main treatment, for children often with parents fully involved: learning about anxiety, building coping skills, and practising short separations that get gradually longer. Schools are usually part of the plan. Antidepressants (SSRIs), prescribed and monitored by a doctor, are sometimes used when therapy isn't enough, more often in older children and adults.",
  "evidence_based_options": ["CBT with graded separation practice", "Parent-involved CBT programmes for children", "School-based plans for gradual return", "SSRI antidepressants when needed, prescribed and monitored by a doctor"],
  "self_help_that_supports_care": ["Calm, brief, predictable goodbyes", "Practising short separations and building up", "Not avoiding separations entirely, which strengthens the fear", "For adults: noticing checking behaviours and gently reducing them"],
  "guideline_refs": ["src-nhs"]},
 "when_to_reach_out": "If fear of separation is stopping a child from going to school or sleeping, or stopping an adult from working or letting loved ones live their lives, and it's lasted weeks or months, ask a doctor for help.",
 "is_not": "Normal separation distress in babies and toddlers, missing someone, or worry after a real loss or danger is not a disorder. In adults, fear of a partner leaving as part of a wider pattern may point to other conditions.",
 "hope_note": "With a clear plan and patient practice, children and adults learn that being apart is safe, and that reunions come.",
 "in_young_people": "This is the most common anxiety disorder in young children. School refusal is a frequent sign. Treating it early protects against later anxiety and depression.",
 "related_topics": ["generalized-anxiety-disorder", "panic-disorder", "selective-mutism", "dependent-personality-disorder", "reactive-attachment-disorder"],
 "glossary_terms": ["attachment", "exposure-therapy", "cbt", "avoidance"],
 "safety": STD_SAFETY,
 "visual": {"color_token": "anxiety", "icon": "wind", "illustration_prompt": "Soft line illustration of a child waving from a school gate while a parent waves back from a short distance, a thin kite string connecting a kite above them. Pastel blue and yellow.", "alt_text": "A child waves from a school gate and a parent waves back from a short distance, a kite flying above them."},
 "communities": ["adaa-online-support-group", "anxiety-uk-peer-support-groups"],
 "sources": [DSM("Anxiety Disorders"), src("src-ncsr-sad", "Prevalence of separation anxiety disorder in the National Comorbidity Survey Replication", "American Journal of Psychiatry (Shear et al.)", "https://pubmed.ncbi.nlm.nih.gov/16741209/", 2006, seen=True), NHS_ANX("separation-anxiety")],
 "review": REV(["No separation-anxiety-specific community found; parent-facing anxiety groups to be added when verified.", "Confirm the NHS page slug."])})

CARDS.append({
 "topic_id": "selective-mutism", "official_name": "Selective Mutism", "plain_title": "When a child can talk, but can't in some places",
 "also_known_as": ["SM", "elective mutism (outdated term)"], "chapter_id": "anxiety", "card_type": "condition", "icd10cm_code": "F94.0", "language_convention": "person-first",
 "one_liner": "A child who speaks freely at home but is unable to speak in certain settings, like school, because of anxiety.",
 "in_simple_words": "Selective mutism is an anxiety condition, usually in young children, where a child who chats happily at home finds it impossible to speak in some situations, most often school or with unfamiliar people. It's not stubbornness or a choice; the words freeze in the throat. It often goes with social anxiety and shyness. With the right understanding and gentle, step-by-step help, most children find their voice.",
 "what_it_can_feel_like": ["At home she never stops talking. At school, not a word in two years. Teachers thought she was being difficult.", "I remember wanting to answer so badly. My mouth wouldn't open.", "The speech therapist never pushed. One whisper to a friend, then a word to the teacher. Now she's in the school play."],
 "common_signs": ["Consistently not speaking in specific settings, like school, despite speaking well elsewhere", "Freezing, looking blank, or avoiding eye contact when expected to speak", "Using gestures, nodding, or whispering to a trusted person instead", "Going on for more than a month (not counting the first month of school)", "Getting in the way of learning or friendships"],
 "myths_vs_facts": [
  {"myth": "The child is choosing not to talk.", "fact": "It's a freeze response, not defiance. The old name 'elective mutism' was dropped because it wrongly implied choice."},
  {"myth": "They'll grow out of it if you wait.", "fact": "Some do, but many don't without help, and the longer it goes on the more fixed it becomes. Early support works best."},
  {"myth": "Pressure or bribes will get them talking.", "fact": "Pressure increases anxiety and silence. Removing pressure and building up in tiny steps is what works."}],
 "how_common": {"plain": "Selective mutism is uncommon, affecting roughly 1 in 150 to 1 in 500 children. It usually starts before age five and is often noticed when school begins.",
  "figure": "Point prevalence roughly 0.2%–0.7% of children in studies; estimates vary with age and method", "source_ref": "src-sm-prev", "note": "Epidemiological research is old and small; treat as a range."},
 "what_helps": {"plain_summary": "The main approach is behavioural: reduce pressure to speak, then gradually build up speaking in new places and with new people in tiny steps, often with a speech and language therapist or psychologist and with school fully involved. Parents are part of the plan. Treating social anxiety alongside helps. Medication is rarely needed but may be considered for older children, prescribed and monitored by a doctor.",
  "evidence_based_options": ["Behavioural, step-by-step 'sliding in' and stimulus-fading programmes", "Speech and language therapy and school-based plans", "CBT for the social anxiety that often accompanies it", "SSRI medication in some older children when therapy isn't enough, prescribed and monitored by a doctor"],
  "self_help_that_supports_care": ["Taking the pressure off: no 'say hello', no bribes, no punishments", "Letting the child communicate in any way at first: gestures, writing, whispers", "Arranging low-key playdates in the child's comfort zone", "Keeping everyone, school included, on the same gentle plan"],
  "guideline_refs": ["src-smira"]},
 "when_to_reach_out": "If a child has not spoken at school or in other settings for more than a month, while speaking normally at home, ask the GP, school, or a speech and language therapist for an assessment. Don't wait for them to grow out of it.",
 "is_not": "Being quiet in a new place for a few weeks, not speaking because of a language barrier, or not speaking because of a speech or communication difficulty is not selective mutism.",
 "hope_note": "Children with selective mutism do find their voices, often sooner than their parents dare hope, once the pressure is lifted and the right steps are in place.",
 "in_young_people": "Selective mutism almost always begins in early childhood. Teenagers and adults who still have it usually also have social anxiety disorder and benefit from the same treatments.",
 "across_cultures": "Children learning a new language may be silent for a while; this is normal and not selective mutism. Children from immigrant families are sometimes wrongly diagnosed, and sometimes missed.",
 "related_topics": ["social-anxiety-disorder", "separation-anxiety-disorder", "communication-disorders", "autism-spectrum-disorder"],
 "glossary_terms": ["avoidance", "exposure-therapy", "fight-flight-freeze-fawn", "shyness-vs-social-anxiety"],
 "safety": STD_SAFETY,
 "visual": {"color_token": "anxiety", "icon": "wind", "illustration_prompt": "Soft line illustration of a child and a teacher sitting side by side on a classroom rug, the child whispering to a friendly puppet, a small speech bubble with a single musical note. Pastel blue and mint.", "alt_text": "A child sits on a classroom rug beside a teacher, whispering to a friendly puppet, a single musical note in a speech bubble."},
 "communities": ["smira-selective-mutism-uk"],
 "sources": [DSM("Anxiety Disorders"), src("src-sm-prev", "Anxiety in children with selective mutism: a meta-analysis (and prevalence overview)", "Child Psychiatry & Human Development (2020)", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7067754", 2020, seen=True), src("src-smira", "SMiRA: Selective Mutism Information & Research Association", "SMiRA (UK registered charity 1022673)", "https://www.selectivemutism.org.uk/", seen=True)],
 "review": REV(["Only one community confirmed (SMiRA, UK). Look for the US Selective Mutism Association page."])})
