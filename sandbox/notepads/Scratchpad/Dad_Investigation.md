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
- **H97: Communication Channel, Inventory & Surface House Audit (Turns 20761-20820)**: FALSIFIED. Audited HuPhone Mailbox/Item Storage (empty), World Map, Quest Log (no active quests), Bag Key Items (HuPhone, TM Case), surface residences (terrace and Wii houses static), and Route 2 barrier.
- **H98: Subterranean Investigation in Sovio Sewers (Turns 20821-20851)**: FALSIFIED. Complete re-traversal of Sovio Sewers (lower walkway row 28, western corridor, Western Terrace, Northern Gangway row 5, vertical bridge col 23, row 13 catwalk, storage room platform 37, 14) confirmed 100% vacated with zero NPCs, dropped items, or active progression triggers. Storage room at (37, 14) displays static inspection text ("Its a simple storage room..").
- **H99: Player Menus, Devices & Party State Audit (Turns 20886-20938)**: FALSIFIED. 100% comprehensive audit across Bag (3 pockets, strictly HuPhone and TM Case in Key Items), Party summaries (Sirius and Zephyr all 3 pages verified, standard moves/abilities, no field moves), Trainer Card (Front: 8 empty rounds, ¥8096, Back: 6 silhouettes), Options (standard GBA settings, Fast text), HuPhone (Item Storage/Mailbox empty, World Map verified, Quest Log confirmed zero active quests), and Metro Station fixtures (scanners inert, platform chairs empty). Progression is NOT gated by an unexamined menu toggle, inventory item, or party option.

## Active Hypotheses for Progression
### Hypothesis H101: Investigation of Overlooked Narrative Event Triggers
- **Core Premise Questioning**: For thousands of turns, exploration operated on the assumption that Jackson is physically standing as an overworld NPC in Sovio City, Lancio Town, or the Sewers waiting to be spoken to. However, exhaustive audits confirm Jackson's sprite is not present anywhere in these maps. Therefore, "finding Dad" is not a sprite-interaction event; it must be an event flag triggered by interacting with a key story figure, inspecting a critical narrative fixture, or advancing an unresolved prerequisite.
- **Empirical Test Results**:
  - Turns 20944-20949 Nurse Joy: Standard heal cycle completed, official Sovio City checkpoint registered, zero narrative announcements.
  - Turns 20950-20966 Corner PC Terminal (12, 1): Someone's PC Box 1 (0 Pokémon stored), Asher's PC Mailbox ("There's no Mail here."), Asher's PC Item Storage ("There are no items."), logged off cleanly.
  - Turns 20967-20969 Framed Town Map (11, 0): Standard regional map display, identical to HuPhone World Map.
- **Investigative Avenues**:
  1. **Sovio Pokémon Center Audit**: CONCLUDED. All internal fixtures (Nurse Joy, PC terminal, Town Map) verified 100% standard with zero story flags.
  2. **Route 2 Eastern Boundary ("I can't go yet... I have things to do!")**: CONCLUDED. Re-confirmed active at (52, 19) in Turn 20974 verbatim: "I can't go yet... I have things to do!".
  3. **Central Plaza & Outdoor Narrative Re-evaluation**: CONCLUDED. Central Plaza confrontation grounds, elevated terrace, and outdoor perimeters verified static with zero story triggers.
- **Falsifiable Success Criteria**: Triggering a new story dialogue/cutscene, learning Jackson's true status, or lifting the turnstile blocker ("I should find dad first!").
