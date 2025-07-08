## I. Game Mechanics & Battle Intel

### A. Tile Mechanics & Traversal Rules
- **Ground/Impassable:** `ground` tiles are walkable, `impassable` tiles are solid walls. All objects (NPCs, items, signs) function as impassable walls.
- **Water:** Surfable tiles. To initiate SURF, I must be adjacent to a water tile and use the move from the party menu. Only Water-type Pokémon can use SURF in the field.
- **Gates (`closed_gate`/`open_gate`/`gate_offscreen`):** `closed_gate` tiles are usually impassable barriers. `open_gate` tiles are previously closed gates that are now open and act as `ground`. `gate_offscreen` represents a gate whose state (open/closed) is unknown because it's not currently on my screen. The state of these can be toggled by switches or other triggers.
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
- **Pokemon Mansion 'Secret Key' Location:** The Cinnabar Gym is locked and requires a 'Secret Key'. The most logical location for this key is somewhere within the Pokémon Mansion. The 'Reachable Barriers' info confirms the gates inside are solvable.
- **Pokemon Mansion 2F Puzzle:** The puzzle involves a floor switch at (3, 13) that toggles the map's connectivity. The key is understanding that pressing the switch opens paths to distant, otherwise unreachable gates, a fact confirmed by the 'Reachable Barriers' API info. The solution is not local to the switch.

### B. Solved Puzzles Archive
- **Pokemon Mansion B1F:** A switch at (19, 26) toggles gate sets. It uses a two-step 'prime and trigger' mechanic: flip the switch to 'prime' a set of gates, then walk to them to open them.
- **Pokemon Mansion 1F:** A secret statue switch at (3, 6) opens northern gates. Eastern gates at (25, 14) are on a hidden trigger.

## III. Tool & Agent Development Log

### A. Agent Failures & Lessons Learned
- **`puzzle_solver_agent` (Deleted):** This agent repeatedly failed to recognize the contradiction between the game's 'Reachable Barriers' data and the `find_path` tool's inability to find a path. **CRITICAL OVERWATCH NOTE (Turn 57391):** Deleting this agent after four failed refinements was a severe process violation. The core principle is to refine iteratively; deletion is a last resort. I must adhere to this protocol.
- **`puzzle_master_agent` (Active):** The first version of this agent failed by suggesting a move into a tile occupied by an NPC. This highlights the need for all agents to validate their output against the current map state, including sprite locations, before making a suggestion.
- **`puzzle_master_agent` (Failure #2):** The agent again failed to consider player reachability. It suggested interacting with a diary that was inaccessible from my trapped location. This confirms the agent MUST validate path existence from the player's current position to the location of its suggested action before outputting a plan.

### B. Tool Flaws
- **`advanced_pathfinder` (Fixed):** This tool was critically flawed. It was designed to find hidden passages by ignoring tile types, but it incorrectly suggested paths through 'impassable' tiles, which the game engine blocks. **Lesson:** Tools must respect fundamental game mechanics. The tool has been refined to ignore puzzle-specific barriers (like `closed_gate`) while still respecting absolute barriers (`impassable`).

### C. Discovered Non-Standard Mechanics
- **Pikachu Traversal:** I can walk through the Pikachu sprite. This is a key mechanic for navigating tight spaces he might be blocking.
- **`puzzle_master_agent` (Reflection):** I committed a process violation by not refining the agent immediately after its first failure (suggesting interaction with Pikachu). I allowed a second failure (suggesting interaction with an unreachable object) before correcting the core issue. **Lesson:** Agent refinement must be performed instantly upon identifying a flaw, without exception.
- **Mansion Puzzle Contingency:** If interacting with the known statue switches continues to fail, my next hypothesis will be that there are hidden floor-plate triggers. I will test this by systematically walking over every accessible tile in the puzzle areas.