# I. Rocket Hideout Investigation
- **Objective:** Find the BOSS.
- **Key Clue:** The **LIFT KEY** is needed to operate the elevator.

### Rocket Hideout B3F Maze
- **Status:** In progress.
- **Key Discovery:** I now possess the **LIFT KEY**.
- **Previous Hypotheses (Invalidated):** Earlier theories involved specific NPC interaction sequences. These are now superseded by having the key.
- **Current Hypothesis:** The ROCKET at (27, 13) mentioned the LIFT KEY. Interacting with him while holding the key should progress the puzzle, or I must use the key on an elevator.

# II. Core Directives & Lessons Learned
- **IMMEDIATE DATA MANAGEMENT (CRITICAL):** As an LLM, my thinking is not continuous. All maintenance tasks (tool creation/fixing, agent definition, notepad updates) are the absolute highest priority and **MUST** be performed successfully in the current turn. Deferring tasks is an invalid strategy and a core failure. My recent delay in fixing the `automated_path_navigator` was a major violation of this directive.
- **IMMEDIATE TOOL MAINTENANCE (CRITICAL):** If a custom tool malfunctions, I **MUST** fix it in the immediately following turn. Deferring tool maintenance is a critical failure.
- **TRUST YOUR TOOLS & AGENTS (CRITICAL):** I must trust my tool and agent outputs as the default assumption. Before debugging, I must first verify my own position and assumptions against the game state. A 'no path found' result or an unexpected hypothesis is crucial information, not an error.
- **PROACTIVE AGENT USE (CRITICAL):** I must use my custom agents for the tasks they were designed for. Failing to do so is inefficient and a critical failure.
- **MAP MARKER DISCIPLINE (CRITICAL):** I must mark every warp tile (both entry and exit) with '🚪' and every defeated trainer with '☠️' immediately after the event. Maintaining accurate markers is essential.
- **HYPOTHESIS VETTING (CRITICAL):** Before attempting to test a hypothesis, I must first confirm it is mechanically possible within the game's established rules.

# III. Game Mechanics & Tile Types (Observed)
- **Post-Battle Position Shift:** The player's character may be moved to a nearby tile after a wild battle concludes.
- **Ghost-type Damage:** Ghost-type moves deal SPECIAL damage, not physical.
- **Purified Zone:** A tile area in Pokémon Tower (5F) that fully heals the party upon entry.
- **Inventory Access Bug (Confirmed):** When the player's inventory contains 21 or more unique item stacks, selecting 'ITEM' from the Start Menu incorrectly opens the HM pocket.
- **Celadon City Fly Anomaly:** Using HM Fly from anywhere within Celadon City teleports the player to the Celadon Department Store entrance.
- **Fee Trigger Tile:** A tile that prompts for an entrance fee, even if the player is already inside the area. Paying the fee a second time broke a scripted movement loop.
- **Path Command Spinner Traversal:** The `path` command can sometimes execute a full path plan that includes spinner tiles without being interrupted. This behavior is inconsistent and needs systematic testing.

### Tile Traversal Rules (Comprehensive)
- **`ground` / `grass`:** Standard walkable tiles.
- **`impassable`:** Walls, objects, NPCs, etc. Cannot be entered.
- **`ledge`:** One-way traversal. Can be jumped down from above (Y-1).
- **`cuttable`:** Tree that can be cut with HM Cut. Respawns on map change.
- **`water`:** Crossable using HM Surf.
- `spinner_up/down/left/right`: Forces movement. The `automated_path_navigator` can now model paths that utilize these tiles.
- `spinner_stop`: A tile that halts movement from a spinner.
- `teleport` / `hole` / `ladder_up` / `ladder_down`: Instant warp tiles.
- **`2x1 Warp Tiles`:** Requires a two-step activation: 1. Stand on a warp tile. 2. Press a directional button into the impassable boundary.
- **`Two-Step Elevator`:** A special warp requiring a two-step process: 1. Interact with the control panel to select a floor. 2. Step onto an adjacent warp tile to travel.
- **`steps`:** Allows movement between `ground` and `elevated_ground`.
- **`elevated_ground`:** Walkable ground at a different elevation.
- **`boulder_barrier` / `boulder_switch`:** Switch that clears a barrier when a boulder is pushed onto it.
- **`closed_gate` / `open_gate` / `gate_offscreen`:** Gates that can block paths.

# IV. Archived Investigations
### The Old Amber
- **Objective:** Retrieve the Old Amber from the Pewter Museum of Science.
- **Status:** On hold pending new leads.
- **Confirmed Puzzle Steps:** 1. Lead with Geodude/fossil, speak to Old Man (1F). 2. Speak to Scientist (2F). 3. Interact with Kabutops Fossil (1F).
- **Untested Agent-Generated Hypotheses:** Lead with a Pokémon holding a 'Nugget' or lead with a Porygon and speak to the Gambler NPC.

# V. Completed Quests
- The Ghost of Lavender Town
- The Copycat's Gift
- The Sleeping Snorlax
- Cerulean City Investigation
- Silph Co. Investigation