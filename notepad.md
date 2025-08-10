# I. Game World Rules

## A. Traversal & Tile Mechanics
- `ground` / `grass`: Standard walkable tiles.
- `impassable` / `unknown`: Cannot be entered.
- `ledge`: A one-way drop. Can be jumped down from an adjacent higher tile, but not climbed up.
- `steps`: Allows vertical movement between `ground` and `elevated_ground`.
- `elevated_ground`: Walkable ground at a different elevation. Movement to `ground` is only possible via `steps`.
- `ladder_up` / `ladder_down` / `warp`: Warps between maps or floors.

## B. Puzzle Mechanics
- **Boulder Pushing:** The player's position does NOT change when pushing a boulder, regardless of direction.
- **Boulder/Item Interaction:** Pushing a boulder onto an item collects the item and moves the boulder into that space.
- **Reset Condition:** Boulder puzzles reset upon leaving and re-entering a map or using ladders between floors.
- **`boulder_switch`:** A floor switch that must have a boulder pushed onto it.
- **`boulder_barrier`:** An impassable wall that is removed when a corresponding `boulder_switch` is activated. State does not update until visible on-screen.
- **`cleared_boulder_barrier`:** Acts as ground. Can sometimes function as a one-way ramp up from `ground` to `elevated_ground`.

## C. General Mechanics
- **Poison Damage:** Poisoned Pokémon in the party lose 1 HP every four steps taken outside of battle.
- **Fainted Pokémon can use HMs:** Confirmed that a fainted Pokémon can be selected to use a field move like Strength.
- **Pikachu Interaction:** When moving onto a tile occupied by Pikachu, the player and Pikachu appear to swap positions. The first button press turns to face, the second moves.
- **Dig Field Move:** Can be used to escape caves, acting as an Escape Rope.
- **Surf Mechanic:** To use Surf, the player must be standing on a tile adjacent to the water AND be facing the water tile.

# II. Battle Intelligence

## A. Type Effectiveness Chart (Verified)
- **Super Effective (2x damage):**
  - Electric > Flying, Water, Rock
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

## B. Strategic Notes
- **"No Will to Fight" Message:** A party menu cursor error on a fainted Pokémon, not a refusal to battle.
- **Body Slam:** Can cause paralysis.

# III. My Methodology

## A. Core Principles
- **Hypothesis-Driven Approach:** I must form a single, testable hypothesis, document it, test it, and record the conclusion. Trust direct observation over system hints that may have broader interpretations.
- **Tool Reliability & Immediate Action:** A tool that produces an incorrect or impossible result is a critical failure. I MUST fix it immediately with `define_tool` instead of deferring the task or attempting workarounds. I must not break tools to fit a flawed hypothesis.
- **System Feedback is Truth:** When a system validation check contradicts my tools, I must trust the system and investigate the discrepancy instead of proceeding with a flawed plan. This often indicates a flaw in my tool's logic or my own understanding.

## B. Future Tool Development
- A `boulder_puzzle_solver` tool is a high priority to automate complex puzzle solutions. It should perform a state-space search to find a valid sequence of player movements and boulder pushes.