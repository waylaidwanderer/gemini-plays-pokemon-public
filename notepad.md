# I. Rocket Hideout Investigation
- **Objective:** Find the BOSS.
- **Key Clue:** The **LIFT KEY** is needed to operate the elevator.
- **Current Hypothesis & Test Plan:** The elevator accessed from the isolated eastern section of B1F appears to be a red herring, leading only to dead-end loops. The LIFT KEY is likely for a different elevator in the main, previously explored part of the hideout.
  1.  **Test:** Confirm the two-step elevator mechanic works consistently by returning to B1F.
  2.  **Action:** Once on B1F, navigate back to the main hideout area.
  3.  **Explore:** Systematically search the main sections of B2F, B3F, and B4F for a new, previously inactive elevator.

# II. Key Discoveries & Lessons Learned
- **IMMEDIATE DATA MANAGEMENT (CRITICAL):** As an LLM, my thinking is not continuous. All maintenance tasks (tool creation/fixing, agent definition, notepad updates) are the absolute highest priority and **MUST** be performed successfully in the current turn. Deferring tasks is an invalid strategy and a core failure.
- **IMMEDIATE TOOL MAINTENANCE (CRITICAL):** If a custom tool malfunctions, I **MUST** fix it in the immediately following turn. Deferring tool maintenance is a critical failure. (Self-assessment lesson from `deposit_pc_item_by_index` failure).
- **TRUST YOUR TOOLS (CRITICAL):** I must trust my tool outputs as the default assumption. Before debugging a tool, I must first verify my own position and assumptions against the game state.
- **PROACTIVE AGENT USE:** I must use my custom agents for the tasks they were designed for. Failing to do so is inefficient.
- **MAP MARKER DISCIPLINE:** I must mark every warp tile (both entry and exit) with '🚪' immediately after use. Hallucinations must be resolved before placing markers.
- **HYPOTHESIS VETTING:** Before attempting to test a hypothesis, I must first confirm it is mechanically possible within the game's established rules.

# III. Game Mechanics & Tile Types (Observed)
- **Post-Battle Position Shift:** Sometimes, after a wild battle concludes, the player's character may be moved to a different, nearby tile.
- **Ghost-type Damage:** Ghost-type moves deal SPECIAL damage, not physical.
- **Purified Zone:** A specific tile area in the Pokémon Tower (5F) that fully heals the party upon entry.
- **Inventory Access Bug (Confirmed):** When the player's inventory contains 21 or more unique item stacks, selecting 'ITEM' from the Start Menu incorrectly opens the HM pocket.
- **Celadon City Fly Anomaly:** Attempting to use HM Fly from anywhere within Celadon City teleports the player back inside the Celadon Department Store entrance.
- **Fee Trigger Tile:** A tile that prompts for an entrance fee, even if the player is already inside the area. Paying the fee a second time broke a scripted movement loop.

### Tile Traversal Rules (Comprehensive)
- **`ground` / `grass`:** Standard walkable tiles.
- **`impassable`:** Walls, objects, NPCs, etc. Cannot be entered.
- **`ledge`:** One-way traversal. Can be jumped down from above (Y-1).
- **`cuttable`:** Tree that can be cut with HM Cut. Respawns on map change.
- **`water`:** Crossable using HM Surf.
- `spinner_up/down/left/right`: Forces movement in the specified direction.
- `spinner_stop`: A tile that halts movement from a spinner.
- `teleport` / `hole` / `ladder_up` / `ladder_down`: Instant warp tiles.
- **`2x1 Warp Tiles`:** Requires a two-step activation: 1. Stand on a warp tile. 2. Press a directional button into the impassable boundary.
- **`Two-Step Elevator`:** A special warp requiring a two-step process: 1. Interact with the control panel to select a destination floor. 2. Step onto one of the adjacent warp tiles to travel.
- **`steps`:** Allows movement between `ground` and `elevated_ground`.
- **`elevated_ground`:** Walkable ground at a different elevation.
- **`boulder_barrier` / `boulder_switch`:** Switch that clears a barrier when a boulder is pushed onto it.
- **`closed_gate` / `open_gate` / `gate_offscreen`:** Gates that can block paths.

# IV. Future Development Ideas
- **Agent: Puzzle Solver:** An agent that takes a puzzle objective and a list of failed hypotheses and suggests new, mechanically-sound tests. Could be refined to understand known game mechanics like two-step warps.
- **Tool: Elevator Operator:** A tool to automate the two-step process of using an elevator: `use_elevator(destination_floor)`.
- **Agent: Inventory Manager:** An agent to suggest which items to deposit to manage the 20-item inventory bug.

# V. Archived Discoveries
## Archived Investigations
### The Old Amber
- **Objective:** Retrieve the Old Amber from the Pewter Museum of Science.
- **Status:** On hold pending new leads.
- **Confirmed Puzzle Steps:** 1. Lead with Geodude/fossil, speak to Old Man (1F). 2. Speak to Scientist (2F). 3. Interact with Kabutops Fossil (1F).
- **Untested Agent-Generated Hypotheses:** Lead with a Pokémon holding a 'Nugget' or lead with a Porygon and speak to the Gambler NPC.

## Completed Quests
- The Ghost of Lavender Town
- The Copycat's Gift
- The Sleeping Snorlax
- Cerulean City Investigation
- Silph Co. Investigation

# V. Rocket Hideout B3F Maze
- **Objective:** Solve the spinner maze to reach the warp to B4F.
- **Current Hypothesis (from Agent):** Interacting with Pikachu while he is on tile (18, 16) may disable the spinner trap at (19, 17).
- **Test Plan:**
  1. Current state: Gem at (20, 16), Pikachu at (19, 16).
  2. Move Left to (19, 16) (swaps with Pikachu). Expected state: Gem at (19, 16), Pikachu at (20, 16).
  3. Move Left to (18, 16). Expected state: Gem at (18, 16), Pikachu at (19, 16).
  4. Move Right to (19, 16) (swaps with Pikachu). Expected state: Gem at (19, 16), Pikachu at (18, 16).
  5. Turn Left to face Pikachu.
  6. Press 'A' to interact.
  7. **Outcome:** Interaction failed. No text appeared, but the game entered a state suggesting a hidden dialogue box. Hypothesis denied.
  8. **New Hypothesis:** A hidden dialogue box must be cleared by pressing 'B'.
  8. **New Hypothesis:** A hidden dialogue box must be cleared by pressing 'B'.