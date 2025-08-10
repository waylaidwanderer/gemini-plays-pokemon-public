# I. Core Gameplay & World Rules
- **Poison Damage:** Poisoned Pokémon in the party lose 1 HP every four steps taken outside of battle.
- **Fainted Pokémon can use HMs:** Confirmed that a fainted Pokémon can be selected to use a field move like Strength.
- **Pikachu Interaction:** When moving onto a tile occupied by Pikachu, the player and Pikachu appear to swap positions. The first button press turns to face, the second moves.
- **Dig Field Move:** Can be used to escape caves, acting as an Escape Rope. This is a key anti-softlock mechanic.
- **Surf Mechanic:** To use Surf from a land tile, the player must be standing on a tile adjacent to the water AND be facing the water tile.

# II. Battle Intelligence
## A. Type Effectiveness Chart (Verified In-Game)
- **Super Effective (2x damage):**
  - Electric > Flying, Water
  - Water > Rock, Ground, Fire
  - Ground > Fire, Electric, Rock, Ground
  - Ice > Ground, Grass, Flying, Dragon
  - Flying > Fighting, Grass, Bug
  - Fighting > Normal, Rock, Ice
- **Not Very Effective (0.5x damage):**
  - Normal !> Rock
- **Immune (0x damage):**
  - Ground immune to Electric
  - Flying immune to Ground

## B. Strategic Notes & Mechanics
- **"No Will to Fight" Message:** A party menu cursor error on a fainted Pokémon, not a refusal to battle.
- **Body Slam:** Can cause paralysis.

# III. Puzzle Mechanics & Solutions
- **Reset Condition:** Boulder puzzles reset upon leaving and re-entering a map or using ladders between floors.
- **Boulder/Item Interaction:** Pushing a boulder onto an item collects the item and moves the boulder into that space.
- **Off-Screen Barrier Update:** A `boulder_barrier` tile's state does not update to `cleared_boulder_barrier` until it is visible on-screen. This is a crucial mechanic for pathfinding.

# IV. Methodology & Lessons Learned
- **Hypothesis-Driven Approach:** I must form a single, testable hypothesis, document it, test it, and record the conclusion.
- **Tool Reliability & Immediate Action:** A tool that produces an incorrect or impossible result is a critical failure. I MUST fix it immediately with `define_tool` instead of deferring the task or attempting workarounds.
- **System Feedback is Truth:** When a system validation check contradicts the output of one of my tools, I must trust the system and immediately investigate the discrepancy instead of proceeding with a flawed plan.
- **Verify All Exits:** Before concluding I am trapped or soft-locked, I must use my pathfinding tool to test routes to ALL available exits (ladders, warps, map connections) on the current map.
- **Pre-emptive Path Planning:** For boulder puzzles, I must use my analysis tools to verify the entire sequence of pushes *before* I start moving anything to avoid soft-locking myself.

# V. Tile Mechanics & Traversal Rules
- **`ground` / `grass`:** Standard walkable tiles.
- **`impassable` / `unknown`:** Cannot be entered.
- **`cleared_boulder_barrier`:** Acts as ground. State only updates from `boulder_barrier` when visible on-screen.
- **`boulder_barrier`:** An impassable wall that is removed when a corresponding `boulder_switch` is activated.
- **`boulder_switch`:** A floor switch that must have a boulder pushed onto it.
- **`steps`:** Allows vertical movement between `ground` and `elevated_ground`.
- **`elevated_ground`:** Walkable ground at a different elevation. Movement to `ground` is only possible via `steps`.
- **`ladder_up` / `ladder_down`:** Warps between floors.
- **Untested Mechanic:** It is unknown if a boulder can be pushed onto a `steps` tile. This needs to be tested.
- **Pushing Mechanics (Correction):** The player's position does NOT change when pushing a boulder, regardless of direction (vertical or horizontal).