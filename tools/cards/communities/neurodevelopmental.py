from helpers import D, NV, c
COMMUNITIES = [
 c("reddit-r-autism", "r/autism", "reddit", "https://www.reddit.com/r/autism/", "subreddit", ["adults", "teens-16+"], "both",
   ["autism-spectrum-disorder"], "global", members=378000, size_note="Tracker figure (tool closed Nov 2025); likely higher now.",
   notes="'Autism news, information and support.' Rules not seen directly.", reviewer="Read rules; check how parent posts and 'cure' content are handled."),
 c("reddit-r-autisticadults", "r/AutisticAdults", "reddit", "https://www.reddit.com/r/AutisticAdults/", "subreddit", ["adults"], "people-with-experience",
   ["autism-spectrum-disorder"], "global", members=126000, size_note="Tracker figure; likely higher now.",
   has_rules=True, notes="For autistic adults, diagnosed or not; describes itself as relaxed and rules-light; asks promoters and people seeking help 'dealing with' an autistic person to read the community guide first.",
   reviewer="Confirm moderation is active and check for pinned crisis resources."),
 c("reddit-r-autisminwomen", "r/AutismInWomen", "reddit", "https://www.reddit.com/r/AutismInWomen/", "subreddit", ["adults"], "people-with-experience",
   ["autism-spectrum-disorder"], "global", members=276000, size_note="Tracker figure; likely higher now.",
   has_rules=True, notes="For autistic women and marginalized genders, including LGBTQIA+ people; excludes cis men.", reviewer="Read rules and check moderation activity."),
 c("nas-online-community", "National Autistic Society Online Community", "nonprofit-forum", "https://www.autism.org.uk/community", "peer-forum", ["adults"], "both",
   ["autism-spectrum-disorder"], "UK (open worldwide)", members=3500, size_note="NAS cites over 3,500 active users; a vendor case study claimed 42,000. Use the NAS figure.",
   has_rules=True, mods=True, notes="Separate areas for autistic adults and for parents and carers, plus women and girls, health and lifestyle, and mental health boards; registration required; stated rules for safety; 18+.",
   reviewer="Record last post date in the adults and parents boards."),
]
