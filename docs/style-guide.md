# Style guide

How every card, glossary entry, and community note on this site is written. If a sentence breaks one of these rules, the build should catch it (word counts, stigma words, schema) or a reviewer should.

## 1. Who we're writing for

A worried 14-year-old at midnight, a parent on a lunch break, an adult who just got a diagnosis and typed it into a search bar. They are scared, tired, and smart. They don't need to be impressed; they need to understand and to know what to do next.

## 2. Voice

- **Warm, plain, direct.** Like a kind nurse explaining something at the bedside, not a textbook and not a wellness influencer.
- **Second person where it helps** ("if you notice", "you deserve"), third person when describing the condition.
- **Honest about uncertainty.** "Studies suggest", "estimates vary", "we couldn't confirm this figure". Never round uncertainty into confidence.
- **Hopeful without promising.** Every card ends with a hope note that is true for most people and overclaims for none. "Most people get better" is fine; "you will be cured" is not.
- **No jokes about the condition.** Light touches are fine ("you don't have to prove it hurts; they'll believe you"); mockery never.

## 3. Reading level

- Target grade 6–8. Short sentences (aim under 20 words), one idea per sentence, common words first.
- Use the condition's name once, then "it". Prefer "talk therapy" to "psychotherapy", "medicine" or "medication" to "pharmacotherapy", "signs" to "symptomatology".
- Explain every clinical term in the sentence where it first appears, or link it to the glossary. Never leave a reader to guess what "prodrome" means.
- Numbers: "about 1 in 10 people" in prose; the precise figure and source go in `how_common.figure`, which the UI collapses.

## 4. Field-by-field rules

| Field | Rule |
|---|---|
| `plain_title` | ≤ 60 characters. A human sentence fragment, not a label: "When worry won't switch off", not "GAD overview". No colon-clichés. |
| `one_liner` | ≤ 20 words, one sentence, states what the thing is. |
| `in_simple_words` | ≤ 80 words. What it is, who it affects, that it's treatable. No lists. |
| `what_it_can_feel_like` | 2–4 first-person composite quotes. Written for this project, not real testimonials; the UI must say so. Never describe methods, weights, or graphic events. |
| `common_signs` | 3–6 items, ≤ 15 words each. Describe, don't diagnose: no "five or more of the following", no durations as thresholds. |
| `myths_vs_facts` | 1–3 pairs. The fact must be true and sourced in spirit; no straw-man myths. |
| `how_common.plain` | One or two sentences, framed gently. Figure and source separate. |
| `what_helps` | Plain summary, then evidence-based options, then self-help that supports care. Medication is always "prescribed and monitored by a doctor". No doses, no drug brand names, no tapering schedules. |
| `when_to_reach_out` | Concrete triggers plus where to go. Elevated/high cards point to the crisis strip explicitly. |
| `is_not` | What ordinary experience or other condition this is not. Protects against self-diagnosis. |
| `hope_note` | One or two sentences, true, specific to the condition. |
| `in_young_people`, `across_cultures`, `strengths_and_differences` | Optional; include when the brief or the evidence makes them matter. |

## 5. Language rules

- **Person-first by default:** "a person with schizophrenia", "people who use drugs", "a child with ODD".
- **Identity-first where the community prefers it:** "autistic people", "Deaf", "transgender person". Record the choice in `language_convention` and explain it in `language_convention_note` when it isn't obvious.
- **Never:** crazy, insane, psycho, nuts, lunatic, addict, junkie, alcoholic (as a noun), anorexic/bulimic (as a noun), schizo, retarded, suffers from, victim of (for a living person; "survivor" or "person who experienced"), committed suicide (use "died by suicide"), "successful/unsuccessful attempt", "OCD" or "bipolar" as adjectives for ordinary behaviour, "clean" for abstinent, "normal" for people without a condition, "the mentally ill".
- **Use:** died by suicide, suicide attempt, self-injury, person with a substance use disorder, in recovery, abstinent, neurotypical, people without the condition.
- **Culture:** describe cultural concepts in their own terms, never as "folk beliefs", "superstition", "exotic", or "primitive". Say what the community says it is.
- **Sex and gender:** say "women" or "men" when the DSM criteria do, and acknowledge trans and non-binary people where relevant. Never "biological sex", "transgenderism", "sex change".
- **Age:** "children", "teens", "young people", "older adults". Not "the elderly".

## 6. Safe messaging (suicide, self-harm, eating, substances, abuse)

- No methods, means, locations, notes, or step-by-step descriptions, anywhere, including quotes and illustrations.
- No numbers for weight, calories, BMI, or "lowest weight" on eating-disorder cards (the build fails if it finds them).
- No dosing, sourcing, or "how to" on substance cards; harm-reduction information stays general ("never use alone", "naloxone").
- No descriptions of abusive or violent acts beyond what's needed to recognise them.
- Suicide is "a cause of death", not an "epidemic"; it is never framed as a solution, an escape, or inexplicable.
- Every elevated or high card shows the crisis strip, and its reach-out block repeats the first line of the strip.
- Illustrations: daylight, connection, something in progress. Never isolation, danger, or the object of the condition.

## 7. Communities and helplines

- Describe what the reader will find: who runs it, who it's for, how it's moderated, what it costs, hours for lines.
- Say "peer support, not professional advice" on every peer community. Say "not a crisis service" on every non-crisis line.
- Never list a community that hasn't been seen in a search result or opened; never guess a subreddit name, invite link, or phone number.
- Record every rejection in `docs/excluded-communities.md` so it isn't re-added.

## 8. Sources and claims

- Every figure needs a `source_ref` on the same card; every source records how it was accessed and whether it's verified.
- Prefer the primary paper or the official guideline; when only a secondary summary was seen, say so in the source note.
- Cite DSM-5-TR for names, codes, and structure only. Never reproduce its text.
- When a claim can't be sourced, soften it ("some research suggests") or cut it.

## 9. Formatting

- British/American spelling: cards use the spelling of the country most associated with the source or community; the glossary lists both where they differ. Don't mix within a card.
- No em-dashes in card prose; use commas, full stops, or parentheses sparingly.
- Numbers under ten as words in prose, except ages, times, and figures.
- One space after a full stop. Sentence case for headings. No exclamation marks.

## 10. Before you submit a card

1. Run the build; fix every reported problem.
2. Read the card aloud. Would the 14-year-old understand it? Would the clinician wince?
3. Check the crisis strip flag matches the sensitivity.
4. Check every community and source has a note on what a reviewer must confirm.
5. Add open questions to `review.open_questions` rather than leaving them in your head.
