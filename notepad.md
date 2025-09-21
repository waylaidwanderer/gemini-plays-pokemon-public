# I. Core Directives & Lessons Learned
- **IMMEDIATE DATA & TOOL MAINTENANCE (CRITICAL):** As an LLM, my thinking is not continuous. All maintenance tasks (tool creation/fixing, agent definition, notepad updates) are the absolute highest priority and **MUST** be performed successfully in the current turn. Deferring tasks is an invalid strategy.
- **TRUST YOUR TOOLS & AGENTS (CRITICAL):** I must trust my tool and agent outputs as the default assumption. Before debugging, I must first verify my own position and assumptions against the game state.
- **VERIFY POSITION (CRITICAL):** I have a history of position hallucinations. I **MUST** check my position in the Game State Information at the start of every turn before forming a plan.
- **MAP MARKER DISCIPLINE (CRITICAL):** I must mark every warp tile (both entry and exit) with '🚪' and every defeated trainer with '☠️' immediately.
- **HYPOTHESIS VETTING (CRITICAL):** Before attempting to test a hypothesis, I must first confirm it is mechanically possible within the game's established rules.
- **Agent Escalation Protocol:** If manual puzzle attempts fail repeatedly or direct navigation is impossible in a complex area, I MUST escalate to my specialized agents (`sequence_puzzle_solver`, `multi_stage_navigator`) before continuing with manual attempts.

# II. Game Mechanics & Tile Types (Observed)
- **Post-Battle Position Shift:** Player may be moved after a wild battle.
- **Ghost-type Damage:** Ghost-type moves deal SPECIAL damage.
- **Purified Zone:** A healing area in Pokémon Tower (5F).
- **Inventory Access Bug (Confirmed):** With 21+ unique item stacks, 'ITEM' from the Start Menu opens the HM pocket.
- **Celadon City Fly Anomaly:** Using HM Fly from anywhere within Celadon City teleports the player to the Celadon Department Store entrance.
- **Fee Trigger Tile:** A tile that prompts for an entrance fee, even if already inside. Paying a second time broke a scripted loop.
- **Fossil Trap:** Interacting with the fossil exhibits in the Pewter Museum of Science can trigger a trap that temporarily places the player on an impassable tile. This trap can be escaped by pressing the 'B' button.

### Tile Traversal Rules (Comprehensive)
- `ground` / `grass`: Standard walkable tiles.
- `impassable`: Walls, objects, NPCs, etc. Cannot be entered.
- `ledge`: One-way traversal. Can be jumped down from above (Y-1).
- `cuttable`: Tree that can be cut with HM Cut. Respawns on map change.
- `water`: Crossable using HM Surf.
- `spinner_*`: Forces movement. The `automated_path_navigator` can model paths that utilize these tiles.
- `spinner_stop`: A tile that halts movement from a spinner.
- `teleport` / `hole` / `ladder_*`: Instant warp tiles.
- `2x1/1x2 Warp Tiles`: Requires a two-step activation (stand on tile, press into boundary).
- `Two-Step Elevator`: Special warp (interact with panel, step onto adjacent warp).
- `steps`: Allows movement between `ground` and `elevated_ground`.
- `boulder_barrier` / `boulder_switch`: Switch that clears a barrier when a boulder is pushed onto it.
- `gate_*`: Gates that can block paths.

# III. Completed Quests
- The Ghost of Lavender Town
- The Copycat's Gift
- The Sleeping Snorlax
- Cerulean City Investigation
- Silph Co. Investigation
- Rocket Hideout Investigation
- The Old Amber Retrieval

# IV. Key NPCs & Blockers
- Mt. Moon Rocket Grunt (30, 12): Confirmed he requires an unrevived fossil to pass. Dialogue: "If you find a fossil, give it to me and scram!"

# V. Agent & Tool Development Ideas
- **Lost Item Investigator Agent:** An agent that takes an objective (e.g., 'Find TM28') and a list of clues, then proposes a ranked sequence of locations to search and actions to perform.

# VI. Current Investigation: Unrevived Fossil
- **Objective:** Obtain an unrevived fossil to give to the Rocket Grunt on Mt. Moon B2F.
- **Current Location:** Mt. Moon B2F (Dead End).
- **Strategy:** My manual exploration of Mt. Moon has been highly inefficient due to its partitioned, multi-floor layout. I am pivoting to a new strategy: I will systematically visit each floor (1F, B1F, B2F) to gather complete map data, and then use my `multi_stage_navigator` agent to compute an optimal path to the Rocket Grunt at (30, 12) on B2F.
- **Next Step:** Escape the current dead-end area on B2F by taking the ladder at (26, 10) back to B1F.

# VII. Archived Investigations

### Mt. Moon Fossil Search (Manual Exploration Phase)
- **Hypothesis:** An unrevived fossil can be obtained from an NPC or item ball in Mt. Moon.
- **Test Results:**
    - **Super Nerd at (13, 9) on B2F:** FAILED. This NPC only provided information about the Cinnabar Lab after being defeated. He did not provide a fossil.
    - **Eastern section of 1F:** FAILED. Explored fully, found no fossils or relevant NPCs.
    - **Hiker at (6, 7) on 1F:** FAILED. The Hiker still blocks the path with the dialogue "Kids like you shouldn't be here!". This path is not currently accessible.
    - **Ladders at (6,6), (18,12) on 1F & (26,10) on B2F:** FAILED. All explored ladders so far have led to isolated, dead-end sections of the lower floors.
- **Next Step:** Systematically explore Mt. Moon B1F.

# VII. Puzzle: Old Amber Retrieval (ARCHIVED - COMPLETED)
- **Objective:** Retrieve the Old Amber from the Pewter Museum of Science.
- **Status:** STUCK. The path at (13, 5) remains blocked by a Scientist.
- **Failed Hypotheses (Manual & Agent - Exhaustive List):**
    - **Sequence (Misinterpreted as a solution):** The sequence of (1. Lead with fossil, talk to Old Man -> 2. Talk to Scientist (2F) -> 3. Interact with Space Shuttle -> 4. Interact with Kabutops Fossil) was previously thought to be the solution based on a misinterpretation of event summaries. The game state confirms the Scientist at (13, 5) did NOT move. This sequence is confirmed to be a **FAILURE**.
    - Spoke to the 'Old Man' (2, 5) after the initial puzzle sequence. (Result: 'magnificent fossil!')
    - Interact with 'AerodactylFossil' (3, 4), then spoke to the 'Old Man' (2, 5). (Result: 'magnificent fossil!')
    - Interact with 'KabutopsFossil' (3, 7), then 'AerodactylFossil' (3, 4), then spoke to the 'Old Man' (2, 5). (Result: 'magnificent fossil!')
    - Lead with a revived Aerodactyl and spoke to the 'Old Man' (2, 5). (Result: 'magnificent fossil!')
    - Use 'Cut' on 'AerodactylFossil' (3, 4). (Result: "There isn't anything to CUT!")
    - Path at (12, 5) is open after puzzle sequence. (Result: Path is blocked by a wall, not the Scientist).
    - Sequence: Lead with Pikachu -> interact with Pikachu NPC -> interact with KabutopsFossil -> interact with AerodactylFossil -> speak to the Old Man. (Result: Old Man turned, but dialogue unchanged and path remains blocked).
    - Lead with a Water-type Pokémon and interact with the KabutopsFossil. (Result: Triggered the standard fossil trap, no change.)
    - Interact with the KabutopsFossil, then speak to the MUSEUM1F_GAMBLER. (Result: Standard 'magnificent fossil!' dialogue, no change).
    - Sequence: Interact with KabutopsFossil -> (Pikachu NPC gone) -> interact with AerodactylFossil. (Result: Triggered standard fossil traps, no change in the blocked path.)
    - Stand on the tile to the left of the 'MUSEUM1F_GAMBLER' (at (1, 5)) to make him face the fossils. While he is facing left, interact with the 'AerodactylFossil' at (3, 4). (Result: Gambler turned UP, not left. Interacting with the fossil was a standard trap. No change.)
    - Use the Itemfinder on the empty floor tiles surrounding the fossils. (Result: 'Nope! ITEMFINDER isn't responding.')
    - Interact with the 'MUSEUM1F_GAMBLER' at (2, 5) while having the Coin Case item in your inventory. (Result: 'magnificent fossil!')

- **New Hypotheses (To Be Tested):**
    - **Hypothesis 1 (Agent - FAILED):** Sequence: AerodactylFossil -> KabutopsFossil -> Gambler.
    - **Hypothesis 2 (Agent - FAILED):** Stand at (3, 5) and talk to Gambler.
    - **Hypothesis 3 (Agent - Invalid):** Interact with fossils from the west side (tiles are impassable).
    - **Hypothesis 4 (Agent - FAILED):** Interact with KabutopsFossil x2, AerodactylFossil x1, then talk to Gambler.
- **Hypothesis 5 (Agent - New):** Stand on the tile directly above the 'MUSEUM1F_GAMBLER' at coordinates (2, 4) and then interact with him.
- **Hypothesis 6 (Agent - FAILED):** Step 1: Interact with the 'KabutopsFossil' at coordinates (3, 7) exactly seven times in a row. Step 2: Immediately speak to the 'MUSEUM1F_GAMBLER' at (2, 5). (Result: Interacting with the fossil repeatedly only triggers the trap.)
- **Hypothesis 7 (Agent - FAILED):** Step 1: Speak to the 'MUSEUM1F_GAMBLER' at (2, 5). Step 2: Exit the Pewter Museum of Science entirely. Step 3: Re-enter the museum and immediately speak to the 'MUSEUM1F_GAMBLER' again without interacting with anything else. (Result: Standard 'magnificent fossil!' dialogue, no change).
- **Hypothesis 8 (Agent - FAILED / Untestable):** While having an unrevived fossil item (e.g., Dome Fossil or Helix Fossil) in your inventory, stand in front of the 'MUSEUM1F_GAMBLER' at (2, 5) and 'Use' the fossil item from the bag menu. (Note: PC item storage checked, no unrevived fossils found).
- **Hypothesis 9 (Agent - FAILED):** Stand on the tile at (3, 5), to the right of the fossil display. First, face UP towards the 'AerodactylFossil'. Then, without leaving the tile, turn to face LEFT and initiate conversation with the 'MUSEUM1F_GAMBLER' at (2, 5). (Result: 'magnificent fossil!' dialogue, no change).

# VIII. Self-Assessment Takeaways (Turn 230965)
- **Agent Utilization:** I need to actively look for opportunities to use my `multi_stage_navigator` and `sequence_puzzle_solver` agents to test their effectiveness.
- **Fossil Quest - Backup Plan:** If a systematic search of Mt. Moon yields no new fossil items, my backup plan is to test if the Rocket Grunt will accept a *revived* fossil, as my previous tests only involved unrevived or renamed Pokémon.
- **Automated Path Navigator - Ledge Logic:** The tool failed at turn 230960 by attempting to move up into a ledge. It needs to be refined to correctly interpret and navigate around ledges from all directions, not just when jumping down.

# IX. Archived Investigations
### TM28 (DIG) - Cerulean Backyard
- **Hypothesis:** TM28 (DIG) is a hidden item in the Cerulean Backyard.
- **Test:** Used ITEMFINDER at (30, 10).
- **Result:** FAILED. ITEMFINDER did not respond.
- **Hypothesis:** TM28 (DIG) appeared as a visible item at (31, 10) after defeating the Rocket Grunt.
- **Test:** Navigated to (32, 10) and visually inspected the tile.
- **Result:** FAILED. No item sprite is present at (31, 10).