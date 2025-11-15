# Gem's Brain 🧠

## 1. My Custom Toolkit
### Agents
- **`quest_progression_advisor`:** Suggests next logical story step.
- **`city_exploration_planner`:** Creates efficient exploration routes for new cities.
- **`world_navigator_agent`:** Suggests new regions to investigate when stuck.
- **`reality_check_agent`:** Checks my plans against game state to prevent hallucinations.
- **`puzzle_solver_agent`:** Suggests simple, logical tests for puzzles.

### Tools
- **`deterministic_battle_strategist`:** Recommends battle actions and moves.
- **`path_and_execute_v3`:** Finds and executes a path to a target coordinate.
- **`plan_next_exploration_step`:** Finds the closest unseen tile to explore.
- **`pokemon_nicknamer`:** Automates nicknaming Pokémon.
- **`select_battle_option`:** Selects main battle menu options.
- **`stun_npc`:** Freezes/unfreezes NPC movement.
- **`define_tool`:** Creates new reusable tools.
- **`delete_agent`:** Deletes custom agents.

## 2. 🚨 CRITICAL DIRECTIVES & LESSONS
- **IMMEDIATE MAINTENANCE:** All data management (notepad, markers) and tool/agent fixes MUST be done in the same turn a new discovery or bug is found. There is no 'later'.
- **REALITY CHECKS:** My internal sense of location is unreliable. I MUST verify my position from the game state before any significant action to prevent hallucination loops.
- **COORDINATE SYSTEM:** Map data is 0-indexed (`0 <= coordinate < dimension`). Pathfinding tools MUST use this logic.
- **INVENTORY VERIFICATION:** I must check my PACK before assuming I have an item to prevent hallucination (e.g., the nonexistent ESCAPE ROPE incident).
- **TEXT BOXES:** If 'A' fails to advance text, the next hypothesis is to try 'B'.
- **TOOL MISUSE:** `autopress_buttons=true` is ONLY for tools that output button strings, not coordinates or decisions.
- **ITEM MANAGEMENT:** Taking a held item with a full bag destroys it. The only safe way to free a slot is to have a Pokémon hold an item.
- **DIG GLITCH (CRITICAL):** Using DIG as a field move in the Olivine Lighthouse dead-end room causes a game-breaking glitch, corrupting all player data. Avoid using DIG as a field move until further testing.

## 3. Main Quest & Active Leads
- **Primary Objective:** Find the 'special medicine' to heal the sick Ampharos at the top of the Olivine Lighthouse.
- **Legendary Beasts:** Suicune, Raikou, and Entei have been awakened in the Burned Tower. The Sage in the Tin Tower has asked me not to enter.
- **Sudowoodo Tree (Route 36):** The path is blocked by a strange tree. I have the SQUIRTBOTTLE. The puzzle may need to be solved again.
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

## 5. Untested Assumptions
- **Azalea Gym:** The statues at the entrance might be switches. Alt: They do nothing, and the puzzle is floor-based or involves trainer interaction order.

## 6. Confirmed System Mechanics
- **Respawning Obstacles:** HM-cleared obstacles (like CUT_TREE) respawn upon re-entering a map.
- **HM Move Permanence:** HM moves cannot be forgotten through normal means.
- **Multi-Press Dialogue:** Some NPCs require pressing 'A' multiple times to advance text.
- **Phone List Limit:** The phone list can become full.
- **`stun_npc` Tool:** Freezes an NPC's movement but does not make them traversable.
- **Evolution via Trade:** MACHOKE, KADABRA, HAUNTER, and GRAVELER evolve by trading.
- **Defeated Trainers as Obstacles:** Trainers in the Azalea Gym remain impassable after defeat.

### 7. Tile Mechanics
### Impassable
- BOOKSHELF, BUOY, COUNTER, CUT_TREE (needs CUT), HEADBUTT_TREE (needs HEADBUTT), MART_SHELF, PC (interactable), PILLAR, RADIO, ROCK (needs STRENGTH), TOWN_MAP, TV, VOID, WALL, WHIRLPOOL, WINDOW
### Traversable
- FLOOR, GRASS, TALL_GRASS (wild encounters)
### Warp Tiles
- DOOR, LADDER, STAIRCASE (two-way)
- PIT, WARP_CARPET_DOWN, WARP_CARPET_RIGHT (one-way)
### Conditional & One-Way
- FLOOR_UP_WALL (ledge, up only)
- LEDGE_HOP_DOWN (down only)
- LEDGE_HOP_LEFT (left only)
- LEDGE_HOP_RIGHT (right only)
- WATER (impassable without SURF)

## 8. Journey Log & Puzzle Solutions
### Procedural Rules & Learnings
- **Warp Marking:** Mark new warps as 'Unverified'. After use, update both sides with the correct "To <Map Name> (<x>, <y>)" label.
- **Reality Check:** Always verify my position from the game state before any significant action to prevent hallucination loops.
- **Immediate Tile Testing:** Upon entering a new area, immediately test and document any unverified tile types.

### Key Discoveries & Solved Puzzles
- **Goldenrod Dept. Store:** A bargain sale is happening now (per Todd's call).
- **Route 41 (WHIRL ISLANDS):** Interior is 'pitch-black' (needs FLASH).
- **Cianwood City:** Received SHUCKIE from a Rocker whose other Pokémon was stolen.
- **Route 30 Ledge:** Confirmed one-way (down only).

# Tool Development Log

# Procedural Rules (From Overwatch Critique)
- **Reality Check:** Before any significant navigation or map-changing action, I MUST use my `reality_check_agent` to verify my position and assumptions against the game state.
- **Immediate Tile Testing:** Upon entering a new area, I must immediately test and document any unverified tile types before proceeding with exploration.

- **Inventory Hallucination (CRITICAL):** During turn 40942, I attempted to use an ESCAPE ROPE that I did not possess. This indicates a severe failure to verify my inventory before forming a plan. I must always check my PACK before assuming I have a specific item.

- **PIT:** A one-way warp tile, activated by moving onto it.
- **Olivine Lighthouse 3F (Western Section):** Confirmed dead end for ascending. The Youngster NPC at (3, 9) confirms the path is blocked.
- Phone Call (Rematch): JACK (SCHOOLBOY) wants a rematch in NATIONAL PARK and gave a tip about DEFENSE CURL + ROLLOUT.
- Phone Call (Rematch): JACK (SCHOOLBOY) wants a rematch in NATIONAL PARK and gave a tip about DEFENSE CURL + ROLLOUT.

# Cianwood Pharmacy Log
- Tile Testing Complete: Confirmed BOOKSHELF, TV, TOWN_MAP, RADIO, and WINDOW are all impassable.

## 5. Agent/Tool Development Ideas (New)
- **`phone_call_summarizer` Agent:** Parses phone call dialogue to extract key information (rematches, items) and suggest notepad updates.

# Route 36 Sudowoodo Puzzle Log (Solved)
- Hypothesis 1 (Failed): Using SQUIRTBOTTLE on the Sudowoodo at (35, 9) from below (35, 10) resulted in the message "But nothing happened...".
- Unexpected Solution: After the failed attempt, moving to the adjacent left tile (34, 9) and then turning to face the Sudowoodo's location (pressing Right) caused the Sudowoodo to disappear, clearing the path. The exact trigger is unclear, but this sequence of actions solved the puzzle.

## Special Events & Swarms
- **Hiker Anthony:** Dunsparce swarm in Dark Cave.

## Moomoo Farm Quest Mechanics
- The sick Miltank requires a specific item named 'BERRY'. Other named berries like 'BITTER BERRY' or 'MINT BERRY' do not work for this quest. (Confirmed in Moomoo Farm Barn)

# Self-Assessment Action Items (Turn 42181)
- **Task:** Test unverified tile types (MART_SHELF, PILLAR) at the next opportunity (e.g., in the Olivine Mart) to confirm their traversability.

# Olivine Good Rod House Puzzle (Solved)
- **Problem:** Trapped in the house. The 'WARP_CARPET_DOWN' at the exit did not activate through any standard movement (from above, side) or interaction ('A', 'B', 'Select').
- **Hypothesis (Falsified):** Re-interacting with the Fishing Guru would unlock the exit.
- **Solution:** Opening the main menu with 'Start' and then pressing 'Down' on the D-pad triggered the exit warp. This confirms the existence of non-obvious, menu-based puzzle solutions.

# Olivine Lighthouse 2F Puzzle
- The warp tile at (17, 11) does not activate when stepped on from the left or from below. Its function is currently unknown.

- **VOID:**

# Olivine Lighthouse 1F Dead-End Puzzle (Solved)
- **Problem:** Trapped in a room after falling through a pit. All simple interactions (menu tricks, talking to NPC, stepping on warps) failed.
- **Hypothesis (Confirmed):** The move DIG can be used as an escape rope to exit certain indoor areas.
- **Solution:** Taught TM28 DIG to a Pokémon and used the move from the party menu to warp back to the entrance of the map (Olivine City).

# Glitch World Escape Log
- **CRITICAL BUG (GAME-BREAKING):** Using DIG in the Olivine Lighthouse 1F dead-end room (accessed by falling through a pit) teleports the player to a glitch map (ID 18_247) and corrupts all player data (Pokémon, inventory, money). This is a potential soft-lock. Hypothesis for escape: Use FLY.