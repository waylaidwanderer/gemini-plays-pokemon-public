## I. Core Protocols & Game Philosophy
- **Immediate Data Management:** I will use `define_map_marker` and `notepad_edit` on the *same turn* a discovery is made. Deferring tasks is a critical failure.
- **Agent & Tool Protocol:** Agent and tool refinement is an IMMEDIATE action. If a tool is faulty or a better one can be conceived, I MUST define/redefine it on the IMMEDIATE next turn.
- **Hypothesis-Driven Gameplay:** I will rigorously document my hypotheses, tests, and conclusions in my notepad. I will avoid repeating failed strategies and will pivot to new goals if progress stalls after multiple documented attempts.

## II. Game Mechanics & Battle Intel
### A. Tile Mechanics & Traversal Rules
- **Ground/Impassable:** `ground` tiles are walkable, `impassable` tiles are solid walls. All objects (NPCs, items, signs) function as impassable walls.
- **Ledges:** One-way only. Can be jumped down (from Y-1 to Y+2 in one move), but are impassable from below (Y+1) and from the sides (X-1, X+1).
- **Spinner Tiles:** Force movement in a specific direction. Destinations must be mapped manually.
- **Hole Tiles:** Warp tiles that lead to a lower map area. Often function as one-way drops.
- **Gates (`closed_gate`/`open_gate`):** The state of these can be toggled by switches or other triggers.

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

## III. Puzzle & Hypothesis Log
### A. In-Progress Puzzles & Active Hypotheses
#### A1. Pokemon Mansion Multi-Floor Puzzle
- **Observation:** I am physically isolated in the western corridor of 1F. The game guarantees the eastern gates at (25, 14) are reachable barriers, but my `pathfinder` tool cannot find a path on this floor.
- **Active Hypothesis:** The path to the eastern corridor of 1F is not on this floor. The 'Reachable Barrier' message, combined with the pathfinder's failure, strongly suggests the path is via a warp or hole on another floor (2F, 3F, or B1F) that leads back down to the isolated eastern section of 1F.

### B. Solved Puzzles & Confirmed Mechanics
- **1F West Switch (Confirmed):** The switch at (3, 6) on 1F alternates between opening two sets of gates. First press opens the gates at (25, 14). A second press closes those and opens the gates at (17, 8). This switch does NOT solve the main puzzle of reaching the eastern corridor.
- **B1F Dynamic Gates:** The switch at (19, 26) toggles which set of gates (Western, Northern, or Eastern) is affected by a dynamic trigger.

### C. Deprecated Hypotheses (Pokemon Mansion 1F Puzzle)
- **Direct Path from West to East on 1F:** This was my initial assumption, but my `pathfinder` tool, even after being fixed, could not find a path. This confirms the solution is not a simple walk.
- **Alternating Switch Solution:** Repeatedly flipping the switch at (3, 6) only toggles between two states and does not grant access to the sealed eastern room. (Failed after 10+ attempts).
- **Multi-floor Solution (Direct Trigger):** The trigger for the 1F sealed room is located on 2F or 3F and directly affects the 1F gates. (This is a secondary hypothesis to return to if the systematic search fails).