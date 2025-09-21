# I. The Old Amber Investigation
- **Objective:** Retrieve the Old Amber from the Pewter Museum of Science.
- **Status:** In progress. Next step is to travel to Pewter City.
- **Confirmed Puzzle Steps:** 1. Lead with Geodude/fossil, speak to Old Man (1F). 2. Speak to Scientist (2F). 3. Interact with Kabutops Fossil (1F).
- **Untested Agent-Generated Hypotheses:** Lead with a Pokémon holding a 'Nugget' or lead with a Porygon and speak to the Gambler NPC.

# II. Core Directives & Lessons Learned
- **IMMEDIATE DATA MANAGEMENT (CRITICAL):** As an LLM, my thinking is not continuous. All maintenance tasks (tool creation/fixing, agent definition, notepad updates) are the absolute highest priority and **MUST** be performed successfully in the current turn. Deferring tasks is an invalid strategy and a core failure.
- **IMMEDIATE TOOL MAINTENANCE (CRITICAL):** If a custom tool malfunctions, I **MUST** fix it in the immediately following turn.
- **TRUST YOUR TOOLS & AGENTS (CRITICAL):** I must trust my tool and agent outputs as the default assumption. Before debugging, I must first verify my own position and assumptions against the game state.
- **PROACTIVE AGENT USE (CRITICAL):** I must use my custom agents for the tasks they were designed for.
- **MAP MARKER DISCIPLINE (CRITICAL):** I must mark every warp tile (both entry and exit) with '🚪' and every defeated trainer with '☠️' immediately.
- **HYPOTHESIS VETTING (CRITICAL):** Before attempting to test a hypothesis, I must first confirm it is mechanically possible within the game's established rules.

# III. Game Mechanics & Tile Types (Observed)
- **Post-Battle Position Shift:** Player may be moved after a wild battle.
- **Ghost-type Damage:** Ghost-type moves deal SPECIAL damage.
- **Purified Zone:** A tile area in Pokémon Tower (5F) that fully heals the party.
- **Inventory Access Bug (Confirmed):** With 21+ unique item stacks, 'ITEM' from the Start Menu opens the HM pocket.
- **Celadon City Fly Anomaly:** Using HM Fly from anywhere within Celadon City teleports the player to the Celadon Department Store entrance.
- **Fee Trigger Tile:** A tile that prompts for an entrance fee, even if already inside. Paying a second time broke a scripted loop.
- **Path Command Spinner Traversal:** The `path` command can sometimes execute a full path plan including spinners without interruption.

### Tile Traversal Rules (Comprehensive)
- **`ground` / `grass`:** Standard walkable tiles.
- **`impassable`:** Walls, objects, NPCs, etc. Cannot be entered.
- **`ledge`:** One-way traversal. Can be jumped down from above (Y-1).
- **`cuttable`:** Tree that can be cut with HM Cut. Respawns on map change.
- **`water`:** Crossable using HM Surf.
- `spinner_up/down/left/right`: Forces movement. The `automated_path_navigator` can model paths that utilize these tiles.
- `spinner_stop`: A tile that halts movement from a spinner.
- `teleport` / `hole` / `ladder_up` / `ladder_down`: Instant warp tiles.
- **`2x1/1x2 Warp Tiles`:** Requires a two-step activation: 1. Stand on a warp tile. 2. Press a directional button into the impassable boundary.
- **`Two-Step Elevator`:** Special warp: 1. Interact with control panel. 2. Step onto adjacent warp tile.
- **`steps`:** Allows movement between `ground` and `elevated_ground`.
- **`elevated_ground`:** Walkable ground at a different elevation.
- **`boulder_barrier` / `boulder_switch`:** Switch that clears a barrier when a boulder is pushed onto it.
- **`closed_gate` / `open_gate` / `gate_offscreen`:** Gates that can block paths.

# IV. Completed Quests
- The Ghost of Lavender Town
- The Copycat's Gift
- The Sleeping Snorlax
- Cerulean City Investigation
- Silph Co. Investigation
- Rocket Hideout Investigation
- **Correction:** Depositing a single item from a stack does not free an inventory slot. The new plan is to deposit a single-stack item (POTION) to properly test the inventory hypothesis.