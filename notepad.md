# I. Core Principles & Lessons Learned
- **Immediate Maintenance & Escalation:** I must perform maintenance (notepad, agents) and fix tools *immediately* when a manual approach fails repeatedly. Deferring these actions is a critical process failure. My repeated failure to fix my `path_planner` and `battle_strategist_agent` are prime examples of this lapse.
- **Combat Confirmation Bias:** I must actively try to *disprove* my hypotheses. I wasted significant time assuming my agents were correct because I was seeking confirmation, rather than testing their limits and questioning my own assumptions.
- **Agent & Tool Trust is Mandatory (but requires verification):** I MUST trust my custom agents' and tools' advice, but this trust must be earned through verification. When an agent fails, it must be refined immediately.
- **Systematic Problem Solving:** For any puzzle, I must use my notepad to log observations, form a single testable hypothesis, record the test and its outcome, and then form a conclusion. This structured approach prevents chaos and tunnel vision.

# II. Game Mechanics & Battle Intel

## A. Tile Mechanics & Traversal
- `ground`: Standard walkable tile.
- `impassable`: Walls, furniture, etc. Cannot be walked on.
- `grass`: Tall grass where wild Pokémon appear.
- `ledge`: One-way traversal, can be jumped down but not up.
- `water`: Requires SURF to traverse.
- `cuttable`: A tree that can be cut with HM01 Cut.
- `hole`: A tile that causes the player to fall to the floor below.
- `spinner_up/down/left/right`: Forces movement in a specific direction.
- `gate_offscreen`: Gates not on screen. Treated as potentially open for pathfinding.
- `closed_gate`: A gate that is visibly closed and acts as an impassable wall.
- `open_gate`: A gate that is visibly open and acts as ground.

## B. Confirmed ROM Hack Changes
### B1. Type Matchups & Immunities
- **Super Effective:** Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; Psychic > Flying; Ice > Ground; Ground > Poison; Ground > Fire; Rock > Fire
- **Not Very Effective:** Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); Ice !> Gyarados (Water/Flying); Poison !> Poison; Ice !> Water; Poison !> Ground
- **Immunities:** Flying-type immune to Ground-type moves; Ground-type Pokémon are immune to Electric-type moves; MUK immune to Poison-type moves; HYPNO immune to STUN SPORE (powder moves); MUK immune to THUNDER WAVE (Electric-type status move); MAROWAK (Ground-type) immune to POISON GAS (Poison-type move).

### B2. Battle & Field Mechanics
- **Evasion:** PSYWAVE and CONFUSE RAY can fail against targets with high evasion boosts.
- **Safari Zone:** Has a time limit. When it expires, the player is warped back to the Safari Zone Gate.
- **Gym Battle Loss:** Losing a battle inside a gym does NOT warp you to a Pokémon Center.
- **FLY in battle:** The move FLY can be used to defeat a wild Pokémon and end the battle, even when indoors. This acts as an escape method.
- **FLY in field:** Cannot be used indoors to escape a building.
- **ROAR in battle:** Can end a wild battle by forcing the player's Pokémon to run away.
- **Item Use on Fainted Pokemon:** A FULL RESTORE will not work on a fainted Pokémon.

# III. Active Puzzles

- **Pokemon Mansion 1F - Eastern Corridor Trap:**
  - **Status:** Currently trapped. Goal is to black out.
  - **Hypothesis:** The intended escape is to 'black out'.
  - **Attempt #1 (Weakest Attack):** FAILED. CRAG one-shot the opponent Raticate with STRENGTH despite it being the weakest move.
  - **Attempt #2 (Weakest Attack vs Raticate):** FAILED. CRAG one-shot the opponent Raticate with STRENGTH.
  - **Attempt #3 (Run vs Growlithe):** FAILED (succeeded). Escaped the battle.
  - **Attempt #4 (Weakest Attack vs Growlithe):** FAILED. CRAG one-shot the opponent Growlithe with STRENGTH.
  - **Conclusion:** Both attacking and running are ineffective strategies for fainting. A new approach is required.
  - **Active Plan (Attempt #5):** Consult the `puzzle_solver_agent` with the full context of the paradox (too strong to lose, too fast to fail to run) to generate new hypotheses.

# IV. Solved Puzzles & Key Discoveries
- **Pokemon Mansion 2F - Trapped Room:** Escaped by blacking out.
- **Pokemon Mansion B1F - Gate Switch Puzzle:** Switch at (19, 26) opens northern and western gates.
- **Switch Interaction:** Switches must be interacted with by standing on the tile directly below them and facing up.