from helpers import D, src, DSM, mk
from functools import partial
CARDS = []
X = partial(mk, "elimination", "elimination", "droplet")
DSM_X = DSM("Elimination Disorders")
NICE111 = src("src-nice-cg111", "Bedwetting in under 19s (CG111)", "NICE", "https://www.nice.org.uk/guidance/cg111", 2010, seen=True)
RCN = src("src-raisingchildren-bedwetting", "Bedwetting", "Raising Children Network (Australia)", "https://raisingchildren.net.au/guides/a-z-health-reference/bedwetting", seen=True)
ERIC = src("src-eric", "ERIC, The Children's Bowel and Bladder Charity", "ERIC (UK)", "https://www.eric.org.uk/", note="Site not opened; helpline details from directory listings.")
NWC = src("src-nationwide-enuresis", "Enuresis (Bedwetting)", "Nationwide Children's Hospital (US)", "https://nationwidechildrens.org/conditions/enuresis-bedwetting", seen=True)
X_COMMS = ["eric-uk-helpline", "youngminds-parents-helpline", "family-lives-helpline"]

CARDS.append(X("enuresis", "Enuresis", "Bedwetting past the age most children stay dry", ["bedwetting", "nocturnal enuresis", "daytime wetting (diurnal enuresis)"], "F98.0",
 "Repeated wetting of the bed or clothes, by day or night, in a child aged five or older.",
 "Enuresis is when a child aged five or older keeps wetting the bed or their clothes, at least twice a week for three months, and it isn't explained by a medical condition. Night-time bedwetting is by far the most common form. It's not laziness or naughtiness. Deep sleep, extra urine at night, constipation, and family history all play a part. Most children grow out of it, and simple treatments like bedwetting alarms work well.",
 ["She was mortified about sleepovers. The alarm took about eight weeks and she hasn't looked back.", "My dad wet the bed till he was ten, and so did I. Knowing that helped more than any chart.", "We stopped the punishments once we understood he couldn't wake up. That changed the whole mood at home."],
 ["Wetting the bed or clothes repeatedly, at age five or older", "At least twice a week for three months, or causing real distress", "Most often at night; sometimes in the day, or both", "Not caused by a medical condition or medication", "Often embarrassment, avoiding sleepovers, or low mood"],
 [{"myth": "Bedwetting is laziness or attention-seeking.", "fact": "Children who wet the bed are usually deeply asleep and can't feel the signal. It's a developmental and physical issue, not a behaviour choice."},
  {"myth": "Punishing or shaming will stop it.", "fact": "Punishment makes bedwetting worse and harms the child. Guidelines are clear that children should never be punished for wetting."},
  {"myth": "You just have to wait it out.", "fact": "Many children do grow out of it, but if it's upsetting the child, bedwetting alarms and sometimes medication help a lot and are worth asking about."}],
 {"plain": "About 1 in 5 children still wet the bed at five, 1 in 10 at six, and around 1 in 100 at fifteen or older. Almost all children grow out of it eventually.", "figure": "About 20% at age 5, 10% at age 6 (Raising Children Network); roughly 5%–10% of 5-year-olds (DSM-5-TR text); about 99% dry by 15 (Nationwide Children's)", "source_ref": "src-raisingchildren-bedwetting"},
 {"plain_summary": "First steps are simple: treat constipation, keep daytime drinking regular, avoid caffeine, and never punish wetting. For children seven and over, or younger ones who are motivated, a bedwetting alarm is the first-line treatment in NICE guidance and has the best long-term results. Desmopressin, a medication that reduces night-time urine, can be prescribed and monitored by a doctor for quick results or special occasions. A doctor checks for urine infection, diabetes, or constipation first.",
  "evidence_based_options": ["Bedwetting (enuresis) alarm as first-line treatment", "Treating constipation and reviewing fluids and toileting routine", "Desmopressin prescribed and monitored by a doctor, when appropriate", "Reward systems for agreed behaviours (like drinking well in the day), not for dry nights"],
  "self_help_that_supports_care": ["A calm, no-blame attitude: 'it's not your fault, and we'll fix it together'", "Easy clean-up: waterproof mattress covers, spare sheets, the child helping without shame", "Regular toilet visits before bed; no caffeine", "Talking to the school and planning for trips and sleepovers"],
  "guideline_refs": ["src-nice-cg111"]},
 "If a child is five or older and still wetting, and it's upsetting them or you, ask a doctor, health visitor, school nurse, or continence service for help. See a doctor sooner if wetting starts again after months of being dry, or comes with pain, thirst, or daytime problems.",
 "Wetting in children under five, occasional accidents, wetting caused by urine infection, diabetes, or constipation, and a sudden return of wetting after a stressful event are assessed separately.",
 "Almost every child becomes dry. With an alarm and patience, most do so within a few months.",
 ["encopresis", "separation-anxiety-disorder", "adhd", "autism-spectrum-disorder"],
 ["onset", "gp-primary-care", "school-support-plans"],
 X_COMMS, ("Soft line illustration of a child and parent making a bed together with fresh sheets, morning light, a small plant on the windowsill. Pastel blue and cream.", "A child and parent make a bed together in morning light."),
 [DSM_X, NICE111, RCN, NWC, ERIC], qs=["Confirm current ERIC helpline number and hours."],
 young="Teens with enuresis often feel intense shame and hide it. It's still treatable at any age, and a doctor or continence service will have seen it many times."))

CARDS.append(X("encopresis", "Encopresis", "Soiling, usually because of constipation", ["soiling", "faecal incontinence in children", "fecal incontinence (US spelling)"], "F98.1",
 "Repeated soiling of underwear or other places by a child aged four or older, usually from constipation.",
 "Encopresis is when a child aged four or older repeatedly passes stool into their clothes or in inappropriate places, at least once a month for three months, and it isn't caused by a medical condition. It usually comes from long-standing constipation: a hard mass builds up, the bowel stretches, and softer stool leaks around it without the child feeling it. Children don't do this on purpose. Treating the constipation, with routine and patience, usually fixes it.",
 ["We thought he was being defiant. The paediatrician explained his bowel was so stretched he genuinely couldn't feel it. I felt awful for the shouting.", "The hardest part was school. Once the nurse knew, she helped him clean up quietly and nobody else needed to know."],
 ["Repeated soiling of clothes or inappropriate places, at age four or older", "At least once a month for three months", "Usually signs of constipation: hard or very large stools, tummy pain, avoiding the toilet", "Child may not notice the smell or feel it happening", "Shame, hiding soiled clothes, teasing at school"],
 [{"myth": "Soiling is deliberate or attention-seeking.", "fact": "In most cases the child can't feel the leak because a stretched bowel has lost sensation. It's a physical problem with a physical fix."},
  {"myth": "It's about toilet training being done wrong.", "fact": "Constipation, painful stools, illness, diet, and fear of the toilet are the usual roots. Parents can help now, whatever happened before."},
  {"myth": "Laxatives are dangerous for children.", "fact": "Doctors routinely prescribe and monitor child-safe laxatives to clear the build-up and keep stools soft while the bowel recovers. Stopping too early is the common mistake."}],
 {"plain": "About 1 in 100 five-year-olds have encopresis, more boys than girls. It becomes less common with age.", "figure": "About 1% of 5-year-olds (DSM-5-TR text); estimates in studies range roughly 0.8%–7.8%", "source_ref": "src-dsm", "note": "Needs a primary citation."},
 {"plain_summary": "The main treatment is medical: a doctor clears the built-up stool with laxatives, then keeps stools soft for months with a maintenance dose, prescribed and monitored, while the bowel shrinks back and sensation returns. Alongside that, a regular toilet routine (sitting after meals, feet supported, no pressure), a diet with enough fibre and fluids, and calm praise for sitting rather than for results. Behavioural support helps children who have become afraid of the toilet. If there's no constipation, a different assessment is needed.",
  "evidence_based_options": ["Disimpaction and maintenance laxatives prescribed and monitored by a doctor", "Scheduled toilet sitting after meals with a footstool", "Fibre, fluids, and physical activity", "Behavioural support for toilet fear or refusal; family education"],
  "self_help_that_supports_care": ["No blame, no punishment; matter-of-fact clean-up kits at home and school", "A sticker chart for sitting on the toilet, not for staying clean", "Keeping going with the laxatives for as long as the doctor advises", "A quiet word with the school so the child isn't shamed"],
  "guideline_refs": []},
 "If a child aged four or older is regularly soiling, see a doctor. Treating constipation early is easier and kinder. See a doctor urgently if there's severe tummy pain, vomiting, or blood.",
 "Accidents during toilet training, a single bout of diarrhoea, or soiling caused by a bowel condition, nerve problem, or medication are not encopresis.",
 "With the right treatment the bowel recovers, sensation returns, and the soiling stops. Children and families get their confidence back.",
 ["enuresis", "autism-spectrum-disorder", "adhd", "separation-anxiety-disorder"],
 ["onset", "gp-primary-care", "school-support-plans"],
 X_COMMS, ("Soft line illustration of a child sitting comfortably on a toilet with a footstool, a picture book open, a parent waiting at the door with a kind smile. Pastel blue and sand.", "A child sits comfortably on a toilet with a footstool, reading a picture book."),
 [DSM_X, ERIC], qs=["Find a primary prevalence citation.", "Add a NICE constipation guideline reference (CG99)."]))
