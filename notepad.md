## I. Game Mechanics & Battle Intel

### A. Tile Mechanics & Traversal Rules
- **Ground/Impassable:** `ground` tiles are walkable, `impassable` tiles are solid walls. All objects (NPCs, items, signs) function as impassable walls.
- **Water:** Surfable tiles. To initiate SURF, I must be adjacent to a water tile and use the move from the party menu. Only Water-type Pokémon can use SURF in the field.
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
- **Two-Turn Moves:** The `battle_strategist_agent` initially failed to account for the inefficiency of two-turn moves (like FLY) when a one-turn KO is possible. The agent has been refined to prioritize faster knockouts.

## II. Puzzle & Hypothesis Log

### A. Active Hypotheses
- **Pokemon Mansion 1F Alternating Switch:** The switch at (3, 6) is an alternating switch. The game indicates the eastern gates at (25, 14) are reachable, but they remain closed. The switch's message "Not quite yet!" implies a secondary condition is unmet. My current hypothesis is that the switch has more than two states, or another interaction is required elsewhere on the map after flipping the switch. **Test:** Flip the switch at (3, 6) and observe any changes to the gates.
- **Route 20 Rock Walls:** The impassable rock walls on Route 20 may not be static barriers. **Hypothesis:** The walls can be removed or passed through by an external trigger, item, or specific condition. **Test:** After returning to Route 20, I will attempt to interact ('A' button) with the walls and use the ITEMFINDER nearby.

### B. Solved Puzzles
- **Pokemon Mansion B1F Dynamic Gates (Solved):** The switch at (19, 26) toggles which set of gates (Western, Northern, or Eastern) is affected by a dynamic trigger.

### C. Deprecated Hypotheses
- **Multi-Floor Pathing Solution (Deprecated):** My initial hypothesis was that the path to the eastern side of 1F must be on another floor. **Conclusion:** This was invalidated by a system notification about 'Reachable Barriers' on 1F, confirming the solution is on the same floor.
- **Direct Gate Interaction (Deprecated):** Hypothesized that the 'reachable' eastern gates at (25,14) and (26,14) could be opened by direct interaction ('A' button). **Conclusion:** Failed.
- **Hidden Item (Deprecated):** Hypothesized a hidden item was needed to open the eastern gates. **Conclusion:** ITEMFINDER found nothing.
- **Reachable Barrier Contradiction:** The game's source of truth insists that multiple closed gates on this floor are 'Reachable Barriers'. However, my pathfinding tools show I am in an isolated area and cannot reach them. This contradiction implies a hidden path or non-standard interaction mechanic is at play. All standard interaction attempts have failed.
- **Reachable Barrier Contradiction (NEW HYPOTHESIS):** The game's source of truth insists that multiple closed gates on this floor are 'Reachable Barriers', despite appearing impassable. My puzzle_solver_agent has identified this contradiction. **Hypothesis:** A non-standard game mechanic is at play, allowing passage through objects marked as 'reachable' even if their state is 'closed'. **Test:** Attempt to walk through the West Gates at (17,8).