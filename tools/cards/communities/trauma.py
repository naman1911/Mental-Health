from helpers import D, NV, c
COMMUNITIES = [
 c("reddit-r-griefsupport", "r/GriefSupport", "reddit", "https://www.reddit.com/r/GriefSupport/", "subreddit", ["adults", "teens-16+"], "people-with-experience",
   ["prolonged-grief-disorder", "grief-and-bereavement"], "global", members=120000, size_note="Tracker figure; likely higher now.",
   has_rules=True, mods=True, crisis=True, notes="Mod post from Jan 2026 seen: rules in sidebar, members asked not to question anyone's loss; community wiki with support groups and phone numbers; companion Discord.",
   reviewer="Read sidebar rules and confirm the wiki's crisis resources are current."),
 c("cruse-bereavement-support", "Cruse Bereavement Support (UK) helpline and CruseChat", "phone", "https://www.cruse.org.uk/", "helpline", ["adults", "young-people"], "both",
   ["prolonged-grief-disorder", "grief-and-bereavement"], "UK",
   has_rules=True, mods=True, notes="Free helpline 0808 808 1677 run by trained bereavement volunteers (hours differ between sources); CruseChat live chat Mon–Fri 9am–9pm run by a bereavement counsellor.",
   safety="Charity-run support, not a crisis service.", reviewer="Confirm helpline hours on cruse.org.uk."),
 c("reddit-r-widowers", "r/widowers", "reddit", "https://www.reddit.com/r/widowers/", "subreddit", ["adults"], "people-with-experience",
   ["prolonged-grief-disorder", "grief-and-bereavement"], "global", notes="For people who have lost a spouse or partner; seen in tracker listing only.",
   reviewer="Read rules, check moderation and crisis resources; record member count."),
]
