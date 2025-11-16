# Gem's Brain 🧠

## 1. My Toolkit
### Built-in Tools
- `notepad_edit`
- `run_code`
- `define_agent`
- `delete_agent`
- `define_map_marker`
- `delete_map_marker`
- `stun_npc`
- `define_tool`
- `delete_tool`
- `select_battle_option`

### Custom Agents
- `city_exploration_planner`: Creates efficient exploration routes for new cities.
- `reality_check_agent`: Checks my plans against game state to prevent hallucinations.
- `puzzle_solver_agent`: Suggests simple, logical tests for puzzles.
- `navigation_strategist`: A unified navigation advisor.
- `party_strategist_agent`: Analyzes the player's stored Pokémon and a given strategic goal to recommend an optimal party of three.

### Custom Tools
- `deterministic_battle_strategist`: Recommends battle actions and moves.
- `list_reachable_unseen_tiles`: Lists all reachable unseen tiles from the player's position.
- `plan_path_to_target`: Generates a path to a target coordinate. NOTE: This tool only PLANS the path. You must set `buttons_to_press` to `['path']` to execute it.
- `pokemon_nicknamer`: Automates nicknaming Pokémon.
- `party_leader_switcher`: Automates the process of making a specific Pokémon the party leader.

### Tool Development Ideas
- **`withdraw_pokemon_tool`**: A tool to automate withdrawing a specific Pokémon by name, to avoid manual menu navigation.
- **`menu_navigator_tool`**: Takes a target text option in a menu and generates the button presses to select it.
- **`systematic_room_searcher`**: A tool that takes room boundaries as input and generates a path to systematically check every wall-adjacent tile for secrets.
- **`battle_move_selector`**: A tool that takes a move name and current cursor position to generate the button presses needed to select it in the battle menu.
- **`dungeon_navigator_agent`**: An agent to plan the optimal path through a multi-floor dungeon to reach a specific goal (e.g., 'the top').
- **`inventory_checker`**: A tool that takes an item name and confirms if it's in the bag, returning true/false and quantity. This would prevent inventory-based hallucinations.
- **`puzzle_context_extractor`**: An agent that parses the notepad's Journey Log to automatically extract failed hypotheses for the current puzzle, streamlining input for the `puzzle_solver_agent`.
- **`log_puzzle_attempt`**: A tool to automate adding new hypotheses and results to the Journey Log section of the notepad.

## 2. 🚨 CRITICAL DIRECTIVES & LESSONS
- **IMMEDIATE MAINTENANCE:** All data management (notepad, markers) and tool/agent fixes MUST be done in the same turn a new discovery or bug is found. There is no 'later'.
- **AGENT VERIFICATION:** Agent outputs are hypotheses, not facts. The `world_navigator_agent` incorrectly assumed I had the SECRET POTION just because I had the Storm Badge. I MUST verify all claims, especially those related to inventory, before changing my goals.
- **PATH EXECUTION:** Calling `plan_path_to_target` only generates a path. I MUST set `buttons_to_press` to `["path"]` to actually move, otherwise I will hallucinate my position.
- **REALITY CHECKS:** My internal sense of location is unreliable. I MUST verify my position from the game state before any significant action to prevent hallucination loops.
- **COORDINATE SYSTEM:** Map data is 0-indexed (`0 <= coordinate < dimension`). Pathfinding tools MUST use this logic.
- **INVENTORY VERIFICATION:** I must check my PACK before assuming I have an item to prevent hallucination (e.g., the nonexistent ESCAPE ROPE incident).
- **TEXT BOXES:** Pressing 'B' is not a universal solution for closing text boxes where 'A' fails (e.g., Sailor in Olivine Lighthouse), but it has been confirmed to work for breaking dialogue loops (e.g., Rival on Route 41). This should be tested as an alternative when 'A' is unresponsive.
- **TOOL MISUSE:** `autopress_buttons=true` is ONLY for tools that output button strings, not coordinates or decisions.
- **ITEM MANAGEMENT:** Taking a held item with a full bag destroys it. The only safe way to free a slot is to have a Pokémon hold an item.
- **DIG GLITCH (CRITICAL):** Using DIG as a field move in the Olivine Lighthouse dead-end room causes a game-breaking glitch, corrupting all player data. Avoid using DIG as a field move until further testing.

## 3. Main Quest & Active Leads
- **Primary Objective:** Find the 'special medicine' to heal the sick Ampharos at the top of the Olivine Lighthouse.
- **Legendary Beasts:** Suicune, Raikou, and Entei have been awakened in the Burned Tower. The Sage in the Tin Tower has asked me not to enter.
- **Stolen Pokémon (Cianwood):** A Rocker's Pokémon was stolen. I am currently safekeeping his SHUCKIE.
- **Moomoo Farm:** The Miltank is sick and requires a specific item named 'BERRY'. Other named berries do not work.

### Phone Contacts
- **DANA (LASS):** Route 38 (Rematch).
- **GINA (PICNICKER):** Route 34 (Rematch).
- **HUEY (SAILOR):** OLIVINE LIGHTHOUSE (Rematch).
- **ANTHONY (HIKER):** Route 33 (Rematch). Chatted about MACHOP & GEODUDE.
- **JACK (SCHOOLBOY):** NATIONAL PARK (Rematch). Chatted about VOLTORB.
- **ALAN (SCHOOLBOY):** Route 36 (Rematch). Chatted about beating a Ledyba.

## Special Events & Swarms
- **Hiker Anthony:** Dunsparce swarm in Dark Cave.

## 4. World State & Blocked Paths
- **Tin Tower:** Path blocked by a Sage (legendary beasts awakened).
- **Olivine Lighthouse:** Path up is blocked, needs 'special medicine'.
- **Route 41 (WHIRL ISLANDS):** Interior is 'pitch-black' (needs FLASH); WHIRLPOOL tiles are impassable.
- **Route 42:** Path to Mahogany Town blocked by water (needs SURF).
- **Goldenrod Underground:** Locked door at (18, 6) is unsolved.
- **Route 40/41 Water Route:** Confirmed dead end. Multiple pathfinding attempts to the west failed, blocked by a buoy maze.
- **Battle Tower:** The receptionist at (7, 6) on BattleTower1F stated that only three Pokémon may be entered. This is a confirmed prerequisite.

## 5. Untested Assumptions
- **FLY HM:** I'm assuming FLY isn't working due to a story event or a bug. **Alternative Hypothesis:** Maybe it only works from certain locations (like cities) or I'm missing a prerequisite I'm unaware of.
- **Azalea Gym:** The statues at the entrance might be switches. Alt: They do nothing, and the puzzle is floor-based or involves trainer interaction order.
- **Battle Tower:** I'm assuming it's a side quest. **Alternative Hypothesis:** Progressing inside might unlock a new path or item needed for the main story.

## 6. Confirmed System Mechanics
- **Respawning Obstacles:** HM-cleared obstacles (like CUT_TREE) respawn upon re-entering a map.
- **HM Move Permanence:** HM moves cannot be forgotten through normal means.
- **Multi-Press Dialogue:** Some NPCs require pressing 'A' multiple times to advance text.
- **Phone List Limit:** The phone list can become full.
- **`stun_npc` Tool:** Freezes an NPC's movement but does not make them traversable.
- **Evolution via Trade:** MACHOKE, KADABRA, HAUNTER, and GRAVELER evolve by trading.
- **Defeated Trainers as Obstacles:** Trainers in the Azalea Gym remain impassable after defeat.
- **STRENGTH HM:** The move STRENGTH is used to *push* boulders, not break them. The boulder requires an empty space on the opposite side to be moved.

### 7. Tile Mechanics
### Impassable
- BOOKSHELF, BUOY, COUNTER, CUT_TREE (needs CUT), HEADBUTT_TREE (needs HEADBUTT), MART_SHELF, PC (interactable), PILLAR, RADIO, ROCK (needs STRENGTH), TV, VOID, WALL, WHIRLPOOL, WINDOW
- **TOWN_MAP:** Impassable. Interactable from the tile below it (3,1), which displays a full-screen map of the Whirl Islands. This view is cancelled by any subsequent directional input.
### Traversable
- FLOOR (standard traversable ground), GRASS, TALL_GRASS (wild encounters)
### Warp Tiles
- DOOR, LADDER, STAIRCASE (two-way)
- PIT (one-way)
- WARP_CARPET_RIGHT (one-way)
### Conditional & One-Way
- FLOOR_UP_WALL (ledge, down only)
- LEDGE_HOP_DOWN (down only)
- LEDGE_HOP_LEFT (left only)
- LEDGE_HOP_RIGHT (right only)
- WATER (impassable without SURF)
- WARP_CARPET_DOWN (One-way exit. Observed to be inactive when stepped on, suggesting it is the destination of a warp from another location.)

## 8. Journey Log & Puzzle Solutions
### Solved Puzzles & Key Discoveries
- **Sudowoodo Tree (Route 36):** Solved by using the SQUIRTBOTTLE to initiate a battle.
- **Goldenrod Dept. Store:** A bargain sale is happening now (per Todd's call).
- **Route 41 (WHIRL ISLANDS):** Interior is 'pitch-black' (needs FLASH).
- **Cianwood City:** Received SHUCKIE from a Rocker whose other Pokémon was stolen.
- **Route 30 Ledge:** Confirmed one-way (down only).
- **Olivine Lighthouse 1F Secret Passage:** The Sailor at (8, 2) is not a simple dialogue NPC. Passage is a confirmed dead end.
- **LIGHTHOUSE SAILOR CRASH (CRITICAL):** Previously observed that interacting with the Sailor at Olivine Lighthouse 5F (8, 11) and advancing his dialogue to the battle prompt caused a game-breaking crash. A recent test (Turn 43093) resulted in only dialogue. The crash may be conditional. AVOID BATTLE INTERACTION.
- **LIGHTHOUSE SAILOR CRASH 2 (CRITICAL):** Interacting with the Sailor at Olivine Lighthouse 3F (9, 2) while standing on the warp at (9, 3) causes a game-breaking crash, corrupting all save data. AVOID THIS INTERACTION.
- **Olivine Lighthouse Descent Puzzle:** Solved. The solution involved ascending to 6F and finding a new pit on the eastern side at (16, 5) or (17, 5) to access the eastern sections of the lower floors.

#### CianwoodLugiaSpeechHouse Escape Log
- **Objective:** Exit the house. Player is trapped with movement locked.
- **Hypothesis 56 (Self-Generated):** Pressing the 'B' button from the overworld will cancel the movement lock. **Result:** Success! Movement was unlocked after pressing 'B'.
- **Dana's Gift:** DANA called from Route 38. She has a gift for me.

#### Battle Tower 1F Escape Log
- **Objective:** Exit the room. The exit door at (7, 0) is blocked by the Receptionist. The exit warps at (7, 9) and (8, 9) are inactive.
- **Summary of Failed Hypotheses:**
    - **Movement:** All simple movement patterns onto and across the warp tiles at (7,9) and (8,9) have failed (vertical entry, lateral entry, continuous movement).
    - **Interaction:** Interacting with all visible objects (NPCs, PC, Sign) has yielded no results. Systematically pressing 'A' on both warp tiles while facing all four cardinal directions has also failed. All dialogue options with the Receptionist have been explored.
    - **BATTLE TOWER SAVE CORRUPTION (CRITICAL):** Saving the game to start the battle challenge, regardless of party composition, causes a catastrophic, game-breaking glitch that **completely corrupts all player data**, including name, money, Pokedex, party, and inventory. This action permanently destroys the save file. **THIS PATH MUST BE AVOIDED AT ALL COSTS.** The only way to escape the initial menu loop without saving is to press 'B' at the level select menu and then select 'YES' to cancel the challenge.
    - **Item-based:** Using the ITEMFINDER yielded no results. Equipping all three party members with different held items did not change the outcome of interacting with the Receptionist.
    - **Sequential:** Interacting with the Cooltrainer F and then immediately walking onto the warp tile at (7,9) failed.
- **Current Hypothesis:** The battle challenge is glitching because my party's levels (12, 48, 20) are invalid for any of the challenge brackets. The intended solution is to assemble a team of three Pokémon at or below level 10 to successfully enter the L:10 challenge.
#### Battle Tower 1F Escape Log (Update)
- **Failed Hypothesis (NPC Interaction):** Interacting with the Cooltrainer F at (3, 9) and the Youngster at (14, 9) yields only generic dialogue and does not trigger an escape event. This confirms that interacting with the trainers on the lower floor is not the solution.