# I. Rocket Hideout Investigation
- **Objective:** Find the BOSS.
- **Key Clue:** The **LIFT KEY** is needed to operate the elevator.

# II. Game Corner Investigation Plan
- **Objective:** Determine the purpose of the Game Corner and find any hidden paths or items.
- **Key Clue:** An NPC at (3, 11) revealed a rumor that the Game Corner is run by Team Rocket. This makes the poster at (10, 5) a high-priority target for investigation as a potential secret switch.

# III. Key Discoveries & Lessons Learned
- **IMMEDIATE DATA MANAGEMENT (CRITICAL):** As an LLM, my thinking is not continuous. All maintenance tasks (tool creation/fixing, agent definition, notepad updates) are the absolute highest priority and **MUST** be performed successfully in the current turn. Deferring tasks is an invalid strategy and a core failure.
- **TRUST YOUR TOOLS (CRITICAL):** I must trust my tool outputs as the default assumption. Before debugging a tool, I must first verify my own position and assumptions against the game state.
- **PROACTIVE AGENT USE:** I must use my custom agents for the tasks they were designed for. Failing to do so is inefficient.
- **MAP MARKER DISCIPLINE:** I must mark every warp tile (both entry and exit) with '🚪' immediately after use.
- **COMBAT CONFIRMATION BIAS:** I must actively test all possible solutions to a puzzle, even those that seem counter-intuitive or have a minor cost. 
- **HYPOTHESIS VETTING:** Before attempting to test a hypothesis, I must first confirm it is mechanically possible within the game's established rules.

# IV. Game Mechanics & Tile Types (Observed)
- **Post-Battle Position Shift:** Sometimes, after a wild battle concludes, the player's character may be moved to a different, nearby tile.
- **Ghost-type Damage:** Ghost-type moves deal SPECIAL damage, not physical.
- **Purified Zone:** A specific tile area in the Pokémon Tower (5F) that fully heals the party upon entry.
- **Inventory Access Bug (Confirmed):** When the player's inventory contains 21 or more unique item stacks, selecting 'ITEM' from the Start Menu incorrectly opens the HM pocket. Depositing items to bring the count to 20 or below resolves this issue.
- **Celadon City Fly Anomaly:** Attempting to use HM Fly from anywhere within Celadon City teleports the player back inside the Celadon Department Store entrance.
- **Fee Trigger Tile:** A tile that prompts for an entrance fee, even if the player is already inside the area. Paying the fee a second time broke a scripted movement loop.

### Tile Traversal Rules (Comprehensive)
- **`ground` / `grass`:** Standard walkable tiles. `grass` can trigger wild encounters.
- **`impassable`:** Walls, objects, NPCs, etc. Cannot be entered.
- **`ledge`:** One-way traversal. Can be jumped down from above (Y-1), but cannot be climbed up or moved across horizontally.
- **`cuttable`:** A tree that can be cut with HM Cut. Becomes `ground` after cutting but respawns on map change.
- **`water`:** Crossable using HM Surf. Impassable otherwise.
- **`spinner_up/down/left/right`:** Forces movement in the specified direction.
- **`teleport` / `hole` / `ladder_up` / `ladder_down`:** Warp tiles that trigger an instant map transition upon entry.
- **`2x1 Warp Tiles`:** Some warps (e.g., Silph Co. elevator) require a two-step activation: 1. Stand on one of the warp tiles. 2. Press a directional button into the impassable boundary to trigger the warp.
- **`steps`:** The only tile type that allows movement between `ground` and `elevated_ground`.
- **`elevated_ground`:** Walkable ground at a different elevation. Can only be accessed from `steps` tiles.
- **`boulder_barrier` / `boulder_switch`:** A switch that, when a boulder is pushed onto it, clears a corresponding barrier elsewhere.
- **`closed_gate` / `open_gate` / `gate_offscreen`:** Gates that can block paths. `gate_offscreen` state is unknown and assumed open for pathfinding.

# V. Future Development Ideas
- **Agent Idea: Inventory Manager:** An agent to suggest which items to deposit to manage the 20-item inventory bug or optimize the bag for a specific task.
- **Hypothesis Test Plan:** To combat fixation, after exhausting current hypotheses, I will ask the `puzzle_hypothesis_generator` for new ideas but exclude the Gambler NPC to see if it generates novel suggestions for other areas.

# VI. Archived Discoveries
## Archived Investigations
### The Old Amber
- **Objective:** Retrieve the Old Amber from the Pewter Museum of Science.
- **Final Obstacle:** A Scientist at (13, 5) on 1F blocks the path.
- **Status:** On hold pending new leads.
- **Confirmed Puzzle Steps (Internal Museum Sequence):**
  1. Lead with a Geodude or a revived fossil Pokémon and speak to the Old Man at (2, 5) on 1F.
  2. Speak to the Scientist at (8, 6) on 2F, who mentions the space exhibit.
  3. Interact with the Kabutops Fossil at (3, 7) on 1F.
- **Failed Hypotheses:**
  - Using battle moves on overworld NPCs/objects is impossible.
  - Leading with various Pokémon (Aerodactyl, SPARKY) and speaking to the Gambler at (2, 5) only changes his dialogue.
  - Completing the puzzle sequence does not move the blocking scientist.
  - Using key items (Coin Case) or consumable items (REVIVE) on NPCs or exhibits has no effect.
  - Meowth with 'Pay Day' seems unavailable on Route 7.
  - Using 'Dig' on fossil exhibits is prevented by dialogue.
- **Untested Agent-Generated Hypotheses:**
  - Have the lead Pokémon hold a 'Nugget' and then speak to the MUSEUM1F_GAMBLER at (2, 5).
  - Lead with a Porygon and speak to the MUSEUM1F_GAMBLER at (2, 5).

## Completed Quests
- **The Ghost of Lavender Town:** Rescued Mr. Fuji, received POKé FLUTE.
- **The Copycat's Gift:** Gave POKé DOLL to COPYCAT, received TM31 MIMIC.
- **The Sleeping Snorlax:** Woke Snorlax on Route 11 with POKé FLUTE.
- **Cerulean City Investigation:** Defeated Rocket Grunt and Gym Leader Misty in a rematch. Officer Jenny still blocks Route 9.

## Silph Co. Investigation
- **Key Finding (7F):** A Silph Worker at (14, 14) revealed: "We canceled the MASTER BALL project because of TEAM ROCKET."