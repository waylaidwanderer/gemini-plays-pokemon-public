# Game Knowledge

## Game Mechanics
### General Mechanics
- Talking to Mom does NOT heal my Pokémon. This is a critical mechanic difference from other games.
- Resting in the player's bed does NOT heal Pokémon.
- Stunning an NPC can break scripted events, causing dialogue loops. It can also be a reliable solution for interacting with moving NPCs.
- The `stun_npc` effect is temporary and resets when changing maps. (Verified in Azalea Pokémon Center)
- Repeatedly interacting with an object (like a sign) without new results can lead to loops. I must dismiss dialogue before attempting to move.
- The 'Select' button on the nicknaming screen toggles between uppercase and lowercase keyboards.
- An item in a Poké Ball on the ground must be interacted with from an adjacent tile, not by walking onto it.

### Tile Traversal and Movement Rules
- **BOOKSHELF**: Impassable. (Verified)
- **BUOY**: Traversability unknown, assumed impassable. Might require Surf. (Observed on Route 32)
- **CAVE**: Traversable warp.
- **COUNTER**: Impassable. (Verified by observation)
- **CUT_TREE**: Impassable, requires a specific ability/item to remove. (Verified)
- **DOOR**: Traversable, acts as a warp tile. (Verified)
- **FLOOR**: Traversable. (Verified on multiple routes, including Route 36)
- **FLOOR_UP_WALL**: A complex one-way tile with location-dependent behavior.
  - **(Union Cave 1F):** A complex one-way tile. You can move UP from a FLOOR tile *onto* a FLOOR_UP_WALL tile (Verified at (3, 18)), but you cannot move DOWN *onto* it (Verified at (6, 18)) or UP *from* it (Verified at (5, 18)).
  - **(Union Cave B1F):** A complex one-way tile. You can move UP from a FLOOR_UP_WALL tile to a FLOOR tile. You cannot move DOWN from a FLOOR tile onto a FLOOR_UP_WALL tile (Verified at (12, 24), (7, 24), and re-verified at (5, 24) on turn 19885). However, you CAN move DOWN from a FLOOR_UP_WALL tile onto a LADDER tile (Verified at (7, 19)).
  - **(Route 32 & Dark Cave Violet Entrance):** Impassable from above. You cannot move DOWN from a FLOOR tile onto a FLOOR_UP_WALL tile. (Verified by manual test on Route 32 at (7, 75) and by pathing failure in Dark Cave at (2, 16)).
- **HEADBUTT_TREE**: Impassable. (Verified by observation)
- **INCENSE_BURNER**: Impassable. (Verified by observation in Kurt's House)
- **LADDER**: A complex warp with directional activation. To descend from 1F to B1F, I moved onto the ladder at (5, 19). To ascend from B1F to 1F, I moved DOWN from (7, 18) onto the ladder at (7, 19). Simple interaction (pressing A or a direction while standing on it) does not work. (Verified)
- **LEDGE_HOP_DOWN/LEFT/RIGHT**: One-way traversal.
- **LONG_GRASS**: Traversable, contains wild Pokémon. (Verified by encounters on Route 30)
- **MART_SHELF**: Impassable. (Verified by pathfinder consistently treating it as a wall)
- **PC**: Impassable. Interacting from an adjacent tile can trigger events. (Verified)
- **PILLAR**: Conditionally passable. Becomes impassable after a short time. Interaction with a specific Sage at (12, 3) makes it passable. (Verified)
- **RADIO**: Impassable. (Verified by attempting to walk on it)
- **STAIRCASE**: Traversable, acts as a warp tile. (Verified)
- **TALL_GRASS**: Traversable, contains wild Pokémon. (Verified)
- **TOWN_MAP**: Impassable. (Verified by observation)
- **TV**: Impassable. (Verified)
- **UNKNOWN**: Traversable. Verified at (28, 32) and (8, 26) in Ilex Forest.
- **VOID**: Impassable. (Verified by attempting to walk into it from (9, 4) on Route31VioletGate on Turn 19292).
- **WALL**: Impassable. (Verified)
- **WARP_CARPET_DOWN**: Traversable warp. Requires pressing 'Down' on the tile to activate. (Verified)
- **WARP_CARPET_LEFT**: Traversable warp. Requires pressing 'Left' while standing on the tile to activate. (Verified at 2,10 in Azalea Town, 0,4 in IlexForestAzaleaGate, and 0,4 on Route32RuinsOfAlphGate)
- **WARP_CARPET_RIGHT**: Traversable warp. Requires pressing 'Right' on the tile to activate. (Verified at 3,42 in Ilex Forest)
- **WATER**: Impassable. (Verified by pathing attempts)
- **WINDOW**: Impassable. (Verified)

### HM Usage Mechanics (CRITICAL DISCOVERY)
- HMs are not taught to Pokémon from the bag or menu like TMs. Instead, to use an HM move outside of battle, you must interact directly with the corresponding overworld obstacle (e.g., press 'A' on a CUT_TREE). The game will then prompt you to use the move if a compatible Pokémon is in your party. (Verified with HM01 Cut in Ilex Forest).

## World & Story
### Location Notes
#### Route 29
- The southern path is a dead end.
- The western path is blocked by CUT_TREEs and HEADBUTT_TREEs.

#### Route 30
- MR. POKEMON's house is located here. (Confirmed)

#### Route 32
- The central path on Route 32, accessed via a one-way ledge from the west, appears to be a dead end going south due to a line of `FLOOR_UP_WALL` tiles. However, there is a one-tile-wide gap at (14, 34) that allows passage south, so it is not a dead end.
- Hidden SUPER POTION at (11, 40).

#### Violet City
- Building at (21, 29) is a house with a trade NPC, not the Gym.
- The eastern and western sides of Cherrygrove City are connected by a walkable path that goes around the central body of water.
- YOUNGSTER at (5, 18) mentioned a 'wiggly tree' that 'squirms and dances'. This is likely a hint about how to interact with HEADBUTT_TREEs.
- Violet City Gatehouse Warp: Currently impassable and a dead end for now.

##### Sprout Tower
- 1F Path: A solid wall at x=4 divides the first floor, making the Sage at (3, 5) unreachable from the east. Defeating other Sages does not alter the layout.

#### Route 33
- Hiker Anthony is on this route. He gives his phone number instead of battling.

#### Azalea Town
- Hiker Anthony called to say there are lots of DUNSPARCE in DARK CAVE.

#### Dark Cave (Violet Entrance)
- **Discovery:** This entrance is a confirmed dead end. Even with Flash, the area is a small, isolated section completely blocked off by one-way ledges and walls, making further exploration impossible from this side.

## Pokémon & Battle Info
### Battle Mechanics
*Ignis learned EMBER at Lv12.*
*Ignis grew to Lv21 and learned QUICK ATTACK, replacing SMOKESCREEN.*
*Type Effectiveness Chart*:
- Ground is super-effective against Fire. (Verified in battle vs Falkner's Pidgey's MUD-SLAP).
- Normal is not very effective against Rock/Ground. (Verified in battle vs Hiker Daniel's Onix).
- Psychic is not very effective against Bug. (Verified vs Caterpie)
- Fire is super-effective against Bug/Grass. (Verified vs Paras)
- Bug is super-effective against Psychic. (Verified in battle vs Zubat's Leech Life on Glyph).

*Pokémon Types Discovered*:
- SANDSHREW: Ground
- WEEDLE: Bug/Poison

### PC Storage
- Currently empty.

## TMs & HMs
### TM31 MUD-SLAP
- **Description:** Reduces the foe's accuracy.
- **Compatible Party Pokémon:** Ignis (Quilava), Aether (Pidgey), O (Togepi).
- **Incompatible Party Pokémon:** Glyph (Unown).
### HM05 FLASH
- **Description:** Blinds the foe to reduce accuracy. Lights up dark caves.
- **Compatible Party Pokémon:** O (Togepi).
- **Incompatible Party Pokémon:** Ignis (Quilava), Glyph (Unown), Aether (Pidgey).
### HM01 Cut
- **Description:** A move that can cut down small trees.
- **Compatible Party Pokémon:** [Untested]
- **Incompatible Party Pokémon:** [Untested]

## Available Tools & Agents
### Built-in Tools
- `notepad_edit`: Edits the persistent notepad.
- `run_code`: Executes a single-use Python script.
- `define_agent`: Creates or updates a custom agent.
- `delete_agent`: Deletes a custom agent.
- `define_map_marker`: Creates or updates a map marker.
- `delete_map_marker`: Deletes a map marker.
- `stun_npc`: Temporarily freezes or unfreezes an NPC.
- `define_tool`: Creates or updates a reusable custom tool.
- `delete_tool`: Deletes a custom tool.
- `select_battle_option`: Automatically selects a main battle menu option.

### Custom Tools & Agents
- `deterministic_battle_strategist`: A deterministic, non-LLM tool for battle advice.
- `find_adjacent_traversable_tiles`: Finds traversable tiles next to a target.
- `find_reachable_unseen_tiles`: Finds unseen tiles that are confirmed to be reachable.
- `path_and_execute`: Generates and executes a path to a target coordinate.
- `notepad_refactor_assistant`: Agent to help refactor the notepad.
- `debugging_assistant`: Agent that analyzes and corrects faulty Python scripts.
- `puzzle_solver_strategist`: Agent that suggests the next hypothesis for a puzzle.

## Untested Mechanics & Hypotheses
- Test the damage of EMBER vs. QUICK ATTACK on a Water-type.
- Test `HEADBUTT_TREE`s by interacting with them with different Pokémon in the lead to see if any move can be used.
- Rigorously test all one-way tiles (e.g., LEDGE_HOP_DOWN/LEFT/RIGHT, FLOOR_UP_WALL on Union Cave 1F) by attempting to move in all four directions from them to definitively confirm their movement restrictions.
- Test TALL_GRASS on Route 36.
- Test `WARP_CARPET_LEFT` again to determine consistent activation method.
- Test `FLOOR_UP_WALL` on Union Cave B1F by attempting to move in all four directions to confirm its one-way warp mechanic.
- Test `LEDGE_HOP_LEFT` and `LEDGE_HOP_DOWN` tiles on Route 33 by attempting to move against their intended direction to confirm one-way traversal.
- Test lateral (left/right) movement from and onto `FLOOR_UP_WALL` tiles to fully understand their mechanics.
- Rigorously test all `LEDGE_HOP` tiles in Ilex Forest by attempting to move in all four directions to confirm their movement restrictions.

# Investigations

## Active Investigations

### Route 36 'Odd Tree' Puzzle
- **Objective:** Get past the tree blocking the path at (35, 9).
- **Observations:**
  - The tree is a unique 'WEIRD_TREE' sprite that wiggles.
  - Lass Dana's dialogue at (49, 8) confirms this tree blocks the way to Goldenrod City.
  - A Fisher at (44, 9) mentioned he couldn't break it with a punch.
  - A Youngster in Violet City mentioned a 'wiggly tree' that 'squirms and dances'.

#### Solution Discovery Log
- **Hypothesis 1:** Interacting with the tree by pressing 'A' will trigger an event.
  - **Test 1:** Stood at (36, 9), faced the tree, and pressed 'A' with Ignis (Quilava) in the lead.
  - **Result:** No text appeared, no event triggered. Interaction failed.
  - **Conclusion:** A simple 'A' press with Quilava as the lead Pokémon is not the solution.

- **Hypothesis 2:** The lead Pokémon affects the interaction with the tree.
  - **Test 1 (Ignis):** Stood at (36, 9), faced the tree, and pressed 'A'. Result: No text appeared, no event triggered. Interaction failed.
  - **Test 2 (Aether):** Stood at (36, 9), faced the tree, and pressed 'A'. Result: No text appeared, no event triggered. Interaction failed.
  - **Test 3 (O):** Stood at (36, 9), faced the tree, and pressed 'A'. Result: No text appeared, no event triggered. Interaction failed.
  - **Test 4 (Glyph):** Stood at (36, 9), faced the tree, and pressed 'A'. Result: No text appeared, no event triggered. Interaction failed.
  - **Conclusion:** Hypothesis 2 is disproven. The lead Pokémon has no effect on a simple 'A' press interaction with the tree.

- Re-verification (Turn 10826): Stood at (36, 9), faced the tree at (35, 9), and pressed 'A'.
  - **Result:** No text appeared, no event triggered. This re-confirms that a simple 'A' press is not the solution. I have exhausted all simple interaction hypotheses.
  - **Conclusion:** The 'Odd Tree' is almost certainly a story-based roadblock that requires an item or event from elsewhere. I am pivoting to explore the rest of Route 36.

#### Untested Assumptions
- The tree is a story-based roadblock that will be removed after an event elsewhere, not a solvable puzzle at this time.
- The solution requires a specific key item from my pack (e.g., Squirtbottle).
- The interaction is dependent on the time of day.
- The solution involves using the Pokégear radio near the tree.
- The tree must be interacted with from the tile directly below it (35, 10). (Status: Untestable as of Turn 17023. Path confirmed to be blocked by `generate_path_plan` tool.)

### Ilex Forest FARFETCH'D Puzzle
- **Objective:** Get the FARFETCH'D to the apprentice at (7, 28).
- **Discovery Log:**
  - **Successful Step:** Interacted with FARFETCH'D at (10, 35) from above (10, 34), causing it to move to (15, 29).
  - **Failed Step:** Interacted with FARFETCH'D at (15, 29) from below (15, 30), causing it to reset to its starting position at (15, 25).
  - **Failed Step:** Interacted with FARFETCH'D at (20, 24) from the right (21, 24), causing it to reset to its starting position at (15, 25).
  - **Past Failure Note (Turns 13600-13606):** Pursued an invalid test plan based on the hallucination that the bird was at its starting position of (15, 25), misinterpreting an object-linked map marker. This led to wasted turns on a flawed premise.
  - **Successful Step:** Interacted with FARFETCH'D at (15, 25) from below (15, 26), causing it to move to (20, 24).
  - **Successful Step (Part 2):** Interacted with FARFETCH'D at (20, 24) from above (20, 23), causing it to move south and off-screen.
  - **Current State:** The FARFETCH'D is now in an unknown location, presumably in the southern part of this maze.
  - **Hypothesis 3:** Walking around the southern clearing will trigger the FARFETCH'D's appearance.
    - **Test:** Walked a loop from (28, 29) -> (29, 29) -> (29, 30) -> (28, 30) -> (28, 29).
    - **Result:** No event triggered.
    - **Conclusion:** Hypothesis 3 is disproven. Simple movement in the southern clearing is not the solution.
  - **Next Step:** Return to the previously identified functional twig pile at (16, 28) and step on it, as this is a known puzzle interaction mechanic.

### Dark Cave Exploration
- **Objective:** Fully explore Dark Cave to find an alternative route to Goldenrod City.
- **Background:** The 'Odd Tree' on Route 36 is an impassable story-block. My current strategic pivot is to fully explore Dark Cave, as Hiker Anthony's repeated calls suggest its importance.
- **Hypothesis:** Dark Cave contains a path that bypasses the 'Odd Tree' and leads towards Goldenrod City.
- **Exploration Plan:**
  1. Enter Dark Cave from the most promising entrance (likely through Union Cave, as the Route 31 entrance was a dead end).
  2. Systematically explore every path, prioritizing unseen tiles.
  3. Use Flash if necessary and available to illuminate dark areas.
  4. Document any branching paths, obstacles (like water or boulders), and potential HM requirements.
  5. If a path leads to a new exit, mark the location and explore the new area.

# Appendix: Detailed Failure & Reflection Log

### Specific Failure Incidents & Process Violations
- **CRITICAL PROCESS FAILURE (Recent Turns):** Repeatedly deferred critical actions like notepad updates and agent fixes, violating the 'IMMEDIATE ACTION' and 'TOOL MAINTENANCE' core principles. This resulted in operating with flawed data and plans.
- **RECURRING DEBUGGING FAILURE (Turns 10750-10774):** I have been stuck in a loop toggling the coordinate system logic in my `find_path_to_target_bfs` tool. The evidence from the player's position in the XML (`<Row id="12">`, `<Tile id="2">` for position (2, 12)) definitively proves that the XML `id` attributes are 1-indexed and correspond directly to game coordinates. My repeated re-introduction of `+ 1` to the parsing logic was a critical, recurring hallucination.
- **CRITICAL PROCESS FAILURE (Turn 13142):** Deferred a mandatory notepad update to fix an incomplete tool list by one turn in order to continue a battle. This is a violation of the 'IMMEDIATE ACTION' principle for data management.
- **CRITICAL REASONING FAILURE (Turn 14554):** My `generate_path_plan` tool correctly reported that no path existed to the Ilex Forest Shrine from my position at (8, 26). Instead of trusting the tool's output and analyzing the map, I incorrectly assumed the tool was broken. A manual review confirmed my path was blocked by impassable tiles. This is a major failure to trust my own tools and a repeat of past mistakes.
- **CRITICAL HALLUCINATION (Turn 15350):** Believed I was at (14, 0) on Route 32 and attempted to move 'Up' to enter Violet City. In reality, I was at (6, 80) and my 'Up' press moved me to the cave entrance at (6, 79), warping me back into Union Cave. This is a severe failure of state tracking and location awareness.
- **PROCESS VIOLATION (Turn 15018):** Failed to consult map marker for Fisher at (15, 27) in Union Cave before pathing, causing a movement blockage. This highlights a need for greater diligence in pre-planning.

### Reflection-Based Updates (Turn 11695)
- **CRITICAL REASONING FAILURE (Turns 11683-11690):** I became stuck in a multi-turn loop attempting to fix the `generate_path_plan` tool. I repeatedly submitted identical, broken code, failing to notice that I had not actually removed the incorrect line from the `impassable_types` set. This was a severe failure of process and attention to detail.
- **CRITICAL REASONING FAILURE (Turns 11717-11720):** After multiple failed attempts to fix my pathfinder's one-way ledge logic, I finally implemented aversion that seemed simpler and more correct. However, it was a fundamentally backward and based on a complete misunderstanding of the mechanic. The game immediately blocked my movement, proving the new code was broken. My logic from turn 11694 was actually correct, and my 'fix' was a regression that wasted several turns. This is a major failure in debugging and logical reasoning.

# Reflection Log (Turn 11852)
- **CRITICAL HALLUCINATION (Turn 11872):** Believed a warp to Union Cave existed at (11, 9) on the AzaleaTown map (8_7). The system confirmed no warp exists there. The actual warp to Union Cave is on Route 33 (8_6) at (11, 9). This was a major failure in location awareness.
- **CRITICAL HALLUCINATION (Turn 11928):** Believed a warp to Dark Cave existed at (34, 5) on the VioletCity map (10_5). The system confirmed no warp exists there. This was a major failure in location awareness.

### Reflection-Based Updates (Turn 20113)
- **CRITICAL PROCESS FAILURE (Turns 20059-20071):** I have been stuck in a multi-turn debugging loop with the `path_and_execute` tool due to a critical failure to trust my `debugging_assistant` agent. The agent correctly identified the necessary fix (a hierarchical `if/elif` structure) on turn 20056, but I incorrectly reverted this fix on turn 20059 based on a flawed manual analysis. This mistrust, as highlighted by the system critique on turn 20071, was the root cause of the prolonged failure and is a major process violation.