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
- **Current Location:** Mt. Moon 1F.
- **Strategy:** My manual exploration of Mt. Moon has been highly inefficient and prone to hallucination. I am pivoting to a new strategy as advised by the Overwatch system: I will systematically visit each floor (1F, B1F, B2F) to gather complete map data, and then use my `multi_stage_navigator` agent to compute an optimal path.
- **Correction:** My previous understanding of the path taken was a hallucination. I have arrived on B2F at (26, 10) via a ladder from B1F at (18, 12).
- **Next Step:** Explore the current partition of B2F to continue data collection.

# VII. Archived Investigations

### Mt. Moon Fossil Search (Manual Exploration Phase)
- **Hypothesis:** An unrevived fossil can be obtained from an NPC or item ball in Mt. Moon.
- **Test Results:**
    - **Super Nerd at (13, 9) on B2F:** FAILED. This NPC only provided information about the Cinnabar Lab after being defeated. He did not provide a fossil.
    - **Eastern section of 1F:** FAILED. Explored fully, found no fossils or relevant NPCs.
    - **Hiker at (6, 7) on 1F:** FAILED. The Hiker still blocks the path with the dialogue "Kids like you shouldn't be here!". This path is not currently accessible.
    - **Ladders at (6,6), (18,12) on 1F & (26,10) on B2F:** FAILED. All explored ladders so far have led to isolated, dead-end sections of the lower floors.
- **Next Step:** Systematically explore Mt. Moon B1F.

# VII. Puzzle: Old Amber Retrieval (Completed)
- **Summary:** Solved via a complex, multi-step sequence involving NPC and exhibit interactions across both floors of the Pewter Museum.
- **Key Lesson:** Puzzles in this hack can require non-obvious sequences of interactions that are not hinted at directly. The solution involved speaking to an Old Man with a specific Pokémon (Geodude), interacting with an unrelated exhibit (space shuttle), and then interacting with a fossil exhibit. This highlights the need for creative, systematic hypothesis testing, and confirms the value of the `sequence_puzzle_solver` agent for future complex puzzles.

# VIII. Self-Assessment & Overwatch Critique Takeaways (Turn 231171)
- **CRITICAL - Tool Maintenance:** My highest priority is immediate tool maintenance. I failed by deferring a fix for the `automated_path_navigator`. Faulty tools **MUST** be fixed in the same turn they are discovered.
- **Tool Consolidation:** My battle navigation is split between `select_move_by_slot` and `select_battle_option`. I should consolidate these into a single, more robust tool to reduce errors.
- **Notepad Organization:** Long, archived sections (like the Pewter Museum puzzle) should be condensed to improve readability. This must be done incrementally due to tool limitations.

# IX. Archived Investigations
### TM28 (DIG) - Cerulean Backyard
- **Hypothesis:** TM28 (DIG) is a hidden item in the Cerulean Backyard.
- **Test:** Used ITEMFINDER at (30, 10).
- **Result:** FAILED. ITEMFINDER did not respond.
- **Hypothesis:** TM28 (DIG) appeared as a visible item at (31, 10) after defeating the Rocket Grunt.
- **Test:** Navigated to (32, 10) and visually inspected the tile.
- **Result:** FAILED. No item sprite is present at (31, 10).