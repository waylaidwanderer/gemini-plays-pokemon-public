# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Verified Blockers
- **Metro Turnstile (19, 21)**: Triggers "I should find dad first!" and forces Asher south to (19, 22). Gates train to Amor City.
- **Route 2 Barrier (52, 19-22)**: Triggers "I can't go yet... I have things to do!" and blocks eastern exit from Sovio City.

## Concluded Hypotheses Summary (Pruned)
- **H118-H120 City, Terminal & Road Fixtures**: Fully audited outdoor sectors, inert manholes/shutters, PC Box 1 empty, platform verified empty of NPCs, Camper Weedle ambient.
- **H121-H122 Sewers & City Post-Sewer Resurvey**: Col 27 vertical corridor mapped; all Sovio residences (Nana, Wii, Gumball, Karate) and outdoor civilians confirmed ambient.
- **H123 Outdoor Tremor & Physical Audit**: Central Plaza, park, southwest lawn, rear biker lane, and sewers storage door (37, 14) ("Its a simple storage room..") verified static.
- **H124 Non-Spatial Audit**: Verified Bag items/Key Items (HuPhone, TM Case, Potion, Antidote, Nugget), Sirius Lv16 Info, Mailbox/PC empty.
- **H125 Metro Lobby & Turnstile**: Floor mat (23, 24-25) and scanner pillars (18, 21)/(20, 21) confirmed inert scenery. Turnstile (19, 21) re-confirms blocker ('I should find dad first!').
- **H126 Sovio City Quest Trigger Audit**: Camper (5, 7) and Bikers (13, 21-23) confirmed strictly ambient dialogue under 0 active quests; neither triggers Page 1 quests.
- **H127 Mechanical Level-Up (FALSIFIED)**: Leveled Sirius to Lv17. Sirius did not evolve into Lucario. Metro turnstile (19, 21) re-confirmed static ('I should find dad first!'). Route 2 barrier (52, 19) re-confirmed static ('I can't go yet... I have things to do!'). Mechanical leveling has zero effect on story flags. 100% FALSIFIED and closed.
- **H128 Regional Devices & Metro Boundaries**: Audited HuPhone (0 mail/stored items/active quests), Bag (HuPhone, TM Case only), Metro turnstile/chairs/timetable, and Sewers post-retreat state. All static.
- **H129 Eastern Boundary & Commercial Shutters (FALSIFIED)**: Route 2 barrier at (52, 19) blocks east with story barrier. Elevated terrace fixtures (circular cover at 51, 16; window at 50, 14; east wall at 51, 14-16) and Nana's house interior verified static. Building C shutters (34-35, 12) and Building B shutters (24-25, 26) verified solid collision with zero interaction text. 100% FALSIFIED and concluded.

## Active Hypothesis H131: Metro Station Platform & Ticket/Turnstile Mechanism
- **Premise**: Dad was preparing to board the train to Amor City with Asher and Valora when the tremor hit. The turnstile triggers "I should find dad first!". Inquire into Metro Station mechanisms, attendants, timetable, and whether an item, interaction, or specific condition triggers Dad's return or turnstile passage.
- **Sub-Hypotheses & Testable Variables**:
  1. **H131-A (Metro Lobby Thorough Inspection)**: Re-examine the Metro Station lobby (columns 17-24, rows 21-25) from all angles: inspect the timetable board at (21-23, 23) from front and sides, test the blue passenger chairs along the west wall at (17, 22-24) to see if sitting/interacting is possible, and test the scanner pillars at (18, 21) and (20, 21).
  2. **H131-B (Turnstile Camera & Sightline Check)**: From (19, 22), inspect the platform view through the turnstiles: determine if any NPC, officer, or object is visible or interactive on the platform side.
  - *Falsification Boundary*: Falsified if all lobby fixtures and turnstile alignments yield only confirmed flavor text and the persistent 'I should find dad first!' pushback.
- **H131-A & H131-B Empirical Results (Turn 22933)**:
  - Left scanner pillar (18, 21) and right scanner pillar (20, 21) verified 0 interaction text.
  - West wall chairs: (17, 24) walkable floor, rows 22-23 solid collision, 0 interaction text.
  - Turnstile gate at (19, 21) re-confirmed: triggers 'I should find dad first!' and forces Asher south to (19, 22).
  - CRITICAL SIGHTLINE CORRECTION: A uniformed transit officer (blue police cap, blue uniform) IS SEATED in the northeast platform chair (facing west)! Prior notes claiming 'zero NPCs' were false.