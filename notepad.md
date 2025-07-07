## I. Core Protocols & Game Philosophy
- **Immediate Data Management:** I will use `define_map_marker` and `notepad_edit` on the *same turn* a discovery is made. Deferring tasks is a critical failure.
- **Agent & Tool Protocol:** Agent and tool refinement is an IMMEDIATE action. If a tool is faulty or a better one can be conceived, I MUST define/redefine it on the IMMEDIATE next turn.
- **Hypothesis-Driven Gameplay:** I will rigorously document my hypotheses, tests, and conclusions in my notepad. I will avoid repeating failed strategies and will pivot to new goals if progress stalls after multiple documented attempts. When the game provides contradictory information (e.g., a barrier is marked as 'reachable' but a path cannot be found), my primary hypothesis must be that a non-standard game mechanic is at play, and my recommended action should be to test that possibility directly.

## II. Game Mechanics & Battle Intel
### A. Tile Mechanics & Traversal Rules
- **Ground/Impassable:** `ground` tiles are walkable, `impassable` tiles are solid walls. All objects (NPCs, items, signs) function as impassable walls.
- **Gates (`closed_gate`/`open_gate`):** `closed_gate` tiles are usually impassable barriers. `open_gate` tiles are previously closed gates that are now open and act as `ground`. The state of these can be toggled by switches or other triggers.
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

## III. Puzzle & Hypothesis Log
### A. Current Puzzles
- **Pokemon Mansion 2F Alternating Switch:** The switch at (3, 12) alternates between two states. State 1 opens the northern gates at (10, 5) and (10, 6). State 2 closes the northern gates and is intended to open the gates at (19, 9), (20, 9), (8, 23), and (8, 24). System has confirmed these four gates are 'Reachable Barriers', suggesting a way to open them exists on this floor. **Current Hypothesis:** Flipping the switch to State 2 is the first step. The next step is to find another trigger or path.

### B. Solved Puzzles
- **Pokemon Mansion 1F Alternating Switch (Solved):** The switch at (3, 6) is an alternating switch. Pressing it toggles between opening the eastern gates (25, 14) and the western gates (17, 8). The final solution requires opening the western gates, passing through them, which then automatically triggers the eastern gates to open, granting access to the southern area of the mansion.
- **Pokemon Mansion B1F Dynamic Gates (Solved):** The switch at (19, 26) toggles which set of gates (Western, Northern, or Eastern) is affected by a dynamic trigger.

### C. Deprecated Hypotheses
- **Multi-Floor Pathing Solution (Deprecated):** My initial hypothesis was that the path to the eastern side of 1F must be on another floor. **Conclusion:** This was invalidated by a system notification about 'Reachable Barriers' on 1F, confirming the solution is on the same floor.

#### B4. Pokemon Evolution & Moves
- **Marowak Evolution:** Confirmed that Marowak evolves from Cubone at Lv. 38.
- **REVENANT (Marowak) learned THRASH** at Lv. 38, replacing TAIL WHIP.
### Pokemon Mansion 1F - Gate Puzzle Plan
**Observation:** The system confirms the gates at (21, 18) and (27, 28) are reachable, but no direct path is visible. The switch at (3, 6) is the only interactive element.
**Hypothesis:** A specific sequence involving the switch is required to open all gates.
**Test Plan:**
1. Go to the switch at (3, 6) and interact with it to open the western gates at (17, 8).
2. Walk through the western gates.
3. **Expected Outcome:** The eastern gates at (25, 14) will open as a chain reaction.
4. **Test:** Proceed through the eastern gates and explore the newly accessible southern area.
5. **Expected Outcome:** Find a new trigger or item in the southern area that opens the final gates at (21, 18) and (27, 28).
6. **Conclusion:** To be determined after testing.