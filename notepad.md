# I. Core Principles & Lessons Learned
- **Immediate Maintenance & Escalation:** I must perform maintenance (notepad, agents) and fix tools *immediately* when a manual approach fails repeatedly. Deferring these actions is a critical process failure. My repeated failure to fix my `path_planner` tool is a prime example of this lapse.
- **Combat Confirmation Bias:** I must actively try to *disprove* my hypotheses. I wasted significant time assuming my `path_planner` was correct because I was seeking to confirm it worked, rather than testing its limits and questioning my own assumption that the map was fully connected.
- **Agent & Tool Trust is Mandatory:** I MUST trust my custom agents' and tools' advice. My `puzzle_solver_agent` correctly identified the eastern corridor as a potential trap, which I initially dismissed.
- **Systematic Problem Solving:** For any puzzle, I must use my notepad to log observations, form a single testable hypothesis, record the test and its outcome, and then form a conclusion. This structured approach prevents chaos and tunnel vision.

# II. Game Mechanics & Battle Intel

## A. Tile Mechanics & Traversal
- `ground`: Standard walkable tile.
- `impassable`: Walls, furniture, etc. Cannot be walked on.
- `gate_offscreen`: These gates are not on screen. For pathfinding, they must be treated as potentially open to encourage exploration of routes that go off-screen.
- `closed_gate`: A gate that is visibly closed and acts as an impassable wall.
- `open_gate`: A gate that is visibly open and acts as ground.
- `hole`: A tile that causes the player to fall to the floor below.
- `water`: Requires SURF to traverse.

## B. Confirmed ROM Hack Changes
### B1. Type Matchups & Immunities
- **Super Effective:** Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; Psychic > Flying; Ice > Ground; Ground > Poison; Ground > Fire; Rock > Fire
- **Not Very Effective:** Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); Ice !> Gyarados (Water/Flying); Poison !> Poison; Ice !> Water; Poison !> Ground
- **Immunities:** Flying-type immune to Ground-type moves; Ground-type Pokémon are immune to Electric-type moves; MUK immune to Poison-type moves; HYPNO immune to STUN SPORE (powder moves); MUK immune to THUNDER WAVE (Electric-type status move); MAROWAK (Ground-type) immune to POISON GAS (Poison-type move).

### B2. Battle & Field Mechanics
- **Evasion:** PSYWAVE and CONFUSE RAY can fail against targets with high evasion boosts.
- **Safari Zone:** Has a time limit. When it expires, the player is warped back to the Safari Zone Gate.
- **Gym Battle Loss:** Losing a battle inside a gym does NOT warp you to a Pokémon Center.
- **Run from Battle Mechanic:** Attempting to switch Pokémon from the party screen can sometimes result in running from the battle instead.
- **FLY in battle:** The move FLY can be used to defeat a wild Pokémon and end the battle, even when indoors. This acts as an escape method.
- **FLY in field:** Cannot be used indoors to escape a building.
- **ROAR in battle:** Can end a wild battle by forcing the player's Pokémon to run away.
- **Item Use on Fainted Pokemon:** A FULL RESTORE will not work on a fainted Pokémon.

# III. Active Puzzles

- **Pokemon Mansion 1F - Eastern Corridor Trap:**
  - **Status:** Currently trapped. Blackout attempt #1 failed (CRAG one-shot the opponent).
  - **Hypothesis:** The intended escape is to 'black out'.
  - **Active Plan (Attempt #2):** Intentionally fail to run from a wild battle to take damage without attacking, leading to a faint.

# IV. Solved Puzzles & Key Discoveries
- **Pokemon Mansion 2F - Trapped Room (SOLVED):** Escaped by blacking out after the last party member fainted in a wild battle.
- **Pokemon Mansion B1F - Gate Switch Puzzle (SOLVED):** The switch at (19, 26) opens the northern and western gates.
- **Switch Interaction:** Switches must be interacted with by standing on the tile directly below them and facing up.
- **Diary Interaction:** Diaries must be interacted with from the side, not from below.