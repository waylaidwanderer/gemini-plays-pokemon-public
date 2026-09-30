# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Current Blockers & Ground Truths
- Metro Station turnstile at (19, 21): Triggers "I should find dad first!" and repels player 1 step South.
- Route 2 exit at (52, 19-21): Triggers "I can't go yet... I have things to do!" and repels player 1 step West.
- Jackson last seen departing the Metro Station lobby into Sovio City following the seismic tremor (Turn 1437).
- Team Siara grunts permanently retreated from Sovio Sewers after Marie's broadcast (Turn 2682).
- Eastern Storage Room at (36-37, 14): Audited inert Turn 8637 ("Its a simple storage room...").
- Dark Sector / Basement: Explored; contains rugged Rock Smash rock at (22, 10) and Nugget at (23, 4). All accessible sewer sectors confirmed cleared and inert.

## Falsified Hypotheses
- **Hypothesis 1 (Side Quest State Dependency)**: Falsified Turn 9376. Cancelling "Lost Toy" did not affect Metro or Route 2 roadblocks.
- **Hypothesis 2 (Surface NPC Persistence Audit)**: Falsified Turns 9462-9537. All surface civilian NPCs and residential structures in Sovio City strictly cycle ambient flavor dialogue with zero secondary branches or progression triggers.
- **Hypothesis 3 (Environmental & Structural Features in Sovio Metro & City)**: Falsified Turns 9637-9788. All accessible structural fixtures (park barrels, alley walls, boundary alcoves, timetable display, scanner pillars, decorative manholes) empirically tested with zero interaction triggers.
- **Hypothesis 4 (Macro-Traversal & Level 15 Evolution)**: Falsified. Riolu evolves via friendship, not level 15. Lancio Town and Route 1 NPCs exhibit static ambient dialogue.
- **Hypothesis 5 (Inventory & Key Item Triggers / Bag Items / HuPhone Inspection)**: Falsified Turns 9856-9901. HuPhone apps (Item Storage, Mailbox, World Map, Quest Log) and Bag pockets audited static with zero interactive story triggers or progression tools.
- **Hypothesis 6 (Macro-Exploration of Route 1 & Lancio Town Boundaries)**: Falsified Turns 10042-10103. Route 1 southern corridor, Lancio Pokémon Center, Professor Ivo's Lab (basement stairs story-blocked), Southwest Beach, Northwest House (boy kicks out), Lancio Harbor pier (no boat/ferry), fisherman (ambient), and dockside house facade exhaustively audited. All regional perimeters remain strictly bounded with zero secondary branches or open warps.

## Hypothesis 7 (Empirical Re-evaluation of Transit Hub & Sewer Storage Triggers)
- **Proposition**: Progression requires resolving Dad's status through an unverified interaction trigger rather than physical map discovery. Specifically, either:
  (a) The sewer storage room threshold at (36-37, 14) requires multi-angle cardinal testing or item/party interaction to trigger Jackson's discovery,
  (b) The Metro turnstile at (19, 21) or station attendant at (22, 19) has an untriggered interaction parameter, or
  (c) A map reload event flag triggers in Sovio City surface after returning from Lancio Town.
- **Protocol**:
  1. Complete transit across Route 1 to enter Sovio City.
  2. Test Sovio City plaza and Pokémon Center for any reloaded event scripts or NPC dialogue shifts.
  3. Re-probe the Metro Station turnstile (19, 21), timetable, and attendant line-of-sight from (19, 22) and (20, 22).
  4. Descend into Sovio Sewers to the Eastern Storage Room at (36-37, 14); execute comprehensive 4-directional interaction testing (facing North, South, East, West on tiles 36,14 and 37,14).
- **Falsification Criteria**:
  - Prop (a) Falsification: If all 4 cardinal angles and item/party probes on the sewer storage room threshold at (36-37, 14) return static dialogue ("Its a simple storage room...").
  - Prop (b) Falsification: If Metro Station turnstile (19, 21), attendant (22, 19), and lobby fixtures return static repulsion text ("I should find dad first!").
  - Prop (c) Falsification: If a full re-survey of Sovio City surface NPCs and buildings following map reload confirms identical ambient text without new story flags.
  - Overall Hypothesis 7 is FALSIFIED only when all three sub-propositions (a, b, c) have been empirically tested and falsified, proving the required trigger is located elsewhere.
## Turn 10498 Reflection & Macro Routing Re-alignment
- **Reflection**: Re-evaluated Route 1 topology. In early-game progression (Turns 666-1165), Asher traversed from Lancio to Sovio via the Northwest Clearing (Mike at 29, 20 and Sonia at 27, 15) to Duke (45, 12) and Sovio City (53, 0).
- **Hypothesis 10 (Far-Western Sector Columns 0-4 Northbound Survey)**:
  - **Context**: Columns 12-18 are confirmed blocked northward by solid trees/hedges at rows 40-42.
  - **Resolution (Turn 10524)**: FALSIFIED for columns 3-4. Probed (4, 44) and (4, 43) (open alcove adjacent to Cut Tree), (4, 42) (solid pine tree trunk), (3, 44) and (3, 43) (solid pine trees). Northern passage at column 5 is gated by the Cut Tree.
- **Central Meadow Row 38 Testing (Turns 10585-10587)**: (28, 40) blocked by small pine tree. (27, 38) confirmed solid pine tree trunk collision. Row 38 confirmed blocked across columns 26-29.
- **Cottage East Perimeter Audit (Verified Turns 10614-10625)**: Column 42 tested across rows 21, 22, and 24: solid pine trees and trunks. Confirmed zero passage exists east from the Cottage area into the Eastern Meadow. The Cottage area is an isolated landing south of the row 20 one-way ledge, connecting exclusively south via the Sand Highway.
- **Column 26 Collision Test (Verified Turn 10646)**: Stepping Up from (26, 39) into (26, 38) resulted in solid collision with a pine tree trunk.
- **Hypothesis 11 (Route 1 Northbound Connection Survey)**:
  - **Proposition**: Progression back to Sovio City requires identifying the verified northbound passage out of the southern Route 1 loop.
  - **Candidate Avenues**:
    1. Avenue A: Signboard 2 sector (columns 18-21, rows 40-44) to audit whether the corridor toward Youngster Mike (29, 20) branches north from the southern path.
    2. Avenue B: Western boundary of the Sand Highway (columns 34-35, rows 27-36) to audit for an unverified westward opening.