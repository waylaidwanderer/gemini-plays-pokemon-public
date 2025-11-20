# Game Mechanics & Systems
- The Day/Night cycle is an important mechanic in this game, affecting events.
- Received 5 POKé BALLS from the scientist in Elm's Lab. I can now catch wild Pokémon.
- I must investigate the PC in the Pokémon Center to understand its function.

# Current Quest: Challenge the Violet City Gym
- **Objective:** Travel to Violet City and defeat the Gym Leader.
- **Status:** In Violet City.
- **Plan:** Explore the city, investigate Sprout Tower, then challenge the Gym.

# Key Items
- **MYSTERY EGG:** An egg from MR. POKEMON for PROF. ELM to study.
- **POKéDEX:** A high-tech encyclopedia from PROF. OAK to record POKéMON data.

# Strategic Lessons
- **CRITICAL:** When using `notepad_edit` with the "replace" action, the `old_text` must be an EXACT match. Copy from system suggestions if available to avoid errors.

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
- **VULCAN (CYNDAQUIL):** Lv12
- **CHRONO (HOOTHOOT):** Lv3
- **WEAVER (SPINARAK):** Lv3
- **AUDREYII (BELLSPROUT):** Lv5

# Violet City Intel
- An Officer mentioned I should visit SPROUT TOWER.

# Strategic Lessons
- **CRITICAL:** When using `notepad_edit` with the "replace" action, the `old_text` must be an EXACT match. Copy from system suggestions if available to avoid errors.
- **CRITICAL:** Trust and consistently use my own tools (`select_battle_option`, `pre_action_checklist`, etc.) to improve efficiency and reduce errors. Manual inputs for automatable tasks are a bad habit.

- My custom tools operate ONLY on the data provided to them. If `find_path` fails, the root cause might be my incorrect assumption about its input data (e.g., `map_xml_string` only contains seen tiles), not a flaw in the algorithm. I must trust the tool's output as a reflection of the data it sees.
- Before pathfinding, I must visually inspect the map for one-way traversal tiles like ledges. My tools are only as good as my understanding of the map mechanics. `find_path` returning 'No path found' is critical information about the map's structure, not a tool failure.

# Strategic Lessons
- **`notepad_edit` Safeguard:** The 'replace' and 'overwrite' actions have a character loss threshold to prevent accidental data deletion. For large-scale refactoring, use small, incremental 'replace' actions.

# Tool Development

# Tool Development Lessons
- If a tool produces an incorrect outcome, I must not assume the problem is external (e.g., game timing). I must first verify the tool's own logic and output. Deferring tool maintenance is a critical failure.

# Item Interaction
- Items on the ground (POKE_BALLs) must be interacted with from an adjacent tile, not by standing on them.