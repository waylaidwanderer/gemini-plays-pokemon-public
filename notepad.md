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
  - **Status:** Currently trapped. All agent-generated hypotheses have been tested and have failed.
  - **Failed Hypotheses Log:**
    - **Blackout (Weakest Attack):** FAILED (3 attempts). CRAG is too strong.
    - **Blackout (Run/Fail):** FAILED (2 attempts). Successfully ran away, which defeats the purpose of fainting.
    - **Blackout (Waste Turn w/ Item):** FAILED (1 attempt). Accidentally caught the Pokémon.
    - **Escape Item/Move:** FAILED. No Escape Rope or Pokémon with Dig.
    - **Hidden Switch:** FAILED. Checked all tiles in the corridor.
  - **Conclusion:** The only remaining possibility is a variation of the 'step-counter' gate hypothesis.
  - **Attempt #6 (Long Walk):** FAILED. A long, uninterrupted walk did not open the gate.
  - **Conclusion:** All conventional escape hypotheses have been exhausted. The only remaining solution is an unconventional blackout.
  - **New Hypothesis:** A specific wild Pokémon (Grimer) can inflict poison, allowing CRAG to faint from damage over time outside of battle.
  - **Active Plan:** SOLVED. The blackout strategy worked. To escape the corridor, the player's last conscious Pokémon must be poisoned. Then, in a subsequent battle, use a non-damaging move or item (like the POKé FLUTE) to waste turns, allowing the opponent to attack until the player's Pokémon faints.

# IV. Solved Puzzles & Key Discoveries
- **Pokemon Mansion 2F - Trapped Room:** Escaped by blacking out.
- **Pokemon Mansion B1F - Gate Switch Puzzle:** Switch at (19, 26) opens northern and western gates.
- **Switch Interaction:** Switches must be interacted with by standing on the tile directly below them and facing up.
  - **Attempt #5 (Hidden Switch):** FAILED. Systematically checked every tile in the corridor. No hidden switches found. All agent hypotheses are now exhausted. Re-attempting blackout strategy as the only remaining possibility.