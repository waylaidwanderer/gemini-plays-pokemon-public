# I. Game World Rules

## A. Traversal & Tile Mechanics
- `ground` / `grass`: Standard walkable tiles.
- `impassable` / `unknown`: Cannot be entered.
- `ledge`: A one-way drop. Can be jumped down from an adjacent higher tile, but not climbed up.
- `steps`: Allows vertical movement between `ground` and `elevated_ground`.
- `elevated_ground`: Walkable ground at a different elevation. Movement to `ground` is only possible via `steps`.
- `ladder_up` / `ladder_down` / `warp`: Warps between maps or floors.

## B. Puzzle Mechanics
- **Boulder Pushing:** The player's position does NOT change when pushing a boulder.
- **Boulder/Item Interaction:** Pushing a boulder onto an item collects the item and moves the boulder into that space.
- **Reset Condition:** Boulder puzzles reset upon leaving and re-entering a map or using ladders between floors.
- **`boulder_switch`:** A floor switch that must have a boulder pushed onto it.
- **`boulder_barrier`:** An impassable wall that is removed when a corresponding `boulder_switch` is activated. State does not update until visible on-screen.
- **`cleared_boulder_barrier`:** Acts as ground. Can sometimes function as a one-way ramp up from `ground` to `elevated_ground`.

## C. General Mechanics
- **Poison Damage:** Poisoned Pokémon in the party lose 1 HP every four steps taken outside of battle.
- **Fainted Pokémon can use HMs:** A fainted Pokémon can be selected to use a field move like Strength.
- **Pikachu Interaction:** When moving onto a tile occupied by Pikachu, the player and Pikachu appear to swap positions. The first button press turns to face, the second moves.
- **Dig Field Move:** Can be used to escape caves, acting as an Escape Rope.
- **Surf Mechanic:** To use Surf, the player must be standing on a tile adjacent to the water AND be facing the water tile.

# II. Battle Intelligence

## A. Type Effectiveness Chart (Verified)
- **Super Effective (2x damage):**
  - Water > Rock, Ground, Fire
  - Ground > Fire, Electric, Rock, Ground
  - Ice > Ground, Grass, Flying, Dragon
  - Flying > Fighting, Grass, Bug
  - Fighting > Normal, Rock, Ice
  - Electric > Water, Flying
- **Not Very Effective (0.5x damage):**
  - Normal !> Rock
- **Immune (0x damage):**
  - Ground immune to Electric
  - Flying immune to Ground

## B. Strategic Notes
- **"No Will to Fight" Message:** A party menu cursor error on a fainted Pokémon, not a refusal to battle.
- **Body Slam:** Can cause paralysis.

# III. My Methodology

## A. Core Principles
- **IMMEDIATE ACTION IS PARAMOUNT:** A broken tool is a critical failure. I MUST fix it immediately with `define_tool` instead of deferring the task or attempting workarounds. Fixing tools is my highest priority, above any gameplay objective.
- **Hypothesis-Driven Approach:** I must form a single, testable hypothesis, document it, test it, and record the conclusion. I must actively try to disprove my own conclusions to avoid confirmation bias.
- **Trust Direct Observation:** System hints can be misleading. Direct, in-game observation (e.g., walking into a wall) is the ultimate source of truth.

## B. Tool Triage (Active Issues)
- **`boulder_puzzle_solver`:** Deleted. The tool was critically flawed, causing timeouts and preventing progress. A manual approach to puzzles is currently more reliable.

## C. Active Hypothesis (Victory Road 1F) - Manual Approach
- **Previous Hypothesis (Failed):** Pushing the boulder at (6, 16) south would clear a path to the eastern platform.
- **Conclusion (Attempt 1):** This was a critical error. Pushing the boulder to (6, 17) trapped me in the western section, forcing a reset via Dig. I failed to consider the negative consequences of the move. This is a lesson in thinking through all outcomes before acting.
- **New Hypothesis:** The main puzzle solution requires accessing the eastern elevated platform to push the boulder at (15, 3) onto the switch at (18, 14). The correct access point to this platform is via the steps at (16, 8).
- **Plan:**
    1. Navigate to the steps at (16, 8).
    2. Ascend to the eastern elevated platform.
    3. Maneuver the boulder at (15, 3) onto the switch at (18, 14).
    4. Verify the barrier at (10, 13) is cleared.
    5. Proceed to the ladder at (2, 2).

# IV. Tool Development Ideas
- **Boulder Puzzle Assistant:** A tool that, instead of solving the whole puzzle, analyzes the current state and suggests all possible valid moves for each boulder on the map. This would help in manual solving without the risk of a complex solver timing out or getting stuck.