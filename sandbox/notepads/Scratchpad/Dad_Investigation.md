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
- **Hypothesis 8 (Western Sector Columns 5-9 Northbound Route)**: Falsified Turns 10388-10396. (5, 44), (7, 44), and (9, 44) are solid tree obstacles; rows 42-44 form an unbroken tree wall across columns 5-10 with zero northward exits.

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
## Hypothesis 9 (Investigation of Unexplored Route 1 Boundaries for Northbound Passage)
- **Proposition**: The passable route to Sovio City (53, 0) connects via an unexplored boundary on Route 1, either:
  (a) An unverified opening from the Central Meadow / bird tracks trail (columns 27-32, rows 38-40),
  (b) Unchecked western corridors from the Sand Highway between rows 30-36 (below row 28 which was blocked at x=32), or
  (c) Traversal extending east along row 44 past column 26.
- **Rationale**:
  1. The Cottage sector is an enclosed dead-end basin with the row 20 ledge strictly a one-way southward drop.
  2. The western sector (columns 5-18) is completely blocked northward by unbroken trees at rows 42-44 (Hypothesis 8 falsified).
  3. Sovio City is located at (53, 0), and Bug Catcher Duke is at (45, 12).
- **Protocol**:
  1. Return to the overworld at (31, 40).
  2. Probe row 38 across columns 28-32 in the Central Meadow to verify if an opening exists.
  3. If Central Meadow is completely enclosed north, probe row 44 east of column 26.
- **Falsification Criteria**:
  - Prop (a) Falsification: If row 38 across columns 28-32 is completely solid trees.
  - Prop (b) Falsification: If Sand Highway west flank rows 30-36 are solid trees.
  - Prop (c) Falsification: If row 44 east of column 26 terminates in solid obstacles.
