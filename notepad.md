## I. Game Mechanics & Battle Intel

### A. Tile Mechanics & Traversal Rules
- **Ground/Impassable:** `ground` tiles are walkable, `impassable` tiles are solid walls. All objects (NPCs, items, signs) function as impassable walls.
- **Water:** Surfable tiles. To initiate SURF, I must be adjacent to a water tile and use the move from the party menu. Only Water-type Pokémon can use SURF in the field.
- **Gates (`closed_gate`/`open_gate`/`gate_offscreen`):** `closed_gate` tiles are impassable. `open_gate` tiles are open and act as `ground`. `gate_offscreen` represents a gate whose state is unknown because it's not on screen. The state of these can be toggled by switches or other triggers like player movement (pressure plates).
- **Ledges:** One-way only. Can be jumped down (from Y-1 to Y+2 in one move), but are impassable from below (Y+1) and from the sides (X-1, X+1).
- **Spinner Tiles:** Force movement in a specific direction. Destinations must be mapped manually.
- **Hole Tiles:** Warp tiles that lead to a lower map area. Often function as one-way drops.
- **Scripted Event Tiles:** Some tiles trigger events. The tile in front of the Cinnabar Gym door (19, 5) pushes the player back and displays a 'locked' message.

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
- **Key Mechanic: 'Alternating Doors':** Switches, often hidden in statues, can open and close sets of gates. The effect can be on the same floor or different floors. Sometimes a switch needs to be 'primed' and then the player has to walk to the gate to trigger it to open.

### B. Solved Puzzles Archive
- **Pokemon Mansion B1F (Gate Switch):** A switch at (19, 26) toggles two sets of gates using a 'prime and trigger' mechanic. Flip the switch to prime a set, then walk to them to open.
- **Pokemon Mansion 1F (Statue Switch):** A secret statue switch at (3, 6) opens the eastern gates at (17,8).
- **Pokemon Mansion 2F (Pressure Plate Mechanic):** Confirmed a 'prime and trigger' mechanic. Walking onto certain tiles (e.g., (11, 10)) acts as a pressure plate, toggling the state of nearby gates (e.g., opening the gates at (10, 5) and (10, 6)). This explains the 'Reachable Barrier' contradiction without needing a hidden passage. My previous 'hidden passage' hypothesis was incorrect.

## III. Tool & Agent Development Log

### A. Agent Failures & Lessons Learned
- **`battle_strategist_agent` (Flawed Knowledge):** The agent repeatedly hallucinated Pokémon types from their nicknames. I have performed a major overhaul of its system prompt to force it to use only the provided type data, forbidding any inference.

### B. Tool Flaws & Consolidations
- **`advanced_pathfinder` (Fixed):** The tool now correctly treats `closed_gate` tiles as impassable.
- **`find_path` (Consolidated):** The `find_path_to_adjacent` tool was redundant and has been merged into the main `find_path` tool.

### C. Discovered Non-Standard Mechanics
- **Pikachu Traversal:** I can walk through the Pikachu sprite. This is a key mechanic for navigating tight spaces he might be blocking.