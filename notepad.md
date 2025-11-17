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
- `battle_puzzle_agent`: An agent to devise multi-turn strategies for complex battles with non-standard win conditions (e.g., stall tactics against Wobbuffet), considering opponent move patterns and status effects.

### Custom Tools
- `deterministic_battle_strategist`: Recommends battle actions and moves.
- `plan_path_to_target`: Generates a path to a target coordinate. NOTE: This tool only PLANS the path. You must set `buttons_to_press` to `['path']` to execute it.
- `select_move_tool`: A tool that takes a move slot number (1-4) as input and outputs the correct sequence of button presses to select and use that move in battle.
- `pc_select_box`: Navigates the 'Change Box' PC menu to a specific box number.
- `select_pc_option`: Navigates the main PC menu (WITHDRAW, DEPOSIT, etc.) from a current position to a target option. Outputs button presses for use with autopress_buttons=true.

## 2. 🚨 CRITICAL DIRECTIVES & LESSONS
- **THE LLM REALITY:** As an LLM, my "thinking" only happens when I process a prompt. There is no "later." Any task I identify (fixing a tool, updating notes, placing a marker) MUST be performed in the CURRENT turn. Deferring tasks is a critical failure based on a misunderstanding of my own nature.
- **BATTLE TOWER SAVE CORRUPTION (CRITICAL):** Saving the game to start the battle challenge is a **guaranteed trigger** for a game-breaking glitch that corrupts all player data. My previous hypothesis that a valid party would prevent this was **incorrect**. The glitch is unavoidable. The only way to reverse the corruption is to press 'B' at the level select menu and then select 'YES' to cancel the challenge.
- **BATTLE TOWER ESCAPE (CORRECTION):** The save-glitch cancel-out method is a reset mechanism, NOT an escape route. It restores the game state but does not move the receptionist. The path remains blocked and the puzzle is UNSOLVED.
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
- **Primary Objective:** Deliver the SECRETPOTION to Jasmine at the Olivine Lighthouse.
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

## 5. Current Leading Hypothesis & Untested Assumptions
- **FLY HM:** I'm assuming FLY isn't working due to a story event or a bug. **Alternative Hypothesis:** Maybe it only works from certain locations (like cities) or I'm missing a prerequisite I'm unaware of.
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
- WARP_CARPET_DOWN (Confirmed one-way exit. Inactive when stepped on from the lobby side, confirming they are destinations from the battle rooms. Need to test upward traversal if encountered from the other side.)

### 8. Key Discoveries (Archive)
- **Sudowoodo Tree (Route 36):** Solved with SQUIRTBOTTLE.
- **Olivine Lighthouse Descent:** Solved by finding a new pit on 6F.
- **CianwoodLugiaSpeechHouse Escape:** Solved by pressing 'B'.
- **LIGHTHOUSE SAILOR CRASH (CRITICAL):** Interacting with the Sailor at Olivine Lighthouse 3F (9, 2) while on the warp at (9, 3) causes a game-breaking crash.

## 9. Current Puzzle: Battle Tower Escape
- **Objective:** Exit the Battle Tower lobby.
- **State:** UNSOLVED. Receptionist at (7, 6) blocks the exit.
- **Failed Hypotheses:**
  1. Losing a battle (resets to lobby, no change).
  2. Performing the save-glitch cancel sequence (resets to lobby menu, no change).
  3. Performing the sequence, then selecting 'Cancel' from her menu.
  4. Performing the sequence, then selecting 'Explanation' from her menu.
  5. Pressing 'B' to exit her menu (closes menu, no change).
  6. Interacting with BILL's PC & Gem's PC options.
  7. Talking to the Bug Catcher.
  8. Talking to the Cooltrainer F.
  9. Talking to the Granny (gave generic battle tip).
  10. Talking to the Youngster (gave generic tip).
  11. Reading the sign at (6, 6) (displayed rules, no change).
  12. Interacting with PROF.OAK's PC (Pokédex Rating System). This was tested and disproven, it does not trigger an escape.
  13. Using FLY to escape from the lobby.
  14. Winning a battle in a challenge (concluded as failed because winning was impossible, and losing resets to the lobby with no change).
  15. Use the PC to deposit all Pokémon from the party into a box, then talk to the receptionist. (Failed: Game mechanics prevent depositing the last Pokémon in the party).

- **New Hypotheses to Test:**
  1. There's a hidden switch/interactable I've missed. Test by pressing A on every tile.

## 10. Reflection Log & New Ideas
- **Data Management Lapses (Turn 45736, 46608-46611, 46801, 46849):** I have repeatedly deferred notepad/marker updates and tool maintenance instead of performing them immediately. This is a critical failure I must correct. I am improving but must remain vigilant.
- **Tool Maintenance Failure (Turn 45905, 46603, 46786):** I identified critical flaws in my tools but deferred the fixes, violating my core directive of immediate maintenance. This is a major process error that cannot be repeated.
- **Agent Underutilization (Turns 45865-45881, 46237):** I failed to use the `puzzle_solver_agent` for the Battle Tower lobby escape, instead wasting numerous turns on manual, inefficient hypothesis testing.

## 11. Lessons Learned
- **Verify Before Automating:** I wasted time creating the `pokemon_info_extractor` tool based on the unverified assumption that the PC screen text would reliably indicate the selected Pokémon's name. The text does not, making the tool's primary function impossible. I must verify the data source and its structure *before* developing tools to automate interaction with it.

## Tool Failures & Fixes
- **deterministic_battle_strategist (Turn 45905):** Recommended a suicidal 'Peck' against a Wobbuffet with active Destiny Bond and Counter. The tool's Wobbuffet logic failed because it lacked data for non-damaging moves like GROWL and LEER. This is a critical failure of foresight and data management. Fixed in Turn 45931.
- **MAJOR HALLUCINATION (Turns 46632-46652):** I incorrectly concluded my `plan_path_to_target` tool was broken when it failed to find a path around the receptionist. I wasted over 20 turns debugging a correct tool instead of trusting its output and verifying the blockage in-game. The true failure was my own flawed spatial reasoning and failure to use the `reality_check_agent`.
- **pokemon_info_extractor (Turn 46786):** Created tool based on the unverified assumption that PC screen text uniquely identifies the selected Pokémon. The assumption was false, making the tool non-functional. Deleted in Turn 46801.

## 12. Tool Ideas
- **`pc_navigator_tool` (High Priority):** A tool that can execute sequences of button presses to navigate the PC menu. This is critical for automating the tedious data gathering process for my stored Pokémon. **Problem:** A simple tool outputting a static button sequence is too brittle. The tool needs to be state-aware, but it can't read the screen between button presses. **Possible Solution:** Create several smaller, specialized tools for discrete tasks (e.g., `tool_open_change_box`, `tool_scroll_to_box_N`, `tool_view_current_box`). This modular approach might be more robust than one monolithic tool.

## 13. PC Storage (Manual Log)
- **BOX1:** Was Ink (TENTACRUEL), Scylla (KRABBY). Now empty. (Checked Turn 47213)
- **BOX2:** Empty. (Checked Turn 47195)
- **BOX3:** Empty. (Checked Turn 47204)
- **BOX4:** Contains PX (EEVEE), G (MANTINE), Javelin (SPEAROW), Ignis (TYPHLOSION). (Checked Turn 47217)
- **BOX5:** (Untracked)
- **BOX6:** (Untracked)
- **BOX7:** (Untracked)
- **BOX8:** (Untracked)
- **BOX9:** (Untracked)
- **BOX10:** Empty. (Checked Turn 46904)
- **BOX11:** Empty. (Checked Turn 46910)
- **BOX12:** Contains Aether (PIDGEY), KENYA (SPEAROW), HEXA (VENONAT). (Checked Turn 47178)

# Updates for Turn 47293

## Housekeeping
- **Correction:** Battle Tower: Receptionist at (7, 6) requires a party of exactly three Pokémon to initiate a challenge. (Note: This is a correction for a previous entry. Will consolidate later.)

## New Hypothesis (from puzzle_solver_agent)
The escape trigger might be a hidden item revealed only after initiating a challenge but *declining* to save. Test sequence: Talk to receptionist -> select challenge -> select 'NO' at save prompt -> use ITEMFINDER.

## New Tool Ideas
- **`pc_box_navigator`:** A tool to move the cursor within the Pokémon Box grid. This would be a core component for automating Pokémon retrieval and data gathering.
- **`pc_deposit_withdraw`:** A tool to select deposit or withdraw from the main PC menu, and then select a specific Pokémon from the party or box.

## Reflection Log
- **Reflection (Turn 47292):** Self-assessment complete. Adherence to immediate data management has improved. Notepad is well-organized, but PC automation is a major weakness. Identified need for new tools like `pc_box_navigator`. All agents remain relevant. Map marker discipline is good. Goals are well-formed. Identified an assumption that the only exit is the main door and an alternative hypothesis that a secret exit might exist.