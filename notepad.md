# Gem's Brain 🧠

## 1. 🚨 CRITICAL DIRECTIVES & LESSONS
- **HALLUCINATION & REALITY CHECKS (MANDATORY):** I have a documented history of critical failures from flawed spatial reasoning and location hallucinations (e.g., Radio Tower 1F, Mt. Mortar, Game Corner, Underground). I MUST use the `reality_check_agent` BEFORE planning significant navigation or puzzle-solving actions to prevent this recurring error. Trusting system warnings for correction instead of proactively using my own tools is a critical failure.
- **PRINCIPLE OF SIMPLICITY (BATTLE TOWER):** After 40+ complex failed hypotheses, the solution was simply walking onto the exit warp carpet. I assumed it was a one-way entrance without ever testing it. This is a catastrophic failure of the scientific method. ALWAYS test the simplest, most fundamental assumptions first before escalating to complex theories.
- **THE LLM REALITY:** As an LLM, my "thinking" only happens when I process a prompt. There is no "later." Any task I identify (fixing a tool, updating notes, placing a marker) MUST be performed in the CURRENT turn. Deferring tasks is a critical failure based on a misunderstanding of my own nature.
- **REALITY CHECKS (MANDATORY):** I have a documented history of critical failures from flawed spatial reasoning and location hallucinations (e.g., Radio Tower 1F, Mt. Mortar). I MUST use the `reality_check_agent` BEFORE planning significant navigation or puzzle-solving actions to prevent this recurring error.
- **BATTLE TOWER GLITCH (CRITICAL):** Accepting the battle challenge and saving triggers a guaranteed, game-breaking data corruption glitch. This is unavoidable. The only fix is to press 'B' at the level select menu and cancel the challenge. This restores the save data but is a reset mechanism, NOT an escape route from the lobby.
- **IMMEDIATE MAINTENANCE:** All data management (notepad, markers) and tool/agent fixes MUST be done in the same turn a new discovery or bug is found. There is no 'later'.
- **PATH EXECUTION:** Calling `plan_path_to_target` only generates a path. I MUST set `buttons_to_press` to `["path"]` to actually move, otherwise I will hallucinate my position.
- **COORDINATE SYSTEM:** Map data is 0-indexed (`0 <= coordinate < dimension`). Pathfinding tools MUST use this logic.
- **INVENTORY VERIFICATION:** I must check my PACK before assuming I have an item to prevent hallucination (e.g., the nonexistent ESCAPE ROPE incident).
- **TEXT BOXES:** Pressing 'B' is not a universal solution for closing text boxes where 'A' fails (e.g., Sailor in Olivine Lighthouse), but it has been confirmed to work for breaking dialogue loops (e.g., Rival on Route 41). This should be tested as an alternative when 'A' is unresponsive.
- **TOOL MISUSE:** `autopress_buttons=true` is ONLY for tools that output button strings, not coordinates or decisions.
- **ITEM MANAGEMENT:** Taking a held item with a full bag destroys it. The only safe way to free a slot is to have a Pokémon hold an item.
- **DIG GLITCH (CRITICAL):** Using DIG as a field move in the Olivine Lighthouse dead-end room causes a game-breaking glitch, corrupting all player data. Avoid using DIG as a field move until further testing.

## 2. Main Quest & Active Leads
- **Dark Cave Lead:** Received mail on the Battle Tower PC from 'RANDY'. Message: 'DARK CAVE leads to another road.' This confirms it's a through-route.
- **Legendary Beasts:** Suicune, Raikou, and Entei have been awakened in the Burned Tower. The Sage in the Tin Tower has asked me not to enter.
- **Stolen Pokémon (Cianwood):** A Rocker's Pokémon was stolen. I am currently safekeeping his SHUCKIE.
- **Moomoo Farm:** The Miltank is sick and requires a specific item named 'BERRY'. Other named berries do not work.
- **Hidden Items (Burned Tower):** An NPC in the Ecruteak Itemfinder house mentioned there are hidden items in the Burned Tower.

### Phone Contacts
- **DANA (LASS):** Route 38 (Rematch requested again).
- **GINA (PICNICKER):** Route 34 (Rematch requested again).
- **HUEY (SAILOR):** OLIVINE LIGHTHOUSE (Rematch).
- **ANTHONY (HIKER):** Route 33. Chatted about his MACHOP and seeing wild GEODUDE.
- **JACK (SCHOOLBOY):** NATIONAL PARK (Rematch). Chatted about VOLTORB.
- **ALAN (SCHOOLBOY):** Route 36 (Rematch). Chatted about beating a Ledyba.
- **TODD (CAMPER):** ROUTE 34 (Rematch requested).

## Special Events & Swarms
- **Hiker Anthony:** Dunsparce swarm in Dark Cave.

## 3. World State & Blocked Paths
- **Tin Tower:** Path blocked by a Sage (legendary beasts awakened).
- **Route 41 (WHIRL ISLANDS):** Interior is 'pitch-black' (needs FLASH); WHIRLPOOL tiles are impassable.
- **Route 42:** Path to Mahogany Town blocked by water (needs SURF).
- **Goldenrod Underground:** Locked door at (18, 6) is unsolved.
- **Route 40/41 Water Route:** Confirmed dead end. Multiple pathfinding attempts to the west failed, blocked by a buoy maze.

## 4. New Hypotheses & Future Tests
- **Bugged Youngster (Route 32):** Current assumption is the interaction is permanently bugged. **Alternative Hypothesis:** The bug might be state-dependent (e.g., resets after leaving the map, time-of-day). **Test (Low Priority):** After making more progress, return to Route 32 and attempt to interact with the Youngster at (3, 45) again.
- **Path to Mahogany Town:** Current assumption is the only path is south through Route 32 and Union Cave. **Alternative Hypothesis:** The water route east of Ecruteak City (Route 42) might now be passable with SURF. The 'DARK CAVE leads to another road' lead is also a viable alternative. **Test:** If the southern path becomes blocked, prioritize exploring Dark Cave or returning to Route 42.
- **Mt. Mortar Purpose:** Current hypothesis is that Mt. Mortar is a side area, not the main path to Mahogany Town, based on repeated dead ends. **Alternative Hypothesis:** A required HM (like Waterfall) may be needed to fully explore it, or a hidden switch/item controls the waterfalls.
- **Dark Cave Path:** Current hypothesis is that Dark Cave is not the primary path to Mahogany Town, despite the mail from 'RANDY'. **Alternative Hypothesis:** My initial exploration was incomplete and a viable path exists.

## 5. Confirmed System Mechanics
- **Respawning Obstacles:** HM-cleared obstacles (like CUT_TREE) respawn upon re-entering a map.
- **HM Move Permanence:** HM moves cannot be forgotten through normal means.
- **Multi-Press Dialogue:** Some NPCs require pressing 'A' multiple times to advance text.
- **Phone List Limit:** The phone list can become full.
- **Evolution via Trade:** MACHOKE, KADABRA, HAUNTER, and GRAVELER evolve by trading.
- **Defeated Trainers as Obstacles:** Trainers in the Azalea Gym remain impassable after defeat.
- **STRENGTH HM:** The move STRENGTH is used to *push* boulders, not break them. The boulder requires an empty space on the opposite side to be moved.

## 6. Tile Mechanics
### Impassable
- BOOKSHELF, BUOY, COUNTER, CUT_TREE (needs CUT), HEADBUTT_TREE (needs HEADBUTT), MART_SHELF, PC (interactable), PILLAR, RADIO, ROCK (needs STRENGTH), TV, VOID, WALL, WHIRLPOOL, WINDOW, WATERFALL (untested, likely needs HM), INCENSE_BURNER, RadioTower2FSalesSign, RadioTower2FOaksPKMNTalkSign, RadioTower2FPokemonRadioSign
- **TOWN_MAP:** Impassable. Interactable from the tile below it (3,1), which displays a full-screen map of the Whirl Islands. This view is cancelled by any subsequent directional input.
### Traversable
- **FLOOR:** Standard traversable ground. Visual appearance may vary (e.g., patterned carpets, plain floors), but the function is the same.
- GRASS, TALL_GRASS (wild encounters)
- **LADDER:** Can function as a standard traversable floor (e.g., Route 32 pier), not just a vertical warp.
### Warp Tiles
- DOOR, LADDER, STAIRCASE (two-way)
- PIT (one-way)
- WARP_CARPET_LEFT (two-way, requires facing left)
- WARP_CARPET_RIGHT (two-way, requires facing right)
- WARP_CARPET_DOWN (two-way, requires facing down)
- CAVE (impassable warp)
### Conditional & One-Way (Movement FROM tile)
- **CRITICAL TEST PENDING (HIGH PRIORITY):** My pathfinder assumes `LEDGE_HOP_DOWN` tiles are one-way. This is unverified. I MUST test this at the next opportunity.
  - **Hypothesis:** It is impossible to move 'Up' onto a `LEDGE_HOP_DOWN` tile.
  - **Test Plan:**
    1. Locate the nearest `LEDGE_HOP_DOWN` tile.
    2. Position player on the tile directly below it.
    3. Press 'Up' to attempt to move onto the ledge tile.
    4. **Record Outcome:** Document whether the movement was successful or blocked. This test is mandatory to resolve the unverified mechanic.
- LEDGE_HOP_LEFT: Can only move Left from this tile.
- LEDGE_HOP_RIGHT: Can only move Right from this tile.
- FLOOR_UP_WALL: Can only move Down from this tile. Impassable from above (cannot move Down onto it).
- WATER (impassable without SURF)

## 8. Lessons Learned
- **Verify Before Automating:** I wasted time creating the `pokemon_info_extractor` tool based on the unverified assumption that the PC screen text would reliably indicate the selected Pokémon's name. The text does not, making the tool's primary function impossible. I must verify the data source and its structure *before* developing tools to automate interaction with it.
- **MAJOR HALLUCINATION (Turns 46632-46652):** I incorrectly concluded my `plan_path_with_warnings` tool was broken when it failed to find a path around the receptionist. I wasted over 20 turns debugging a correct tool instead of trusting its output and verifying the blockage in-game. The true failure was my own flawed spatial reasoning and failure to use the `reality_check_agent`.
- **Pathing Blockage (Moving NPCs):** If a planned path is blocked by a moving NPC, the most efficient solution is to immediately recalculate the path from the current position rather than attempting complex workarounds or waiting.

## 9. Archived Puzzle Logs

## Gym Leaders
- **Jasmine (Olivine City):** Uses Steel-type Pokémon.

## 11. Archived Sudowoodo Puzzle Log

- **Tool Limitation (Pathfinder Warnings):** My `plan_path_with_warnings` tool relies on a hardcoded list of static NPC names (`id-name`). This is brittle because some NPC types (like COOLTRAINER_M) can be both static and moving. This causes false positive warnings. **Future Improvement:** Investigate if there's a way to provide the `is_moving_npc` flag to the tool for more accurate warnings.

## 12. Custom Tools & Agents

## 12. Custom Tools & Agents

### Built-in Tools
- **notepad_edit**: Edits the notepad.
- **run_code**: Executes Python code.
- **define_agent**: Creates or updates a custom agent.
- **delete_agent**: Deletes a custom agent.
- **define_map_marker**: Creates or updates a map marker.
- **delete_map_marker**: Deletes a map marker.
- **stun_npc**: Freezes or unfreezes an NPC's movement.
- **define_tool**: Creates or updates a custom tool.
- **delete_tool**: Deletes a custom tool.
- **select_battle_option**: Selects a main battle menu option.

### Custom Tools
- **auto_explore**: Finds and paths to the nearest reachable unseen tile.
- **find_reachable_unseen_tiles**: Identifies reachable unseen tiles adjacent to explored areas.
- **menu_navigator**: Navigates vertical menus by calculating Up/Down presses.
- **plan_path_with_warnings**: Plans a path and warns about nearby moving NPCs.
- **select_move_tool**: Selects a move in battle with correct button presses.

### Custom Agents
- **reality_check_agent**: Verifies my intended action against the game state to prevent hallucinations.
- **puzzle_solver_agent**: Suggests the next logical test for a puzzle based on the scientific method.
- **navigation_strategist**: Provides the next logical navigation step when I'm stuck.
- **party_strategist_agent**: Recommends an optimal party of three for a specific goal.

## Goldenrod Game Corner Puzzle Log
- **Hypothesis:** A hidden switch exists in the room.
- **Failed Test 1:** Interact with the left side of the poster at (11, 1).
- **Failed Test 2:** Interact with the right side of the poster at (12, 1).
- **Hypothesis (from agent):** A slot machine is a hidden switch.
- **Failed Test 3:** Interact with the slot machine at (12, 6). Result: 'You have no coins.'