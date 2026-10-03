# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Verified Blockers
- **Route 2 Barrier (52, 19-22)**: Triggers "I can't go yet... I have things to do!" and blocks eastern exit from Sovio City.
- **Metro Turnstile (19, 21)**: Triggers "I should find dad first!" and forces Asher south to (19, 22). Scanner pillars (18, 21) and (20, 21) verified 100% inert; platform chairs verified empty; north wall across columns 21-23 is solid brick with timetable board mounted.
- **Rugged Rocks (Sovio Sewers)**: Obstacles at (22, 10) in Dark Sector and (10, 18) / (9, 17) in southwest corridor require specialized equipment.
- **Storage Room (37, 14)**: Verified single static inspection trigger ("Its a simple storage room..") with solid collision at (37, 15); platform fully audited.

## Concluded Hypotheses
- **H60-H94 (Baseline Sweeps & Local Trigger Invalidation - Turns 7232-20521)**: FALSIFIED. Comprehensive audits across Sovio City residences, Central Plaza confrontation ground tiles, Metro lobby fixtures/turnstiles, and post-retreat sewer platforms/storage rooms are 100% static with zero hidden progression triggers. Jackson's presence in the sewers was an unverified narrative assumption from the early cutscene; no character sprite or rescue event was ever physically verified in the storage room.
- **Route 1 Cut Tree (Turns 20616-20622)**: Performed stationary interaction facing North into Cut tree at (5, 44); confirmed zero dialogue prompt appears without Cut learned.
- **H95: Lancio Town Regional & Facility Audit (Turns 20616-20723)**: FALSIFIED. Comprehensive empirical audit across Lancio Town confirmed that all facilities, residents, and harbor pier are static with zero progression triggers. Concluded zero external story triggers exist in Lancio Town.
- **H96: Multi-Angle Decorative Tile Pixel-Hunting (Turns 20724-20760)**: FALSIFIED. Pixel-hunting orientation-dependent interaction on decorative road tiles is ungrounded in engine mechanics; abandoned per critique.
- **H97: Communication Channel, Inventory & Surface House Audit (Turns 20761-20820)**: FALSIFIED for surface house triggers. Empirical results:
  - HuPhone Mailbox & Item Storage: Audited empty ("There's no Mail here", "There are no items").
  - HuPhone Quest Log & World Map: World Map clean, Quest Status confirms "You aren't doing any Quest currently...".
  - Bag Key Items: Strictly HuPhone and TM Case; Poké Balls, Items, TMs standard.
  - Metro Lobby: Turnstile re-confirmed "I should find dad first!", platform chairs verified empty.
  - Surface Residences: Re-audited terrace house (49, 14) and Wii house (39, 7) (both confirmed 100% static ambient dialogue).
  - Route 2 Barrier: Re-confirmed active ("I can't go yet... I have things to do!"). Column 51 roof collision confirmed solid.
- **H98: Subterranean Investigation in Sovio Sewers (Turns 20821-20851)**: FALSIFIED. Complete re-traversal of Sovio Sewers (lower walkway row 28, western corridor, Western Terrace, Northern Gangway row 5, vertical bridge col 23, row 13 catwalk, storage room platform 37, 14) confirmed 100% vacated with zero NPCs, dropped items, or active progression triggers. The storage room at (37, 14) re-confirmed static inspection text ("Its a simple storage room.."). The Dark Sector was previously cleared (Nugget and Lost Toy retrieved), and rugged rocks require equipment not currently possessed.

- **H99: Player Menus, Devices & Party State Audit (Turns 20886-20938)**: CONCLUDED / FALSIFIED. Comprehensive audit across Bag (3-pocket engine, Key Items strictly HuPhone and TM Case; zero tickets or equipment), Party (Sirius Lv16, Zephyr Lv2, all 3 summary pages audited, standard abilities/moves, Black Belt held, no field moves), Trainer Card (Front: 8 empty rounds, ¥8096, Back: 6 silhouettes), Options (standard GBA settings, Fast text), HuPhone (Item Storage/Mailbox empty, World Map verified, Quest Log confirmed zero active quests), and Metro Station fixtures (scanner pillars inert, platform chairs empty). Confirmed progression is NOT gated by an unexamined menu toggle, inventory item, or party option.

## Active Hypotheses for Progression
### Hypothesis H101: Investigation of Overlooked Narrative Event Triggers
- **Core Premise Questioning**: For thousands of turns, exploration operated on the assumption that Jackson is physically standing as an overworld NPC in Sovio City, Lancio Town, or the Sewers waiting to be spoken to. However, exhaustive audits confirm Jackson's sprite is not present anywhere in these maps. Therefore, "finding Dad" is not a sprite-interaction event; it must be an event flag triggered by interacting with a key story figure, inspecting a critical narrative fixture, or advancing an unresolved prerequisite.
- **Investigative Avenues**:
  1. **Sovio Pokémon Center Audit**: Re-examine Nurse Joy, the PC terminal, and residents specifically regarding news or updates following the Siara retreat.
  2. **Route 2 Eastern Boundary ("I can't go yet... I have things to do!")**: Re-evaluate what explicit prerequisites ("things to do") are required before Asher can leave Sovio City.
  3. **Valora & Central Plaza Investigation**: Search for clues regarding Valora's destination or Jackson's movements following the Metro tremor.
- **Falsifiable Success Criteria**: Triggering a new story dialogue/cutscene, learning Jackson's true status, or lifting the turnstile blocker ("I should find dad first!").
