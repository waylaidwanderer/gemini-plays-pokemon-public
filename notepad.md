# Game Mechanics & Systems
- The Day/Night cycle is an important mechanic in this game, affecting events.
- Received 5 POKé BALLS from the scientist in Elm's Lab. I can now catch wild Pokémon.
- The PC in Pokémon Centers is used for Pokémon and item storage.

# Current Quest: Find the Next Gym
- **Objective:** Locate and challenge the next Gym Leader.
- **Status:** The Sprout Tower investigation is complete.

# Key Items
- **MYSTERY EGG:** An egg from MR. POKEMON for PROF. ELM to study.
- **POKéDEX:** A high-tech encyclopedia from PROF. OAK to record POKéMON data.
- **HM05 FLASH:** Obtained from the Elder of Sprout Tower. Illuminates dark caves. Requires the Zephyr Badge to use outside of battle.

# Strategic Lessons
- **Automation:** I must trust and consistently use my own tools (like `select_battle_option`) to improve efficiency and reduce errors. Inconsistent use is a failure of strategy.
- **Tool Trust & Root Hypothesis:** If a trusted tool (like `find_path`) provides a result that contradicts my belief, the error is almost certainly in my foundational understanding (root hypothesis) of the game state, not in the tool itself. I must immediately challenge and test my own assumptions about game mechanics or map layout, rather than attempting to 'fix' a tool that is functioning correctly based on the game's actual rules.
- **Tool Maintenance:** If a tool produces an incorrect outcome, I must not assume the problem is external. I must first verify the tool's own logic and output. Deferring tool maintenance is a critical failure.
- **Automation:** I must trust and consistently use my own tools (like `select_battle_option`) to improve efficiency and reduce errors.
- **Item Interaction:** Items on the ground (POKE_BALLs) must be interacted with from an adjacent tile, not by standing on them.
- **Data Hygiene:** Map markers for resolved events (like collected items) must be deleted immediately to avoid confusion and wasted turns.

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
- **PC**: An interactable object used to access the Pokémon Storage System (Bill's PC) and personal item storage (Gem's PC).
- **CAVE**: A traversable warp tile leading into a cave.
- **unseen**: An impassable tile that has not yet been explored.
- **WARP_CARPET_LEFT**: A traversable warp tile at the edge of a map that transitions to the adjacent map on the left.
- **LADDER**: A traversable warp tile that moves the player between floors.

# Battle Mechanics
- Pokémon holding a BERRY can automatically use it to heal themselves when their HP gets low in battle.
- Poisoned Pokémon lose 1 HP every four steps outside of battle.
- Accuracy-lowering moves like SMOKESCREEN are not a guaranteed defense. Opponents can still land hits.
- The auto-activation threshold for a held BERRY is likely below 25% HP.
- Bug-type moves (like LEECH LIFE) are not very effective against Fire-types.
- Grass-type moves (like VINE WHIP) are not very effective against Fire-types.
- Normal-type moves have no effect on Ghost-type Pokémon.

# Menu Navigation
- For complex menu inputs (like on-screen keyboards), perform all directional movements in one turn and the final confirmation ('A' button) in the next. Do not mix directional and action buttons in the same input sequence to avoid errors.

# Archived Objectives
## Finding Mom
- **Hypothesis 1:** Mom is at her usual spot (7, 4). **Result:** Failed. She was not there.
- **Hypothesis 2:** Mom is upstairs. **Result:** Failed. She was not there.
- **Hypothesis 3:** Mom's appearance is triggered by attempting to leave the house. **Result:** Failed.
- **Hypothesis 4:** Mom's appearance is triggered by attempting to leave New Bark Town. **Result:** Failed. I successfully transitioned to Route 29 without her appearing. I have put this objective on hold.

# Party Status
- **VULCAN (CYNDAQUIL):** Lv13
- **CHRONO (HOOTHOOT):** Lv3
- **WEAVER (SPINARAK):** Lv3
- **AUDREYII (BELLSPROUT):** Lv8
- **EGG (TOGEPI):** Lv5
- **Game State Verification:** If a tool fails unexpectedly (e.g., `select_battle_option` outside of battle) or an interaction doesn't work, the first step is to verify the game state. I must confirm I am not hallucinating (e.g., imagining a battle or an item) before attempting the action again or debugging the tool.

# Custom Tools
- **find_path**: Finds a path from a start to an end coordinate on the current map using the A* algorithm.
- **check_unseen_reachability**: Checks which of the known potentially reachable unseen tiles are actually reachable from the player's current position.
- **select_battle_option**: Automatically selects a main battle menu option (FIGHT, PKMN, PACK, RUN).

# NPC Interactions
- Some interactions, like battling a trainer, can be multi-step. Ensure all initial dialogue is cleared with 'A' presses before the main event (like the battle) will trigger.
- **Tool Verification:** My `check_unseen_reachability` tool provided a false negative. Lesson: If a tool's output contradicts system information (like an alert), the tool is likely flawed. I must trust the system and fix the tool immediately rather than trusting the faulty output.

# Strategic Lessons
- **Position Verification:** Always verify my current position and map against the game state information before planning an action. My memory can be unreliable and lead to hallucinations.

# Consumable Items
- Received a BITTER BERRY from the tree at (16, 7) on Route 31.