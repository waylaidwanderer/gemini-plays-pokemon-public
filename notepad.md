# I. Game Mechanics & Traversal

## A. Core Rules
- **Level Cap:** The level cap with 8 badges is 65.
- **"No Will to Fight" Message:** Appears when the party menu cursor is on a fainted Pokémon. It is a cursor error, not a refusal to battle.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves (Hypothesis: May not apply everywhere, e.g., Route 23 SURF).
- **PC Interaction:** To use a PC, stand directly below it, face up, and press 'A'.
- **Surfing:** Not all `ground` tiles adjacent to `water` are valid starting points for SURF. Character orientation might matter (Hypothesis: Untested).
- **Boulder Pushing:** Activate Strength from the party menu. Face the boulder and press the directional button. The boulder moves one tile, but the player's position does not change.
- **Puzzle Resets:** Leaving and re-entering a floor resets all boulders to their original positions.

## B. Tile Glossary & Movement Rules
- `ground`: Standard walkable tile.
- `grass`: Wild Pokémon encounters.
- `water`: Requires SURF.
- `impassable`: Wall.
- `ledge`: One-way traversal. Can only be jumped DOWN from the tile directly above. Acts as a wall from all other directions.
- `elevated_ground`: Walkable, different elevation. Movement to a lower elevation is *only* possible via `steps` tiles or `cleared_boulder_barrier` tiles. Direct movement to a lower `ground` tile is impossible.
- `steps`: Allows movement between elevations. (MECHANICS UNVERIFIED - REQUIRES SYSTEMATIC TESTING)
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
- **Trainer Impassability (Hypothesis):** Defeated trainers do NOT respawn. They generally become impassable obstacles, but this may not be a universal rule. (e.g., The Youngster at (7, 11) on Victory Road 1F might be passable. Needs verification).

# III. Puzzle Mechanics & Key Discoveries

- **Victory Road 1F - Western Platform:** This area contains the ladder to 2F at (2, 2). It is the only way to progress to the next floor, but it is inaccessible until the central barrier at (10, 13) is opened.
- **Victory Road 2F - Western Trap:** This puzzle requires a two-step "prime and trigger" mechanic. Pushing the boulder onto the switch at (2, 17) primes the trap. Leaving the floor and re-entering triggers the event, opening the barrier at (8, 9) and (8, 10).
- **Victory Road 3F - Hole Puzzle:** Pushing the boulder at (14, 13) south into the hole at (14, 15) causes it to drop to the floor below, affecting a puzzle there.

# IV. Current Plans & Lessons Learned

## A. Current Plan
- **Immediate Priority:** Fly to Viridian City to heal fainted party members.
- **Next Step:** After healing, systematically debug and fix the `pathfinder_lite` tool, which is currently unreliable.

## B. Key Lessons
- **Trust Your Tools (Corrected):** I have repeatedly failed to trust my `pathfinder_lite` tool's output. The tool correctly identified there was no path from the upper ledge of Route 22 to Viridian City. My assumption that the tool was broken was incorrect and led to wasted time. I repeated this mistake by attempting to debug the tool for generating what I perceived as invalid paths on the lower section of Route 22, when in fact my understanding of the map was flawed.
- **Verify Map Layout:** Do not assume a path exists based on visual memory or intuition. Jumping down ledges can lead to one-way paths and dead ends. Always analyze the map data carefully before committing to a route.

# V. Future Development Ideas
- **`puzzle_strategist_agent`:** An agent to analyze environmental puzzles (like boulder puzzles) and suggest high-level solutions.
- **`movement_tester_tool`:** An automated tool to test tile transitions and log outcomes, to gather ground-truth data for pathfinding logic.
- **`team_builder_agent`:** An agent to suggest optimal party compositions for major challenges (e.g., Elite Four) based on available Pokémon in the PC.
- **`hm_troubleshooter_agent`:** An agent to automate the systematic testing of HM usage when it fails, trying different adjacent tiles and hypotheses (e.g., fainted vs. healthy Pokémon) to find a solution.

# VI. Tool & Agent Development

## A. Pathfinder Status
- **Status:** The `pathfinder_lite` tool is currently UNRELIABLE and UNTRUSTWORTHY. It has repeatedly generated invalid paths on Route 22.
- **Lesson Learned (Repeated Failure):** I failed to apply the lesson about trusting my tools. Instead of re-evaluating the map when the pathfinder produced unexpected results, I incorrectly assumed the tool was broken and wasted dozens of turns trying to 'fix' it. The tool's output, even when it seems wrong, must be treated as a reflection of the game data, prompting a re-evaluation of my own assumptions first.
- **`steps` Tile Test Plan (On Hold):** The `steps` tile mechanic still requires systematic testing to perfect the pathfinder's elevation logic. This will be addressed when a more complex multi-level area is encountered.