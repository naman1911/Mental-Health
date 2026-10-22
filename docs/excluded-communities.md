# Excluded and not-listed communities

Keep this log so later reviewers don't re-add something that was already checked and rejected. Add one row per decision, with the date.

## Exclusion rules (from the project brief, section 2 and 7.1)

A community is excluded if it promotes or tolerates any of: pro-eating-disorder content, self-harm encouragement, suicide methods or pacts, anti-treatment conspiracies, incel or hate ideology, selling supplements, courses or "miracle cures", MLM recruitment, or unlicensed paid coaching in place of support. It is also excluded if it fails any verification check: doesn't exist, no activity in 14 days, no visible rules or moderation, or commercial purpose.

## Log

| Date | Community | Platform | Decision | Reason |
|---|---|---|---|---|
| 2026-10-22 | NEDA Helpline (US) | phone/chat | Not listed (defunct) | NEDA closed its human helpline in May 2023 and withdrew its replacement chatbot after it gave harmful weight-loss advice. NEDA's website remains a resource hub; its helpline must not be listed as a support line. Source: NPR, 31 May 2023. |
| 2026-10-22 | Any pro-ana / pro-mia / "thinspo" community | any | Excluded (standing rule) | Promotes eating-disorder behaviour. Never list, never link, even to warn. |
| 2026-10-22 | Subreddits or forums whose URL could not be confirmed in a search result | any | Not listed pending verification | Project rule: no guessed community names or URLs. Candidates noted for the reviewer: International Bipolar Foundation, FEAST (family eating-disorder support), ANAD peer groups, r/Autism_Parenting, Griefline (AU, 1300 845 745), The Compassionate Friends, Autistic Self Advocacy Network, Winston's Wish (UK child bereavement, 08088 020 021), AFSP Healing Conversations (US suicide loss), Friends for Survival (US), Ditch the Label (bullying), Kidscape parent advice line (UK), Rethink Mental Illness advice line (UK, 0808 801 0525), Mind Infoline (UK, 0300 123 3393), Self-injury Outreach and Support (SiOS, McGill/Guelph), Unreal (UK depersonalisation charity), r/dpdr, r/selfharm, r/StopSelfHarm, ERIC's current helpline number. The web-search budget ran out before these could be checked; none appeared in a search result, so none is listed. Add after opening each one. |
| 2026-10-22 | r/BPDlovedones | reddit | Not listed | Community rules bar people with borderline personality disorder from participating and much content frames them as abusers. Useful to some family members, but listing it next to the BPD card would expose people with the diagnosis to stigmatising content. Family members are pointed to NEABPD Family Connections instead. |
| 2026-10-22 | r/SuicideWatch | reddit | Not listed pending verification | Large (reported ~600K) and has a documented volunteer moderation model that removes method talk and "tough love" replies, but a 2022 thesis describes it as unmoderated and a 2016 report notes it has no emergency backup. Evidence on moderation conflicts; a reviewer should read the current rules and sample recent threads before deciding. Alternatives to Suicide groups are listed instead for the suicidal-thoughts card. |
| 2026-10-22 | Game Quitters (gamequitters.com) | web | Not listed (commercial) | Sells paid programmes and coaching. The founder-moderated subreddit r/StopGaming is listed with a note; the paid site is not. |
| 2026-10-22 | NEDA website chatbot ("Tessa") | web | Excluded | Withdrawn in 2023 after giving weight-loss advice to people with eating disorders. Never list an automated bot as support. |
| 2026-10-22 | Any community selling "testosterone boosters", "libido supplements" or "dhat cures" | any | Excluded (standing rule) | Supplement and miracle-cure selling. Relevant to the sexual dysfunction and dhat cards. |
| 2026-10-22 | r/Narcissist-themed "survivor" communities that diagnose named ex-partners | reddit/web | Not listed | Encourages armchair diagnosis of third parties and stigmatises people with narcissistic personality disorder. Partner-abuse cards point to domestic abuse helplines instead. |
| 2026-10-22 | 7 Cups | web | Not listed pending verification | Allowed by the brief, but its listener model is unverified volunteers and it sells paid therapy; reviewer should check current moderation and crisis-handling policy before listing. |
| 2026-10-22 | Facebook groups (all) | facebook | Not listed | Brief rule: no Facebook unless nonprofit-run and verified. None could be verified from the build environment. |

## Verification backlog summary (for the QA report)

All 127 listed communities and all 55 crisis-line entries carry `verification_status: needs_verification` (or `conflicting_sources` where listings disagreed). Reason: the build environment's network policy blocked outbound web access, so no community page, subreddit, or helpline page was opened. Each entry records where its details were seen and what a reviewer must check. See `docs/qa-report.md` for the re-verification schedule.
