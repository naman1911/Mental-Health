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
