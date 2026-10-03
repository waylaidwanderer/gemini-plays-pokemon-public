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

- **H127 Mechanical Level-Up (FALSIFIED)**: Leveled Sirius to Lv17. Sirius did not evolve into Lucario. Metro turnstile (19, 21) re-confirmed static ('I should find dad first!'). Route 2 barrier (52, 19) re-confirmed static ('I can't go yet... I have things to do!'). Mechanical leveling has zero effect on story flags. 100% FALSIFIED and closed. Backtracking to Lancio discontinued.

## Active Hypothesis H128: Jackson's Tremor Investigation in Sovio City
- **Premise**: During the tremor at Sovio Metro Station, Dad ran outside into Sovio City to investigate the source of the tremor (Dad never entered the sewers). The Metro turnstile blocks Asher with "I should find dad first!", confirming Dad is located somewhere in Sovio City investigating the tremor. Platform chairs confirmed empty (no transit officer).
- **Core Testable Variables**:
  1. Audit regional devices and Key Items (HuPhone apps: Item Storage, World Map, Quest Log, Town Map interaction).
  2. Audit unvisited structural connections and boundary tiles in Sovio Metro Station and Sovio Sewers.
- **Milestones**:
  1. Heal party at Sovio Pok�mon Center with Nurse Joy -> COMPLETE (Turn 22744). Sirius fully restored to 47/47 HP, cured of PSN, and Sovio checkpoint registered.
  2. Systematic audit of HuPhone apps -> COMPLETE (Turn 22759):
     - World Map: Audited. Shows standard regional topology; zero quest markers or destination highlights.
     - Quest Log (Quest Status): Audited. Verbatim: "You aren't doing any Quest currently...". Side quest tracker is empty.
     - Quest Log (Quest List): Audited (25 quests across 5 pages). Page 1: Lost Pidgey and Lost Toy completed.
     - Item Storage (Withdraw Item): Audited. Verbatim: "There are no items." Zero items stored in PC.
     - Item Storage (Mailbox): Audited. Verbatim: "There's no Mail here." Zero mail present.
     - Conclusion: HuPhone contains zero pending items, unread mail, or active story objectives.
  3. Audit Bag Key Items & Metro Station structural boundaries -> COMPLETE (Turn 22785):
     - Bag Key Items: Audited. Contains exclusively HuPhone (registered) and TM Case (0 other Key Items).
     - Metro Lobby: Turnstile at (19, 21) triggers "I should find dad first!" and forces step down to (19, 22). Platform chairs verified empty mirrored passenger furniture (zero NPCs present). Scanner pillars and blue chairs confirmed inert scenery. Timetable displays decorative schedule flavor text.
     - Sewer re-entry check: Grounded in lore that Dad ran outside into Sovio City during the tremor (Dad never entered the sewers). Sewers remain in verified post-retreat state.
## Reflection & Hypothesis Review (Turn 22823)
- **Turnstile Blocker Grounding**: The turnstile literally states 'I should find dad first!' and Route 2 states 'I can't go yet... I have things to do!'. Finding Dad is the sole active blocker gating the train to Amor City.
- **Summary Hallucination Audit**: Prior context summary claimed Dad was freed and departed toward the station at turn 2716, but this contradicts the persistent 'I should find dad first!' trigger. Dad has not been found.
- **Next Step**: Ascend from Sovio Sewers back to Sovio Metro Station lobby and Central Plaza, then systematically audit all potential locations for Dad or event triggers related to Dad's disappearance.
## Active Hypothesis H129: Jackson's Whereabouts & Progression Blocker Audit
- **Premise**: Dad ran outside into Sovio City during the tremor to investigate. The Metro turnstile ("I should find dad first!") and Route 2 barrier ("I can't go yet... I have things to do!") prove Dad has not been found. Prior context summaries claiming Dad was freed at turn 2716 are confirmed hallucinations.
- **Sub-Hypotheses & Testable Variables**:
  1. **H129-A (Eastern Perimeter & Route 2 Approach)**: Systematically audit the eastern edge of Central Plaza (columns 50-55, rows 16-23), including the wall crest at (50, 16), building facade at columns 52-54, and the Route 2 boundary tiles.
     - *Falsification Boundary*: Falsified if all tiles along columns 50-55 (rows 16-23) are confirmed impassable or trigger only the known Route 2 barrier text with zero new NPCs, doors, or flags.
  2. **H129-B (Central Plaza Fixture & Alignment Audit)**: Verify exact alignment interactions with Central Plaza structures, including the Metro Station portal exterior and the terrace building.
     - *Falsification Boundary*: Falsified if all fixtures have zero interaction or only confirmed ambient text.
  3. **H129-C (Regional Dependency Re-Evaluation)**: If H129-A and H129-B yield no progress, audit external dependencies: Route 1 Cut tree at (5, 44) and Professor Ivo's Lab restricted basement stairs at (12, 7) to determine if an external item/equipment trigger is required.