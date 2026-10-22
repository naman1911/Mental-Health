from helpers import D, NV, c
COMMUNITIES = [
 c("sczaction-peer-groups", "Schizophrenia & Psychosis Action Alliance peer support groups", "video-meeting", "https://sczaction.org/peer-support-groups/", "online-group-meeting", ["adults", "family"], "both",
   ["understanding-psychosis", "schizophrenia", "schizoaffective-disorder", "schizophreniform-disorder", "delusional-disorder", "brief-psychotic-disorder"], "US (online)", has_rules=True, mods=True,
   notes="Peer-led groups for people with schizophrenia and psychosis-related conditions (Schizophrenia Alliance model: no dues, open to anyone who has experienced psychosis) plus biweekly groups for family members and caregivers; also runs an online community on Facebook and Inspire.",
   safety="Peer-led; not a crisis service.", reviewer="Confirm current group schedule and the Inspire community link."),
 c("nami-connection-and-helpline", "NAMI Connection peer support groups and NAMI HelpLine (US)", "web", "https://www.nami.org/Find-Support", "org-resource-hub", ["adults", "family"], "both",
   ["understanding-psychosis", "schizophrenia", "schizoaffective-disorder", "bipolar-i-disorder", "major-depressive-disorder", "catatonia"], "US", has_rules=True, mods=True, crisis=True,
   notes="NAMI Connection: free, peer-led support groups for adults with mental health conditions, run by local affiliates (in person and online). NAMI Family Support Group and Family-to-Family for relatives. NAMI HelpLine 1-800-950-6264, Mon–Fri 10am–10pm ET; text keyword to 62640 (sources differed on the keyword).",
   safety="Information and peer support; NAMI directs crises to 988.", reviewer="Confirm HelpLine text keyword and group finder URL."),
]
