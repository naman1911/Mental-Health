# Excluded and not-listed communities

Keep this log so later reviewers don't re-add something that was already checked and rejected. Add one row per decision, with the date.

## Exclusion rules (from the project brief, section 2 and 7.1)

A community is excluded if it promotes or tolerates any of: pro-eating-disorder content, self-harm encouragement, suicide methods or pacts, anti-treatment conspiracies, incel or hate ideology, selling supplements, courses or "miracle cures", MLM recruitment, or unlicensed paid coaching in place of support. It is also excluded if it fails any verification check: doesn't exist, no activity in 14 days, no visible rules or moderation, or commercial purpose.

## Log

| Date | Community | Platform | Decision | Reason |
|---|---|---|---|---|
| 2026-10-22 | NEDA Helpline (US) | phone/chat | Not listed (defunct) | NEDA closed its human helpline in May 2023 and withdrew its replacement chatbot after it gave harmful weight-loss advice. NEDA's website remains a resource hub; its helpline must not be listed as a support line. Source: NPR, 31 May 2023. |
| 2026-10-22 | Any pro-ana / pro-mia / "thinspo" community | any | Excluded (standing rule) | Promotes eating-disorder behaviour. Never list, never link, even to warn. |
| 2026-10-22 | Subreddits or forums whose URL could not be confirmed in a search result | any | Not listed pending verification | Project rule: no guessed community names or URLs. **Second pass (same day) resolved most of the original list:** added to the directory: Winston's Wish, Griefline, AFSP Healing Conversations, Friends for Survival, The Compassionate Friends, Ditch the Label, Kidscape Parent Advice Line, Rethink advice line, Mind Infoline, SiOS, r/dpdr, International Bipolar Foundation, F.E.A.S.T. Around the Dinner Table, ANAD peer groups, r/Autism_Parenting, ASAN; ERIC's helpline updated to the number on its own site (0808 801 0343, Tue–Thu 10am–1pm). Still pending (not seen in any search result, or evidence insufficient): Unreal (UK DPDR charity: registered charity 1186498 with a peer support programme confirmed, but unrealuk.org itself never appeared in results), r/StopSelfHarm (nothing found), Bipolar UK eCommunity (already listed separately). |
| 2026-10-22 | r/BPDlovedones | reddit | Not listed | Community rules bar people with borderline personality disorder from participating and much content frames them as abusers. Useful to some family members, but listing it next to the BPD card would expose people with the diagnosis to stigmatising content. Family members are pointed to NEABPD Family Connections instead. |
| 2026-10-22 | r/SuicideWatch | reddit | Not listed pending verification | Large (reported ~600K). Second pass found a 2019 moderator announcement of an incitement wiki (how to avoid validating suicidal intent, reporting covert encouragement), which confirms active moderation policy, but only via mirror sites and only from 2019; a 2016 report notes no emergency backup. A reviewer should read the live sidebar and wiki and sample recent threads before deciding. Alternatives to Suicide groups are listed instead for the suicidal-thoughts card. |
| 2026-10-22 | Game Quitters (gamequitters.com) | web | Not listed (commercial) | Sells paid programmes and coaching. The founder-moderated subreddit r/StopGaming is listed with a note; the paid site is not. |
| 2026-10-22 | NEDA website chatbot ("Tessa") | web | Excluded | Withdrawn in 2023 after giving weight-loss advice to people with eating disorders. Never list an automated bot as support. |
| 2026-10-22 | Any community selling "testosterone boosters", "libido supplements" or "dhat cures" | any | Excluded (standing rule) | Supplement and miracle-cure selling. Relevant to the sexual dysfunction and dhat cards. |
| 2026-10-22 | r/Narcissist-themed "survivor" communities that diagnose named ex-partners | reddit/web | Not listed | Encourages armchair diagnosis of third parties and stigmatises people with narcissistic personality disorder. Partner-abuse cards point to domestic abuse helplines instead. |
| 2026-10-22 | 7 Cups | web | Not listed | Second pass: listener guidance routes all suicide talk to a crisis page (a sensible rule) and early coverage mentions background checks, but recent Trustpilot reviews (including 2026) describe harmful listener replies answered only with template messages, no independent evaluation of listener training or safety was found, and the site sells paid therapy. Listing is not justified on current evidence; revisit if an independent audit appears. |
| 2026-10-22 | Facebook groups (all) | facebook | Not listed | Brief rule: no Facebook unless nonprofit-run and verified. None could be verified from the build environment. |

| 2026-10-22 | r/selfharm | reddit | Not listed | Second pass: a 2024 University of Georgia study of 400 posts (forum of ~143K) found about one in five posts seeking answers to self-harm questions such as how to hide scars, and the researchers cautioned against relying on anonymous peers. No rules text was found. Recovery-focused resources (Cornell SIRR, SiOS) are listed instead. |
| 2026-10-22 | Unreal (UK DPDR charity) | web | Not listed pending verification | Registered charity (1186498, founded 2019, Bristol) running a DPDR peer support programme, confirmed via the Charity Commission register; but its own site never appeared in a search result, so no URL is listed. Add after opening unrealuk.org. |

## Verification backlog summary (for the QA report)

All 143 listed communities and all 55 crisis-line entries carry `verification_status: needs_verification` (or `conflicting_sources` where listings disagreed). Reason: the build environment's network policy blocked outbound web access, so no community page, subreddit, or helpline page was opened. Each entry records where its details were seen and what a reviewer must check. See `docs/qa-report.md` for the re-verification schedule.
