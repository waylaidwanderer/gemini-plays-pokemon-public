# Game Mechanics & Systems
- The Day/Night cycle is an important mechanic in this game, affecting events.
- Received 5 POKé BALLS from the scientist in Elm's Lab. I can now catch wild Pokémon.
- The PC in Pokémon Centers is used for Pokémon and item storage.

# Current Quest: Explore Ilex Forest
- **Objective:** Navigate through Ilex Forest to reach the next area.
- **Status:** Currently at the beginning of the forest.

# Key Items
- **HIVEBADGE:** From Bugsy. Allows traded POKéMON up to L30 to obey and enables the use of CUT outside of battle.

- **POKéDEX:** A high-tech encyclopedia from PROF. OAK to record POKéMON data.
- **HM05 FLASH:** Obtained from the Elder of Sprout Tower. Illuminates dark caves. Requires the Zephyr Badge to use outside of battle.

# TMs
- **TM31 MUD-SLAP**
- **TM39 SWIFT**
- **TM49 FURY CUTTER**

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
- **Marker Hygiene for Moving Objects:** When an object with a linked marker moves off-screen, the marker becomes stale. I must immediately delete the marker. A new marker should only be created if/when the object reappears at a new location.

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
- `define_map_marker` / `delete_map_marker`: Manages map markers.
- `select_battle_option`: Automatically selects a main battle menu option (FIGHT, PKMN, PACK, RUN).
- `stun_npc`: Freezes or unfreezes an NPC's movement.

**Custom Tool Management:**
- `define_tool`: Defines a new reusable custom tool.
- `delete_tool`: Deletes a custom tool.

**Custom Agents:**
- `gym_puzzle_solver`: Analyzes gym puzzle descriptions and failed hypotheses to generate new, simple, and testable solutions.

**Custom Tools:**
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
- **DOOR**: A traversable warp tile leading into or out of a building.
- **WATER**: Impassable terrain without a specific HM (likely Surf).
- **HEADBUTT_TREE**: An interactable tree, probably requires the Headbutt move. Impassable.
- **TALL_GRASS**: Fully traversable tile. Wild POKéMON can be encountered here.
- **LEDGE_HOP_RIGHT**: A one-way traversable tile. Can only be entered from the left, moving right.
- **LEDGE_HOP_DOWN**: A one-way traversable tile. Can only be entered from above, moving down.
- **LEDGE_HOP_LEFT**: A one-way traversable tile. Can only be entered from the right, moving left.
- **CUT_TREE**: An impassable tree that likely requires the HM move Cut to remove.
- **COUNTER**: Impassable terrain, usually a barrier in front of an NPC.
- **MART_SHELF**: Impassable terrain, functions like a wall.
- **LONG_GRASS**: Fully traversable tile. Wild POKéMON can be encountered here.
- **PC**: An interactable object used to access the Pokémon Storage System and personal item storage.
- **CAVE**: A traversable warp tile leading into a cave.
- **LADDER**: A traversable warp tile that moves the player between floors.
- **FLOOR_UP_WALL**: A one-way ledge that is impassable from above. Confirmed that moving from a FLOOR tile at (5, 23) down to a FLOOR_UP_WALL tile at (5, 24) is impossible. This tile can only be traversed from below (moving up).
- **WARP_CARPET_RIGHT**: A traversable warp tile at the edge of a map that transitions to the adjacent map on the right. Must move right to activate.
- **WARP_CARPET_DOWN**: *Verification needed.* Likely a traversable warp tile that leads to a lower floor or an area to the south.
- **CUT_08 / CUT_28_GARBAGE**: *Verification needed.* Likely impassable variants of CUT_TREE.
- **VOID**: Impassable terrain that appears to be an empty space off the edge of the map.
- **unseen**: An impassable tile that has not yet been explored.

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
- **Puzzle Solution:** The gym puzzle involves finding two hidden floor switches. The first, located on the path to the right-side trainer, makes a new trainer appear on the left side. The second, on the path to the left-side trainer, makes another new trainer appear. The path to these trainers is not blocked by the Twins in the middle; it is possible to walk around the bottom of the gym. Defeating all trainers is not required to reach Bugsy.

# Self-Assessment Lessons (Turn 4048)
- **Location Verification:** I must ALWAYS verify my current map ID and (x, y) coordinates in the Game State Information before making any navigational plans, tool calls, or creating map markers. My internal sense of location is fallible and has led to critical errors.
- **Trust Tools Over Assumptions:** When a trusted tool (like `find_path`) reports a failure, I must assume my own understanding of the game state is wrong, not the tool. I will immediately re-evaluate my root hypothesis about the map layout or accessibility.
- **Immediate Maintenance:** All data hygiene (marker cleanup) and tool maintenance (fixing bugs, ensuring consistency) tasks must be performed in the immediate turn they are identified. Deferring these tasks creates cascading failures.

# Ilex Forest - Farfetch'd Puzzle
**Hypothesis:** The Farfetch'd moves away from the player in a predictable pattern. The puzzle is to herd it into a corner.

**Test 1:**
1. **Objective:** Observe Farfetch'd's reaction to direct approach.
2. **Starting Position:** (13, 34)
3. **Action:** Move to (14, 32), the tile directly south of the Farfetch'd's current position (14, 31).
4. **Expected Outcome:** The Farfetch'd will move away from me, likely north.
5. **Conclusion:** The Farfetch'd did not move. Hypothesis denied. Approaching from the south does not trigger movement.

**Test 2:**
1. **Objective:** Observe Farfetch'd's reaction to being approached from the side.
2. **Conclusion:** Test failed. The path to the target tile (15, 31) is blocked by the Farfetch'd itself.

**Test 3 (Attempt 1):**
1. **Hypothesis:** The Farfetch'd moves when the player steps on the patches of dry leaves.
2. **Action:** Attempt to move to (14, 29).
3. **Conclusion:** Test failed. Path is blocked by the Farfetch'd at (14, 31).

**Test 3 (Attempt 2):**
1. **Hypothesis:** The Farfetch'd moves when the player steps on the patches of dry leaves.
2. **Starting Position:** (14, 32)
3. **Action:** Move to an alternate leaf pile at (15, 29).
4. **Expected Outcome:** The Farfetch'd will move in response to the sound.
5. **Conclusion:** The Farfetch'd did not move. Hypothesis denied. Stepping on a leaf pile does not, by itself, trigger movement.

**Test 4:**
1. **Hypothesis:** The Farfetch'd is herded by direct interaction (facing it and pressing 'A'). It moves in the opposite direction from which it was approached.
2. **Action:** Move to (15, 26), the tile directly south of the Farfetch'd, and press 'A'.
3. **Expected Outcome:** The Farfetch'd will move north to (15, 24).

**Test 5:**
1. **Hypothesis:** The Farfetch'd is herded by direct interaction (facing it and pressing 'A'). It moves in the opposite direction from which it was approached.
2. **Action:** From (21, 24), face left towards the Farfetch'd at (20, 24) and press 'A'.
3. **Expected Outcome:** The Farfetch'd will move west to (19, 24).

# Self-Assessment Lessons (Turn 4228)
- **Position Verification:** I received a critical warning for a position mismatch. I must ALWAYS verify my current `(x, y)` coordinates in the Game State Information before planning any path or interaction. My internal sense of having moved can be a hallucination, especially after being interrupted by a battle.

**Test 6:**
1. **Hypothesis:** Interaction from an adjacent tile triggers movement along a set path, not just directly away from the player.
2. **Action:** From (15, 26), faced north towards the Farfetch'd at (15, 25) and pressed 'A'.
3. **Outcome:** Success! The Farfetch'd moved along a path to (20, 24).
4. **Conclusion:** The puzzle is solved by repeatedly getting into an adjacent position and interacting with the Farfetch'd to guide it along its route.
- **CUT_08 / CUT_28_GARBAGE**: *Verification needed.* Likely impassable variants of CUT_TREE.