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
- **Pokemon Mansion 1F 'Reachable Barrier' Contradiction:** The game's source of truth insists multiple closed gates are 'Reachable Barriers', but they appear impassable. All standard interaction attempts have failed. The puzzle_solver_agent has identified this contradiction as the key.

### B. Solved Puzzles
- **Pokemon Mansion B1F Dynamic Gates (Solved):** The switch at (19, 26) toggles which set of gates (Western, Northern, or Eastern) is affected by a dynamic trigger.

### C. Deprecated Hypotheses (Pokemon Mansion 1F)
- **Walk-Through Gates (Failed - 2 attempts):** Hypothesized that 'reachable' closed gates could be walked through. Tested on gates at (27, 28) and (28, 28).
- **Direct Gate Interaction (Failed - 2 attempts):** Hypothesized gates could be opened by direct interaction. Tested on gates at (27, 28) and (28, 28).
- **Hidden Item (Failed - 1 attempt):** Hypothesized a hidden item was needed. Used ITEMFINDER, found nothing.
- **Hidden Switch (Failed - 1 attempt):** Hypothesized a hidden switch was on an adjacent wall tile. Interacted with wall at (28, 28).
- **Pikachu Interaction (Failed - 2 attempts):** Hypothesized interacting with Pikachu was the trigger. Tested at (27, 27) and (22, 17).
- **Advanced Pathfinder (Failed - 1 attempt):** Hypothesized a simple geometric path exists through impassable tiles. Path was found by tool but blocked by physical wall at (28, 19).
- **Floor Pressure Plate (Failed - 1 attempt):** Hypothesized a hidden floor trigger opens the gates. Pathfinding to test tile (21, 19) failed.
- **Distant Switch (Failed - 1 attempt):** Hypothesized the 'Mansion Switch' at (3,6) was the trigger. Pathfinding to switch failed.
- **Fake Wall (Failed - 1 attempt):** Hypothesized a 'fake wall' exists. 
    - **Test (Failed):** Walked into wall at (25, 20).
    - **Test (Failed):** Walked into wall at (25, 21).
    - **Test (Failed):** Walked into wall at (25, 22).
    - **Test (Failed):** Walked into wall at (25, 23).
    - **Test (Failed):** Walked into wall at (25, 24).
    - **Test (Failed):** Walked into wall at (25, 22).
- **Main Switch Interaction (Failed - 2 attempts):** Hypothesized the main switch at (3,6) would open the southern gates. Interacting with it from the adjacent tile at (4,6) had no effect.