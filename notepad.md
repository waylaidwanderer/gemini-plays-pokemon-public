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
- **Pokemon Mansion 2F Puzzle:** I am currently trapped in the NW corner of 2F. The switch at (3, 12), triggered by interacting with the floor at (3, 13), seems to be the key, but I am stuck in a loop. The message 'Not quite yet!' suggests a condition is unmet. My current hypothesis is that I need to speak to the Super Nerd at (4, 18) for a new clue.

## III. Solved Puzzles Archive
- **Pokemon Mansion B1F:** A switch at (19, 26) toggles gate sets via a dynamic trigger.
- **Pokemon Mansion 1F:** A secret switch in the statue at (3, 6) opens northern gates. Eastern gates at (25, 14) open via a hidden trigger.