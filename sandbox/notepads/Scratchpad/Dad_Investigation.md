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

## Active Hypothesis H127: Mechanical Progression & Level-Up Investigation
- **Premise**: 126 spatial/dialogue hypotheses exhausted. Testing unexamined mechanical progression variables: leveling up Sirius to Lv17 (482 EXP needed) to test daytime friendship evolution into Lucario and Professor Ivo dialogue reaction.
- **Milestones**:
  1. Inspect Trainer Card (ASHER) -> COMPLETE (Turn 22509). Money: ¥6096, Playtime: 158:06, Rounds: 0/8, Badges: 0/6.
  2. Party Audit & Lead Reorder -> COMPLETE (Turn 22524). Sirius 100% audited across Pages 1-3. Zephyr swapped to Slot 1.
  3. Swap Sirius back to Slot 1 (lead) -> COMPLETE (Turn 22537). Sirius (Lv16 Riolu) confirmed lead; Zephyr (Lv2 Pidgey) in Slot 2.
  4. Battle wild encounters in Sovio Sewers to gain 482 EXP and level Sirius to Lv17 -> COMPLETE (Turn 22658).
     - Benchmarks: Started Turn 22504. Completed Turn 22658 (154 turns elapsed).
     - Progress: Battles 1-14 yielded +529 EXP total (B14 Purrloin Lv6 gave +48 EXP). Sirius reached Lv17 (HP 42/47)!
  5. Falsification Protocol -> IN PROGRESS:
     - Evolution Check: COMPLETE (Turn 22658). Sirius reached Lv17 (Stats: HP 47, Atk 32, Def 31, SpAtk 22, SpDef 25, Speed 23) but did NOT evolve into Lucario. Friendship threshold not met at this level.
     - Blocker Check 1: COMPLETE (Turn 22665). STATIC / FAILED: Turnstile (19, 21) still triggers "I should find dad first!". Level 17 does not unlock Metro.
     - Blocker Check 2: COMPLETE (Turn 22667). STATIC / FAILED: Route 2 barrier (52, 19) still triggers "I can't go yet... I have things to do!". Level 17 does not unlock Route 2.
     - Blocker Check 3: IN PROGRESS -> Heading to Lancio Lab to check Professor Ivo (20, 6).
     - Strict Cutoff: If all three remain static upon reaching Lv17, H127 is 100% FALSIFIED and closed; no further level grinding.