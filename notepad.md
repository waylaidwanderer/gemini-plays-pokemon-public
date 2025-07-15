# I. Core Principles & Lessons Learned
- **Immediate Maintenance & Escalation:** I must perform maintenance (notepad, agents) and fix tools *immediately* when a manual approach fails repeatedly. Deferring these actions is a critical process failure.
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
- `gate_offscreen`: A gate not currently on screen. Its state is unknown and treated as potentially open for pathfinding. Upon entering the screen, its state can be revealed as `open_gate` or `closed_gate`.
- `closed_gate`: A gate that is visibly closed and acts as an impassable wall.
- `open_gate`: A gate that is visibly open and acts as ground.
- `Switch Interaction`: Switches can appear on impassable tiles. They must be interacted with by standing on an adjacent tile (usually below) and facing the switch.
- `secret_passage`: Certain `impassable` wall tiles can be walked through. These are not visually distinct.

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

# III. Current Objective: Find the Secret Key in the Pokemon Mansion

## A. Mansion Puzzle State
- **1F Switch (3, 6):** Controls east/west gates, alternates. Current state: **Toggled once** from original.
- **2F Switch (3, 12):** Also controls gates. Current state: **Pressed 6 times (original state)**.
- **Gate at 2F (8, 23):** Currently **CLOSED**.
- **3F:** Western area is a confirmed dead end.

## B. Current Plan (from `puzzle_solver_agent`)
**Systematic Switch Combination Testing:**
1.  **Hypothesis 1 (SUCCESS):** The 2F switch needs to be toggled from its original state.
    - **Outcome:** The gate at (8, 23) is now OPEN.
    - **Conclusion:** The agent's first hypothesis was correct. The gate opened.

**Hypothesis 2 (Current):** The path beyond the open gate is still blocked. The impassable wall at (15, 23) might be a secret passage that is only active in this specific switch configuration.
    - **Test:** Navigate to the wall at (15, 23) and attempt to walk through it.
    - **Expected Outcome:** The wall will now be passable.
- **Gate/Warp Interaction:** A tile can be both a gate and a warp. Even if a gate is visually closed, the warp can still be reachable and usable if listed as such in the Game State Information.

# V. Mansion Diaries
- **Diary 1 (2F):** "July 5. Guyana, South America. A new POKéMON was discovered deep in the jungle."
- **Diary 2 (2F):** "July 10. We christened the newly discovered POKéMON, MEW."
- **Tile Mechanics:** `warp`: A tile that transports the player to another location, either on the same map or a different one.- **Diary 1 (2F):** "July 5. Guyana, South America. A new POKéMON was discovered deep in the jungle."
- **Diary 2 (2F):** "July 10. We christened the newly discovered POKéMON, MEW."
- `warp`: A tile that transports the player to another location, either on the same map or a different one.