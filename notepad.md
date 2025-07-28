# I. Game Mechanics & Traversal

## A. Core Rules
- **Level Cap:** The level cap with 8 badges is 65.
- **"No Will to Fight" Message:** Appears when the party menu cursor is on a fainted Pokémon. It is a cursor error, not a refusal to battle.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves.
- **PC Interaction:** To use a PC, stand directly below it, face up, and press 'A'.
- **Surfing:** Not all `ground` tiles adjacent to `water` are valid starting points for SURF.
- **Boulder Pushing:** Activate Strength from the party menu. Face the boulder and press the directional button. The boulder moves one tile, but the player's position does not change.
- **Puzzle Resets:** Leaving and re-entering a floor resets all boulders to their original positions.

## B. Tile Glossary & Movement Rules
- `ground`: Standard walkable tile.
- `grass`: Wild Pokémon encounters.
- `water`: Requires SURF.
- `impassable`: Wall.
- `ledge`: One-way traversal. Can only be jumped DOWN from the tile directly above. Acts as a wall from all other directions.
- `elevated_ground`: Walkable, different elevation. Movement to a lower elevation is *only* possible via `steps` tiles or `cleared_boulder_barrier` tiles. Direct movement to a lower `ground` tile is impossible.
- `steps`: Allows movement between elevations.
- `boulder_switch`: Floor switch for boulders.
- `boulder_barrier`: Impassable barrier linked to a boulder switch.
- `cleared_boulder_barrier`: Acts as a one-way ramp. It is only possible to move DOWN from an elevated area onto this tile, not UP from a lower area.
- `hole`: Drops to a lower floor. Pushing a boulder into one causes it to appear on the floor below.
- `spinner`: Forces movement.
- `ladder_up` / `ladder_down`: Warps between floors.

# II. Battle Intel

## A. Type Effectiveness Chart (Verified)
- **Super Effective (2x):** Psychic > Ghost, Poison; Ghost > Psychic; Electric > Rock, Water; Flying > Grass, Poison, Fighting; Ice > Ground, Grass, Flying, Dragon; Ground > Poison, Fire, Electric, Rock; Rock > Fire, Ice, Flying, Bug; Fighting > Normal, Rock, Ice; Water > Fire, Ground, Rock; Grass > Water, Ground, Rock; Bug > Grass, Poison, Psychic; Poison > Grass, Bug
- **Not Very Effective (0.5x):** Normal !> Rock; Electric !> Grass, Electric, Dragon; Rock !> Psychic; Psychic !> Psychic; Poison !> Poison, Ground, Rock, Ghost; Ice !> Water, Ice, Fire; Fighting > Poison, Flying, Psychic, Bug; Water !> Water, Grass, Dragon; Grass !> Fire, Grass, Poison, Flying, Bug, Dragon
- **Immune (0x):** Flying immune to Ground; Ground immune to Electric; Ghost immune to Normal, Fighting
- **Correction:** Psychic-type moves deal NEUTRAL (1x) damage to Rock-type Pokémon.

## B. Trainer Battle Rules
- **Trainer Impassability (Hypothesis):** Defeated trainers do NOT respawn. They generally become impassable obstacles, but this may not be a universal rule.

# III. Puzzle Mechanics & Key Discoveries

- **Victory Road 1F - Western Platform:** This area contains the ladder to 2F at (2, 2).
- **Victory Road 2F - Western Trap:** Pushing the boulder onto the switch at (2, 17) primes a trap that opens the barrier at (8, 9) and (8, 10) after leaving and re-entering the floor.
- **Victory Road 3F - Hole Puzzle:** Pushing the boulder at (14, 13) south into the hole at (14, 15) causes it to drop to the floor below.

# IV. Current Plans & Lessons Learned

## A. Current Plan
- **Immediate Priority:** Systematically debug and fix the `pathfinder_lite` tool. It is currently unreliable and preventing progress. The test case is navigating from Viridian City to Route 22.

## B. Key Lessons
- **Complex Failure Analysis:** My debugging of `pathfinder_lite` was flawed. I incorrectly assumed the tool was broken when it failed to find a path on Route 22, when in fact no path existed. This was a failure on my part to trust the data. However, subsequent tests in Viridian City have proven the tool *is* also fundamentally broken, as it repeatedly generates paths through water and other impassable tiles. Both my assumptions and the tool's code require fixing.

# V. Future Development Ideas
- **`puzzle_strategist_agent`:** An agent to analyze environmental puzzles and suggest high-level solutions.
- **`movement_tester_tool`:** An automated tool to test tile transitions and log outcomes.
- **`team_builder_agent`:** An agent to suggest optimal party compositions for major challenges.
- **`hm_troubleshooter_agent`:** An agent to automate testing of HM usage when it fails.
- **`fly_helper_tool`:** A tool to automate selecting a destination from the Fly menu.

# VI. Tool & Agent Development

## A. Pathfinder Status
- **Status:** The `pathfinder_lite` tool is CRITICALLY UNRELIABLE and UNTRUSTWORTHY. It has repeatedly generated invalid paths into walls (Route 22) and water tiles (Viridian City).
- **Current Action:** The tool is undergoing intensive debugging. I have added logging to trace the A* algorithm's path construction to identify the root cause of the invalid node selection. This is the highest priority task.
- **`tool_diagnostics_agent`:** An agent to analyze a tool's output against game state data to determine if a 'failure' is a correct assessment of the world.