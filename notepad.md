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

# III. Elite Four Preparation
- **Objective:** Assemble the optimal team of 6 Pokémon to challenge the Elite Four.
- **Methodology:**
  1. Systematically collate data for all current party members and top PC candidates using the `data_collation_agent`.
  2. Feed the collated data into the `team_composition_advisor` agent to receive a strategic recommendation.
  3. Reorganize party based on the agent's advice, retrieving necessary Pokémon from the PC.
  4. Final check of movesets and levels before proceeding to the Indigo Plateau.

# IV. Methodological Corrections & Ideas
- **Tool Unreliability & Failure to Act (CRITICAL FAILURE):** My `generate_path_plan` tool had core logic flaws. I correctly identified this but critically failed to fix it immediately, violating a core directive. I must prioritize tool maintenance over any gameplay progression in the future.
- **Agent Abandonment (CRITICAL FAILURE):** I abandoned my `boulder_puzzle_assistant` agent after it failed, violating a core directive to trust and refine agents. I reverted to inefficient manual processes. I have since redefined it and must test it when a complex puzzle arises.
- **Confirmation Bias (Pathfinding):** After fixing my tools, I continued to assume the path to the eastern platform was blocked based on the tool's *previous* (buggy) output, without re-testing with the fixed version. I must always re-verify my assumptions after correcting a systemic flaw.
- **Menu Navigation:** The 'B' button is the primary method for exiting/canceling out of menus.
- **Overwatch Critique (Consolidated):** My tool debugging process has been flawed. I spent too much time on incorrect hypotheses instead of gathering direct observational data. When tools fail repeatedly, I should prioritize a manual walkthrough to understand the mechanics before attempting code fixes. Resetting the puzzle is a valid strategy if stuck.
- **Future Agent Idea:** A 'journey_planner' agent that can devise multi-map routes involving different modes of travel (walking, surfing).
- **Future Tool Idea:** A 'multi_modal_pathfinder' tool that can calculate a single path across disconnected landmasses and water bodies.

# V. Game Mechanics (Verified)
## A. Tile Traversal Rules
- **ground:** Standard walkable tile.
- **grass:** Tall grass where wild Pokémon appear. Walkable.
- **water:** Requires Surf to traverse. Cannot be walked on.
- **impassable:** Cannot be walked on.
- **elevated_ground:** Walkable, but at a different elevation. Can only be accessed via 'steps'.
- **steps:** Allows movement between 'ground' and 'elevated_ground'.
- **ladder_up / ladder_down:** Acts as a warp between floors.
- **ledge:** A one-way drop. Can be jumped down from an adjacent tile above, landing on the tile two spaces below the starting point.
- **cleared_boulder_barrier:** A former barrier that now acts as a one-way ramp, allowing movement up from 'ground' to 'elevated_ground'.
## B. Boulder Pushing
- Boulders CANNOT be pushed onto 'steps' tiles. This is an illegal move.
- **Pushing Mechanic (Corrected):** After pushing a boulder, the player character remains in place; only the boulder moves. This requires repositioning to push again.
- **Future Agent Idea:** A 'boulder_puzzle_planner' agent that takes the output of `boulder_move_finder` and devises a multi-step sequence of pushes and player movements to solve complex puzzles.