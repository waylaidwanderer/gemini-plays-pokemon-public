# I. Game World Rules
## A. Traversal & Tile Mechanics
- `ground` / `grass`: Standard walkable tiles.
- `impassable` / `unknown`: Cannot be entered.
- `ledge`: A one-way drop. Can be jumped down from an adjacent higher tile, but not climbed up.
- `steps`: Allows vertical movement between `ground` and `elevated_ground`.
- `elevated_ground`: Walkable ground at a different elevation. Movement to/from `ground` is ONLY possible via `steps` tiles or by a one-way drop from `elevated_ground` down to `ground`.
- `ladder_up` / `ladder_down` / `warp`: Warps between maps or floors.

## B. Puzzle Mechanics
- **Boulder Pushing (Verified as of Turn 136490):**
  - **Vertical Push:** Pushing a boulder vertically (Up/Down) moves the boulder but does NOT move the player.
  - **Horizontal Push (Adjacent):** Pushing a boulder horizontally (Left/Right) while standing next to it moves the boulder one tile but does NOT move the player.
  - **Horizontal Push (Remote):** Pushing a boulder horizontally from one tile away moves the boulder one tile AND moves the player into the boulder's now-vacant previous space.
- **Boulder/Item Interaction:** Pushing a boulder onto an item collects the item and moves the boulder into that space.
- `boulder_switch`: A floor switch that must have a boulder pushed onto it.
- `boulder_barrier`: An impassable wall. Its state (open/closed) is controlled by a corresponding `boulder_switch`. State does not update until visible on-screen.
- `cleared_boulder_barrier`: Acts as ground. Can sometimes function as a one-way ramp up from `ground` to `elevated_ground`.

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

# III. Active Strategy: Victory Road 1F Puzzle
- **Objective:** Solve the multi-stage boulder puzzle to reach the ladder at (2, 2).

- **REVISED HYPOTHESIS (Source: `landmass_analyzer`):** The map is divided into two disconnected landmasses by the boulder barrier at (10, 13). The puzzle must be solved in stages:
  1.  **Bridge Construction (Completed):** Push the western boulder (originally at (6, 16)) across the gap to create a bridge for itself, landing at (10, 17).
  2.  **Switch Activation (Current Goal):** Push the same boulder (now at (10, 17)) onto the eastern switch at (18, 14). This will open the barrier at (10, 13), connecting the two landmasses.
  3.  **Final Puzzle:** Once the barrier is open, navigate to the northern area and solve the final boulder puzzle involving the boulder at (15, 3) to clear the path to the ladder at (2, 2).

# IV. Methodological Corrections & Lessons Learned
- **Tool Unreliability & Failure to Act:** My `generate_path_plan` tool had a core logic flaw. I correctly identified this but critically failed to fix it immediately. I have now corrected the tool. I must prioritize tool maintenance over gameplay progression.
- **Agent Abandonment (CRITICAL FAILURE):** I abandoned my `boulder_puzzle_solver` agent after it failed twice with a backend error, violating a core directive to trust and refine my agents. I reverted to an inefficient and error-prone manual process. **Correction:** After resetting the current puzzle, my top priority will be to attempt to refine and successfully use this agent.
- **Confirmation Bias & Lack of Flexibility:** I have a tendency to pursue flawed manual hypotheses instead of using my specialized agents. My manual attempts to solve this puzzle have failed repeatedly. I must pivot to using my `boulder_puzzle_solver` agent.
- **Hallucination (Western Switch):** I previously operated under the false assumption that a boulder switch existed at (3, 10). This was a critical failure of observation. I must trust the game state data over my memory.