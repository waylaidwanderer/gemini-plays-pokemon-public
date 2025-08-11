# I. Game World Rules

## A. Traversal & Tile Mechanics
- `ground` / `grass`: Standard walkable tiles.
- `impassable` / `unknown`: Cannot be entered.
- `ledge`: A one-way drop. Can be jumped down from an adjacent higher tile, but not climbed up.
- `steps`: Allows vertical movement between `ground` and `elevated_ground`.
- `elevated_ground`: Walkable ground at a different elevation. Movement to/from `ground` is ONLY possible via `steps` tiles. (Hypothesis confirmed by engine block at (6,10) on Victory Road 1F).
- `ladder_up` / `ladder_down` / `warp`: Warps between maps or floors.

## B. Puzzle Mechanics
- **Boulder Pushing:** Pushing a boulder horizontally moves the player into the boulder's previous tile. Pushing a boulder vertically does NOT move the player. (Hypothesis confirmed on Victory Road 1F).
- **Boulder/Item Interaction:** Pushing a boulder onto an item collects the item and moves the boulder into that space.
- **Reset Condition:** Boulder puzzles reset upon leaving and re-entering a map or using ladders between floors.
- **`boulder_switch`:** A floor switch that must have a boulder pushed onto it.
- **`boulder_barrier`:** An impassable wall that is removed when a corresponding `boulder_switch` is activated. State does not update until visible on-screen.
- **`cleared_boulder_barrier`:** Acts as ground. Can sometimes function as a one-way ramp up from `ground` to `elevated_ground`.
- **Remote Push:** It is possible to push a boulder when standing one tile away from it. The player's position does not change.

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

## B. System Interaction Notes
- **Validation Check Discrepancy:** The system's validation for reachable warps appears to ignore movable obstacles like boulders. This can create a false positive, indicating a path is clear when it is actually blocked. My own tools (`landmass_analyzer`, `generate_path_plan`) provide a more accurate ground truth in these situations.

## C. Tool Trust Protocol
- If a pathfinding tool reports \"no path found,\" my first assumption must be that the map is physically impassable, not that the tool is broken. I must use `landmass_analyzer` to verify connectivity before attempting to debug the pathfinder.

# IV. Active Strategy: Road to the Indigo Plateau
- **Current Objective:** Navigate through Victory Road to reach the Indigo Plateau and challenge the Elite Four.
- **Immediate Plan:** Enter Victory Road 1F and begin solving its puzzles to ascend to the next floor.

# V. Tool Development & Testing Ideas
- **Hypothesis to Test:** The `cleared_boulder_barrier` tile acts as a one-way ramp. Test by attempting to move DOWN from an `elevated_ground` tile onto a `cleared_boulder_barrier` tile.
- **Data Management Note:** I will begin using the '✅' emoji to mark items I have picked up to avoid confusion.
- **New Agent Idea:** `path_diagnoser_agent`. Input: start/end coordinates. Action: Runs `landmass_analyzer` and interprets the output to explain *why* a path might be failing (e.g., \"Target is on a different landmass.\").

- **Victory Road 1F Puzzle Log:**
  - **Hypothesis 1 (Incorrect):** Pushing the boulder at (3, 11) to (3, 10) will open a barrier. (Conclusion: Denied. (3,10) is not a switch. This was a flawed hypothesis based on bad memory.)
  - **Conclusion 1:** **Denied**. After pushing the boulder at (3, 11) to the switch at (3, 10) and navigating to the barrier at (10, 13), I have confirmed the barrier remains closed.
    - **Hypothesis 2:** Both switches on the floor must be activated to open the barrier at (10, 13). The next step is to push the boulder at (6, 16) onto the switch at (18, 14).
  - **Test 2:** Pushed boulder at (6, 16) around and eventually onto the warp tile at (10, 18).
  - **Conclusion 2:** **Denied**. `landmass_analyzer` confirms this action separates me from the target ladder at (2, 2). The map is now split into multiple disconnected landmasses. This was the wrong move. I need to reset the puzzle by exiting and re-entering.