# I. Core Principles & Lessons Learned
- **Immediate Maintenance & Escalation:** I must perform maintenance (notepad, agents) and escalate to powerful tools (like the `puzzle_solver_agent`) *immediately* when a manual approach fails repeatedly. Deferring these actions is a critical process failure.
- **Combat Confirmation Bias:** I must actively try to *disprove* my hypotheses. I wasted significant time on the 'battle reset' theory and assuming my `path_planner` was broken because I was seeking to confirm a past success instead of objectively testing. This is a major cognitive trap to avoid.
- **Agent & Tool Trust is Mandatory:** I MUST trust my custom agents' and tools' advice. Their purpose is to perform complex reasoning and calculations I cannot. My failure to use the `puzzle_solver_agent` and my initial distrust of the `path_planner`'s output caused significant delays.
- **Systematic Problem Solving:** For any puzzle, I must use my notepad to log observations, form a single testable hypothesis, record the test and its outcome, and then form a conclusion. This structured approach prevents chaos and tunnel vision.

# II. Game Mechanics & Battle Intel

## A. Tile Mechanics & Traversal
- This section is for documenting the behavior of different tile types as I discover them.

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
- **'No Will to Fight':** After a Pokémon faints, attempting to switch in the next Pokémon can sometimes fail with the message 'There's no will to fight!'. The cause is unknown, but trying again on the next turn was successful.
- **THUNDERBOLT vs. DIG:** THUNDERBOLT can hit an opponent while it is underground using DIG. This is contrary to standard mechanics and resulted in an accidental knockout when trying to faint.

# III. Active Puzzles
- **Pokemon Mansion B1F - Gate Switch Puzzle:** 
  - **Hypothesis 1 (Failed):** The switch at (19, 26) is multi-state. Pressing it a second time would open the eastern gates. 
    - **Test:** Pressed the switch at (19, 26) twice. 
    - **Outcome:** The first press opened the western gates. The second press did nothing. 
    - **Conclusion:** The switch is not a simple toggle. A new approach is needed.
  - **New Plan:** There are reachable unseen tiles in the western section of this floor. My next step is to explore them.

# IV. Solved Puzzles
- **Pokemon Mansion - Trapped Corridor:** Discovered a hidden one-way passage at 1F (27, 26). The only way to make the wall passable from the south again was to win a wild battle, which resets the tile's state.
- **Pokemon Mansion 1F - Eastern Wing Gate & Positional Trigger:** The gate at (25, 14) is controlled by the switch at (3, 6). Additionally, a positional trigger at (12,10) on 1F closes the gates at (17,8) and (18,8). The switch at (3,6) re-opens them. Direct interaction with the gate does not work.
- **Diary Interaction:** Diaries must be interacted with from the side, not from below.