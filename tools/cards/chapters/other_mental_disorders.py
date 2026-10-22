from helpers import D, src, DSM, mk
from functools import partial
CARDS = []
X = partial(mk, "other-mental-disorders", "other-mental-disorders", "circle-help")
DSM_X = DSM("Other Mental Disorders and Additional Codes")
X_COMMS = ["nami-connection-and-helpline", "mind-side-by-side", "sane-forums-australia", "beyondblue-forums"]

CARDS.append(X("mental-disorders-due-to-another-medical-condition", "Mental Disorders Due to Another Medical Condition", "When a physical illness is the cause of mental symptoms", ["organic mental disorder (outdated)", "secondary psychiatric syndrome"], "F06.x / F07.0 / F09 (varies)",
 "Mood, anxiety, psychosis, or personality changes that are directly caused by a medical illness, not a primary mental disorder.",
 "Sometimes a physical illness is the direct cause of mental symptoms: a thyroid problem causing depression or anxiety, a brain tumour or epilepsy causing personality change, lupus or an infection causing psychosis, or a head injury changing behaviour. The DSM labels these 'due to another medical condition' because treating the medical cause is the key. They're easy to miss. Clues include an unusual age of onset, no family history, or new physical problems.",
 ["Two years of 'treatment-resistant depression' turned out to be an underactive thyroid. One blood test.", "Dad's personality changed completely at 58. Everyone said midlife crisis. It was a frontal lobe tumour, and surgery gave him back to us."],
 ["Mental symptoms that start alongside, or soon after, a physical illness", "Unusual pattern: first episode late in life, no family history, or odd features", "Physical signs the usual condition doesn't explain", "Symptoms that improve when the medical condition is treated"],
 [{"myth": "Mental symptoms are always 'psychological'.", "fact": "Thyroid, hormone, autoimmune, neurological, and infectious conditions can all cause them. Good psychiatry starts with a medical check."},
  {"myth": "If a scan or blood test is normal, it's all in your head.", "fact": "Normal tests rule some causes out, not all. And a primary mental disorder is just as real and treatable as a medical one."}],
 {"plain": "Overall numbers aren't known because these conditions are counted under each medical cause. They're common in hospital settings, especially among older adults.", "figure": "No overall prevalence figure; varies by underlying condition", "source_ref": "src-dsm"},
 {"plain_summary": "Treatment targets the medical cause first: correcting the thyroid, treating the infection or autoimmune disease, managing the epilepsy, removing the tumour. Mental symptoms often ease as the condition improves. In the meantime, the usual treatments for mood, anxiety, or psychosis are used with care, prescribed and monitored by a doctor who knows the medical picture. Psychiatry, neurology, and general medicine often work together.",
  "evidence_based_options": ["Full medical assessment including blood tests and, where indicated, brain imaging", "Treatment of the underlying medical condition", "Psychiatric treatment of the symptoms meanwhile, adjusted for the medical condition", "Joint care between psychiatry and medical specialists"],
  "self_help_that_supports_care": ["Asking for a physical check-up when mental symptoms are new or unusual", "Listing all medications and supplements for the doctor", "Noting the timeline: what started when", "Bringing a family member who's noticed changes"],
  "guideline_refs": []},
 "If mental symptoms have started suddenly, late in life, alongside physical changes, or don't respond to usual treatment, ask for a medical review. If someone becomes confused or behaves very differently over hours or days, seek urgent care.",
 "Being understandably upset about having an illness isn't a disorder due to that illness. Delirium and dementia have their own cards. Depression that happens to coexist with a medical condition, without being caused by it, is diagnosed as depression.",
 "When the cause is found and treated, symptoms that seemed stubborn often lift. It's one reason a medical check is always worth it.",
 ["delirium", "major-and-mild-neurocognitive-disorder", "major-depressive-disorder", "schizophrenia", "when-it-doesnt-fit-a-label"],
 ["differential-diagnosis", "assessment", "gp-primary-care", "psychiatrist"],
 X_COMMS, ("Soft line illustration of a doctor and a person looking at a tablet together with a simple body outline on it, a window with daylight. Pastel grey and mint.", "A doctor and a person look at a tablet showing a simple body outline."),
 [DSM_X], qs=["Add a reference on medical screening in first-episode psychiatric presentations."], card_type="explainer"))

CARDS.append(X("when-it-doesnt-fit-a-label", "When It Doesn't Fit a Label", "Real distress that doesn't match a named diagnosis", ["unspecified mental disorder", "other specified mental disorder", "no diagnosis"], "F99 / Z03.89",
 "Clinicians have codes for distress that doesn't fit a named condition, or for when it's too early to tell.",
 "Not everyone who struggles fits neatly into a diagnosis, and that's fine. The DSM includes 'other specified' and 'unspecified' mental disorder for when symptoms cause real problems but don't match any set of criteria, or when there isn't enough information yet. There's also a code for 'observation for a suspected mental disorder, ruled out'. These aren't failures of diagnosis; they're honesty. Your experience is real whether or not it has a name, and help doesn't depend on a label.",
 ["I didn't tick enough boxes for anything. The psychologist said that didn't make my year any less awful, and we worked on it anyway.", "They put 'unspecified' and I felt dismissed. Then they explained it meant 'we're not guessing'. That helped."],
 ["Real distress or difficulty that doesn't match a named condition", "Symptoms from several areas without fitting any one", "Not enough information yet, or an assessment still underway", "Help still available, whatever the label"],
 [{"myth": "No diagnosis means nothing is wrong.", "fact": "Diagnoses are tools for communication and planning. Distress that doesn't fit a category still deserves care."},
  {"myth": "'Unspecified' means the clinician doesn't know what they're doing.", "fact": "It usually means they're being careful not to pin a label that doesn't fit. Labels can be revised; wrong ones can stick."}],
 {"plain": "These codes are used often, especially early in care and in emergency settings, but there's no meaningful prevalence figure.", "figure": "n/a", "source_ref": "src-dsm"},
 {"plain_summary": "Care focuses on the actual problems: sleep, mood, stress, relationships, safety. Therapy such as CBT or counselling doesn't need a diagnosis to help. A formulation, a shared story of what's going on and why, often works better than a label. Assessment may continue, and a clearer picture can emerge over time. If medication is considered, a doctor prescribes and monitors it for the symptoms that matter most.",
  "evidence_based_options": ["Therapy aimed at the specific difficulties, such as CBT or counselling", "A shared formulation rather than a label", "Ongoing assessment as the picture becomes clearer", "Practical support: sleep, stress, social connection"],
  "self_help_that_supports_care": ["Describing what's hard in your own words, without needing a diagnosis", "Tracking patterns: sleep, mood, triggers", "Asking what the clinician thinks is going on, not just what it's called", "Peer support; many people's experience doesn't fit a box"],
  "guideline_refs": []},
 "If you're struggling and nothing seems to fit, you still deserve support. Ask a doctor or therapist to help with the specific problems you're facing. If you're in crisis, the crisis strip applies with or without a diagnosis.",
 "Ordinary ups and downs, grief, and stress reactions aren't disorders, and a clinician may say so. That isn't dismissal; it's accuracy, and support is still available.",
 "Many people get well without ever being given a neat label. The work is the same: understanding what's going on and changing what can be changed.",
 ["mental-disorders-due-to-another-medical-condition", "adjustment-disorders", "generalized-anxiety-disorder", "major-depressive-disorder"],
 ["diagnosis", "provisional-diagnosis", "formulation", "differential-diagnosis", "self-diagnosis", "mental-health-vs-illness"],
 X_COMMS, ("Soft line illustration of a person and a counsellor drawing a simple mind-map together on paper, a cup of tea, a plant. Pastel grey and butter yellow.", "A person and a counsellor draw a simple mind-map together."),
 [DSM_X], card_type="explainer"))
