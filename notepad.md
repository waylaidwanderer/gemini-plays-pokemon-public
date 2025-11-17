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
- `reality_check_agent`: Checks my plans against game state to prevent hallucinations.
- `puzzle_solver_agent`: Suggests simple, logical tests for puzzles.
- `navigation_strategist`: A unified navigation advisor.
- `party_strategist_agent`: Analyzes the player's stored Pokémon and a given strategic goal to recommend an optimal party of three.

### Custom Tools

- `plan_path_to_target`: Generates a path to a target coordinate.
- `select_move_tool`: A tool that takes a move slot number (1-4) as input and outputs the correct sequence of button presses to select and use that move in battle.
- `pc_navigator`: A unified tool to navigate the PC.
- `systematic_search_tool`: Finds the next logical tile to check in a systematic search.

## 2. 🚨 CRITICAL DIRECTIVES & LESSONS
- **PRINCIPLE OF SIMPLICITY (BATTLE TOWER):** After 40+ complex failed hypotheses, the solution was simply walking onto the exit warp carpet. I assumed it was a one-way entrance without ever testing it. This is a catastrophic failure of the scientific method. ALWAYS test the simplest, most fundamental assumptions first before escalating to complex theories.
- **THE LLM REALITY:** As an LLM, my "thinking" only happens when I process a prompt. There is no "later." Any task I identify (fixing a tool, updating notes, placing a marker) MUST be performed in the CURRENT turn. Deferring tasks is a critical failure based on a misunderstanding of my own nature.
- **BATTLE TOWER SAVE CORRUPTION (CRITICAL):** Saving the game to start the battle challenge is a **guaranteed trigger** for a game-breaking glitch that corrupts all player data. My previous hypothesis that a valid party would prevent this was **incorrect**. The glitch is unavoidable. The only way to reverse the corruption is to press 'B' at the level select menu and then select 'YES' to cancel the challenge.
- **BATTLE TOWER ESCAPE (CORRECTION):** The save-glitch cancel-out method is a reset mechanism, NOT an escape route. It restores the game state but does not move the receptionist. The path remains blocked and the puzzle is UNSOLVED.
- **IMMEDIATE MAINTENANCE:** All data management (notepad, markers) and tool/agent fixes MUST be done in the same turn a new discovery or bug is found. There is no 'later'.

- **PATH EXECUTION:** Calling `plan_path_to_target` only generates a path. I MUST set `buttons_to_press` to `["path"]` to actually move, otherwise I will hallucinate my position.
- **REALITY CHECKS:** My internal sense of location is unreliable. I MUST verify my position from the game state before any significant action to prevent hallucination loops.
- **COORDINATE SYSTEM:** Map data is 0-indexed (`0 <= coordinate < dimension`). Pathfinding tools MUST use this logic.
- **INVENTORY VERIFICATION:** I must check my PACK before assuming I have an item to prevent hallucination (e.g., the nonexistent ESCAPE ROPE incident).
- **TEXT BOXES:** Pressing 'B' is not a universal solution for closing text boxes where 'A' fails (e.g., Sailor in Olivine Lighthouse), but it has been confirmed to work for breaking dialogue loops (e.g., Rival on Route 41). This should be tested as an alternative when 'A' is unresponsive.
- **TOOL MISUSE:** `autopress_buttons=true` is ONLY for tools that output button strings, not coordinates or decisions.
- **ITEM MANAGEMENT:** Taking a held item with a full bag destroys it. The only safe way to free a slot is to have a Pokémon hold an item.
- **DIG GLITCH (CRITICAL):** Using DIG as a field move in the Olivine Lighthouse dead-end room causes a game-breaking glitch, corrupting all player data. Avoid using DIG as a field move until further testing.

## 3. Main Quest & Active Leads
- **Primary Objective:** Challenge the Olivine City Gym and defeat Gym Leader Jasmine.
- **Dark Cave Lead:** Received mail on the Battle Tower PC from 'RANDY'. Message: 'DARK CAVE leads to another road.' This confirms it's a through-route.
- **Legendary Beasts:** Suicune, Raikou, and Entei have been awakened in the Burned Tower. The Sage in the Tin Tower has asked me not to enter.
- **Stolen Pokémon (Cianwood):** A Rocker's Pokémon was stolen. I am currently safekeeping his SHUCKIE.
- **Moomoo Farm:** The Miltank is sick and requires a specific item named 'BERRY'. Other named berries do not work.

### Phone Contacts
- **DANA (LASS):** Route 38 (Rematch).
- **GINA (PICNICKER):** Route 34 (Rematch requested again).
- **HUEY (SAILOR):** OLIVINE LIGHTHOUSE (Rematch).
- **ANTHONY (HIKER):** Route 33 (Rematch). Chatted about MACHOP & GEODUDE.
- **JACK (SCHOOLBOY):** NATIONAL PARK (Rematch). Chatted about VOLTORB.
- **ALAN (SCHOOLBOY):** Route 36 (Rematch). Chatted about beating a Ledyba.

## Special Events & Swarms
- **Hiker Anthony:** Dunsparce swarm in Dark Cave.

## 4. World State & Blocked Paths
- **Tin Tower:** Path blocked by a Sage (legendary beasts awakened).
- **Route 41 (WHIRL ISLANDS):** Interior is 'pitch-black' (needs FLASH); WHIRLPOOL tiles are impassable.
- **Route 42:** Path to Mahogany Town blocked by water (needs SURF).
- **Goldenrod Underground:** Locked door at (18, 6) is unsolved.
- **Route 40/41 Water Route:** Confirmed dead end. Multiple pathfinding attempts to the west failed, blocked by a buoy maze.

## 5. Current Leading Hypothesis & Untested Assumptions
- **Lighthouse Exit:** Current assumption is the only way out is floor-by-floor descent. **Alternative Hypothesis:** A pit might drop me multiple floors or to the exit. **Test:** Investigate all pits encountered during descent.
- **FLY HM:** Current assumption is it's story-disabled. **Alternative Hypothesis:** It only works in open-air locations, not indoors. **Test:** Attempt to use FLY immediately upon exiting the lighthouse.
- **Azalea Gym:** The statues at the entrance might be switches. Alt: They do nothing, and the puzzle is floor-based or involves trainer interaction order.

## 6. Confirmed System Mechanics
- **Respawning Obstacles:** HM-cleared obstacles (like CUT_TREE) respawn upon re-entering a map.
- **HM Move Permanence:** HM moves cannot be forgotten through normal means.
- **Multi-Press Dialogue:** Some NPCs require pressing 'A' multiple times to advance text.
- **Phone List Limit:** The phone list can become full.
- **`stun_npc` Tool:** Freezes an NPC's movement but does not make them traversable. CRITICAL: This tool only works on NPCs that are currently visible on the screen ('live objects').
- **Evolution via Trade:** MACHOKE, KADABRA, HAUNTER, and GRAVELER evolve by trading.
- **Defeated Trainers as Obstacles:** Trainers in the Azalea Gym remain impassable after defeat.
- **STRENGTH HM:** The move STRENGTH is used to *push* boulders, not break them. The boulder requires an empty space on the opposite side to be moved.

## 7. Tile Mechanics
### Impassable
- BOOKSHELF, BUOY, COUNTER, CUT_TREE (needs CUT), HEADBUTT_TREE (needs HEADBUTT), MART_SHELF, PC (interactable), PILLAR, RADIO, ROCK (needs STRENGTH), TV, VOID, WALL, WHIRLPOOL, WINDOW
- **TOWN_MAP:** Impassable. Interactable from the tile below it (3,1), which displays a full-screen map of the Whirl Islands. This view is cancelled by any subsequent directional input.
### Traversable
- FLOOR (standard traversable ground), GRASS, TALL_GRASS (wild encounters), unknown (traversable)
### Warp Tiles
- DOOR, LADDER, STAIRCASE (two-way)
- PIT (one-way)
- WARP_CARPET_RIGHT (one-way)
- WARP_CARPET_DOWN (two-way)
### Conditional & One-Way
- FLOOR_UP_WALL (ledge, down only)
- LEDGE_HOP_DOWN (down only)
- LEDGE_HOP_LEFT (left only)
- LEDGE_HOP_RIGHT (right only)
- WATER (impassable without SURF)

## 8. Reflection Log & New Ideas
- **Data Management Lapses (Turn 45736, 46608-46611, 46801, 46849, 47587-47604, 47631):** I have repeatedly deferred or failed at notepad/marker updates and tool maintenance instead of performing them immediately. This is a critical failure I must correct. I am improving but must remain vigilant.
- **Tool Maintenance Failure (Turn 45905, 46603, 46786):** I identified critical flaws in my tools but deferred the fixes, violating my core directive of immediate maintenance. This is a major process error that cannot be repeated.
- **Agent Underutilization (Turns 45865-45881, 46237):** I failed to use the `puzzle_solver_agent` for the Battle Tower lobby escape, instead wasting numerous turns on manual, inefficient hypothesis testing.
- **Position Hallucination (Turn 48018, 48435):** I have failed to verify my position, leading to failed actions and system warnings. This reinforces the need for constant reality checks against the game state.
- **Goal Flexibility Failure (Turn 48125):** I have been hyper-focused on solving the Battle Tower escape puzzle, violating the core directive to pivot to a new goal when progress stalls. If my current systematic wall search fails, I MUST try a different approach or use the `puzzle_solver_agent` to generate new hypotheses.
- **Tool Creation Success (Turn 48021, 48101):** I successfully identified a repetitive manual task (checking walls) and automated it by creating the `wall_checker_tool` and `systematic_search_tool`, which is a correct application of my directives.
- **New Tool Idea: `persistent_path_executor`**: A tool that can handle moving NPCs by automatically re-planning its path if blocked. This would streamline navigation in areas with many moving obstacles.

## 9. Lessons Learned
- **Verify Before Automating:** I wasted time creating the `pokemon_info_extractor` tool based on the unverified assumption that the PC screen text would reliably indicate the selected Pokémon's name. The text does not, making the tool's primary function impossible. I must verify the data source and its structure *before* developing tools to automate interaction with it.
- **MAJOR HALLUCINATION (Turns 46632-46652):** I incorrectly concluded my `plan_path_to_target` tool was broken when it failed to find a path around the receptionist. I wasted over 20 turns debugging a correct tool instead of trusting its output and verifying the blockage in-game. The true failure was my own flawed spatial reasoning and failure to use the `reality_check_agent`.

## 10. Archived Puzzle Logs
### Battle Tower Escape: SOLVED
- **Solution:** The warp carpets at (7, 9) and (8, 9) were two-way warps. The solution was to simply walk onto them. My core assumption that they were one-way entrances was never tested and was incorrect.
- **Failed Hypotheses (41 total):**