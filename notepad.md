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
- **Gates:** `closed_gate` tiles are impassable barriers. `open_gate` tiles are unlocked and function as `ground`. Some are opened by switches, others require a KEY CARD.

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
*Guiding Principle: I will rigorously test any hypothesis by attempting to falsify it. A single confirmation is not enough; I must try to prove my own conclusions wrong to ensure they are robust.*

### A. Solved Puzzles & Confirmed Mechanics
- **Pokemon Mansion Puzzle (Floors 2-3):** The mansion uses an 'alternating doors' system controlled by switches.
  - **2F Switch (3, 12):** Toggles northern gates (10, 5/6) and southern gates (8, 23/24). (Confirmed T53987)
  - **3F Switch (11, 6):** Toggles central gates (16, 5/6) and southern gates (16, 11/12). (Confirmed T52735)

### B. In-Progress Puzzles & Active Hypotheses
#### B1. Pokemon Mansion Puzzles
- **B1F Switch (19, 26) - Complex Gate Control:** This switch has a multi-state function.
  - **State 1 (Initial):** Western gates (14, 23/24) are open. Eastern gates (27, 18/19) are closed.
  - **State 2 (First Flip):** Western gates close. Eastern gates open. Northern gates (17, 17/18) remain closed.
  - **State 3 (Second Flip):** Western gates re-open. Eastern gates close.
  - **Conclusion:** The switch cycles between opening the western and eastern paths. It does not appear to affect the northern gates or the gates on 1F.
- **1F Gate Puzzle (21, 18 & 22, 18):** These gates have trapped me in an isolated room. My initial hypothesis that the B1F switch controlled them was incorrect. The system has confirmed these gates are 'Reachable Barriers', meaning the solution must be within this sealed section of 1F. My current hypothesis is that the gates open via a hidden mechanism or direct interaction from this side. Test 1: Interact directly with the gate at (21, 18) from the tile below it. Result: FAILED. The gate did not open.
- Test 2: Interact with the other gate at (22, 18). Result: FAILED. The gate did not open.

**Conclusion: Direct interaction with the gates is not the solution.**

### Agent-Assisted Puzzle Solving
**Agent Input:** Called `puzzle_solver_agent` with the current puzzle state (closed gates, defeated scientist).
**Agent Hypothesis:** A hidden, non-obvious switch exists within this sealed room, likely in a statue or piece of furniture.
**New Plan:** Systematically search the room for a hidden interactive object, starting with the statues.
- Test 3: Interacted with the statue at (19, 20) from (19, 21). Result: FAILED.
- Test 4: Interacted with the statue at (18, 20) from (18, 21). Result: FAILED. This statue is not the switch.
- Test 5: Interacted with the statue at (17, 20) from (17, 21). Result: FAILED. This statue is not the switch.