# I. Game Mechanics & Traversal

## A. Core Rules
- **Level Cap:** The level cap with 8 badges is 65.
- **"No Will to Fight" Message:** Appears when the party menu cursor is on a fainted Pokémon. It is a cursor error, not a refusal to battle.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves.
- **PC Interaction:** To use a PC, stand directly below it, face up, and press 'A'.
- **Surfing:** Not all `ground` tiles adjacent to `water` are valid starting points for SURF.
- **Boulder Pushing:** Activate Strength from the party menu. Face the boulder and press the directional button. The boulder moves one tile, but the player's position does not change.
- **Puzzle Resets:** Leaving and re-entering a floor resets all boulders to their original positions.
- **Data Trust:** The map XML data is the ultimate source of truth for traversal. If a tile is marked `impassable` in the XML, it cannot be walked on, even if it appears visually open on screen.

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

# IV. Lessons Learned
- **Trust Automated Tools:** My manual pathing attempts on Route 22 failed due to cognitive bias. A robust, automated tool like `gem_pathfinder` is superior for complex navigation and should be trusted over my own flawed reasoning.
- **Systematic Problem-Solving:** When faced with a navigation paradox, like on Route 22, I must avoid chaotic, repeated manual attempts. The correct approach is to trust the game state data (e.g., `navigable_warps`) as the source of truth and systematically eliminate possibilities.
- **Efficient Debugging:** Repetitively running the same failing test case is inefficient. I must vary the test conditions (e.g., change the target destination) to gather new diagnostic data and isolate bugs more effectively.
- **Immediate Action:** Deferring tasks like tool repair or documentation is a critical error. All maintenance and data logging must be done in the immediate turn of discovery to maintain a coherent internal state.

# V. Future Development Ideas
- `puzzle_strategist_agent`: An agent to analyze environmental puzzles and suggest high-level solutions.
- `movement_tester_tool`: An automated tool to test tile transitions and log outcomes.
- `team_builder_agent`: An agent to suggest optimal party compositions for major challenges.
- `hm_troubleshooter_agent`: An agent to automate testing of HM usage when it fails.
- `fly_helper_tool`: A tool to automate selecting a destination from the Fly menu.

# VI. Tool Development Bugs & Fixes
- **Defeated Trainer Impassability Bug:** Both gem_pathfinder and boulder_puzzle_solver incorrectly treated defeated trainers as impassable. A fix has been implemented to ignore trainers marked with '☠️', but this fix is pending successful real-world verification.
- **Victory Road 1F - Boulder/Steps Interaction (Confirmed):** Boulders cannot be pushed onto `steps` tiles. This was confirmed after multiple failed attempts to push the boulder at (6, 15) north onto the steps at (6, 14).
- **gem_pathfinder Critical Failure:** The tool is fundamentally broken. It fails to find simple, known-valid paths (e.g., from (3,11) to the entrance at (9,18) on Victory Road 1F). It cannot be trusted for navigation until it is completely rewritten or thoroughly debugged. All navigation must be performed manually.