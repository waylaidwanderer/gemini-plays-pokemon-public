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
- **Super Effective:** Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; **Psychic > Flying**
- **Not Very Effective:** Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); **Ice !> Gyarados (Water/Flying)**; Poison !> Poison.
- **Immunities:** Flying-type immune to Ground-type moves; MUK immune to Poison-type moves; **HYPNO immune to STUN SPORE** (powder moves); **MUK immune to THUNDER WAVE** (Electric-type status move).
- **Misc:** Ground is RESISTANT (0.5x) to Fire, NOT immune.

#### B2. Battle & Field Mechanics
- **Evasion:** PSYWAVE and CONFUSE RAY can fail against targets with high evasion boosts.
- **'No Will to Fight':** A fainted or sleeping Pokémon cannot be switched into battle.
- **Safari Zone:** Has a time limit. When it expires, the player is warped back to the Safari Zone Gate.
- **Gym Battle Loss:** Losing a battle inside a gym does NOT warp you to a Pokémon Center.

## II. Puzzle & Hypothesis Log

### A. Active Puzzle: Pokémon Mansion
- **Objective:** Find the 'Secret Key' for the Cinnabar Gym.
- **Key Mechanic:** 'Alternating Doors'. Switches on one floor can affect gates on the same or other floors.
- **Current Hypothesis:** The path forward on 1F requires dropping down from an upper floor into an isolated area.

### B. Solved Puzzles Archive
- **Pokemon Mansion B1F:** A switch at (19, 26) toggles gate sets. It uses a two-step 'prime and trigger' mechanic: flip the switch to 'prime' a set of gates, then walk to them to open them.
- **Pokemon Mansion 1F (Statue Switch):** A secret statue switch at (3, 6) opens the eastern gates at (17,8).

### B. Solved Puzzles Archive
- **Pokemon Mansion B1F:** A switch at (19, 26) toggles gate sets. It uses a two-step 'prime and trigger' mechanic: flip the switch to 'prime' a set of gates, then walk to them to open them.
- **Pokemon Mansion 1F (Statue Switch):** A secret statue switch at (3, 6) opens the eastern gates at (17,8).
- **Pokemon Mansion 1F (Statue Switch):** A secret statue switch at (3, 6) opens the eastern gates at (17,8).
- **Pokemon Mansion 1F (Statue Switch):** A secret statue switch at (3, 6) opens the eastern gates at (17,8).
- **Pokemon Mansion B1F:** A switch at (19, 26) toggles gate sets. It uses a two-step 'prime and trigger' mechanic: flip the switch to 'prime' a set of gates, then walk to them to open them.
- **Pokemon Mansion 1F (Statue Switch):** A secret statue switch at (3, 6) opens the eastern gates at (17,8).

## III. Tool & Agent Development Log

### A. Agent Failures & Lessons Learned
- **`battle_strategist_agent` (Flawed Knowledge):** The agent initially had incorrect type matchup knowledge (e.g., assuming Ground was immune to Fire). It has been refined with the correct type chart and stronger directives to prioritize survival.

### B. Tool Flaws & Consolidations
- **`advanced_pathfinder` (Fixed):** The tool now correctly treats `closed_gate` tiles as impassable.
- **`find_path` (Consolidated):** The `find_path_to_adjacent` tool was redundant and has been merged into the main `find_path` tool.

### C. Discovered Non-Standard Mechanics
- **Pikachu Traversal:** I can walk through the Pikachu sprite. This is a key mechanic for navigating tight spaces he might be blocking.