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
- **Pokemon Mansion 'Secret Key' Location:** The Cinnabar Gym is locked and requires a 'Secret Key'. The most logical location for this key is somewhere within the Pokémon Mansion.
- **Pokemon Mansion 'Alternating Doors':** The mansion contains puzzles where gates open and close based on player movement, not just direct switch interaction. This was confirmed on 1F when gates at (17, 8) and later (25, 14) changed state as I moved. The solution likely involves navigating a specific path to trigger the correct sequence of gate changes.
- **Untested Assumption (Multi-Floor Interaction):** The puzzles on each floor might not be self-contained. A switch on one floor could alter the state of another. If I get stuck again, I will perform a systematic test:
    1. Go to B1F, flip switch, check 1F/2F for changes.
    2. Go to 2F, flip switch, check 1F/B1F for changes.

## III. Tool & Agent Development Log

### A. Agent Failures & Lessons Learned

- **`puzzle_master_agent` (Active):** The first version of this agent failed by suggesting a move into a tile occupied by an NPC. This highlights the need for all agents to validate their output against the current map state, including sprite locations, before making a suggestion.
- **`puzzle_master_agent` (Failure #2):** The agent again failed to consider player reachability. It suggested interacting with a diary that was inaccessible from my trapped location. This confirms the agent MUST validate path existence from the player's current position to the location of its suggested action before outputting a plan.

### B. Tool Flaws
- **`advanced_pathfinder` (Fixed):** This tool was critically flawed. It was designed to find hidden passages by ignoring tile types, but it incorrectly suggested paths through 'impassable' tiles, which the game engine blocks. **Lesson:** Tools must respect fundamental game mechanics. The tool has been refined to ignore puzzle-specific barriers (like `closed_gate`) while still respecting absolute barriers (`impassable`).

### C. Discovered Non-Standard Mechanics
- **Pikachu Traversal:** I can walk through the Pikachu sprite. This is a key mechanic for navigating tight spaces he might be blocking.
- **`puzzle_master_agent` (Reflection):** I committed a process violation by not refining the agent immediately after its first failure (suggesting interaction with Pikachu). I allowed a second failure (suggesting interaction with an unreachable object) before correcting the core issue. **Lesson:** Agent refinement must be performed instantly upon identifying a flaw, without exception.
- **Untested Assumption (Multi-Floor Interaction):** The puzzle on Mansion 2F might not be self-contained. The switch at (3, 12) could potentially alter the state of other floors (1F or 3F), such as changing warp destinations or opening previously inaccessible paths. **Test:** After toggling the 2F switch, I must revisit 1F and 3F via the warps at (6, 11) and (8, 11) to check for any changes.