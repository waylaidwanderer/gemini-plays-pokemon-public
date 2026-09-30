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
## Hypothesis 8 (Investigation of Western Sector Columns 5-9 for Northbound Route)
- **Proposition**: The northern half of Route 1 (leading to Northwest Clearing, Duke, and Sovio City) connects via the western sector (columns 5-9) rather than the central meadow or Cottage basin.
- **Rationale**:
  1. The Cottage sector was empirically confirmed to be an enclosed basin; the row 20 ledge is strictly a one-way southward drop.
  2. Columns 10-18 were previously tested and verified blocked north by hedges/trees.
  3. Columns 5-9 at row 44-48 remain largely unprobed northward, except for a recorded Cut tree at (5, 44).
  4. In the early game (Turns 458-1165), Asher successfully walked from Lancio Town to Sovio City before possessing HM Cut, proving a passable route exists that does not require Cut.
- **Protocol**:
  1. Traverse west along row 44 from (24, 44) to the Central Pine Tree at (11, 44).
  2. Bypass Central Pine Tree south via row 48 to reach column 9.
  3. Systematically probe northward progression across columns 5-9 between rows 44 and 40.
- **Falsification Criteria**:
  - If columns 5-9 are completely enclosed northward by impassable collision (trees, fences, ledges, or mandatory Cut obstacles) with zero passable corridors leading north into the Northwest Clearing.

- **Status**: FALSIFIED (Turns 10388-10396). Empirical tests confirmed: (9, 44) is blocked by a pine tree trunk (Turn 10388); (5, 44) is solid collision and inert to 'A' (Turns 10394-10395); (7, 44) is blocked by a pine tree trunk (Turn 10395). Rows 40-42 form an unbroken wall of dense pine trees across columns 5-10. Zero northward exits exist in the western sector.

## Hypothesis 9 (Investigation of West Flank of Sand Highway / Central Meadow for Corridor to Northwest Clearing)
- **Proposition**: The connection to the northern half of Route 1 (Northwest Clearing: Youngster Mike at 29, 20 and Lass Sonia at 27, 15) branches off westward from the Sand Highway (columns 33-35, rows 26-36) or through the central meadow (columns 28-32, rows 38-40).
- **Rationale**:
  1. The western sector (columns 5-18) is completely blocked northward by rows 40-42 (Hypothesis 8 falsified).
  2. The Cottage basin is an enclosed dead-end to the north with the row 20 ledge strictly a one-way southward drop.
  3. The Sand Highway spans rows 26-38 at columns 34-37, running parallel to the Northwest Clearing (columns 27-29, rows 15-25), with rows 26-36 westward unprobed.
  4. The early game route from Lancio Town to Sovio City passed through the bird tracks into the meadow, defeated Mike and Sonia, and continued east to Duke and Sovio City.
- **Protocol**:
  1. Return east along row 44 to the hedge gap at (26, 43).
  2. Ascend into the central meadow to (29, 40) / (32, 39).
  3. Systematically probe westward progression from the Sand Highway at rows 28-36 to locate the open corridor into the Northwest Clearing.
- **Falsification Criteria**:
  - If the entire western flank of the Sand Highway from row 26 to row 38 is completely sealed by impassable collision (trees/fences) with zero westward openings leading into the Northwest Clearing.
