# Lavender Town Active Exploration & Mapping Log

## Socratic Mapping Protocol
To systematically discover, identify, and map Lavender Town's structures without blind movement:
1. **Perimeter and Grid Sweeping**:
   - We will systematically explore the town grid row-by-row and column-by-column starting from our entry point at (8, 0).
   - Any door or entrance we encounter will be treated as an unverified warp hypothesis.
2. **Identification Protocol**:
   - When we stand adjacent to a building door, we will document its external coordinates.
   - We will enter the building (warp) and record the internal Map ID.
   - We will speak to the NPCs inside to identify the building's function:
     - "Welcome to our POKéMON CENTER!" -> Pokémon Center.
     - "Welcome! May I help you?" -> Poké Mart.
     - Gravestones / channeled ghosts / channelers -> Pokémon Tower.
     - Mr. Fuji's associates / letters / orphans -> Volunteer House.
   - We will then exit and immediately place a highly descriptive map marker on the door (e.g. Poke Center, Poke Mart, Pokemon Tower, residential/houses).
3. **Pristine Record Integrity**:
   - All discoveries will be recorded in this scratchpad first with Turn numbers and Coordinates.
   - Once the town is fully mapped and verified, we will use `lavender_database_agent` to compress and migrate the final verified records to `Locations/LavenderTown`, keeping this scratchpad for active notes.

## Live Exploration Logs
- Turn 28826: Entered Lavender Town at (8, 0) from Route 10 South.
- Turn 28846: Entered Pokémon Center door at (3, 5) on Map 0_4 (Lavender Town), warped to (3, 7) on Map 0_141.
- Turn 28849: Healed full party at the left counter tile (3, 3) facing Up.
- Turn 28860: Entered Volunteer House (Map 0_149). Currently at (2, 7).
- Turn 28867: Standing at (4, 5). Spoke to NPC at (3, 5) who said "That's odd, MR.FUJI isn't here. Where'd he go?" Confirmed this is the Pokémon Volunteer House (Map 0_149).
- Turn 28875: Spoke to girl at (6, 3) who says "This is really MR.FUJI's house."
- Turn 28877: Spoke to Psyduck at (6, 4) who says "Gwappa!"
- Turn 28885: Spoke to Nidorino at (1, 3) who says "NIDORINO: Gaoo!"
- Turn 28887: Completed speaking to all NPCs in Map 0_149. Exited through the door at (2, 7).
- Turn 28902: Spoke to NPC at (5, 3) inside Map 0_229. Confirmed this is the Name Rater's House (Map 0_229).
- Turn 28917: Moving Up from Route 12 (Map 0_23) placed us back on Map 0_4 (Lavender Town) at (8, 17) facing Up.
- Verification: The transition between Map 0_4 (Lavender Town) and Map 0_23 (Route 12) occurs at the boundary between Row 17 on Map 0_4 and Row 0 on Map 0_23. Map 0_23 (Route 12) is connected directly to the south of Lavender Town.
- Turn 28921: Moving East, spotted the Poké Mart with door at (15, 13) on Map 0_4. Entered and cataloged complete inventory.
- Turn 28978: Successfully warped into the Pokémon Tower 1F (Map 0_142) at (10, 17) facing Up, verifying our warp hypothesis for the doorway at (14, 5) on Map 0_4.

## Pokémon Tower 1F (Map 0_142) Exploration & NPC Protocol
- **Objective**: Systematically scan 1F for the stairs leading to 2F while avoiding backtracking and documenting the layout.
- **Methodology (Grid Scan)**:
  - We will trace the floor's navigable paths using the coordinate grid, marking wall tile IDs (TYPE_2889 representing graves or structural walls) and floor tile IDs (TYPE_3fe2 representing passable tiles).
  - The stairs to 2F are traditionally located in the north-eastern region. We will head east/north-east.
- **NPC Interaction Protocol (Burden of Proof)**:
  - If we spot an NPC, we will stand adjacent, record their coordinates, and interact by pressing 'A'.
  - *Hypothesis*: All NPCs on 1F are peaceful mourners and will not trigger combat.
  - *Safety Check*: If an NPC unexpectedly triggers a battle, we will document them as hostile and update our regional database. Otherwise, we will record their full dialogue in the NPC Directory of `Locations/LavenderTown`.

## Pokémon Tower Spiritual Passability Protocol
- **Hypothesis**: The Pokémon Tower can be navigated safely up to a point, but higher floors or specific paths may be hard-blocked by unidentified spiritual entities ("Ghosts") that require the Silph Scope to bypass.
- **Empirical Evidence & Safety Testing**:
  1. We will enter the Pokémon Tower (verify Map ID upon entry).
  2. We will observe overworld sprites. If a battle is triggered by a static sprite, we will test if standard actions are possible.
  3. In wild encounters, if the battle screen shows "GHOST" and our standard attack moves fail/are blocked with "Get out..." text, this constitutes empirical proof of a spiritual block.
  4. If we encounter a hard block (such as on 6F stairs where the ghost cannot be fought or run from without Silph Scope), we will document the exact coordinates as impassable and immediately retreat.
  5. We will not attempt to grind or force battles in the tower if the "GHOST" block is active, to avoid wasting resources.
- Turn 28978: Successfully warped into the Pokémon Tower 1F (Map 0_142) at (10, 17) facing Up, verifying our warp hypothesis for the doorway at (14, 5) on Map 0_4.