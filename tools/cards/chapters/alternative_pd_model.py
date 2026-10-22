from helpers import D, src, DSM, mk
from functools import partial
CARDS = []
X = partial(mk, "alternative-pd-model", "alternative-pd-model", "sliders-horizontal")
DSM_X = DSM("Section III: Alternative DSM-5 Model for Personality Disorders")
AMPD_REV = src("src-ampd-review", "Applications of AMPD and ICD-11 personality functioning and trait specifiers in clinical practice", "International Society for the Study of Personality Disorders", "https://www.personality.org/events/applications-of-ampd-and-icd-11-personality-functioning-and-trait-specifiers-in-clinical-practice", seen=True, note="Not opened; model description from multiple search summaries.")

CARDS.append(X("alternative-model-for-personality-disorders", "Alternative Model for Personality Disorders", "Personality difficulties by severity and traits, not boxes", ["AMPD", "dimensional model", "ICD-11 personality disorder model (similar)"], "n/a (proposed)",
 "A proposed way to describe personality difficulties by how much they affect self and relationships, plus traits.",
 "The alternative model is a proposed way of thinking about personality disorders, similar to the ICD-11 approach. Instead of ten types, it asks two questions. First, how much is a person's sense of self (identity, direction) and their relationships (empathy, closeness) affected, on a scale from none to extreme? Second, which trait patterns are strong: negative emotions, detachment, antagonism, disinhibition, or unusual thinking? The result is a description rather than a label, which many people find fairer and more useful.",
 ["Being told my 'level of functioning' was moderate and my main trait was negative affectivity felt like a description of a person, not a verdict on one.", "The old labels made me feel like a type. This made me feel like me, with some things to work on."],
 ["Difficulties with identity, self-direction, empathy, or intimacy, rated by severity", "Strong trait patterns: negative affectivity, detachment, antagonism, disinhibition, or psychoticism", "Patterns that are stable, long-standing, and not explained by culture or another condition", "Six familiar types kept as optional shorthand, including borderline and antisocial"],
 [{"myth": "This model gets rid of personality disorders.", "fact": "It keeps the idea that lasting patterns can cause real difficulty. It changes how they're described: by severity and traits rather than fixed categories."},
  {"myth": "Dimensional means vague.", "fact": "Severity and trait scores are measurable and often more precise than category labels, and they map directly onto what therapy targets."}],
 {"plain": "The model is used in research and some clinics. Prevalence isn't meaningful for a way of describing; personality disorders overall affect roughly 1 in 10 adults by some estimates.", "figure": "n/a", "source_ref": "src-dsm"},
 {"plain_summary": "Treatment doesn't change because of the model, but planning does: the severity rating guides how intensive and long therapy should be, and the trait profile guides what to work on, for example emotion regulation for negative affectivity or relationships for detachment. The same evidence-based therapies apply: DBT, mentalization-based therapy, schema therapy, and longer-term psychotherapy. Medication is used only for co-occurring conditions, prescribed and monitored by a doctor.",
  "evidence_based_options": ["Structured therapies for personality difficulties: DBT, MBT, schema therapy, transference-focused therapy", "Intensity matched to severity rating", "Trait-targeted skills: emotion regulation, interpersonal skills, impulse control", "Treatment of co-occurring depression, anxiety, or substance use"],
  "self_help_that_supports_care": ["Asking your clinician to describe your difficulties in these terms", "Learning your own trait profile without judgement", "Peer support with others who have personality difficulties", "Tracking the specific skills you're building"],
  "guideline_refs": ["src-ampd-review"]},
 "If a personality disorder label has felt like a verdict, ask a clinician whether they can describe your difficulties in terms of severity and traits instead. If you're in crisis, use the crisis strip.",
 "Having strong traits isn't a disorder. The model requires lasting difficulty in self and relationships. Culture and life stage are taken into account.",
 "Descriptions can change as people change. Many find that framing their difficulties as skills to build, not a type to be, is the start of getting better.",
 ["about-personality-disorders", "borderline-personality-disorder", "antisocial-personality-disorder", "avoidant-personality-disorder", "schizotypal-personality-disorder"],
 ["personality-trait", "identity-disturbance", "formulation", "diagnosis", "stigma"],
 ["mind-side-by-side", "sane-forums-australia", "nami-connection-and-helpline"],
 ("Soft line illustration of a person and a clinician looking at a set of gentle sliders on a tablet, like a sound mixer, a plant on the desk, daylight. Pastel slate and teal.", "A person and a clinician look at gentle sliders on a tablet, like a sound mixer."),
 [DSM_X, AMPD_REV], notes=["Proposed model; the ICD-11 uses a similar approach officially."], card_type="explainer", clin=True))
