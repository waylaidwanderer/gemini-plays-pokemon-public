## I. Core Protocols & Game Philosophy
- **Immediate Data Management:** I will use `define_map_marker` and `notepad_edit` on the *same turn* a discovery is made. Deferring tasks is a critical failure.
- **Agent & Tool Protocol:** Agent and tool refinement is an IMMEDIATE action. If a tool is faulty or a better one can be conceived, I MUST define/redefine it on the IMMEDIATE next turn.
- **Hypothesis-Driven Gameplay:** I will rigorously document my hypotheses, tests, and conclusions in my notepad. I will avoid repeating failed strategies and will pivot to new goals if progress stalls after multiple documented attempts.

## II. Tool Development Log
- **pathfinder:** REFINED (T52445). Added logic to handle impassable destination tiles by pathing to the nearest walkable adjacent tile. REFINED AGAIN (T52447) to correctly recognize 'closed_gate' tiles as impassable. REFINED A THIRD TIME (T52480) to remove dependency on `xml.et` module.

## III. Game Mechanics & Battle Intel
### A. Tile Mechanics & Traversal Rules
- **Ledges:** Ledges are one-way only. They can be jumped down (from Y-1 to Y+2 in one move), but are impassable from below (Y+1) and from the sides (X-1, X+1).
- **Water Tiles (Silph Co.):** The water tiles on the first floor of Silph Co. are purely cosmetic and function as `impassable` walls. They cannot be surfed on.
- **Spinner Tiles:** Spinner tiles force movement in a specific direction. I need to map out their destinations to navigate spinner mazes effectively.
- **Hole Tiles:** Acts as a one-way warp, dropping the player to the floor below. Untested if they can be bypassed (e.g., with Surf).
- **Gates:** `closed_gate` tiles are impassable. Some are opened by switches, while others (like in Silph Co.) require the CARD KEY.
- **Elevators (Silph Co.):** To use the elevator, you must first interact with the control panel (usually on a wall) to select a destination floor. After selecting a floor, you must walk onto the warp tiles at the back of the elevator room to trigger the map transition.
- **Saffron Gym Teleporters:** These are 1x1 warp tiles. To use a warp, I must move onto the tile. If I'm already on a warp tile, I must move off and then back on to trigger it. This is crucial for testing bidirectionality.
- **Open Gates:** `open_gate` tiles are unlocked `closed_gate` tiles and function as `ground`.
- **2x1 Warps (Cinnabar Lab):** To use these horizontal floor warps, you must stand on one of the two tiles and press into the impassable boundary (e.g., Down).

### B. Confirmed ROM Hack Changes
#### B1. Type Matchups & Immunities
- **Super Effective:** Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; **Psychic > Flying** (confirmed: KADABRA's PSYBEAM vs ECHO's GOLBAT)
- **Not Very Effective:** Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); **Ice !> Gyarados (Water/Flying)** (confirmed: NEPTUNE's AURORA BEAM vs Fisherman's GYARADOS).
- **Immunities:** Flying-type immune to Ground-type moves; MUK immune to Poison-type moves; **Electric is effective vs Sabrina's Psychic team, confirming Psychic types are NOT immune to Electric.**; **HYPNO immune to STUN SPORE** (powder moves).

#### B2. Battle & Field Mechanics
- **Evasion:** PSYWAVE and CONFUSE RAY can fail against targets with high evasion boosts (e.g., from MINIMIZE).
- **Struggle:** A Pokémon with 0 PP for all moves will use Struggle, which has low accuracy and causes recoil damage.
- **Multi-Hit Moves:** Moves like FURY ATTACK are a critical threat, bypassing "sturdy" effects.
- **'No Will to Fight':** A fainted or sleeping Pokémon cannot be switched into battle.
- **HM Usage:** Flash, Cut, and Fly MUST be taught to a Pokémon to be used in the field.
- **EXP Distribution:** Experience is shared between the Pokémon that started the battle and any that participated via switch-in.
- **PC Box Full:** When a Pokémon is caught and the active PC box is full, the caught Pokémon is still sent to the PC, but the active box must be changed manually later.
- **Safari Zone:** Has a time limit. When it expires, the player is warped back to the Safari Zone Gate.
- **Gym Battle Loss:** Losing a battle inside a gym does NOT warp you to a Pokémon Center. You respawn in front of the trainer you lost to.

#### B3. NPC & Item Interactions
- **NPC Catch Event:** Some NPCs can trigger a Pokémon 'catch' event upon interaction (e.g., Rocker in Safari Zone East Rest House gave a CHANSEY).
- **Eevee Evolution:** An NPC in Safari Zone North mentioned Eevee can evolve into Flareon or Vaporeon, suggesting multiple evolution paths via stones.
- **EXP.ALL:** Gives EXP to all party Pokémon, even non-participants, but reduces the total EXP gained per Pokémon. Best used for targeted training.

## IV. Puzzle & Hypothesis Log
### A. Active Hypotheses
- **Pokemon Mansion Gate System:** The gates are not on a simple toggle system. Hypothesis: There are hidden pressure plates or a specific sequence of switch interactions that control the gates. Test: Explore the newly opened southern area on 1F to look for triggers. Systematically test each switch in isolation to confirm its direct effect.
- **Pokemon Mansion B1F:** The basement floor, accessible via stairs on 3F, likely holds the SECRET KEY. Hypothesis: The key is guarded by a trainer or hidden behind a puzzle. Test: Fully explore B1F.

### B. Solved Puzzles & Confirmed Mechanics
- **Pokemon Mansion Puzzle (Floors 1-3):** The mansion uses an 'alternating doors' system controlled by switches.
  - **1F Switch (3, 6):** Toggles the western gates at (17, 8/18, 8). (Confirmed T53644)
  - **2F Switch (3, 12):** Toggles northern gates (10, 5/6) and southern gates (8, 23/24). (Confirmed T52787)
  - **3F Switch (11, 6):** Toggles central gates (16, 5/6) and southern gates (16, 11/12). (Confirmed T52735)
- **Saffron Gym Puzzle:** Path to Sabrina was blocked until Silph Co. was cleared, which unlocked the correct teleporter path. (Confirmed T51442)
- **Silph Co. Puzzles (4F & 10F):** CARD KEY was required for many gates. Defeating Giovanni (11F) was the main trigger to activate the correct teleporter paths on 10F. (Confirmed T51271, T51442)

## V. Tool Debugging Log
- **pathfinder (T53767):** The tool is failing to find a path to known reachable tiles on Pokémon Mansion 1F. The game state insists a path exists to the eastern section, but the tool returns an empty list. **Hypothesis:** The tool's logic for parsing the map or its A* implementation has a subtle flaw that doesn't correctly identify all connections in the grid. **Test:** Add extensive print statements to the script to trace the `grid` creation, `start`/`end` nodes, and the state of the `open_set` and `came_from` dictionaries during the search. This will reveal where the algorithm is failing.
- **Warp Reset Mechanic:** If a wild battle is triggered immediately after using a warp to transition between maps, the game may place the player back at the warp's entry point on the original map after the battle concludes. (Observed T53666)
- **Pokemon Mansion 2F Gate System:**
  - **Hypothesis (Attempt 1):** The switch at (3, 12) follows the 'alternating doors' mechanic.
  - **Test (Attempt 1 - Failed):** Interacted with the switch at (3, 12) while at (3, 13) but facing left. No effect. Conclusion: Must be facing the object to interact.
  - **Test (Attempt 2):** Turn to face the switch (Up) and then interact.
- **pathfinder (T53770):** The first layer of debugging was insufficient. The search fails without exploring the map. **Next Test:** Add a print statement inside the A* `while` loop to log every `current` node being processed. This will trace the algorithm's exploration path and reveal where it stops.
- **pathfinder (T53792):** The tool still fails to find a path to the eastern section. The game state is the source of truth, so the tool is bugged. Hypothesis: The manual string parser is failing to correctly identify `open_gate` tiles as traversable. Test: Redefined the tool to add print statements inside the parser loop to log the `tile_type` and `is_impassable` status for every tile. This will confirm or deny the parser hypothesis.
- **pathfinder (T53794):** The parser logs confirmed the `open_gate` tiles are correctly identified as traversable. The bug is not in the parser. New Hypothesis: The `get_neighbors` function is incorrectly evaluating the `impassable` status of the gate tiles. Test: Redefined the tool to add print statements inside `get_neighbors` to trace its decision-making process for every potential neighbor.
- **pathfinder (T53796):** The `get_neighbors` function is the likely culprit. The `open_gate` tiles are correctly parsed as not impassable, but are not being added as neighbors. New Hypothesis: There is a subtle logic error in the general `impassable` check. Test: Redefined the tool to add an explicit `or tile_data['type'] == 'open_gate'` check to the `get_neighbors` function to force it to consider these tiles as valid.