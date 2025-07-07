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
- **Alternating Doors:** A puzzle mechanic where gates open and close based on player movement or switch activation in a specific sequence.

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
#### A1. Pokemon Mansion 1F - Sealed Room Puzzle
- **Observation:** Trapped in a sealed room on 1F. Gates at (21, 18) and (22, 18) are closed. System confirmed these are 'Reachable Barriers'.
- **Active Hypothesis:** The trigger for the 1F gates is located on another floor, likely B1F. The 'Reachable Barriers' notification may refer only to the gates' location, not their trigger's location.

### B. Solved Puzzles & Confirmed Mechanics
- **Pokemon Mansion - Multi-Floor Gate System:**
  - **2F Switch (3, 12):** Toggles northern gates (10, 5/6) and southern gates (8, 23/24) on 2F.
  - **3F Switch (11, 6):** Toggles central gates (16, 5/6) and southern gates (16, 11/12) on 3F.
  - **B1F Dynamic Gates:** The switch at (19, 26) toggles which set of gates (Western, Northern, or Eastern) is affected by a dynamic trigger (likely timer or step-counter).

### C. Deprecated Hypotheses (Pokemon Mansion 1F Puzzle)
- Direct interaction with gates (1 attempt).
- Hidden switch in statues (1 attempt).
- Walking into the gates (1 attempt).
- Scientist interaction post-basement (1 attempt).
- ITEMFINDER use (1 attempt).
- Hidden pressure plate on floor (Exhaustive search of all 23 walkable tiles failed).
- Re-interacting with Scientist after exploring (1 attempt).