# Gem's Brain 🧠

## 1. My Toolkit
### Custom Agents
- `quest_progression_advisor`: Suggests next logical story step.
- `city_exploration_planner`: Creates efficient exploration routes for new cities.
- `world_navigator_agent`: Suggests new regions to investigate when stuck.
- `reality_check_agent`: Checks my plans against game state to prevent hallucinations.
- `puzzle_solver_agent`: Suggests simple, logical tests for puzzles.

### Custom Tools
- `deterministic_battle_strategist`: Recommends battle actions and moves.
- `plan_path_to_target`: Generates a path to a target coordinate. NOTE: This tool only PLANS the path. You must set `buttons_to_press` to `['path']` to execute it.
- `pokemon_nicknamer`: Automates nicknaming Pokémon.
- `stun_npc`: Freezes/unfreezes NPC movement.
- `list_reachable_unseen_tiles`: Lists all reachable unseen tiles from the player's position.

### Tool Development Ideas
- **`systematic_room_searcher`**: A tool that takes room boundaries as input and generates a path to systematically check every wall-adjacent tile for secrets.
- **`battle_move_selector`**: A tool that takes a move name and current cursor position to generate the button presses needed to select it in the battle menu.
- **`dungeon_navigator_agent`**: An agent to plan the optimal path through a multi-floor dungeon to reach a specific goal (e.g., 'the top').
- **`inventory_checker`**: A tool that takes an item name and confirms if it's in the bag, returning true/false and quantity. This would prevent inventory-based hallucinations.

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
- **Route 40/41 Water Route:** Confirmed dead end. Multiple pathfinding attempts to the west failed, blocked by a buoy maze.
- **Battle Tower:** The receptionist at (7, 6) on BattleTower1F stated that only three Pokémon may be entered. This is a confirmed prerequisite.

## 5. Untested Assumptions
- **Azalea Gym:** The statues at the entrance might be switches. Alt: They do nothing, and the puzzle is floor-based or involves trainer interaction order.
- **FLY HM:** I'm assuming FLY isn't working due to a story event or a bug. **Alternative Hypothesis:** Maybe it only works from certain locations (like cities) or I'm missing a prerequisite I'm unaware of.
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
- BOOKSHELF, BUOY, COUNTER, CUT_TREE (needs CUT), HEADBUTT_TREE (needs HEADBUTT), MART_SHELF, PC (interactable), PILLAR, RADIO, ROCK (needs STRENGTH), TOWN_MAP, TV, VOID, WALL, WHIRLPOOL, WINDOW
### Traversable
- FLOOR (standard traversable ground), GRASS, TALL_GRASS (wild encounters)
### Warp Tiles
- DOOR, LADDER, STAIRCASE (two-way)
- PIT, WARP_CARPET_DOWN, WARP_CARPET_RIGHT (one-way)
### Conditional & One-Way
- FLOOR_UP_WALL (ledge, up only)
- LEDGE_HOP_DOWN (down only)
- LEDGE_HOP_LEFT (left only)
- LEDGE_HOP_RIGHT (right only)
- WATER (impassable without SURF)
- WARP_CARPET_DOWN (one-way)

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
- **Olivine Lighthouse 1F Secret Passage:** The Sailor at (8, 2) is not a simple dialogue NPC. 
  - **Hypothesis 1:** Pressing 'A' will trigger a battle. **Result:** Failed. Loops dialogue.
  - **Hypothesis 2:** Pressing 'B' will close the dialogue. **Result:** Failed. Loops dialogue.
  - **Hypothesis 3:** Walking into him will make him move. **Result:** Failed. He is an impassable object.
  - **Conclusion:** The passage is a confirmed dead end.
- **LIGHTHOUSE SAILOR CRASH (CRITICAL):** Previously observed that interacting with the Sailor at Olivine Lighthouse 5F (8, 11) and advancing his dialogue to the battle prompt caused a game-breaking crash. A recent test (Turn 43093) resulted in only dialogue. The crash may be conditional. AVOID BATTLE INTERACTION.
- **LIGHTHOUSE SAILOR CRASH 2 (CRITICAL):** Interacting with the Sailor at Olivine Lighthouse 3F (9, 2) while standing on the warp at (9, 3) causes a game-breaking crash, corrupting all save data. AVOID THIS INTERACTION.

### Olivine Lighthouse Descent Puzzle
- **Objective:** Find path from 6F down to 1F.
- **Current Location:** Solved.
- **Tested Descent Paths from 4F (West Section):**
  - **Path 1 (via 5F):** Taking ladder at 4F (9, 7) to 5F leads back up to 6F or to another ladder at 5F (9, 7) which returns to 4F. This is a loop.
  - **Path 2 (Pit):** Taking pit at 4F (8, 3) leads to an isolated room on 3F (Central). Only exit is a ladder back up to 4F. Confirmed dead end for descent.
  - **Path 3 (Pit):** Taking pit at 4F (9, 3) leads to an isolated room on 3F (Central/East). Only exit is a ladder back up to 4F. Confirmed dead end for descent.
- **Conclusion:** All descent paths from the western section of 4F are confirmed dead ends. The solution involved ascending to 6F and finding a new pit on the eastern side at (16, 5) or (17, 5) to access the eastern sections of the lower floors.
- **Rival's Dialogue (Route 41):** "It was a dark and stormy night… I saw this giant POKéMON flying from the islands. It was scattering feathers from its silver wings."
- **Cianwood City Suicune Event:** Approached Suicune at (10, 14), causing it to flee. Eusine appeared and challenged me to a battle. Defeated Mysticalman Eusine and his Drowzee, Electrode, and Haunter.
- **Whirl Islands Mythical Pokémon:** Requires a 'SILVER WING' to encounter, according to NPCs in Cianwood City.
### CianwoodLugiaSpeechHouse Exit Puzzle (Failed Hypotheses)
- **Hypothesis 1:** Exit via warps (2, 7) or (3, 7) by walking on them. **Result:** Failed. No automatic trigger.
- **Hypothesis 2:** Exit via warps by pressing 'A' on them. **Result:** Failed. Not interactable.
- **Hypothesis 3:** Exit via warps by approaching from a specific direction (up, down, left, right). **Result:** Failed. All directions tested on both warps.
- **Hypothesis 4:** Exit is a secret switch in the bookshelf. **Result:** Failed. Flavor text only.
- **Hypothesis 5:** Exit is triggered by opening the main menu ('Start'). **Result:** Failed.
- **Hypothesis 6:** Exit is triggered by pressing 'Select'. **Result:** Failed. Activated ITEMFINDER.
- **Hypothesis 7:** Re-talking to the Teacher NPC unlocks the exit. **Result:** Failed. Dialogue was identical.
- **Hypothesis 8:** Re-talking to the Twin NPC unlocks the exit. **Result:** Failed. Dialogue was identical.
- **Hypothesis 9:** Re-talking to the Lass NPC unlocks the exit. **Result:** Failed. Dialogue was identical.
- **Hypothesis 10:** Exit is a secret switch in the TV. **Result:** Failed. Flavor text only.
- **Hypothesis 11:** Exit is a secret switch in the Radio. **Result:** Failed. Flavor text only.
- **Hypothesis 12:** Using the ITEMFINDER reveals a hidden exit. **Result:** Failed. No response.
- **Hypothesis 13:** Using an HM move (FLASH) reveals the exit. **Result:** Failed. No Pokémon could learn the move.
- **Hypothesis 14:** Pressing 'B' on the warp tile triggers the exit. **Result:** Failed. No effect.
- **Hypothesis 15:** Using the BICYCLE indoors triggers the exit. **Result:** Failed. Action is not allowed.
- **Hypothesis 16:** Blocking the Lass NPC's path triggers the exit. **Result:** Failed. Her path was altered, but no exit was revealed.
- **Hypothesis 17:** Interacting with the Lass while her path is blocked triggers the exit. **Result:** Failed. Dialogue was identical.
- **Hypothesis 18:** Selecting 'EXIT' from the main menu triggers the exit. **Result:** Failed. It only closed the menu.
- **Hypothesis 19:** Changing the lead Pokémon unlocks the exit. **Result:** Failed. No change.
- **Hypothesis 20:** Using the SQUIRTBOTTLE on the warp tile. **Result:** Failed. Text said 'But nothing happened…'
- **Hypothesis 21:** Tuning the radio via the PokéGear interface. **Result:** Failed. No button combination worked to change the station.
- **Hypothesis 22:** Interacting with the physical radio while the PokéGear radio was active. **Result:** Failed. Played standard broadcast.
- **Hypothesis 23:** Interacting with the Town Map is a secret switch. **Result:** Failed. Flavor text only.

### CianwoodLugiaSpeechHouse Exit Puzzle (Untested Hypotheses)
- **Hypothesis 24:** Stand on a warp tile AND select 'EXIT' from the main menu.
- **Hypothesis 25:** Use an HM move (STRENGTH) inside the house.

## 9. Lessons from Overwatch Critiques
- **Immediate Maintenance (Turn 43741):** Failed to immediately retry a failed `notepad_edit` `overwrite` action. All data and tool maintenance MUST be done in the same turn a need is identified.
- **Incomplete Tool List (Turn 43741):** My list of built-in tools is missing `delete_tool` and `select_battle_option`. I must update this.
### CianwoodLugiaSpeechHouse Exit Puzzle (In Progress)
- **The Problem:** The player is trapped on tile (3, 1), and all standard inputs are disabled, preventing exit via the warps at (2, 7) and (3, 7).
- **Discovery:** Pressing 'Up' while on tile (3, 1) and facing the Town Map at (3, 0) is a trigger. It changes the background screen but does not solve the puzzle on its own.
- **Next Hypothesis:** The trigger may have activated the exit warps. The next step is to attempt to move to one of the warp tiles.
- **Hypothesis 26:** Pressing 'Start' after triggering the map view will open the main menu. **Result:** Failed. No effect.
- **Hypothesis 27:** Pressing 'A' on the Town Map after triggering the map view will cause an interaction. **Result:** Failed. No effect.