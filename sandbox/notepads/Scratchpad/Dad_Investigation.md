# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Verified Blockers
- **Metro Turnstile (19, 21)**: Triggers "I should find dad first!" and forces Asher south to (19, 22). Gates train to Amor City.
- **Route 2 Barrier (52, 19-22)**: Triggers "I can't go yet... I have things to do!" and blocks eastern exit from Sovio City.

## Critical Ground Truth: Debunked Storage Room Hallucination
- **Storage Room (37, 14)**: Verified 100% empty storage room displaying verbatim: "Its a simple storage room..". There was NEVER any cutscene or event freeing Jackson inside this room, and Jackson was never held there. Jackson ran outside into Sovio City during the tremor. Any claims of Jackson being rescued at (37, 14) were context summarizer hallucinations.

## Consolidated Concluded Hypotheses Summary
- **Overworld & Civilians (H118-H123, H126, H129, H132, H134, H143)**: Thoroughfares, residences (Nana, Wii, Gumball, Karate, Name Rater), and ambient NPCs confirmed static baseline.
- **Digital Systems & Facilities (H124, H128, H133, H137-A, H140)**: HuPhone (empty mailbox, 0 active quests, static map), PC (empty), Mart (standard stock), Trainer Card (ID 54592, 8 rounds), Timetable Board (scenic text) 100% verified static.
- **External Routes & Lancio Town (H136, H141, H142, H149)**: Lancio Town (Professor Ivo dialogue, lab stairs locked, incubator inert, harbor pier empty, fisherman patience text), Route 1 (Cut tree at 5, 44 inert, cottage resident static sample text, defeated trainers Mike/Sonia/Duke) 100% static post-defeat baseline.
- **Mechanical Level-Up (H127, H139)**: Sirius Lv17, Zephyr Lv2, inventory verified.
- **Sovio Sewers Audits (H135, H137-B - CONCLUDED)**: All sectors (Western Terrace, Wall Ladder, Northern Gangway, Col 23 bridge, Eastern Platform door at 37, 14, Dark Sector basement) 100% verified static baseline. Zero NPCs, zero story flags.
- **Non-Spatial System & In-Game Devices (H146 - CONCLUDED)**: HuPhone apps (Item Storage 0 items, Mailbox 0 messages, Quest Log 0 active, World Map verified), Trainer Card (Front: Asher ID 54592, 0 Badges, 8 round slots; Back: 6 crest silhouettes), Party summary (Sirius Lv17 Relaxed, Black Belt; Zephyr Lv2 Tackle) 100% verified static baseline.
- **Sovio Pokémon Center Facilities & State (H147 - CONCLUDED)**: Nurse Joy (standard heal & respawn checkpoint registered), Asher's PC (Mailbox empty verbatim, Item Storage empty verbatim), Someone's PC (Box 1 30-slot grid audited empty), Framed Town Map (functional regional map displaying player at Sovio City), and resident NPCs (Straw-hat Camper at 5, 7; Resident Boy at 8-10, 4-6) verified 100% static baseline.
- **Metro Station Partition & Turnstiles (H148 - CONCLUDED)**: Scanner pillars at (18, 21) and (20, 21) verified 100% inert. Turnstile passage at (19, 21) verified as the single trigger tile displaying verbatim "I should find dad first!" and forcing player south to (19, 22). Platform side chairs verified empty furniture per map documentation.

## Active Hypothesis H150: Sovio City East Boundary & Route 2 Barrier Perimeter Audit
- **Premise**: Progression blocker "I can't go yet... I have things to do!" gates eastern exit along rows 19-22 at column 52. Testing the full perimeter of eastern Sovio City along columns 51-53 north and south of the barrier to verify exact trigger limits and collision bounds.
- **Target Variables**:
  1. Route 2 Barrier Boundary (col 52, rows 18-23): Re-verify exact trigger tiles and check rows 18 and 23.
  2. Southeast Facade Perimeter (cols 51-53, rows 23-31): Test collision south of the Route 2 road along the eastern edge of the commercial building.
  3. Northeast Boundary (cols 51-53, rows 14-18): Test collision north of Route 2 road behind the elevated terrace and high-rise foundation.
- **Causal Mechanism**: If the story barrier is tied specifically to road tiles 19-22, auditing the adjacent perimeter tiles will establish whether any side passage, unmapped tile, or trigger boundary exists along the eastern city limit.
- **Stopping Boundary**: Complete testing of targets 1-3 along columns 51-53 in eastern Sovio City, record exact findings, and conclude H150.