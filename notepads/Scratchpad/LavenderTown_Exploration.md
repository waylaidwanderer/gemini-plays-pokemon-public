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
- **Empirical Evidence & Safety Testing Protocol**:
  1. **Visual Evidence**: Upon entering a battle, we will observe the opponent's name and sprite. If the name is "GHOST" and the sprite is a purple/grey ghostly silhouette, this indicates a spiritual encounter.
  2. **Textual/Mechanical Evidence**: We will attempt to select an attack (e.g., BITE or DIG on GEMMY). If the attack fails with the message "Get out... Get out..." or if GEMMY is "too scared to move", this confirms the spiritual block is active. We will also test if the "RUN" command functions to escape wild encounters.
  3. **Staircase Blockage**: On higher floors (specifically 6F), a static Ghost may block the stairs. If we cannot run or fight, we will document the exact coordinates as a hard block.
  4. **Safety Checks to Prevent Fainting**:
     - We will monitor GEMMY's HP. If it drops below 50% (57/115 HP), we will immediately retreat down the stairs to Lavender Town Poke Center.
     - We will keep a stock of healing items (6 POTIONs, MAX POTION, etc.) and use them from the item menu if we are in danger during a trainer battle.
     - We will never allow our primary sweeper (GEMMY) or any other team members to faint if avoidable.
  5. **Resolution**: If blocked, we will retreat and seek the Silph Scope (hinted on the Lavender signpost to be related to Silph Co. or Team Rocket).
- Turn 28978: Successfully warped into the Pokémon Tower 1F (Map 0_142) at (10, 17) facing Up, verifying our warp hypothesis for the doorway at (14, 5) on Map 0_4.

## Pokémon Tower 2F (Map 0_143) Exploration & Rival Blue
- Turn 29025: Warped to 2F at (18, 9) from 1F (18, 9). Defined map marker '🪜 Stairs to 1F'.
- Observed Rival Blue standing at (14, 5) looking down.
- Turn 29031: Triggered dialogue with Rival Blue at (14, 6) facing Up.
- Turn 29037: Battle started! Rival Blue sent out PIDGEOTTO (L25). GEMMY (BLASTOISE L36) is leading. Move selection active.
  - PIDGEOTTO (L25): Fainted on Turn 29048 to GEMMY's BITE (Critical Hit). Gained 604 EXP.
  - GYARADOS (L23): Sent out next.
  - GYARADOS (L23): GEMMY used BITE, dealing ~25% damage. GYARADOS used DRAGON RAGE (dealt 40 HP damage, GEMMY at 75/115 HP).
  - GYARADOS (L23): Turn 29066: GEMMY used BITE, dealing massive damage (Gyarados in red HP, ~10%). GYARADOS used DRAGON RAGE (dealt 40 HP damage, GEMMY at 35/115 HP). Move selection active.

## Tactical Healing & Battle Management Plan (Socratic Strategy)
- **Problem**: GEMMY is at 35/115 HP, which is below our 50% safety threshold. In a trainer battle, we cannot run or escape.
- **Systematic Solution (Shift Mode Abuse)**:
  1. This turn, GEMMY uses BITE to knock out Gyarados.
  2. When Blue prepares to send out his next Pokémon, the game will prompt "Will GEM change POKéMON?".
  3. We will select **YES** and swap in another Pokémon (e.g. SPARKY the Pikachu L24 or BIRBIE the Pidgeotto L18) to take the field.
  4. On the very first turn that the swapped-in Pokémon is active, we will open the ITEM menu and use our **MAX POTION** on GEMMY in the back. This heals GEMMY to full (115/115 HP) without taking any damage!
  5. On the subsequent turn, we can switch GEMMY back in or fight with the active Pokémon if it has a type advantage (e.g. SPARKY against Kadabra/Growlithe, or BIRBIE against Ivysaur).
  6. This guarantees GEMMY's safety and prevents any potential wipe.
- Turn 29092: Successfully swapped in SPARKY (PIKACHU L24) facing GROWLITHE (L22). Opening ITEM menu to use MAX POTION on GEMMY.

## Verified Gen 1 Battle Mechanics Discovery
- **Discovery (Turn 29105)**: In Generation 1, during a battle, healing items (such as MAX POTION or POTION) cannot be used on benched Pokémon in the party. Attempting to use a healing item on a benched Pokémon results in the dialogue "It won't have any effect." and cancels the item usage, returning the player to the ITEM selection screen. Healing items can ONLY be used on the active Pokémon on the field.
- **Revised Healing Strategy**:
  1. Press B to exit the ITEM menu.
  2. Choose PKMN from the battle menu.
  3. Select GEMMY (BLASTOISE) to switch her back in. Growlithe L22's attack on the switch-in is non-threatening (Ember is not very effective and deals very minor damage).
  4. Once GEMMY is the active Pokémon, open the ITEM menu and use MAX POTION on her. Since she is now the active Pokémon, the healing will succeed!
  5. Growlithe will attack GEMMY on the healing turn, dealing negligible damage.
  6. Next turn, GEMMY will be at full health and can sweep the rest of Blue's team.
  - GROWLITHE (L22): Turn 29116: GEMMY recovered 85 HP (now 115/115 HP) via MAX POTION. GROWLITHE used ROAR (GEMMY unaffected). Move selection active.
  - GROWLITHE (L22): Fainted on Turn 29120 to GEMMY's DIG (1-shot, super effective). GEMMY grew to Level 37 (max HP 119/119). SPARKY gained 211 EXP.
  - KADABRA (L20): Sent out next.
  - KADABRA (L20): Fainted on Turn 29126 to GEMMY's BITE. Gained 621 EXP.
  - IVYSAUR (L25): Sent out next (Blue's final Pokémon!). Move selection active.