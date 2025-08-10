# I. Game Mechanics & Traversal Rules
- **Poison Damage:** Poisoned Pokémon in the party lose 1 HP every four steps taken outside of battle.
- **Fainted Pokémon can use HMs:** Confirmed that a fainted Pokémon can be selected to use a field move like Strength.
- **Pikachu Interaction:** When moving onto a tile occupied by Pikachu, the player and Pikachu appear to swap positions. The first button press turns to face, the second moves.
- **Dig Field Move:** Can be used to escape caves, acting as an Escape Rope. This is a key anti-softlock mechanic.
- **Surf Mechanic:** To use Surf from a land tile, the player must be standing on a tile adjacent to the water AND be facing the water tile.
- **Boulder Pushing:** The player's position does NOT change when pushing a boulder, regardless of direction.
- **`ground` / `grass`:** Standard walkable tiles.
- **`impassable` / `unknown`:** Cannot be entered.
- **`cleared_boulder_barrier`:** Acts as ground. State only updates from `boulder_barrier` when visible on-screen.
- **`boulder_barrier`:** An impassable wall that is removed when a corresponding `boulder_switch` is activated. State does not update until visible.
- **`boulder_switch`:** A floor switch that must have a boulder pushed onto it.
- **`steps`:** Allows vertical movement between `ground` and `elevated_ground`.
- **`elevated_ground`:** Walkable ground at a different elevation. Movement to `ground` is only possible via `steps`.
- **`ledge`:** A one-way drop. Can be jumped down from an adjacent higher tile, but not climbed up.
- **`ladder_up` / `ladder_down`:** Warps between floors.

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

# IV. Methodology & Lessons Learned
- **Hypothesis-Driven Approach:** I must form a single, testable hypothesis, document it, test it, and record the conclusion. Trust direct observation over system hints that may have broader interpretations.
- **Tool Reliability & Immediate Action:** A tool that produces an incorrect or impossible result is a critical failure. I MUST fix it immediately with `define_tool` instead of deferring the task or attempting workarounds. I must not break tools to fit a flawed hypothesis.
- **System Feedback is Truth:** When a system validation check contradicts my tools, I must trust the system and investigate the discrepancy instead of proceeding with a flawed plan. This often indicates a flaw in my tool's logic or my own understanding.
- **Pre-emptive Path Planning:** For boulder puzzles, I must use my analysis tools to verify the entire sequence of pushes *before* I start moving anything to avoid soft-locking myself.
- **Future Tool Development:** A `boulder_puzzle_solver` tool is a high priority to automate complex puzzle solutions. It should perform a state-space search to find a valid sequence of player movements and boulder pushes.