import json, collections
import os, pathlib
ROOT = str(pathlib.Path(__file__).resolve().parents[1])

V = "verified"          # code or name confirmed in an APA/ICD source text seen during this session
N = "needs_verification" # from reference knowledge of DSM-5-TR; to be re-checked when pages can be opened

def t(topic_id, name, code, card_type="condition", folded=None, priority="medium",
      sensitivity="standard", code_status=N, lang="person-first", note=None, cross=None, aka=None):
    d = collections.OrderedDict()
    d["topic_id"] = topic_id
    d["official_name"] = name
    if aka: d["also_known_as"] = aka
    d["icd10cm_code"] = code
    d["card_type"] = card_type
    d["folded_variants"] = [ {"name": n, "icd10cm_code": c} for n, c in (folded or []) ]
    d["section"] = "II"
    d["priority"] = priority
    d["sensitivity_level"] = sensitivity
    d["language_convention"] = lang
    d["code_status"] = code_status
    if note: d["notes"] = note
    if cross: d["cross_listed_in"] = cross
    return d

def ch(chapter_id, num, official, plain, summary, icon, topics, section="II", folds=None, notes=None):
    d = collections.OrderedDict()
    d["chapter_id"] = chapter_id
    d["chapter_number"] = num
    d["section"] = section
    d["official_name"] = official
    d["plain_name"] = plain
    d["plain_summary"] = summary
    d["color_token"] = chapter_id
    d["icon"] = icon
    d["chapter_level_folds"] = [ {"name": n, "icd10cm_code": c, "folded_into": f} for n, c, f in (folds or []) ]
    if notes: d["notes"] = notes
    for x in topics: x["section"] = section
    d["topics"] = topics
    return d

SUB = "substance-medication-induced-mental-disorders"
AMC = "mental-disorders-due-to-another-medical-condition"

chapters = []

# 1 Neurodevelopmental
chapters.append(ch("neurodevelopmental", 1, "Neurodevelopmental Disorders", "Brains that develop differently",
  "Differences in how the brain grows and works that show up early in life and shape learning, attention, movement, communication, and social life.",
  "sprout", [
  t("intellectual-developmental-disorder", "Intellectual Developmental Disorder (Intellectual Disability)",
    "F70–F73 (by severity)", folded=[("Mild", "F70"), ("Moderate", "F71"), ("Severe", "F72"), ("Profound", "F73"),
    ("Global Developmental Delay", "F88"), ("Unspecified Intellectual Developmental Disorder", "F79")],
    priority="medium", note="Severity is set by adaptive functioning, not IQ score alone. Strengths framing required."),
  t("communication-disorders", "Communication Disorders", "F80.x", card_type="condition-group",
    folded=[("Language Disorder", "F80.2"), ("Speech Sound Disorder", "F80.0"),
    ("Social (Pragmatic) Communication Disorder", "F80.82"), ("Unspecified Communication Disorder", "F80.9")],
    priority="low"),
  t("childhood-onset-fluency-disorder", "Childhood-Onset Fluency Disorder (Stuttering)", "F80.81", aka=["Stuttering", "Stammering"],
    priority="medium", note="Adult-onset fluency disorder is coded F98.5 and mentioned as a sub-section."),
  t("autism-spectrum-disorder", "Autism Spectrum Disorder", "F84.0", priority="high", lang="identity-first",
    note="Identity-first ('autistic person') per the preference of most autistic self-advocacy organizations. Strengths framing required."),
  t("adhd", "Attention-Deficit/Hyperactivity Disorder", "F90.x (by presentation)", aka=["ADHD", "ADD (older term)"],
    folded=[("Combined presentation", "F90.2"), ("Predominantly inattentive presentation", "F90.0"),
    ("Predominantly hyperactive/impulsive presentation", "F90.1"), ("Other Specified ADHD", "F90.8"), ("Unspecified ADHD", "F90.9")],
    priority="high", lang="mixed", note="Many adults say 'ADHDer' or 'I have ADHD'; card uses 'person with ADHD' and notes the variety. Strengths framing required."),
  t("specific-learning-disorder", "Specific Learning Disorder", "F81.x (by area)", aka=["Dyslexia", "Dyscalculia", "Dysgraphia"],
    folded=[("With impairment in reading (dyslexia)", "F81.0"), ("With impairment in written expression (dysgraphia)", "F81.81"),
    ("With impairment in mathematics (dyscalculia)", "F81.2")], priority="high", lang="mixed",
    note="'Dyslexic' as identity-first is common and accepted; card notes both. Strengths framing required."),
  t("developmental-coordination-disorder", "Developmental Coordination Disorder", "F82", aka=["Dyspraxia (UK usage)"], priority="low"),
  t("stereotypic-movement-disorder", "Stereotypic Movement Disorder", "F98.4", priority="low"),
  t("tic-disorders", "Tic Disorders (including Tourette's Disorder)", "F95.x", card_type="condition-group", aka=["Tourette syndrome"],
    folded=[("Tourette's Disorder", "F95.2"), ("Persistent (Chronic) Motor or Vocal Tic Disorder", "F95.1"),
    ("Provisional Tic Disorder", "F95.0"), ("Other Specified Tic Disorder", "F95.8"), ("Unspecified Tic Disorder", "F95.9")],
    priority="medium"),
  ], folds=[("Other Specified Neurodevelopmental Disorder", "F88", "chapter intro"), ("Unspecified Neurodevelopmental Disorder", "F89", "chapter intro")]))

# 2 Psychotic
chapters.append(ch("psychotic", 2, "Schizophrenia Spectrum and Other Psychotic Disorders", "Psychosis & schizophrenia",
  "Conditions where a person's mind can lose touch with what is real for a while: hearing or seeing things others don't, or holding firm beliefs that don't match the evidence.",
  "sun-moon", [
  t("understanding-psychosis", "Psychosis (explainer)", "n/a", card_type="explainer", priority="high", sensitivity="elevated",
    note="Not a DSM diagnosis. Explains what psychosis is, early signs, and early-intervention services. Hub for this chapter."),
  t("delusional-disorder", "Delusional Disorder", "F22", sensitivity="elevated"),
  t("brief-psychotic-disorder", "Brief Psychotic Disorder", "F23", sensitivity="elevated"),
  t("schizophreniform-disorder", "Schizophreniform Disorder", "F20.81", sensitivity="elevated", priority="low"),
  t("schizophrenia", "Schizophrenia", "F20.9", priority="high", sensitivity="elevated"),
  t("schizoaffective-disorder", "Schizoaffective Disorder", "F25.x (by type)", folded=[("Bipolar type", "F25.0"), ("Depressive type", "F25.1")],
    sensitivity="elevated"),
  t("catatonia", "Catatonia", "F06.1", card_type="condition-group", sensitivity="elevated", priority="low",
    folded=[("Catatonia Associated With Another Mental Disorder (specifier)", "F06.1"),
    ("Catatonic Disorder Due to Another Medical Condition", "F06.1"), ("Unspecified Catatonia", "F06.1 (code first R29.818)")]),
  ], folds=[("Substance/Medication-Induced Psychotic Disorder", "F1x.x59 (varies by substance)", SUB),
            ("Psychotic Disorder Due to Another Medical Condition", "F06.0 / F06.2", AMC),
            ("Other Specified Schizophrenia Spectrum and Other Psychotic Disorder", "F28", "understanding-psychosis"),
            ("Unspecified Schizophrenia Spectrum and Other Psychotic Disorder", "F29", "understanding-psychosis")],
  notes="Schizotypal (Personality) Disorder is listed in this chapter but its criteria sit in Personality Disorders; it gets its card there."))

# 3 Bipolar
chapters.append(ch("bipolar", 3, "Bipolar and Related Disorders", "Bipolar & mood swings",
  "Conditions where mood and energy swing between very high (mania or hypomania) and very low (depression), far beyond everyday ups and downs.",
  "waves", [
  t("bipolar-i-disorder", "Bipolar I Disorder", "F31.x (by current episode)", priority="high", sensitivity="elevated",
    note="Code depends on current or most recent episode and severity (F31.0–F31.78). Elevated because suicide risk is raised and the card must carry a crisis strip."),
  t("bipolar-ii-disorder", "Bipolar II Disorder", "F31.81", priority="high", sensitivity="elevated"),
  t("cyclothymic-disorder", "Cyclothymic Disorder", "F34.0", priority="medium"),
  ], folds=[("Substance/Medication-Induced Bipolar and Related Disorder", "F1x.x4 (varies)", SUB),
            ("Bipolar and Related Disorder Due to Another Medical Condition", "F06.33 / F06.34", AMC),
            ("Other Specified Bipolar and Related Disorder", "F31.89", "bipolar-ii-disorder"),
            ("Unspecified Bipolar and Related Disorder", "F31.9", "bipolar-ii-disorder")]))

# 4 Depressive
chapters.append(ch("depressive", 4, "Depressive Disorders", "Depression & low mood",
  "When sadness, emptiness, or irritability settles in, drains energy and interest, and gets in the way of daily life.",
  "sunrise", [
  t("disruptive-mood-dysregulation-disorder", "Disruptive Mood Dysregulation Disorder", "F34.81", aka=["DMDD"], priority="medium",
    note="Children and young teens only (diagnosed between ages 6 and 18)."),
  t("major-depressive-disorder", "Major Depressive Disorder", "F32.x / F33.x (single / recurrent, by severity)", aka=["Depression", "Clinical depression", "MDD"],
    priority="high", sensitivity="elevated",
    note="Elevated because of suicide risk; crisis strip required. Specifiers (seasonal pattern, peripartum onset, with anxious distress, with psychotic features) are sub-sections."),
  t("persistent-depressive-disorder", "Persistent Depressive Disorder", "F34.1", aka=["Dysthymia", "PDD"], priority="high", sensitivity="elevated"),
  t("premenstrual-dysphoric-disorder", "Premenstrual Dysphoric Disorder", "F32.81", aka=["PMDD"], priority="high"),
  t("perinatal-depression-and-anxiety", "Perinatal (Peripartum) Depression and Anxiety (explainer)", "n/a (specifier: 'with peripartum onset')", card_type="explainer",
    priority="high", sensitivity="elevated",
    note="Not a separate DSM diagnosis; it is the 'with peripartum onset' specifier for depressive and bipolar episodes. Included because it is one of the most-searched topics and has strong peer communities (for example Postpartum Support International)."),
  ], folds=[("Substance/Medication-Induced Depressive Disorder", "F1x.x4 (varies)", SUB),
            ("Depressive Disorder Due to Another Medical Condition", "F06.31 / F06.32 / F06.34", AMC),
            ("Other Specified Depressive Disorder", "F32.89", "major-depressive-disorder"),
            ("Unspecified Depressive Disorder", "F32.A", "major-depressive-disorder"),
            ("Unspecified Mood Disorder", "F39", "major-depressive-disorder")]))

# 5 Anxiety
chapters.append(ch("anxiety", 5, "Anxiety Disorders", "Anxiety & fear",
  "When worry or fear shows up too often, too strongly, or sticks around, and gets in the way of life.",
  "wind", [
  t("separation-anxiety-disorder", "Separation Anxiety Disorder", "F93.0", priority="medium"),
  t("selective-mutism", "Selective Mutism", "F94.0", priority="medium"),
  t("specific-phobia", "Specific Phobia", "F40.2xx (by type)", folded=[("Animal", "F40.218"), ("Natural environment", "F40.228"),
    ("Blood-injection-injury", "F40.23x"), ("Situational", "F40.248"), ("Other", "F40.298")], priority="high"),
  t("social-anxiety-disorder", "Social Anxiety Disorder", "F40.10", aka=["Social phobia"], priority="high"),
  t("panic-disorder", "Panic Disorder", "F41.0", priority="high", note="'Panic attack' is a specifier, not a diagnosis; covered in the glossary and in this card's 'is_not' field."),
  t("agoraphobia", "Agoraphobia", "F40.00", priority="medium"),
  t("generalized-anxiety-disorder", "Generalized Anxiety Disorder", "F41.1", aka=["GAD"], priority="high"),
  ], folds=[("Substance/Medication-Induced Anxiety Disorder", "F1x.x80 (varies)", SUB),
            ("Anxiety Disorder Due to Another Medical Condition", "F06.4", AMC),
            ("Other Specified Anxiety Disorder", "F41.8", "generalized-anxiety-disorder"),
            ("Unspecified Anxiety Disorder", "F41.9", "generalized-anxiety-disorder")]))

# 6 OCD
chapters.append(ch("ocd-related", 6, "Obsessive-Compulsive and Related Disorders", "Obsessions, compulsions & repeated behaviours",
  "Unwanted thoughts that keep coming back, and repeated actions a person feels driven to do, including picking, pulling, hoarding, and worry about appearance.",
  "repeat", [
  t("obsessive-compulsive-disorder", "Obsessive-Compulsive Disorder", "F42.2", aka=["OCD"], priority="high"),
  t("body-dysmorphic-disorder", "Body Dysmorphic Disorder", "F45.22", aka=["BDD"], priority="high", sensitivity="elevated",
    note="Elevated: high rates of suicidal thoughts in BDD; crisis strip required. Muscle dysmorphia is a sub-section."),
  t("hoarding-disorder", "Hoarding Disorder", "F42.3", priority="medium"),
  t("trichotillomania", "Trichotillomania (Hair-Pulling Disorder)", "F63.3", priority="medium"),
  t("excoriation-disorder", "Excoriation (Skin-Picking) Disorder", "F42.4", aka=["Dermatillomania"], priority="medium"),
  ], folds=[("Substance/Medication-Induced Obsessive-Compulsive and Related Disorder", "F1x.x88 (varies)", SUB),
            ("Obsessive-Compulsive and Related Disorder Due to Another Medical Condition", "F06.8", AMC),
            ("Other Specified Obsessive-Compulsive and Related Disorder (body-focused repetitive behavior disorder, obsessional jealousy, olfactory reference disorder, shubo-kyofu, koro, jikoshu-kyofu)", "F42.8", "obsessive-compulsive-disorder"),
            ("Unspecified Obsessive-Compulsive and Related Disorder", "F42.9", "obsessive-compulsive-disorder")]))

# 7 Trauma
chapters.append(ch("trauma", 7, "Trauma- and Stressor-Related Disorders", "Trauma, stress & loss",
  "What can happen after something frightening, overwhelming, or deeply painful: the mind and body stay on alert, or get stuck, long after the event.",
  "shield", [
  t("reactive-attachment-disorder", "Reactive Attachment Disorder", "F94.1", priority="low", sensitivity="elevated"),
  t("disinhibited-social-engagement-disorder", "Disinhibited Social Engagement Disorder", "F94.2", priority="low", sensitivity="elevated"),
  t("posttraumatic-stress-disorder", "Posttraumatic Stress Disorder", "F43.10", aka=["PTSD"], priority="high", sensitivity="elevated",
    note="Sub-sections: PTSD in children 6 and younger; dissociative subtype; complex PTSD (an ICD-11 diagnosis, not DSM-5-TR) explained in 'is_not' and glossary."),
  t("acute-stress-disorder", "Acute Stress Disorder", "F43.0", priority="medium", sensitivity="elevated"),
  t("adjustment-disorders", "Adjustment Disorders", "F43.2x (by subtype)", folded=[("With depressed mood", "F43.21"), ("With anxiety", "F43.22"),
    ("With mixed anxiety and depressed mood", "F43.23"), ("With disturbance of conduct", "F43.24"),
    ("With mixed disturbance of emotions and conduct", "F43.25"), ("Unspecified", "F43.20")], priority="high"),
  t("prolonged-grief-disorder", "Prolonged Grief Disorder", "F43.81", priority="high", sensitivity="elevated",
    note="New in DSM-5-TR. Printed as F43.8 in the 2022 text; ICD-10-CM F43.81 from 2022-10-01 per the APA September 2022 coding update. Must not pathologize ordinary grief; pairs with the 'grief-and-bereavement' card."),
  ], folds=[("Other Specified Trauma- and Stressor-Related Disorder (adjustment-like disorders, persistent response to trauma with PTSD-like symptoms, ataque de nervios)", "F43.89 (was F43.8)", "posttraumatic-stress-disorder"),
            ("Unspecified Trauma- and Stressor-Related Disorder", "F43.9", "posttraumatic-stress-disorder")]))

# 8 Dissociative
chapters.append(ch("dissociative", 8, "Dissociative Disorders", "Feeling disconnected",
  "When memory, sense of self, or sense of what's real breaks apart or feels far away, often as a way the mind copes with overwhelming stress.",
  "layers", [
  t("dissociative-identity-disorder", "Dissociative Identity Disorder", "F44.81", aka=["DID", "Multiple personality disorder (outdated term)"], priority="high", sensitivity="elevated",
    lang="mixed", note="Many people with DID use 'system' language; card notes this."),
  t("dissociative-amnesia", "Dissociative Amnesia", "F44.0", folded=[("With dissociative fugue", "F44.1")], priority="medium", sensitivity="elevated"),
  t("depersonalization-derealization-disorder", "Depersonalization/Derealization Disorder", "F48.1", aka=["DPDR"], priority="high", sensitivity="elevated"),
  ], folds=[("Other Specified Dissociative Disorder (OSDD)", "F44.89", "dissociative-identity-disorder"),
            ("Unspecified Dissociative Disorder", "F44.9", "dissociative-identity-disorder")]))

# 9 Somatic
chapters.append(ch("somatic", 9, "Somatic Symptom and Related Disorders", "When the body carries the stress",
  "Real physical symptoms, or deep worry about illness, that take over daily life, whatever tests show.",
  "activity", [
  t("somatic-symptom-disorder", "Somatic Symptom Disorder", "F45.1", priority="medium"),
  t("illness-anxiety-disorder", "Illness Anxiety Disorder", "F45.21", aka=["Health anxiety", "Hypochondria (outdated term)"], priority="high"),
  t("functional-neurological-symptom-disorder", "Functional Neurological Symptom Disorder (Conversion Disorder)", "F44.4–F44.7 (by symptom type)", aka=["FND"], priority="medium",
    folded=[("With weakness or paralysis", "F44.4"), ("With abnormal movement", "F44.4"), ("With swallowing symptoms", "F44.4"), ("With speech symptom", "F44.4"),
    ("With attacks or seizures", "F44.5"), ("With anesthesia or sensory loss", "F44.6"), ("With special sensory symptom", "F44.6"), ("With mixed symptoms", "F44.7")]),
  t("psychological-factors-affecting-other-medical-conditions", "Psychological Factors Affecting Other Medical Conditions", "F54", priority="low"),
  t("factitious-disorder", "Factitious Disorder", "F68.10 / F68.A", folded=[("Imposed on self", "F68.10"), ("Imposed on another", "F68.A")],
    priority="low", sensitivity="elevated", note="Imposed on another involves harm to a child or dependent; frame carefully and link to child-protection help."),
  ], folds=[("Other Specified Somatic Symptom and Related Disorder (brief somatic symptom disorder, brief illness anxiety disorder, pseudocyesis)", "F45.8", "somatic-symptom-disorder"),
            ("Unspecified Somatic Symptom and Related Disorder", "F45.9", "somatic-symptom-disorder")]))

# 10 Eating
chapters.append(ch("eating", 10, "Feeding and Eating Disorders", "Eating & food",
  "When eating, food, weight, or body shape take up far too much space in life and start to harm health.",
  "leaf", [
  t("pica", "Pica", "F98.3 (children) / F50.83 (adults)", priority="low", sensitivity="high",
    code_status=V, note="Adult code changed from F50.89 to F50.83 on 2024-10-01 (APA coding update)."),
  t("rumination-disorder", "Rumination Disorder", "F98.21 (children) / F50.84 (adults)", priority="low", sensitivity="high",
    code_status=V, note="Adult code changed from F50.89 to F50.84 on 2024-10-01."),
  t("avoidant-restrictive-food-intake-disorder", "Avoidant/Restrictive Food Intake Disorder", "F50.82", aka=["ARFID"], priority="high", sensitivity="high"),
  t("anorexia-nervosa", "Anorexia Nervosa", "F50.01x / F50.02x (by type, severity, remission)", priority="high", sensitivity="high", code_status=V,
    folded=[("Restricting type", "F50.010–F50.014, F50.019"), ("Binge-eating/purging type", "F50.020–F50.024, F50.029")],
    note="Since 2024-10-01 codes carry severity and remission digits. A correction to severity specifiers is under APA comment until 2026-10-29. The card never states weights or BMI."),
  t("bulimia-nervosa", "Bulimia Nervosa", "F50.2x (by severity, remission)", priority="high", sensitivity="high", code_status=V,
    folded=[("Mild through extreme, in remission, unspecified", "F50.20–F50.25")]),
  t("binge-eating-disorder", "Binge-Eating Disorder", "F50.81x (by severity, remission)", aka=["BED"], priority="high", sensitivity="high", code_status=V,
    folded=[("Mild through extreme, in remission, unspecified", "F50.810–F50.814, F50.819")]),
  ], folds=[("Other Specified Feeding or Eating Disorder (atypical anorexia nervosa, low-frequency bulimia, low-frequency binge eating, purging disorder, night eating syndrome)", "F50.89", "anorexia-nervosa / bulimia-nervosa / binge-eating-disorder as relevant"),
            ("Unspecified Feeding or Eating Disorder", "F50.9", "anorexia-nervosa")],
  notes="Every card in this chapter is high sensitivity: crisis strip on, no numbers about weight, calories, or BMI."))

# 11 Elimination
chapters.append(ch("elimination", 11, "Elimination Disorders", "Bladder & bowel control",
  "Wetting or soiling past the age when most children have gained control. Common, treatable, and nobody's fault.",
  "droplet", [
  t("enuresis", "Enuresis", "F98.0", aka=["Bedwetting"], priority="medium"),
  t("encopresis", "Encopresis", "F98.1", priority="low"),
  ], folds=[("Other Specified Elimination Disorder", "N39.498 (urinary) / R15.9 (fecal)", "enuresis / encopresis"),
            ("Unspecified Elimination Disorder", "R32 (urinary) / R15.9 (fecal)", "enuresis / encopresis")]))

# 12 Sleep
chapters.append(ch("sleep", 12, "Sleep-Wake Disorders", "Sleep",
  "Trouble falling asleep, staying asleep, staying awake, or sleeping at the right times, and the strange things that can happen during sleep.",
  "moon", [
  t("insomnia-disorder", "Insomnia Disorder", "F51.01", priority="high"),
  t("hypersomnolence-disorder", "Hypersomnolence Disorder", "F51.11", priority="low"),
  t("narcolepsy", "Narcolepsy", "G47.41x / G47.42x (by type)", priority="medium",
    folded=[("Narcolepsy with cataplexy or hypocretin deficiency (type 1)", "G47.411"), ("Narcolepsy without cataplexy and either without hypocretin deficiency or hypocretin unmeasured (type 2)", "G47.419"),
    ("Narcolepsy with cataplexy or hypocretin deficiency due to a medical condition", "G47.421"), ("Narcolepsy without cataplexy and without hypocretin deficiency due to a medical condition", "G47.429")]),
  t("breathing-related-sleep-disorders", "Breathing-Related Sleep Disorders", "G47.3x", card_type="condition-group", priority="medium",
    folded=[("Obstructive Sleep Apnea Hypopnea", "G47.33"), ("Central Sleep Apnea", "G47.31 / R06.3 / G47.37"), ("Sleep-Related Hypoventilation", "G47.34 / G47.35 / G47.36")]),
  t("circadian-rhythm-sleep-wake-disorders", "Circadian Rhythm Sleep-Wake Disorders", "G47.2x", card_type="condition-group", priority="medium",
    folded=[("Delayed sleep phase type", "G47.21"), ("Advanced sleep phase type", "G47.22"), ("Irregular sleep-wake type", "G47.23"),
    ("Non-24-hour sleep-wake type", "G47.24"), ("Shift work type", "G47.26"), ("Unspecified type", "G47.20")]),
  t("parasomnias", "Parasomnias (NREM Sleep Arousal Disorders and REM Sleep Behavior Disorder)", "F51.3 / F51.4 / G47.52", card_type="condition-group", priority="medium",
    folded=[("Sleepwalking type", "F51.3"), ("Sleep terror type", "F51.4"), ("Rapid Eye Movement Sleep Behavior Disorder", "G47.52")]),
  t("nightmare-disorder", "Nightmare Disorder", "F51.5", priority="medium"),
  t("restless-legs-syndrome", "Restless Legs Syndrome", "G25.81", priority="medium"),
  ], folds=[("Substance/Medication-Induced Sleep Disorder", "F1x.x82 (varies)", SUB),
            ("Other Specified Insomnia Disorder", "G47.09", "insomnia-disorder"), ("Unspecified Insomnia Disorder", "G47.00", "insomnia-disorder"),
            ("Other Specified Hypersomnolence Disorder", "G47.19", "hypersomnolence-disorder"), ("Unspecified Hypersomnolence Disorder", "G47.10", "hypersomnolence-disorder"),
            ("Other Specified Sleep-Wake Disorder", "G47.8", "chapter intro"), ("Unspecified Sleep-Wake Disorder", "G47.9", "chapter intro")]))

# 13 Sexual dysfunctions
chapters.append(ch("sexual-dysfunctions", 13, "Sexual Dysfunctions", "Sex & intimacy difficulties",
  "Ongoing trouble with desire, arousal, orgasm, or pain during sex that causes distress. Common, and usually helped by treatment.",
  "heart", [
  t("delayed-ejaculation", "Delayed Ejaculation", "F52.32", priority="low", sensitivity="elevated"),
  t("erectile-disorder", "Erectile Disorder", "F52.21", priority="medium", sensitivity="elevated"),
  t("female-orgasmic-disorder", "Female Orgasmic Disorder", "F52.31", priority="medium", sensitivity="elevated"),
  t("female-sexual-interest-arousal-disorder", "Female Sexual Interest/Arousal Disorder", "F52.22", priority="medium", sensitivity="elevated"),
  t("genito-pelvic-pain-penetration-disorder", "Genito-Pelvic Pain/Penetration Disorder", "F52.6", aka=["Vaginismus and dyspareunia (older terms)"], priority="medium", sensitivity="elevated"),
  t("male-hypoactive-sexual-desire-disorder", "Male Hypoactive Sexual Desire Disorder", "F52.0", priority="low", sensitivity="elevated"),
  t("premature-early-ejaculation", "Premature (Early) Ejaculation", "F52.4", priority="medium", sensitivity="elevated"),
  ], folds=[("Substance/Medication-Induced Sexual Dysfunction", "F1x.x81 (varies)", SUB),
            ("Other Specified Sexual Dysfunction", "F52.8", "chapter intro"), ("Unspecified Sexual Dysfunction", "F52.9", "chapter intro")],
  notes="Elevated sensitivity for the sexual-content rule (clinical-neutral tone), not for crisis risk. Crisis strip still shown per the project rule for elevated cards."))

# 14 Gender dysphoria
chapters.append(ch("gender-dysphoria", 14, "Gender Dysphoria", "Gender dysphoria",
  "The distress some people feel when the gender they know themselves to be doesn't match the sex they were assigned at birth. Being transgender is not a disorder; the distress is what this chapter is about.",
  "rainbow", [
  t("gender-dysphoria", "Gender Dysphoria", "F64.0 (adolescents and adults) / F64.2 (children)", priority="high", sensitivity="elevated", lang="identity-first",
    folded=[("Gender Dysphoria in Children", "F64.2"), ("Gender Dysphoria in Adolescents and Adults", "F64.0"),
    ("Other Specified Gender Dysphoria", "F64.8"), ("Unspecified Gender Dysphoria", "F64.9")],
    note="Identity-first ('trans person', 'transgender people') per community preference. Note that ICD-11 uses 'gender incongruence' outside the mental-disorders chapter. Elevated because of high suicide-risk statistics in trans youth; crisis strip required."),
  ]))

# 15 Disruptive
chapters.append(ch("disruptive", 15, "Disruptive, Impulse-Control, and Conduct Disorders", "Anger, impulses & behaviour",
  "When controlling anger, urges, or actions is a real struggle, in a way that hurts the person or the people around them.",
  "compass", [
  t("oppositional-defiant-disorder", "Oppositional Defiant Disorder", "F91.3", aka=["ODD"], priority="medium"),
  t("intermittent-explosive-disorder", "Intermittent Explosive Disorder", "F63.81", aka=["IED"], priority="medium"),
  t("conduct-disorder", "Conduct Disorder", "F91.x (by onset)", folded=[("Childhood-onset type", "F91.1"), ("Adolescent-onset type", "F91.2"), ("Unspecified onset", "F91.9")],
    priority="medium", note="Stigma risk: frame as a pattern that often follows adversity and is treatable, not a label for 'bad kids'."),
  t("pyromania", "Pyromania", "F63.1", priority="low"),
  t("kleptomania", "Kleptomania", "F63.2", priority="low"),
  ], folds=[("Other Specified Disruptive, Impulse-Control, and Conduct Disorder", "F91.8", "chapter intro"),
            ("Unspecified Disruptive, Impulse-Control, and Conduct Disorder", "F91.9", "chapter intro")],
  notes="Antisocial Personality Disorder is listed here but its criteria sit in Personality Disorders; it gets its card there."))

# 16 Substance
chapters.append(ch("substance", 16, "Substance-Related and Addictive Disorders", "Alcohol, drugs & gambling",
  "When using a substance, or gambling, becomes hard to control and keeps causing problems, and what recovery can look like.",
  "anchor", [
  t("substance-use-disorders-overview", "Substance Use Disorders (explainer)", "n/a", card_type="explainer", priority="high", sensitivity="elevated",
    note="Explains what a 'use disorder' is, severity levels (mild, moderate, severe), intoxication, withdrawal, and remission. Hub for this chapter."),
  t("alcohol-use-disorder", "Alcohol Use Disorder", "F10.10 (mild) / F10.20 (moderate, severe)", aka=["Alcoholism (older term)"], priority="high", sensitivity="elevated",
    folded=[("Alcohol Intoxication", "F10.x20 (varies)"), ("Alcohol Withdrawal", "F10.x30 / F10.x31 (varies)"), ("Alcohol-induced mental disorders", "varies")]),
  t("caffeine-related-disorders", "Caffeine-Related Disorders", "F15.920 / F15.93", card_type="condition-group", priority="low",
    folded=[("Caffeine Intoxication", "F15.920"), ("Caffeine Withdrawal", "F15.93")],
    note="Caffeine Use Disorder is a Section III condition for further study and has its own card there."),
  t("cannabis-use-disorder", "Cannabis Use Disorder", "F12.10 (mild) / F12.20 (moderate, severe)", priority="high", sensitivity="elevated",
    folded=[("Cannabis Intoxication", "F12.x20 (varies)"), ("Cannabis Withdrawal", "F12.x3 (varies)")]),
  t("hallucinogen-related-disorders", "Hallucinogen-Related Disorders", "F16.10 / F16.20", card_type="condition-group", priority="medium", sensitivity="elevated",
    folded=[("Phencyclidine Use Disorder", "F16.10 / F16.20"), ("Other Hallucinogen Use Disorder", "F16.10 / F16.20"),
    ("Phencyclidine Intoxication", "F16.x20 (varies)"), ("Other Hallucinogen Intoxication", "F16.x20 (varies)"), ("Hallucinogen Persisting Perception Disorder", "F16.983")]),
  t("inhalant-use-disorder", "Inhalant Use Disorder", "F18.10 (mild) / F18.20 (moderate, severe)", priority="low", sensitivity="elevated",
    folded=[("Inhalant Intoxication", "F18.x20 (varies)")]),
  t("opioid-use-disorder", "Opioid Use Disorder", "F11.10 (mild) / F11.20 (moderate, severe)", priority="high", sensitivity="elevated",
    folded=[("Opioid Intoxication", "F11.x2 (varies)"), ("Opioid Withdrawal", "F11.x3 (varies)")]),
  t("sedative-hypnotic-anxiolytic-use-disorder", "Sedative, Hypnotic, or Anxiolytic Use Disorder", "F13.10 (mild) / F13.20 (moderate, severe)", aka=["Benzodiazepine use disorder"], priority="medium", sensitivity="elevated",
    folded=[("Sedative, Hypnotic, or Anxiolytic Intoxication", "F13.x20 (varies)"), ("Sedative, Hypnotic, or Anxiolytic Withdrawal", "F13.x3 (varies)")]),
  t("stimulant-use-disorder", "Stimulant Use Disorder", "F15.10 / F15.20 (amphetamine-type) ; F14.10 / F14.20 (cocaine)", priority="high", sensitivity="elevated",
    folded=[("Amphetamine-type substance use disorder", "F15.10 / F15.20"), ("Cocaine use disorder", "F14.10 / F14.20"), ("Other or unspecified stimulant use disorder", "F15.10 / F15.20"),
    ("Stimulant Intoxication", "varies"), ("Stimulant Withdrawal", "varies")]),
  t("tobacco-use-disorder", "Tobacco Use Disorder", "Z72.0 (mild) / F17.20x (moderate, severe)", aka=["Nicotine dependence", "Vaping dependence"], priority="high",
    folded=[("Tobacco Withdrawal", "F17.203")]),
  t("other-or-unknown-substance-use-disorder", "Other (or Unknown) Substance Use Disorder", "F19.10 (mild) / F19.20 (moderate, severe)", priority="low", sensitivity="elevated"),
  t("gambling-disorder", "Gambling Disorder", "F63.0", priority="high", sensitivity="elevated", note="The only non-substance addictive disorder in Section II."),
  t(SUB, "Substance/Medication-Induced Mental Disorders (explainer)", "varies by substance and disorder", card_type="explainer", priority="medium", sensitivity="elevated",
    note="One cross-chapter card for the substance- or medication-induced psychotic, bipolar, depressive, anxiety, obsessive-compulsive, sleep, sexual, delirium and neurocognitive variants."),
  ], notes="No dosing, sourcing, or use instructions on any card. Harm-reduction pointers only to official organizations. Section II lists 'tobacco' rather than 'nicotine'; the card explains that vaping counts."))

# 17 Neurocognitive
chapters.append(ch("neurocognitive", 17, "Neurocognitive Disorders", "Memory, thinking & dementia",
  "Changes in memory, attention, language, or judgment caused by a brain condition, from sudden confusion to the slow changes of dementia.",
  "lamp", [
  t("delirium", "Delirium", "F05 (due to another medical condition); others vary", priority="medium", sensitivity="elevated",
    folded=[("Substance Intoxication Delirium", "varies"), ("Substance Withdrawal Delirium", "varies"), ("Medication-Induced Delirium", "varies"),
    ("Delirium Due to Another Medical Condition", "F05"), ("Delirium Due to Multiple Etiologies", "F05 + others"), ("Other Specified Delirium", "R41.0"), ("Unspecified Delirium", "R41.0")]),
  t("major-and-mild-neurocognitive-disorder", "Major and Mild Neurocognitive Disorder (explainer)", "F02.8x / F02.A–C (major); G31.84 (mild); varies by cause", card_type="explainer", priority="high",
    note="Explains what 'neurocognitive disorder' and 'dementia' mean, major vs mild, and how codes depend on cause, severity and behavioural features (ICD-10-CM severity codes F02.A/B/C and F01.A/B/C from 2022-10-01)."),
  t("alzheimers-disease-neurocognitive-disorder", "Neurocognitive Disorder Due to Alzheimer's Disease", "G30.9 + F02.8x (major); G31.84 (mild)", aka=["Alzheimer's disease"], priority="high"),
  t("frontotemporal-neurocognitive-disorder", "Frontotemporal Neurocognitive Disorder", "G31.09 + F02.8x (major); G31.84 (mild)", aka=["Frontotemporal dementia", "FTD"], priority="medium"),
  t("lewy-body-neurocognitive-disorder", "Neurocognitive Disorder With Lewy Bodies", "G31.83 + F02.8x (major); G31.84 (mild)", aka=["Lewy body dementia"], priority="medium"),
  t("vascular-neurocognitive-disorder", "Vascular Neurocognitive Disorder", "F01.5x / F01.A–C (major); G31.84 (mild)", aka=["Vascular dementia"], priority="medium"),
  t("traumatic-brain-injury-neurocognitive-disorder", "Neurocognitive Disorder Due to Traumatic Brain Injury", "S06.2X9S + F02.8x (major); G31.84 (mild)", aka=["TBI"], priority="medium"),
  t("parkinsons-disease-neurocognitive-disorder", "Neurocognitive Disorder Due to Parkinson's Disease", "G20.x + F02.8x (major); G31.84 (mild)", priority="medium"),
  t("huntingtons-disease-neurocognitive-disorder", "Neurocognitive Disorder Due to Huntington's Disease", "G10 + F02.8x (major); G31.84 (mild)", priority="low"),
  t("neurocognitive-disorder-other-causes", "Neurocognitive Disorders Due to Other Causes", "varies", card_type="condition-group", priority="low",
    folded=[("Substance/Medication-Induced Neurocognitive Disorder", "varies"), ("Neurocognitive Disorder Due to HIV Infection", "B20 + F02.8x"),
    ("Neurocognitive Disorder Due to Prion Disease", "A81.9 + F02.8x"), ("Neurocognitive Disorder Due to Another Medical Condition", "varies + F02.8x"),
    ("Neurocognitive Disorder Due to Multiple Etiologies", "varies"), ("Unspecified Neurocognitive Disorder", "R41.9")]),
  ]))

# 18 Personality
chapters.append(ch("personality", 18, "Personality Disorders", "Personality & patterns of relating",
  "Long-standing patterns in how a person thinks, feels, and relates to others that cause real distress or trouble. These are treatable, and the labels have often been misused.",
  "fingerprint", [
  t("about-personality-disorders", "Personality Disorders (explainer: general criteria, clusters, and stigma)", "n/a", card_type="explainer", priority="high",
    note="Covers the DSM-5-TR general definition, the three clusters, why the labels are controversial, and that treatment works."),
  t("paranoid-personality-disorder", "Paranoid Personality Disorder", "F60.0", priority="low", note="Cluster A"),
  t("schizoid-personality-disorder", "Schizoid Personality Disorder", "F60.1", priority="low", note="Cluster A"),
  t("schizotypal-personality-disorder", "Schizotypal Personality Disorder", "F21", priority="low", note="Cluster A. Also listed in the psychotic disorders chapter.", cross=["psychotic"]),
  t("antisocial-personality-disorder", "Antisocial Personality Disorder", "F60.2", aka=["ASPD"], priority="medium", note="Cluster B. Also listed in the disruptive disorders chapter. High stigma; avoid 'psychopath'/'sociopath' labels.", cross=["disruptive"]),
  t("borderline-personality-disorder", "Borderline Personality Disorder", "F60.3", aka=["BPD", "Emotionally unstable personality disorder (ICD-10 term)"], priority="high", sensitivity="elevated",
    note="Cluster B. Elevated for suicide and self-harm risk; crisis strip required. DBT and other treatments work; say so."),
  t("histrionic-personality-disorder", "Histrionic Personality Disorder", "F60.4", priority="low", note="Cluster B"),
  t("narcissistic-personality-disorder", "Narcissistic Personality Disorder", "F60.81", aka=["NPD"], priority="medium", note="Cluster B. Widely misused online as an insult; card addresses this."),
  t("avoidant-personality-disorder", "Avoidant Personality Disorder", "F60.6", aka=["AvPD"], priority="medium", note="Cluster C"),
  t("dependent-personality-disorder", "Dependent Personality Disorder", "F60.7", priority="low", note="Cluster C"),
  t("obsessive-compulsive-personality-disorder", "Obsessive-Compulsive Personality Disorder", "F60.5", aka=["OCPD"], priority="medium", note="Cluster C. Not the same as OCD; card explains the difference."),
  ], folds=[("Personality Change Due to Another Medical Condition", "F07.0", AMC),
            ("Other Specified Personality Disorder", "F60.89", "about-personality-disorders"), ("Unspecified Personality Disorder", "F60.9", "about-personality-disorders")],
  notes="All cards in this chapter go on the 'needs human review' list."))

# 19 Paraphilic
chapters.append(ch("paraphilic", 19, "Paraphilic Disorders", "Unusual sexual interests that cause harm or distress",
  "An unusual sexual interest on its own is not a disorder. It becomes one when it causes the person serious distress, or harms or risks harming someone else.",
  "scale", [
  t("paraphilic-disorders-overview", "Paraphilic Disorders (explainer: interest vs disorder)", "n/a", card_type="explainer", priority="medium", sensitivity="elevated",
    note="Hub card. Explains the paraphilia vs paraphilic disorder distinction in neutral clinical language."),
  t("courtship-paraphilic-disorders", "Voyeuristic, Exhibitionistic, and Frotteuristic Disorders", "F65.3 / F65.2 / F65.81", card_type="condition-group", priority="low", sensitivity="elevated",
    folded=[("Voyeuristic Disorder", "F65.3"), ("Exhibitionistic Disorder", "F65.2"), ("Frotteuristic Disorder", "F65.81")]),
  t("sexual-masochism-and-sadism-disorders", "Sexual Masochism Disorder and Sexual Sadism Disorder", "F65.51 / F65.52", card_type="condition-group", priority="low", sensitivity="elevated",
    folded=[("Sexual Masochism Disorder", "F65.51"), ("Sexual Sadism Disorder", "F65.52")],
    note="Must distinguish consensual kink (not a disorder) from the disorder."),
  t("pedophilic-disorder", "Pedophilic Disorder", "F65.4", priority="medium", sensitivity="elevated",
    note="Own card because prevention-focused help exists (for example Stop It Now). Communities only from professional or recognized nonprofit sources."),
  t("fetishistic-and-transvestic-disorders", "Fetishistic Disorder and Transvestic Disorder", "F65.0 / F65.1", card_type="condition-group", priority="low", sensitivity="elevated",
    folded=[("Fetishistic Disorder", "F65.0"), ("Transvestic Disorder", "F65.1")],
    note="Must not conflate cross-dressing or being transgender with a disorder."),
  ], folds=[("Other Specified Paraphilic Disorder", "F65.89", "paraphilic-disorders-overview"), ("Unspecified Paraphilic Disorder", "F65.9", "paraphilic-disorders-overview")],
  notes="Grouping decision for user approval: 8 DSM diagnoses folded into 4 cards plus an explainer. Clinical-neutral tone; no explicit content."))

# 20 Other mental disorders
chapters.append(ch("other-mental-disorders", 20, "Other Mental Disorders and Additional Codes", "When it doesn't fit a label",
  "Codes for when something is clearly wrong but doesn't match a named condition, or when a medical illness is causing mental symptoms.",
  "circle-help", [
  t(AMC, "Mental Disorders Due to Another Medical Condition (explainer)", "F06.x / F07.0 / F09 (varies)", card_type="explainer", priority="medium",
    note="One cross-chapter card for all 'due to another medical condition' variants (psychotic, bipolar, depressive, anxiety, obsessive-compulsive, personality change, catatonic, and the 'other specified' and 'unspecified' versions)."),
  t("when-it-doesnt-fit-a-label", "Other Specified and Unspecified Mental Disorder; No Diagnosis (explainer)", "F99 / Z03.89", card_type="explainer", priority="low",
    folded=[("Other Specified Mental Disorder", "F99"), ("Unspecified Mental Disorder", "F99"), ("No Diagnosis or Condition", "Z03.89")]),
  ]))

# 21 Medication-induced
chapters.append(ch("medication-induced", 21, "Medication-Induced Movement Disorders and Other Adverse Effects of Medication", "Medication side effects",
  "Movement problems and other effects that some psychiatric medicines can cause. Knowing the signs helps you and your doctor act early.",
  "stethoscope", [
  t("medication-induced-movement-disorders", "Medication-Induced Movement Disorders", "G21.x / G24.x / G25.x", card_type="condition-group", priority="medium",
    folded=[("Medication-Induced Parkinsonism (antipsychotic or other dopamine receptor blocking agent)", "G21.11"), ("Other Medication-Induced Parkinsonism", "G21.19"),
    ("Medication-Induced Acute Dystonia", "G24.02"), ("Medication-Induced Acute Akathisia", "G25.71"), ("Tardive Dyskinesia", "G24.01"),
    ("Tardive Dystonia", "G24.09"), ("Tardive Akathisia", "G25.71"), ("Medication-Induced Postural Tremor", "G25.1"), ("Other Medication-Induced Movement Disorder", "G25.79")]),
  t("neuroleptic-malignant-syndrome", "Neuroleptic Malignant Syndrome", "G21.0", priority="medium", sensitivity="elevated", note="Medical emergency; card leads with 'call emergency services'."),
  t("antidepressant-discontinuation-syndrome", "Antidepressant Discontinuation Syndrome", "T43.205A / D / S", priority="high",
    note="Commonly searched. Card stresses never stopping medication suddenly without a doctor's plan; no dosing or taper schedules."),
  ], folds=[("Other Adverse Effect of Medication", "T50.905A / D / S", "medication-induced-movement-disorders")]))

# 22 Other conditions (Z codes etc.)
chapters.append(ch("clinical-focus", 22, "Other Conditions That May Be a Focus of Clinical Attention", "Life situations that affect mental health",
  "Not illnesses, but things happening in a person's life, like abuse, grief, money, housing, or school trouble, that a clinician may note and help with.",
  "life-buoy", [
  t("suicidal-thoughts-and-behavior", "Suicidal Behavior (symptom codes)", "T14.91XA / T14.91XD (current) ; Z91.51 (history)", card_type="clinical-focus", priority="high", sensitivity="high", code_status=V,
    folded=[("Current Suicidal Behavior, initial encounter", "T14.91XA"), ("Current Suicidal Behavior, subsequent encounter", "T14.91XD"), ("History of Suicidal Behavior", "Z91.51")],
    note="New symptom codes in DSM-5-TR. Written to safe-messaging rules; leads with crisis help; no methods."),
  t("nonsuicidal-self-injury", "Nonsuicidal Self-Injury (symptom codes)", "R45.88 (current) ; Z91.52 (history)", card_type="clinical-focus", priority="high", sensitivity="high", code_status=V,
    folded=[("Current Nonsuicidal Self-Injury", "R45.88"), ("History of Nonsuicidal Self-Injury", "Z91.52")]),
  t("grief-and-bereavement", "Uncomplicated Bereavement", "Z63.4", card_type="clinical-focus", priority="high", sensitivity="elevated",
    note="Ordinary grief is not a disorder. Pairs with prolonged-grief-disorder and must make the difference clear without judging anyone's grief."),
  t("family-and-relationship-problems", "Relational Problems", "Z62.x / Z63.x", card_type="clinical-focus", priority="high",
    folded=[("Parent-Child Relational Problem", "Z62.820 / Z62.821 / Z62.822 / Z62.898"), ("Sibling Relational Problem", "Z62.891"), ("Upbringing Away From Parents", "Z62.29"),
    ("Child Affected by Parental Relationship Distress", "Z63.8"), ("Relationship Distress With Spouse or Intimate Partner", "Z63.0"),
    ("Disruption of Family by Separation or Divorce", "Z63.5"), ("High Expressed Emotion Level Within Family", "Z63.8")]),
  t("child-abuse-and-neglect", "Child Maltreatment and Neglect", "T74.x / T76.x / Z62.81x / Z69.x (varies)", card_type="clinical-focus", priority="high", sensitivity="high",
    folded=[("Child Physical Abuse", "T74.12XA (confirmed) / T76.12XA (suspected)"), ("Child Sexual Abuse", "T74.22XA / T76.22XA"),
    ("Child Neglect", "T74.02XA / T76.02XA"), ("Child Psychological Abuse", "T74.32XA / T76.32XA")],
    note="Representative codes; the DSM lists further codes for encounters, history and perpetrators. Frame as a situation with help available, never as the child's fault."),
  t("partner-violence-and-adult-abuse", "Adult Maltreatment and Neglect", "T74.x / T76.x / Z69.x / Z91.4x (varies)", card_type="clinical-focus", priority="high", sensitivity="high",
    folded=[("Spouse or Partner Violence, Physical", "T74.11XA / T76.11XA"), ("Spouse or Partner Violence, Sexual", "T74.21XA / T76.21XA"),
    ("Spouse or Partner Neglect", "T74.01XA / T76.01XA"), ("Spouse or Partner Abuse, Psychological", "T74.31XA / T76.31XA"),
    ("Adult Abuse by Nonspouse or Nonpartner", "T74.x1XA / T76.x1XA")],
    note="Representative codes. Links to domestic-violence helplines in each region."),
  t("school-and-work-problems", "Educational and Occupational Problems", "Z55.x / Z56.x", card_type="clinical-focus", priority="medium",
    folded=[("Academic or Educational Problem", "Z55.9"), ("Problem Related to Current Military Deployment Status", "Z56.82"), ("Other Problem Related to Employment", "Z56.9")]),
  t("housing-and-money-problems", "Housing and Economic Problems", "Z59.x", card_type="clinical-focus", priority="medium",
    folded=[("Homelessness (sheltered, unsheltered)", "Z59.01 / Z59.02"), ("Inadequate Housing", "Z59.10 / Z59.11 / Z59.12 / Z59.19"), ("Discord With Neighbor, Lodger, or Landlord", "Z59.2"),
    ("Problem Related to Living in a Residential Institution", "Z59.3"), ("Lack of Adequate Food or Safe Drinking Water", "Z59.41 / Z58.6"), ("Extreme Poverty", "Z59.5"),
    ("Low Income", "Z59.6"), ("Insufficient Social or Health Insurance or Welfare Support", "Z59.7"), ("Unspecified Housing or Economic Problem", "Z59.9")],
    note="Z59 sub-codes were expanded by ICD-10-CM in 2021–2022; exact list needs verification."),
  t("social-environment-and-identity-stress", "Problems Related to the Social Environment", "Z60.x / Z65.8", card_type="clinical-focus", priority="medium",
    folded=[("Phase of Life Problem", "Z60.0"), ("Problem Related to Living Alone", "Z60.2"), ("Acculturation Difficulty", "Z60.3"),
    ("Social Exclusion or Rejection", "Z60.4"), ("Target of (Perceived) Adverse Discrimination or Persecution", "Z60.5"), ("Religious or Spiritual Problem", "Z65.8")]),
  t("crime-disaster-and-legal-problems", "Problems Related to Crime, Disaster, War, and the Legal System", "Z65.x", card_type="clinical-focus", priority="medium", sensitivity="elevated",
    folded=[("Conviction in Civil or Criminal Proceedings Without Imprisonment", "Z65.0"), ("Imprisonment or Other Incarceration", "Z65.1"), ("Problems Related to Release From Prison", "Z65.2"),
    ("Problems Related to Other Legal Circumstances", "Z65.3"), ("Victim of Crime", "Z65.4"), ("Victim of Terrorism or Torture", "Z65.4"), ("Exposure to Disaster, War, or Other Hostilities", "Z65.5")]),
  t("health-care-access-and-treatment-adherence", "Problems Related to Access to Care and Nonadherence", "Z75.x / Z91.19", card_type="clinical-focus", priority="low",
    folded=[("Unavailability or Inaccessibility of Health Care Facilities", "Z75.3"), ("Unavailability or Inaccessibility of Other Helping Agencies", "Z75.4"),
    ("Nonadherence to Medical Treatment", "Z91.19")]),
  t("other-circumstances-a-clinician-may-note", "Other Circumstances of Personal History and Additional Conditions", "varies", card_type="clinical-focus", priority="low",
    folded=[("Personal History of Psychological Trauma", "Z91.49"), ("Personal History of Military Deployment", "Z91.82"), ("Wandering Associated With a Mental Disorder", "Z91.83"),
    ("Malingering", "Z76.5"), ("Borderline Intellectual Functioning", "R41.83"), ("Age-Related Cognitive Decline", "R41.81"), ("Overweight or Obesity", "E66.9"),
    ("Unwanted Pregnancy", "Z64.0"), ("Multiparity", "Z64.1"), ("Discord With Social Service Provider", "Z64.4"), ("Other Personal Risk Factors", "Z91.89")]),
  ], notes="Framed as life situations, not personal failures. Codes are representative: the DSM-5-TR chapter lists many more sub-codes, and ICD-10-CM has expanded the Z55–Z65 and Z91 ranges since 2022. Full code list needs verification."))

# Section III
chapters.append(ch("further-study", 23, "Conditions for Further Study", "Being studied, not official diagnoses",
  "Patterns researchers are still studying. They are not official diagnoses, and no one should be labelled with them, but people do live with these experiences.",
  "flask-conical", [
  t("attenuated-psychosis-syndrome", "Attenuated Psychosis Syndrome", "n/a", card_type="further-study", priority="medium", sensitivity="elevated"),
  t("depressive-episodes-with-short-duration-hypomania", "Depressive Episodes With Short-Duration Hypomania", "n/a", card_type="further-study", priority="low", sensitivity="elevated"),
  t("caffeine-use-disorder", "Caffeine Use Disorder", "n/a", card_type="further-study", priority="low"),
  t("internet-gaming-disorder", "Internet Gaming Disorder", "n/a", card_type="further-study", priority="high",
    note="ICD-11 has 'gaming disorder' as an official diagnosis; card explains the difference between the two manuals."),
  t("neurobehavioral-disorder-prenatal-alcohol-exposure", "Neurobehavioral Disorder Associated With Prenatal Alcohol Exposure", "n/a", card_type="further-study", priority="low",
    note="Relates to fetal alcohol spectrum disorders; frame with no blame toward parents."),
  t("suicidal-behavior-disorder", "Suicidal Behavior Disorder", "n/a", card_type="further-study", priority="medium", sensitivity="high"),
  t("nonsuicidal-self-injury-disorder", "Nonsuicidal Self-Injury Disorder", "n/a", card_type="further-study", priority="medium", sensitivity="high"),
  ], section="III", notes="DSM-5's Persistent Complex Bereavement Disorder was removed from this list when Prolonged Grief Disorder entered Section II (APA, 2022). Search-confirmed."))

chapters.append(ch("alternative-pd-model", 24, "Alternative DSM-5 Model for Personality Disorders", "A different way to describe personality difficulties",
  "An optional model that describes personality difficulties by how much they affect a person's sense of self and relationships, and by traits, instead of fixed categories.",
  "sliders-horizontal", [
  t("alternative-model-for-personality-disorders", "Alternative DSM-5 Model for Personality Disorders (explainer)", "n/a", card_type="explainer", priority="medium",
    note="One explainer covering Criterion A (level of personality functioning) and Criterion B (five trait domains) in plain words."),
  ], section="III"))

chapters.append(ch("culture", 25, "Culture and Psychiatric Diagnosis", "Culture & distress",
  "Every culture has its own ways of naming and expressing suffering. These are some of the best-described ones, written with respect and without claiming they are 'disorders'.",
  "globe", [
  t("culture-and-mental-health", "Culture and Psychiatric Diagnosis; the Cultural Formulation Interview (explainer)", "n/a", card_type="explainer", priority="medium",
    note="Explains cultural syndromes, cultural idioms of distress, cultural explanations, and the Cultural Formulation Interview."),
  t("ataque-de-nervios", "Ataque de nervios", "n/a", card_type="cultural-concept", priority="medium", sensitivity="elevated", note="Latin American and Latino communities. Check against Spanish-language sources."),
  t("dhat-syndrome", "Dhat syndrome", "n/a", card_type="cultural-concept", priority="medium", sensitivity="elevated", note="South Asia. Check against Indian sources (for example Indian Journal of Psychiatry)."),
  t("khyal-cap", "Khyâl cap", "n/a", card_type="cultural-concept", priority="low", sensitivity="elevated", note="Cambodian communities. Check against Khmer-community sources."),
  t("kufungisisa", "Kufungisisa", "n/a", card_type="cultural-concept", priority="low", note="Shona (Zimbabwe). Check against Zimbabwean sources (for example Friendship Bench research)."),
  t("maladi-moun", "Maladi moun", "n/a", card_type="cultural-concept", priority="low", note="Haitian communities. Check against Haitian sources."),
  t("nervios", "Nervios", "n/a", card_type="cultural-concept", priority="medium", note="Latino communities. Check against Spanish-language sources."),
  t("shenjing-shuairuo", "Shenjing shuairuo", "n/a", card_type="cultural-concept", priority="low", note="Chinese communities. Check against Chinese sources."),
  t("susto", "Susto", "n/a", card_type="cultural-concept", priority="low", note="Latin American communities. Check against Spanish-language sources."),
  t("taijin-kyofusho", "Taijin kyofusho", "n/a", card_type="cultural-concept", priority="medium", note="Japan. Check against Japanese sources."),
  ], section="III", notes="DSM-5-TR glossary lists these nine concepts (search-confirmed, page range 871–879 in secondary sources). All cultural-concept cards go on the 'needs human review' list, ideally reviewed by someone from the culture."))

out = collections.OrderedDict()
out["dsm_edition"] = "DSM-5-TR"
out["dsm_published"] = "2022-03"
out["icd10cm_codes_as_of"] = "2025-10-01 (APA September 2025 coding update)"
out["verified_on"] = "2026-10-22"
out["verification_notes"] = (
  "Chapter structure and condition names follow the DSM-5-TR (2022) classification. code_status 'verified' means the code was seen in APA or ICD-10-CM text quoted by web search during this session; "
  "'needs_verification' means it comes from reference knowledge of the DSM-5-TR classification and must be re-checked against psychiatry.org or the CDC ICD-10-CM tabular list when pages can be opened. "
  "See docs/version-check.md.")
out["card_types"] = ["condition", "condition-group", "further-study", "cultural-concept", "clinical-focus", "explainer"]
out["sensitivity_levels"] = {"standard": "no crisis strip required", "elevated": "crisis strip required (trauma, psychosis, substance use, sexual topics, raised suicide risk)", "high": "crisis strip required (suicide, self-harm, eating disorders, abuse)"}
out["chapters"] = chapters
out["totals"] = {"chapters": len(chapters), "topics": sum(len(c["topics"]) for c in chapters),
  "by_card_type": dict(collections.Counter(tp["card_type"] for c in chapters for tp in c["topics"])),
  "folded_variants": sum(len(tp["folded_variants"]) for c in chapters for tp in c["topics"]) + sum(len(c["chapter_level_folds"]) for c in chapters)}

ids = [tp["topic_id"] for c in chapters for tp in c["topics"]]
assert len(ids) == len(set(ids)), [i for i in ids if ids.count(i) > 1]
with open(f"{ROOT}/data/taxonomy.json", "w") as f:
    json.dump(out, f, indent=2, ensure_ascii=False)
print(json.dumps(out["totals"], indent=1))
for c in chapters:
    print(f'{c["chapter_number"]:>2} {c["section"]:<3} {c["official_name"][:60]:<60} topics={len(c["topics"]):>2} folds={sum(len(t["folded_variants"]) for t in c["topics"]) + len(c["chapter_level_folds"])}')
