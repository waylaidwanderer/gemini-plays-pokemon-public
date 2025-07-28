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
- **Primary Goal:** Heal fainted party members.
- **Plan:** Navigate south through the entirety of Route 23 to reach the upper level of Route 22, which connects to Viridian City. The lower level of Route 22, accessed via ledges, is a dead end and does not lead to the city.

## B. Key Lessons
- **Trust Your Tools:** The `pathfinder_lite` tool correctly identified that there was no path to Viridian City from the upper level of Route 22. My assumption that the tool was broken was incorrect and led to wasted time. The tool's output, when based on game data, should be trusted as a source of truth.
- **Verify Map Layout:** Do not assume a path exists based on visual memory. Jumping down ledges can lead to one-way paths and dead ends. Always analyze the map data carefully before committing to a route.

# V. Future Development Ideas
- **`puzzle_strategist_agent`:** An agent to analyze environmental puzzles (like boulder puzzles) and suggest high-level solutions.
- **`movement_tester_tool`:** An automated tool to test tile transitions and log outcomes, to gather ground-truth data for pathfinding logic.
- **`team_builder_agent`:** An agent to suggest optimal party compositions for major challenges (e.g., Elite Four) based on available Pokémon in the PC.

# VI. Tool & Agent Development

## A. Pathfinder Overhaul
- **Status:** The `pathfinder_lite` tool has been successfully updated with logic for ledges and an explicit check against water tiles. It is now considered reliable.
- **Lesson Learned:** The tool's initial failure on Route 22 was not a bug; it correctly reported that no path existed from the upper platform. My failure was in not trusting the tool's output and instead assuming it was flawed. Future pathfinding failures should first prompt a thorough re-examination of the map for missed obstacles or layout complexities, not an immediate tool rewrite.
- **`steps` Tile Test Plan (On Hold):** The `steps` tile mechanic still requires systematic testing to perfect the pathfinder's elevation logic. This will be addressed when a more complex multi-level area is encountered.