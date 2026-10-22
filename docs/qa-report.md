# QA report

Generated 2026-10-22 from the build outputs. Everything in this report is reproducible by running the four build scripts in `tools/README.md`; the counts below come from the generated JSON, not from memory.

## 1. What was built

| Item | Count |
|---|---|
| Chapters in taxonomy | 25 |
| Topics in taxonomy / cards written | 153 / 153 (100% coverage) |
| Folded variants recorded in the taxonomy | 192 |
| Glossary terms | 305 (clinical 118, everyday 79, treatment 81, rights 27) |
| Communities in the directory | 127 (helpline 46, subreddit 35, online-group-meeting 20, org-resource-hub 12, peer-forum 9, in-person-group-finder 5) |
| Crisis and support lines | 52 across US, UK, IE, CA, AU, IN, plus 3 global directories |
| Unique sources cited on cards | 200 |
| Card types | condition 110, clinical-focus 13, explainer 11, cultural-concept 9, further-study 7, condition-group 3 |
| Sensitivity levels | standard 73, elevated 68, high 12 (crisis strip on 80 cards) |
| Cards with In young people / Across cultures / Strengths / Sub-sections | 83 / 59 / 9 / 50 |
| Language convention | person-first 144, identity-first 2, mixed 7 |

## 2. Honesty statement: what was and wasn't verified

**No external web page was opened during this build.** The cloud environment's network policy returned 403 for every outbound fetch (psychiatry.org, nimh.nih.gov, nice.org.uk, reddit.com, and every helpline site). The only research tool that worked was a web-search API that returns titles, URLs, and short snippets. Consequences, applied uniformly:

- Every source on every card and glossary term is `verification_status: needs_verification`. `access_method` distinguishes `seen-in-search-results` (the URL and a snippet appeared in a search result from the publisher's own domain: 117 sources) from `not-opened` (a well-known page cited from memory: 83 sources).
- Every community is `needs_verification` with a `reviewer_notes` line saying what to check. No subreddit name, Discord invite, or URL was guessed; anything not seen in a search result went to the pending list in `docs/excluded-communities.md`.
- Every crisis line is `needs_verification` (37) or `conflicting_sources` (12, where directories disagreed on a number or hours), except the six national emergency numbers marked `verified`. Known risks: PAPYRUS HOPELINE247 has moved from an 0800 to an 0300 number per a 2026 listing; India's Childline 1098 is being merged into 112; ERIC's helpline number appears three different ways.
- Prevalence figures: 143 cards carry a figure with a source; 10 carry `n/a` because no meaningful population figure exists (explainers, Z-codes, idioms); 81 carry a `how_common.note` flagging that the number was taken from a search snippet, is clinic-based, or needs a primary citation.
- A bug found and fixed in this pass: both builders had been marking `seen` sources as `verified`. That overstated the evidence and has been corrected to `needs_verification` everywhere.

## 3. Hard-rule checklist

| Rule | How it is enforced | Status |
|---|---|---|
| Not a diagnostic tool | `common_signs` capped at 3–6 plain items, no counts or durations as thresholds, every card's signs block is rendered under a 'describes, doesn't diagnose' line (design system §5.6); `is_not` and `when_to_reach_out` on every card | Pass, enforced by schema and build |
| No DSM text copied | All prose written fresh; only names and ICD-10-CM codes cited; `src-dsm` note states the text was not reproduced | Pass, needs human spot-check |
| No invented facts, stats, or links | Every figure has `source_ref` resolving to a source on the same card (build fails otherwise); every URL carries access method and status; communities only if seen in search | Pass, pending verification |
| No guessed helpline numbers | Numbers only from search snippets, with conflicting ones flagged `conflicting_sources` | Pass, pending verification |
| Safe messaging | Stigma-word regex fails the build; weight/calorie regex fails high-sensitivity cards; no methods on suicide, self-harm, paraphilic, pyromania cards (manual); crisis strip forced by schema on elevated/high | Pass, needs suicide-prevention reviewer |
| Non-stigmatising language | Regex plus per-card `language_convention` and note; 'addict', 'suffers from', 'committed suicide', 'psycho' etc. blocked | Pass |
| Never link harmful communities | Exclusion log with standing rules; pro-ED, pro-self-harm, incel, MLM, supplement-selling never listed | Pass |
| Reading grade 6–8 | Flesch-Kincaid estimate on reader-facing prose; see §4 | **Partial, see below** |
| WCAG AA | Token generator asserts ≥4.5:1 text and ≥3:1 borders in both themes | Pass (min 4.53:1) |

## 4. Reading level

The build computes a Flesch-Kincaid grade over all reader-facing prose on a card (one-liner, in simple words, signs, myths, what helps, reach out, is not, hope, optional blocks). Mean grade across 153 cards: **9.4**. Over the `in_simple_words` paragraph alone: **10.7**. 128 cards score above 8 on the full-card measure and 135 on the summary paragraph.

Why: the estimator counts syllables, and condition names ('neurocognitive', 'depersonalization', 'antidepressant') and treatment names ('psychotherapy', 'physiotherapy') are unavoidable on a card about them; one 'schizotypal personality disorder' adds about a grade to a sentence. Sentence length is already moderate (mean 17.7 words per sentence in the summary paragraphs), but 16.8% of summary words have three or more syllables, which is what drives the score. The brief's 6–8 target is met in tone and sentence structure, and missed on vocabulary for medical topics. Note that the summary paragraph scores *higher* than the full card because it is where the condition name and treatment names are densest.

Cards above grade 10 on the full-card measure (the simplification backlog, highest first):

- alternative-model-for-personality-disorders (11.7; summary paragraph 11.6)
- hallucinogen-related-disorders (11.6; summary paragraph 13.4)
- schizotypal-personality-disorder (11.4; summary paragraph 15.5)
- traumatic-brain-injury-neurocognitive-disorder (11.3; summary paragraph 13.0)
- lewy-body-neurocognitive-disorder (11.3; summary paragraph 11.0)
- frontotemporal-neurocognitive-disorder (11.2; summary paragraph 12.4)
- attenuated-psychosis-syndrome (11.2; summary paragraph 14.3)
- depressive-episodes-with-short-duration-hypomania (11.1; summary paragraph 14.2)
- parkinsons-disease-neurocognitive-disorder (11.0; summary paragraph 11.7)
- other-circumstances-a-clinician-may-note (11.0; summary paragraph 14.3)
- neurocognitive-disorder-other-causes (11.0; summary paragraph 10.0)
- neurobehavioral-disorder-prenatal-alcohol-exposure (11.0; summary paragraph 12.5)
- narcissistic-personality-disorder (11.0; summary paragraph 11.7)
- huntingtons-disease-neurocognitive-disorder (11.0; summary paragraph 12.3)
- delayed-ejaculation (11.0; summary paragraph 16.1)
- about-personality-disorders (11.0; summary paragraph 11.0)
- social-environment-and-identity-stress (10.9; summary paragraph 12.0)
- medication-induced-movement-disorders (10.9; summary paragraph 12.2)
- dependent-personality-disorder (10.9; summary paragraph 12.3)
- neuroleptic-malignant-syndrome (10.8; summary paragraph 12.9)
- maladi-moun (10.8; summary paragraph 13.7)
- schizoaffective-disorder (10.7; summary paragraph 10.5)
- premature-early-ejaculation (10.7; summary paragraph 12.9)
- obsessive-compulsive-personality-disorder (10.7; summary paragraph 13.3)
- catatonia (10.7; summary paragraph 12.6)
- brief-psychotic-disorder (10.7; summary paragraph 14.6)
- taijin-kyofusho (10.6; summary paragraph 13.8)
- stimulant-use-disorder (10.6; summary paragraph 13.0)
- schizophrenia (10.6; summary paragraph 13.5)
- dissociative-amnesia (10.5; summary paragraph 11.0)
- crime-disaster-and-legal-problems (10.5; summary paragraph 13.0)
- female-orgasmic-disorder (10.4; summary paragraph 11.7)
- alzheimers-disease-neurocognitive-disorder (10.4; summary paragraph 11.7)
- stereotypic-movement-disorder (10.3; summary paragraph 10.9)
- nervios (10.3; summary paragraph 13.0)
- mental-disorders-due-to-another-medical-condition (10.3; summary paragraph 12.9)
- intellectual-developmental-disorder (10.3; summary paragraph 10.9)
- genito-pelvic-pain-penetration-disorder (10.3; summary paragraph 11.5)
- functional-neurological-symptom-disorder (10.3; summary paragraph 11.4)
- delirium (10.3; summary paragraph 13.6)
- shenjing-shuairuo (10.2; summary paragraph 13.5)
- psychological-factors-affecting-other-medical-conditions (10.2; summary paragraph 13.6)
- pica (10.2; summary paragraph 11.0)
- male-hypoactive-sexual-desire-disorder (10.2; summary paragraph 11.5)
- caffeine-related-disorders (10.2; summary paragraph 12.1)
- other-or-unknown-substance-use-disorder (10.1; summary paragraph 10.6)
- histrionic-personality-disorder (10.1; summary paragraph 10.9)
- family-and-relationship-problems (10.1; summary paragraph 14.8)
- factitious-disorder (10.1; summary paragraph 9.1)
- ataque-de-nervios (10.1; summary paragraph 11.7)
- antisocial-personality-disorder (10.1; summary paragraph 14.5)
- suicidal-behavior-disorder (10.0; summary paragraph 10.9)
- nonsuicidal-self-injury-disorder (10.0; summary paragraph 13.8)
- female-sexual-interest-arousal-disorder (10.0; summary paragraph 11.8)
- dhat-syndrome (10.0; summary paragraph 11.0)
- delusional-disorder (10.0; summary paragraph 10.8)
- bipolar-ii-disorder (10.0; summary paragraph 12.1)

Recommended fix for the next pass: (a) a reader-facing glossary popover already handles the long words; (b) rewrite the `what_helps.plain_summary` blocks on the cards above, which are the longest sentences; (c) in `in_simple_words`, use the condition name once and then 'it', and prefer 'talk therapy' over 'psychotherapy', 'physio' over 'physiotherapy'; (d) split sentences over 22 words. Cards at or below grade 8 on the full measure: 25.

## 5. Needs-human-review list

**Clinician sign-off requested on 60 cards** (`review.needs_clinician_signoff: true`), because the topic carries stigma, legal weight, or safety risk: personality disorders, psychotic disorders, paraphilic disorders, substance cards, neurocognitive cards, suicide and self-harm, abuse cards, gender dysphoria, eating disorders, and every cultural concept (community reviewer as well as clinician).

Reviewer roles needed:
- A psychiatrist or clinical psychologist for all 60 flagged cards.
- A suicide-prevention specialist for safe messaging on the 12 high-sensitivity cards.
- A pharmacist for the three medication-induced cards.
- Lived-experience reviewers for: autism and ADHD (identity-first wording), DID (system language), BPD, schizophrenia, trans and gender-diverse people, eating disorders, FASD.
- Community reviewers from Latino, South Asian, Cambodian, Zimbabwean/Shona, Haitian, Chinese, and Japanese backgrounds for the nine cultural concept cards.
- A child-protection professional for the child abuse, factitious disorder, and pedophilic disorder cards.
- A forensic clinician for the paraphilic chapter.

**Open questions logged on cards: 195.** The full list is in each card's `review.open_questions`; the most common are 'find a primary prevalence citation' (65), 'confirm figures by opening the source' (49), and 'add a guideline reference' (10).

## 6. Per-chapter status

| Chapter | Cards | Elevated/high | Clinician sign-off | Mean grade |
|---|---|---|---|---|
| Brains that develop differently | 9 | 0 | 0 | 9.3 |
| Psychosis & schizophrenia | 7 | 7 | 6 | 10.2 |
| Bipolar & mood swings | 3 | 2 | 2 | 9.4 |
| Depression & low mood | 5 | 4 | 1 | 7.7 |
| Anxiety & fear | 7 | 0 | 0 | 7.6 |
| Obsessions, compulsions & repeated behaviours | 5 | 2 | 1 | 7.8 |
| Trauma, stress & loss | 6 | 6 | 3 | 8.0 |
| Feeling disconnected | 3 | 3 | 2 | 9.5 |
| When the body carries the stress | 5 | 1 | 1 | 10.0 |
| Eating & food | 6 | 6 | 4 | 8.8 |
| Bladder & bowel control | 2 | 0 | 0 | 8.2 |
| Sleep | 8 | 1 | 0 | 8.4 |
| Sex & intimacy difficulties | 7 | 7 | 0 | 10.3 |
| Gender dysphoria | 1 | 1 | 1 | 9.2 |
| Anger, impulses & behaviour | 5 | 1 | 2 | 9.1 |
| Alcohol, drugs & gambling | 13 | 11 | 3 | 9.4 |
| Memory, thinking & dementia | 10 | 1 | 0 | 10.7 |
| Personality & patterns of relating | 11 | 5 | 11 | 10.3 |
| Unusual sexual interests that cause harm or distress | 5 | 5 | 4 | 9.4 |
| When it doesn't fit a label | 2 | 0 | 0 | 9.1 |
| Medication side effects | 3 | 1 | 0 | 10.4 |
| Life situations that affect mental health | 12 | 6 | 4 | 9.0 |
| Being studied, not official diagnoses | 7 | 4 | 4 | 10.3 |
| A different way to describe personality difficulties | 1 | 0 | 1 | 11.7 |
| Culture & distress | 10 | 6 | 10 | 10.0 |

## 7. Re-verification schedule

| What | Before launch | Then |
|---|---|---|
| Crisis lines (55) | Open every `source_url`; call or text each line once; set `verified_on` | Quarterly, and immediately on any news of a number change |
| Communities (127) | Open each; check rules, moderator activity, last post date, pinned crisis resources; sample 10 recent threads | Every 90 days; remove on first sign of harm |
| Sources (200 card, plus glossary) | Open each; confirm the figure quoted; replace secondary summaries with primary papers | Annually, and on each DSM-5-TR supplement (APA publishes updates roughly yearly; next eating-disorder severity-code change is in consultation to 2026-10-29) |
| DSM-5-TR version check | Re-run `docs/version-check.md` steps | Every six months |
| Reading grade | Re-run build; work the §4 backlog | Each content change |
| Design tokens | Re-run `tools/build_design_tokens.py` | Each palette change |

## 8. Schemas

- `schemas/card.schema.json`: one card; conditional rule forces `show_crisis_strip: true` for elevated/high; sources require `verification_status`.
- `schemas/glossary.schema.json`: the glossary file.
- `schemas/community.schema.json`: the community directory; moderation fields are tri-state (true/false/null = unknown).
- `schemas/crisis-line.schema.json`: crisis and support lines with `conflicting_sources` and `defunct` statuses.

All four data sets validate against their schemas in the build.

## 9. Known limitations

- Research depth was limited to search snippets; many 'how common' figures are secondary summaries of the DSM-5-TR text rather than primary studies.
- Only English; only six countries' helplines plus global directories.
- Community member counts come from third-party trackers and are approximate.
- The what-it-can-feel-like quotes are composites written for this project, not real testimonials, and should be labelled as such in the UI.
- No front-end has been built; `docs/design-system.md` describes it.
