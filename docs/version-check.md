# DSM version check

**Checked on:** 2026-10-22
**Result:** DSM-5-TR (American Psychiatric Association, March 2022) is still the current edition. No DSM-6 or "DSM-5.x" has been published or formally announced. Work continues on DSM-5-TR.

## How this was checked

The session's cloud container blocks direct connections to psychiatry.org and most other outside sites (the environment's network policy answered 403 to every connect). Pages could therefore not be opened and read in full. The findings below come from web search results that quote the APA's own pages and PDFs. Each item names the APA source URL that should be opened and re-read by a human reviewer, or by this project once network access is widened.

| Status | Meaning |
|---|---|
| `search-confirmed` | The fact appeared in search-engine text quoting an APA page or PDF |
| `needs_verification` | Reported by a secondary site only, or not found in search |

## What was found

### 1. Current edition

- DSM-5-TR was published in 2022 and remains the standard manual. `search-confirmed`
  Source: https://www.psychiatry.org/psychiatrists/practice/dsm (APA)
- The APA's Future DSM Strategic Committee released a "roadmap" on 2026-01-28 (five papers in the *American Journal of Psychiatry*). It proposes a future name, "Diagnostic and Scientific Manual", and four organizing domains. **No release date and no edition name were announced.** `search-confirmed`
  Sources: https://www.psychiatry.org/news-room/news-releases/apa-releases-roadmap-for-future-of-dsm (APA); https://www.psychiatrictimes.com/view/updating-the-dsm-reviewing-the-new-apa-dsm-recommendations
- At the 2025 APA Annual Meeting a spokesperson gave an informal target of "about four years" for the next edition. Outside commentators estimate 2029–2030. These are not APA commitments. `needs_verification` (Medscape report, not opened)
  Source: https://www.medscape.com/viewarticle/apa-unveils-early-plans-next-dsm-2025a1000eu1

### 2. Official updates to DSM-5-TR since 2022

The APA posts a yearly "DSM-5-TR Update" supplement (criteria and text changes) and a yearly ICD-10-CM coding update, both effective 1 October.

| Update | Effective | What changed (summary) | Status |
|---|---|---|---|
| September 2022 supplement and coding update | 2022-10-01 | Prolonged Grief Disorder coding update (now F43.81); Other Specified Trauma- and Stressor-Related Disorder (now F43.89); coding updates for major and mild neurocognitive disorder and delirium | `search-confirmed` for the headings; exact codes `needs_verification` |
| September 2023 supplement | 2023-10-01 | Not surfaced by search in this session | `needs_verification` |
| September 2024 supplement and coding update | 2024-10-01 | New adult pica code F50.83 and adult rumination disorder code F50.84; anorexia nervosa, bulimia nervosa and binge-eating disorder gained severity- and remission-specific codes (for example F50.010–F50.014 restricting type; F50.20–F50.25; F50.810–F50.814) | `search-confirmed` |
| September 2025 supplement and coding update | 2025-10-01 | Standardized wording for recording "other specified" presentations across bipolar, depressive, somatic, eating, insomnia and delirium categories; clarified the word "cyclothymia" in Other Specified Bipolar examples; multiple sclerosis code G35 → G35.D | `search-confirmed` |
| 2026 | — | APA states no ICD-10-CM code changes are planned for DSM-5-TR in 2026; criteria and text changes will be posted in early 2027 | `search-confirmed` (APA DSM page text quoted in search) |
| Open comment period | 2026-09-29 to 2026-10-29 | Proposed correction to the severity specifiers for anorexia nervosa, bulimia nervosa and binge-eating disorder. A proposal, not a change | `search-confirmed` |

Sources to open and re-read:
- https://www.psychiatry.org/psychiatrists/practice/dsm/updates-to-dsm
- https://www.psychiatry.org/psychiatrists/practice/dsm/updates-to-dsm/dsm5tr-code-updates
- https://www.psychiatry.org/getmedia/304e9a98-ca5c-4e04-97d7-30b4756705eb/APA-DSM5TR-Update-September-2022.pdf
- https://www.psychiatry.org/getmedia/172db6ec-8146-4bb4-be2a-49e9c61bcc94/APA-DSM5TR-ICD10CM-Code-Updates-092024.pdf
- https://www.psychiatry.org/getmedia/2ed086b0-ec88-42ec-aa0e-f442e4af74e6/APA-DSM5TR-Update-September-2024.pdf
- https://www.psychiatry.org/getmedia/b68a5776-f88c-45c7-9535-fd219d7aa5cb/APA-DSM5TR-Update-September-2025.pdf
- https://www.psychiatry.org/psychiatrists/practice/dsm/proposed-changes

### 3. What this means for the project

- Build on DSM-5-TR. Use the chapter structure of the 2022 text.
- Use ICD-10-CM codes as of the October 2025 coding update. Where a code changed after 2022, `data/taxonomy.json` records the current code and notes the old one.
- Eating-disorder severity codes may be corrected again after the October 2026 comment period. Re-check them at the next clinical review.
- Re-run this check whenever the APA posts a new supplement (expected early 2027) and at the 12-month clinical review.

## Caveat

Because no page was opened directly, every item above should be treated as "reported, not read". A reviewer with normal web access should open the APA links and confirm before publication. This is logged as an open item in the QA report.
