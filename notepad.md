# Game Mechanics & Systems
- The Day/Night cycle is an important mechanic in this game, affecting events.
- Received 5 POKé BALLS from the scientist in Elm's Lab. I can now catch wild Pokémon.
- The PC in Pokémon Centers is used for Pokémon and item storage.

# Current Quest: Find the Next Gym
- **Objective:** Locate and challenge the next Gym Leader.
- **Status:** Exploring Route 33 to find the next town.

# Key Items
- **MYSTERY EGG:** An egg from MR. POKEMON for PROF. ELM to study.
- **POKéDEX:** A high-tech encyclopedia from PROF. OAK to record POKéMON data.
- **HM05 FLASH:** Obtained from the Elder of Sprout Tower. Illuminates dark caves. Requires the Zephyr Badge to use outside of battle.

# Consumable Items
- Received a BITTER BERRY from the tree at (16, 7) on Route 31.

# Strategic Lessons
- **Tool Trust & Root Hypothesis:** If a trusted tool (like `find_path`) provides a result that contradicts my belief (e.g., reports "No path found"), the error is almost certainly in my foundational understanding of the game state, not in the tool itself. I must immediately trust the tool's output and challenge my own assumptions about map layout or game mechanics. My mental model of the map is fallible; the tool's analysis of the map data is not. This is a critical lesson learned from repeated failures in Union Cave.
- **Automation:** I must trust and consistently use my automation tools (like `select_battle_option`) to improve efficiency and reduce errors. Inconsistent use is a failure of strategy.
- **Tool Maintenance & Verification:** If a tool produces an incorrect outcome or contradicts system information, I must not assume the problem is external. The tool is likely flawed and must be fixed immediately. Deferring tool maintenance is a critical failure.
- **Tool Consistency:** When one tool's logic is updated (like `find_path`), any other tools that use similar logic (`check_unseen_reachability`) must be updated immediately to prevent conflicting results and strategic errors.
- **Data Hygiene:** Map markers for resolved events (like collected items) must be deleted immediately to avoid confusion and wasted turns. When updating a marker for an object (e.g., after defeating a trainer), the old marker must be deleted to prevent redundant and conflicting information. Markers should also be linked to their corresponding `object_id` whenever possible to ensure they move with the object.
- **Position Verification:** My internal sense of position can be unreliable and lead to hallucinations. I must always verify my current `(x, y)` coordinates in the Game State Information before planning any path or interaction.
- **Notepad Precision:** When using `notepad_edit`'s `replace` action, the `old_text` must be an exact, character-for-character match. Using `overwrite` is often safer for larger reorganizations.
- **Game State Verification:** If a tool fails unexpectedly or an interaction doesn't work, the first step is to verify the game state. I must confirm I am not hallucinating before attempting the action again or debugging the tool.
- **Item Interaction:** Items on the ground (POKE_BALLs) must be interacted with from an adjacent tile, not by standing on them.
- **NPC Interactions:** Some interactions, like battling a trainer, can be multi-step. Ensure all initial dialogue is cleared with 'A' presses before the main event (like the battle) will trigger.
- **Pathfinding Logic:** If a path is repeatedly blocked or a tool reports 'No path found,' do not assume you are soft-locked. Re-examine the map visually for alternative routes like ledges or other one-way tiles that may have been missed.
- **Tile Mechanic Verification:** I must verify the mechanics of every tile type through direct observation and experimentation. Assumptions based on a tile's name can be wrong and lead to critical tool failures. I must never assume I know how a tile works until I have tested it.
- **Immediate Correction Principle:** If an in-game observation contradicts a hypothesis (e.g., a failed movement), my absolute highest priority is to immediately correct my internal knowledge base (notepad) and any related tools. Deferring this creates cascading errors.
- **Dialogue & Movement:** I must ensure all dialogue boxes are closed by pressing 'A' before attempting any movement inputs. Trying to move with text on screen will fail.

# Battle Mechanics
- Pokémon holding a BERRY can automatically use it to heal themselves when their HP gets low in battle.
- Poisoned Pokémon lose 1 HP every four steps outside of battle.
- Accuracy-lowering moves like SMOKESCREEN are not a guaranteed defense.
- The auto-activation threshold for a held BERRY is likely below 25% HP.
- Bug-type moves (like LEECH LIFE) are not very effective against Fire-types.
- Grass-type moves (like VINE WHIP) are not very effective against Fire-types.
- Normal-type moves have no effect on Ghost-type Pokémon.
- Normal-type moves (like TACKLE) are not very effective against Rock/Ground-types (like GEODUDE).

# Menu Navigation
- For complex menu inputs (like on-screen keyboards), perform all directional movements in one turn and the final confirmation ('A' button) in the next. Do not mix directional and action buttons in the same input sequence to avoid errors.

# Available Tools
**Built-in Tools:**
- `notepad_edit`: Edits this notepad.
- `run_code`: Executes a single-use Python script.
- `define_agent` / `delete_agent`: Manages custom reasoning agents.
- `define_tool` / `delete_tool`: Manages custom tools.
- `define_map_marker` / `delete_map_marker`: Manages map markers.
- `stun_npc`: Freezes or unfreezes an NPC's movement.
- `select_battle_option`: Automatically selects a main battle menu option (FIGHT, PKMN, PACK, RUN).

**Custom Agents & Tools:**
- `gym_puzzle_solver`: Analyzes gym puzzle descriptions and failed hypotheses to generate new, simple, and testable solutions.
- `find_path`: Finds a path from a start to an end coordinate on the current map using the A* algorithm.
- `check_unseen_reachability`: Checks which of the known potentially reachable unseen tiles are actually reachable from my current position.

# Tile Mechanics
- **WALL**: Impassable terrain.
- **FLOOR**: A standard, fully traversable tile.
- **TOWN_MAP**: An interactable object on a wall; impassable.
- **STAIRCASE**: A traversable warp tile that moves the player between floors.
- **TV**: An impassable object.
- **BOOKSHELF**: An impassable object.
- **WINDOW**: An impassable object, functions like a wall.
- **RADIO**: An impassable object.
- **WARP_CARPET_DOWN**: A traversable warp tile that leads outside or to a lower floor.
- **WARP_CARPET_RIGHT**: A traversable warp tile at the edge of a map that transitions to the adjacent map on the right.
- **DOOR**: A traversable warp tile leading into or out of a building.
- **WATER**: Impassable terrain without a specific HM (likely Surf).
- **HEADBUTT_TREE**: An interactable tree, probably requires the Headbutt move. Impassable.
- **TALL_GRASS**: Fully traversable tile. Wild POKéMON can be encountered here.
- **LEDGE_HOP_RIGHT**: A one-way traversable tile. Can only be entered from the left, moving right.
- **LEDGE_HOP_DOWN**: A one-way traversable tile. Can only be entered from above, moving down.
- **LEDGE_HOP_LEFT**: A one-way traversable tile. Can only be entered from the right, moving left.
- **CUT_TREE**: An impassable tree that likely requires the HM move Cut to remove.
- **COUNTER**: Impassable terrain, usually a barrier in front of an NPC.
- **VOID**: Impassable, appears to be an empty space off the edge of the map.
- **MART_SHELF**: Impassable terrain, functions like a wall.
- **LONG_GRASS**: Fully traversable tile. Wild POKéMON can be encountered here.
- **CUT_08 / CUT_28_GARBAGE**: *Verification needed.* Likely impassable variants of CUT_TREE.
- **PC**: An interactable object used to access the Pokémon Storage System and personal item storage.
- **CAVE**: A traversable warp tile leading into a cave.
- **unseen**: An impassable tile that has not yet been explored.
- **WARP_CARPET_LEFT**: A traversable warp tile at the edge of a map that transitions to the adjacent map on the left.
- **LADDER**: A traversable warp tile that moves the player between floors.
- **FLOOR_UP_WALL**: A one-way ledge that is impassable from above. Confirmed that moving from a FLOOR tile at (5, 23) down to a FLOOR_UP_WALL tile at (5, 24) is impossible. This tile can only be traversed from below (moving up).

# Party Status
- **VULCAN (QUILAVA):** Lv19
- **CHRONO (HOOTHOOT):** Lv4
- **WEAVER (SPINARAK):** Lv3
- **EGG (TOGEPI):** Lv5
- **ROCKY (ONIX):** Lv8

# Object Mechanics
- **TEACHER / LASS / BIRD**: These objects are impassable and function as walls.
- **FRUIT_TREE**: An impassable, interactable object. Gives one BERRY item (like PRZCUREBERRY) when interacted with for the first time. Subsequent interactions yield nothing.

# NPC Dialogue
- **POKEFAN_M in Violet City House:** Traded Pokémon grow quickly but may disobey without the correct Gym Badge.
- Received MIRACLE SEED from a trainer on Route 32.

# Crafting
- Kurt in Azalea Town can make special POKé BALLS from APRICORNS. I received a LURE BALL from him as an example.

# Azalea Gym Info
- Gym Guide: The Gym Leader is BUGSY. His Bug POKéMON are weak to Fire and Flying-type moves.

# Azalea Gym Puzzle
- **Objective:** Defeat Bugsy. Path is blocked by defeated Twins at (4, 10) and (5, 10).
- **Hypothesis 1:** Battle Bug Catcher at (8, 9) by talking to him.
  - **Test:** Interacted from below (8, 10), from the side (9, 9), and walked into his line of sight.
  - **Conclusion:** Failed. NPC only gives dialogue. Does not trigger battle.
- **Hypothesis 2:** A switch must be activated to move the platforms.
  - **Test 2a (Statues):** Interacted with statues at (3, 13) and (6, 13) from below.
    - **Conclusion:** Failed. Only displays gym name. Marked with '🚫'.
  - **Test 2b (Wall Objects):** Interacted with red objects at (2, 9) and (7, 9) from below.
    - **Conclusion:** Failed. No interaction occurred. Marked with '🚫'.

# Azalea Gym Puzzle (Agent Hypotheses)
- **Hypothesis A1:** The path is cleared by triggering a battle with the Bug Catcher at (8, 9) by approaching him from behind.
  - **Test Plan:** Walk onto the tile directly behind the Bug Catcher at coordinate (8, 10).
- **Hypothesis A2:** The defeated Twins will move after being spoken to again.
  - **Test Plan:** Approach the defeated Twins at coordinates (4, 10) and (5, 10) and interact with them.
  - **Conclusion:** Failed. Interacting with the Twin at (4, 10) triggered new dialogue, but they did not move.
- **Hypothesis A3:** The Twins will move after all other trainers in the gym have been defeated.
  - **Test Plan:** Locate and defeat every other trainer in the gym, then return to the Twins to see if they have moved. (Currently blocked by un-battleable trainer).
- **Hypothesis A4:** Stepping on a hidden switch on the floor will cause the Twins to move.
  - **Test Plan:** Systematically walk over every single accessible floor tile in the gym.

# Azalea Gym Puzzle (Agent Hypotheses 2)
- **Hypothesis B1:** Interacting with the red objects in the reverse sequence (left then right) will move the Twins.
  - **Test Plan:** Interact with the red object at (2, 9), then interact with the red object at (7, 9). Check if the Twins at (4, 10) and (5, 10) have moved.
- **Hypothesis B2:** The red objects are switches that move the spider platforms, which is necessary to progress.
  - **Test Plan:** Interact with the red object at (2, 9) and observe if either spider platform moves. Repeat this test for the red object at (7, 9).
- **Hypothesis B3:** The Twins will move only after all trainers in the gym are defeated, and the red objects are required to reach the remaining trainers.
  - **Test Plan:** Use the red objects to manipulate the spider platforms to reach and battle the trainer at (8, 9) and any other undefeated trainers. After all trainers are defeated, check if the Twins have moved.
- **Hypothesis B4:** Leaving and re-entering the gym will reset the position of the defeated Twins, clearing the path.
  - **Test Plan:** Exit the gym through the entrance and then immediately re-enter. Check if the Twins at (4, 10) and (5, 10) have moved.
- **Hypothesis B4:** Leaving and re-entering the gym will reset the position of the defeated Twins, clearing the path.
  - **Conclusion:** Failed. The Twins' position did not change after re-entering the gym.

# Azalea Gym Puzzle (Agent Hypotheses 2)
- **Hypothesis B1:** Interacting with the red objects in the reverse sequence (left then right) will move the Twins.
  - **Test Plan:** Interact with the red object at (2, 9), then interact with the red object at (7, 9). Check if the Twins at (4, 10) and (5, 10) have moved.
- **Hypothesis B2:** The red objects are switches that move the spider platforms, which is necessary to progress.
  - **Test Plan:** Interact with the red object at (2, 9) and observe if either spider platform moves. Repeat this test for the red object at (7, 9).
- **Hypothesis B3:** The Twins will move only after all trainers in the gym are defeated, and the red objects are required to reach the remaining trainers.
  - **Test Plan:** Use the red objects to manipulate the spider platforms to reach and battle the trainer at (8, 9) and any other undefeated trainers. After all trainers are defeated, check if the Twins have moved.
- **Hypothesis B4:** Leaving and re-entering the gym will reset the position of the defeated Twins, clearing the path.
  - **Test Plan:** Exit the gym through the entrance and then immediately re-enter. Check if the Twins at (4, 10) and (5, 10) have moved.
  - **Conclusion:** Failed. The Twins' position did not change after re-entering the gym.