# I. Core Principles & Lessons Learned
- **Immediate Maintenance & Escalation:** I must perform maintenance (notepad, agents) and fix tools *immediately* when a manual approach fails repeatedly. Deferring these actions is a critical process failure. My repeated failure to fix my `path_planner` tool is a prime example of this lapse.
- **Combat Confirmation Bias:** I must actively try to *disprove* my hypotheses. I wasted significant time assuming my `path_planner` was correct because I was seeking to confirm it worked, rather than testing its limits.
- **Agent & Tool Trust is Mandatory:** I MUST trust my custom agents' and tools' advice. 
- **Systematic Problem Solving:** For any puzzle, I must use my notepad to log observations, form a single testable hypothesis, record the test and its outcome, and then form a conclusion. This structured approach prevents chaos and tunnel vision.

# II. Game Mechanics & Battle Intel

## A. Tile Mechanics & Traversal
- `gate_offscreen`: These tiles should be treated as walkable for pathfinding purposes to encourage exploration of routes that go off-screen.
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
- **Run from Battle Mechanic:** Attempting to switch Pokémon from the party screen can sometimes result in running from the battle instead.
- **FLY in battle:** The move FLY can be used to defeat a wild Pokémon and end the battle, even when indoors. This acts as an escape method.
- **ROAR in battle:** Can end a wild battle by forcing the player's Pokémon to run away.
- **Item Use on Fainted Pokemon:** A FULL RESTORE will not work on a fainted Pokémon.
- **Weird Typing:** My LAPRAS (NEPTUNE) was displayed as a GHOST type in battle. This needs further investigation.
- **'No Will to Fight':** After a Pokémon faints, attempting to switch in the next Pokémon can sometimes fail with the message 'There's no will to fight!'.
- **THUNDERBOLT vs. DIG:** THUNDERBOLT can hit an opponent while it is underground using DIG.

# III. Active Puzzles
- **Pokemon Mansion B1F - Gate Switch Puzzle:**
  - **Observation:** There are three sets of gates: Northern, Western, and Eastern. A switch at (19, 26) seems to control them. There are also unseen tiles in the far west.
  - **Current Hypothesis:** The solution to opening the eastern gates lies within the unexplored western section of the floor.
  - **Test Plan:** Navigate to the unseen tiles in the west and explore the area for new switches or clues.

# IV. Solved & Failed Puzzles
- **Pokemon Mansion B1F - Switch Hypothesis (Failed):**
    - **Hypothesis:** The switch at (19, 26) is multi-state. Pressing it a second time would open the eastern gates. 
    - **Test:** Pressed the switch at (19, 26) twice. 
    - **Outcome:** The first press opened the western gates. The second press did nothing. 
    - **Conclusion:** The switch is not a simple toggle.
- **Pokemon Mansion - Trapped Corridor:** Discovered a hidden one-way passage at 1F (27, 26). Winning a wild battle resets the tile's state.
- **Pokemon Mansion 1F - Eastern Wing Gate & Positional Trigger:** The gate at (25, 14) is controlled by the switch at (3, 6). A positional trigger at (12,10) on 1F closes the gates at (17,8) and (18,8). The switch at (3,6) re-opens them.
- **Diary Interaction:** Diaries must be interacted with from the side, not from below.