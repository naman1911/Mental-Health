from helpers import D, NV, c
COMMUNITIES = [
 c("reddit-r-bipolar", "r/bipolar", "reddit", "https://www.reddit.com/r/bipolar/", "subreddit", ["adults", "teens-16+"], "people-with-experience",
   ["bipolar-i-disorder", "bipolar-ii-disorder", "cyclothymic-disorder", "schizoaffective-disorder"], "global", members=295000, size_note="Third-party tracker figure.",
   notes="Described as peer support for people with bipolar disorder, cyclothymia, or schizoaffective disorder, or seeking diagnosis. Rules not seen directly.",
   reviewer="Read the sidebar rules; check for pinned crisis resources and whether family posts are redirected."),
 c("dbsa-online-support-groups", "DBSA online support groups", "video-meeting", "https://www.dbsalliance.org/support/online-support-groups/", "online-group-meeting",
   ["adults", "young-adults"], "both", ["bipolar-i-disorder", "bipolar-ii-disorder", "major-depressive-disorder", "persistent-depressive-disorder"], "US (some groups open worldwide)",
   has_rules=True, mods=True, crisis=True, notes="Depression and Bipolar Support Alliance; free peer-led groups, trained peer facilitators, hosted on HeyPeers and by local chapters; also family and parent groups; crisis page points to 988.",
   reviewer="Confirm current meeting schedule and the family/friends group link."),
 c("reddit-r-bipolarsos", "r/BipolarSOs", "reddit", "https://www.reddit.com/r/BipolarSOs/", "subreddit", ["adults"], "family-and-carers",
   ["bipolar-i-disorder", "bipolar-ii-disorder"], "global", members=52000, size_note="Trackers showed ~50K–55K.",
   has_rules=True, mods=True, notes="For partners and loved ones. Mods require posts to be about the poster's own relationship; posts generalizing about 'all bipolar people' are removed. Tone can be raw; vent-heavy.",
   safety="Vent-heavy space for partners. Peer support, not professional advice. Reviewer to judge whether tone is appropriate to link from a condition card.",
   reviewer="Sample recent posts for stigmatizing generalizations before approving."),
]
COMMUNITIES += [
 c("bipolar-uk-ecommunity", "Bipolar UK eCommunity", "nonprofit-forum", "https://www.bipolaruk.org/get-support/online-community/", "peer-forum", ["adults"], "both",
   ["bipolar-i-disorder", "bipolar-ii-disorder", "cyclothymic-disorder"], "UK (open worldwide)", members=15000, size_note="Over 15,000 members per Bipolar UK.",
   has_rules=True, mods=True, crisis=True, notes="Charity-run forum open 24/7, moderated 8am–8pm daily (conversations) and set hours for peer-support-group spaces; published house rules; explicitly not a crisis service.",
   reviewer="Register and record last post date."),
]
