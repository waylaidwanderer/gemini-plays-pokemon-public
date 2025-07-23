# I. Game Mechanics

## A. Tile Mechanics (Advanced)
- **Ledge:** Can be jumped down (one-way). Moving down into a ledge tile moves the player two tiles down.
- **Cuttable Tree:** Requires HM Cut to pass. Respawn on map change.
- **Water:** Requires HM Surf to traverse.
- **Boulder:** Requires HM Strength to move.
- **Hole:** Warps player to a lower floor.
- **Ladder (Up/Down):** Warps player between floors.
- **Warp:** An instant transition point between maps.
- **Steps:** Allows movement between different ground elevations and can act as a valid entry point to water for Surfing.
- **Spinner (up, down, left, right):** Forces movement.
- **Spinner Stop:** A tile that halts spinner movement.
- **Elevated Ground:** Walkable ground at a different elevation. Cannot use Surf from this tile type.
- **Gate (`gate_offscreen`, `closed_gate`, `open_gate`):** Barriers that may open or close.
- **Boulder Switch & Barrier:** `boulder_switch` tiles are activated by boulders, which changes a `boulder_barrier` tile into a `cleared_boulder_barrier` tile.
- **Cleared Boulder Barrier (Corrected):** Functions as a one-way ramp. It can only be entered from a `steps` tile when moving from `ground` to `elevated_ground`. It is impassable from adjacent `ground` tiles and cannot be used to move down from `elevated_ground` to `ground`. This mechanic was fully confirmed and the pathfinder was corrected on Turn 95901.

## B. General Heuristics & Rules
- **PC Interaction:** To use a PC, stand directly below it, face up, and press 'A'.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves.
- **"No Will to Fight" Message (Correction):** Appears when the party menu cursor is on a fainted Pokémon.
- **Level Cap:** The level cap with 8 badges is 65.
- **Special NPC Interaction:** Certain puzzles may require walking *through* an NPC rather than interacting with them (e.g., Summer Beach House).
- **Boulder Puzzle Mechanics:** Boulders cannot be pushed directly into standard `water` tiles. They must be pushed into `hole` tiles to affect lower floors.
- **PC Tile Anomaly:** The tile for interacting with the Pokémon Center PC is sometimes labeled as `grass` in the map data, despite being indoors.

# II. Battle Intel

## A. Type Effectiveness Chart (Verified)
- **Super Effective (2x):** Psychic > Ghost, Poison; Ghost > Psychic; Electric > Rock, Water; Flying > Grass, Poison, Fighting; Ice > Ground, Grass, Flying, Dragon; Ground > Poison, Fire, Electric, Rock; Rock > Fire, Ice, Flying, Bug; Fighting > Normal, Rock, Ice; Water > Fire, Ground, Rock; Grass > Water, Ground, Rock; Bug > Grass, Poison, Psychic; Poison > Grass, Bug.
- **Not Very Effective (0.5x):** Normal !> Rock; Electric !> Grass, Electric, Dragon; Rock !> Psychic; Psychic !> Psychic; Poison !> Poison, Ground, Rock, Ghost; Ice !> Water, Ice, Fire; Fighting > Poison, Flying, Psychic, Bug; Water !> Water, Grass, Dragon; Grass !> Fire, Grass, Poison, Flying, Bug, Dragon.
- **Immune (0x):** Flying immune to Ground; Ground immune to Electric; Ghost immune to Normal, Fighting.
- **Type Correction (Psychic vs. Rock):** Psychic-type moves deal NEUTRAL (1x) damage to Rock-type Pokémon, not 'not very effective' as previously assumed. This was verified in the battle against Pixel's Alakazam vs. my Golem (CRAG).

## B. Trainer Rosters & Movesets

### Giovanni (Viridian Gym Leader)
- **Team:**
  - NIDOKING (Lv54) - Moves: Ice Beam, Blizzard, Thunderbolt, Earthquake
  - DUGTRIO (Lv53) - Moves: Fissure, Slash, Earthquake, Rock Slide
  - NIDOQUEEN (Lv54) - Moves: Ice Beam, Earthquake, Thunderbolt, Body Slam
  - PERSIAN (Lv55) - Moves: Bubblebeam, Slash, Hyper Beam, Thunderbolt
  - RHYDON (Lv55) - Moves: Rock Slide, Earthquake

### Cool Trainer M (Victory Road 1F)
- **Team:**
  - ELECTABUZZ (Lv53)
  - SNORLAX (Lv53) - Moves: Harden
  - SLOWBRO (Lv53) - Moves: Psychic, Waterfall
  - PORYGON (Lv53) - Moves: Agility
- **Notes:** This trainer spams Hyper Potions when his Pokémon are at low health.

## C. Battle Lessons
- **Level Disparity:** A large level gap can be more dangerous than type immunity.
- **Misleading Battle Text:** The on-screen text for move effectiveness can be incorrect. The actual damage calculation follows my verified type chart.
- **Ground-Type Immunity Extension:** Ground-types are immune to Electric-type *status* moves (like THUNDER WAVE).

# III. Future Development Ideas (Prioritized)
- **Puzzle Orchestrator Agent:** Create an agent that can manage multi-step puzzles, like the ones in Victory Road. It would take the overall goal (e.g., 'open the northern barrier') and use my existing `boulder_puzzle_solver` and `gem_pathfinder` tools to generate and execute the full sequence of moves and pushes required.
- **Pokedex Analysis (Review):** Overwatch noted potential overlap with the 'team_composition_advisor_agent'. Review existing agent's capabilities before creating a new one to avoid redundancy.
- **Elixer Mechanic (Correction):** Elixers only restore PP, not HP. This was verified on Turn 96074 with CRAG in Victory Road 2F.

# IV. Archive

## A. Strategic Lessons & Reflections
*This section contains a log of past failures and corrected procedural flaws. It serves as a reminder of lessons learned to prevent repeating them.*
- **Core Lesson:** Trust data (game state, tool outputs) over intuition. Abandon failing strategies immediately. Adhere to the scientific method for all puzzles (Observe, Hypothesize, Test, Conclude, Experiment).
- **Procedural Mandates:** All tool/agent maintenance and data correction are the immediate, highest-priority action. When a core logic bug is found, audit all other tools for the same flaw. Consult map markers and available tools before acting. Use systematic, minimal tests for debugging complex tools.
- **Past Hallucinations:** I have a history of hallucinating game state (location, battle outcomes, badge count). I must strictly ground all actions and reasoning in the provided Game State Information as the single source of truth.
- **Confirmation Bias on Route 23 (Turn 95544):** I repeatedly failed to find a land-only path to Victory Road but persisted with workarounds instead of accepting the tool's output, which indicated a water crossing was mandatory. This wasted significant time. Lesson: Trust the data from my tools over my own assumptions, and if a hypothesis is repeatedly falsified, abandon it immediately.

## B. Agent & Tool Refinement Log
- **Battle Strategist Agent (Turn 91179):** Updated the agent's system prompt to force it to prioritize survival by assuming a worst-case scenario (a super-effective critical hit from the opponent's best move) and to heavily weigh level disparity as a key risk factor.
- **Battle Strategist Agent (Turn 94114):** Updated agent prompt to correctly interpret the 'training' goal, prioritizing EXP gain for lower-level party members over simply winning with the strongest Pokémon.
- **`delete_map_marker` Tool (Turn 95077):** Standardized gate markers to use '✅' for open and '⛔' for closed.
- **`retreat_planner_agent` (Turn 96236):** Refined the agent's system prompt to require it to check the player's inventory before suggesting item-based solutions. It will now provide a walking path if no fast-travel item is available.

## C. Tool Development Log
- **Pathfinder & Boulder Puzzle Solver:** Fixed a bug preventing land-to-water SURF transitions and corrected ledge traversal logic. Consolidated redundant tools.
- **`spinner_maze_solver`:** Rewrote path reconstruction logic to fix a critical bug.
- **`reachable_shoreline_finder`:** Created to systematically identify valid SURF starting points. Updated on Turn 94090 to handle elevation changes via 'steps' tiles.
- **`connectivity_checker`:** Deleted due to redundancy with robust pathfinder.
- **`find_closest_unseen_tile`:** Deleted on Turn 95731 due to flawed logic.
- **`boulder_puzzle_solver` (Turn 95239-95310):** Created and refined to solve boulder puzzles, correcting multiple logic and crash bugs.

## D. Basic Tile Mechanics (Archive)
- **Ground:** Standard walkable tile.
- **Impassable:** Walls, objects, etc. Cannot be entered.
- **Grass:** Tall grass for wild Pokémon encounters.

### Cool Trainer M (Victory Road 3F)
- **Location:** (29, 6)
- **Team:**
  - CHARIZARD (Lv52) - Moves: Flamethrower, Slam
  - MAGNETON (Lv52)

### Cool Trainer M (Victory Road 3F)
- **Location:** (29, 6)
- **Team:**
  - CHARIZARD (Lv52) - Moves: Flamethrower, Slam
  - MAGNETON (Lv52)

# V. Tool Development Backlog
- **`gem_pathfinder` Bug:** The tool generates paths that transition from land to water even when the target is on land, causing movement to fail. It needs to be updated to handle land-only pathing correctly, possibly by adding a state for 'walking' vs 'surfing' or by disallowing land-to-water transitions when the final destination is on land.