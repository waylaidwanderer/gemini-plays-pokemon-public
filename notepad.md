## I. Game Mechanics & Battle Intel

### A. Tile Mechanics & Traversal Rules
- **Ground/Impassable:** `ground` tiles are walkable, `impassable` tiles are solid walls. All objects (NPCs, items, signs) function as impassable walls.
- **Water:** Surfable tiles. To initiate SURF, I must be adjacent to a water tile and use the move from the party menu. Only Water-type Pokémon can use SURF in the field.
- **Gates (`closed_gate`/`open_gate`/`gate_offscreen`):** `closed_gate` tiles are impassable. `open_gate` tiles are open and act as `ground`. `gate_offscreen` represents a gate whose state is unknown because it's not on screen. The state of these can be toggled by switches or other triggers like player movement (pressure plates).
- **Ledges:** One-way only. Can be jumped down (from Y-1 to Y+2 in one move), but are impassable from below (Y+1) and from the sides (X-1, X+1).
- **Spinner Tiles:** Force movement in a specific direction. Destinations must be mapped manually.
- **Hole Tiles:** Warp tiles that lead to a lower map area. Often function as one-way drops.

### B. Confirmed ROM Hack Changes
#### B1. Type Matchups & Immunities
- **Super Effective:** Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; **Psychic > Flying** (confirmed: KADABRA's PSYBEAM vs ECHO's GOLBAT)
- **Not Very Effective:** Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); **Ice !> Gyarados (Water/Flying)** (confirmed: NEPTUNE's AURORA BEAM vs Fisherman's GYARADOS); Poison !> Poison (confirmed: ECHO's SLUDGE vs MUK).
- **Immunities:** Flying-type immune to Ground-type moves; MUK immune to Poison-type moves; **Electric is effective vs Sabrina's Psychic team, confirming Psychic types are NOT immune to Electric.**; **HYPNO immune to STUN SPORE** (powder moves); **MUK immune to THUNDER WAVE** (Electric-type status move).

#### B2. Battle & Field Mechanics
- **Evasion:** PSYWAVE and CONFUSE RAY can fail against targets with high evasion boosts (e.g., from MINIMIZE).
- **'No Will to Fight':** A fainted or sleeping Pokémon cannot be switched into battle.
- **EXP Distribution:** Experience is shared between the Pokémon that started the battle and any that participated via switch-in.
- **Safari Zone:** Has a time limit. When it expires, the player is warped back to the Safari Zone Gate.
- **Gym Battle Loss:** Losing a battle inside a gym does NOT warp you to a Pokémon Center. You respawn in front of the trainer you lost to.
- **Two-Turn Moves:** The `battle_strategist_agent` initially failed to account for the inefficiency of two-turn moves (like FLY) when a one-turn KO is possible. The agent has been refined to prioritize faster knockouts.

## II. Puzzle & Hypothesis Log

### A. Active Hypotheses
- **Pokemon Mansion 'Secret Key' Location:** The Cinnabar Gym is locked and requires a 'Secret Key'. The most logical location for this key is somewhere within the Pokémon Mansion.
- **Pokemon Mansion 'Alternating Doors':** The mansion contains puzzles where gates open and close based on player movement, not just direct switch interaction. This was confirmed on 1F when gates at (17, 8) and later (25, 14) changed state as I moved. The solution likely involves navigating a specific path to trigger the correct sequence of gate changes.
- **Untested Assumption (Multi-Floor Interaction):** The puzzles on each floor might not be self-contained. A switch on one floor could alter the state of another. If I get stuck again, I will perform a systematic test.

### B. Solved Puzzles Archive
- **Pokemon Mansion B1F:** A switch at (19, 26) toggles gate sets. It uses a two-step 'prime and trigger' mechanic: flip the switch to 'prime' a set of gates, then walk to them to open them.
- **Pokemon Mansion 1F (Statue Switch):** A secret statue switch at (3, 6) opens the eastern gates at (17,8).

## III. Tool & Agent Development Log

### A. Agent Failures & Lessons Learned
- **`puzzle_master_agent` (Looping Failure):** The agent repeatedly suggested interacting with the same switch on Mansion 2F, even after it failed to produce results. This indicates a failure to recognize a loop and generate creative, alternative hypotheses. It has been refined with a loop-breaking directive.

### B. Tool Flaws & Consolidations
- **`advanced_pathfinder` (Fixed):** This tool was critically flawed. It was designed to find hidden passages by ignoring tile types, but it incorrectly suggested paths through 'impassable' tiles, which the game engine blocks. **Lesson:** Tools must respect fundamental game mechanics. The tool has been refined to ignore puzzle-specific barriers (like `closed_gate`) while still respecting absolute barriers (`impassable`).
- **`find_path` (Consolidated):** The `find_path_to_adjacent` tool was redundant. Its functionality has been merged into the main `find_path` tool with an optional `adjacent` parameter, creating a single, more robust pathfinding utility.

### C. Discovered Non-Standard Mechanics
- **Pikachu Traversal:** I can walk through the Pikachu sprite. This is a key mechanic for navigating tight spaces he might be blocking.

### A. Current Puzzle: Pokemon Mansion
- **Objective:** Find the 'Secret Key' to unlock the Cinnabar Gym.
- **Hypothesis:** The key is located somewhere within the Pokémon Mansion.
- **Key Mechanic:** The mansion's puzzles are based on an 'Alternating Doors' system. A single switch can toggle the state of multiple gates across the floor. The switch at (3, 6) on 1F controls both the northern gates at (17,8) and the eastern gates at (25,14). I need to navigate between floors to reach different sections of 1F to proceed.

### C. Current Puzzle: Mansion 1F Corridor Contradiction
- **Contradiction:** The game state lists the gates at (25, 14) as 'Reachable Barriers', but all attempts to find a path through standard movement or local interactions have failed.
- **Conclusion:** This proves a non-standard path or traversal mechanic exists on this floor.