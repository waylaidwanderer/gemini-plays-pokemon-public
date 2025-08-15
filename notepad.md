# I. Game Mechanics & World Knowledge

## A. Core Gameplay (Verified)
- **Battle Style:** Set mode.
- **Items in Battle:** Prohibited.
- **Level Caps:** Active and enforced.
- **PC Interaction:** To use a PC, stand on the tile directly *below* it and face *up* before pressing 'A'.
- **Menu Navigation:** The 'B' button is the primary method for exiting/canceling out of menus.
- **Forced Sleeping Switch:** The game will force you to send out or switch to a sleeping Pokémon if no other conscious Pokémon are available. This is a mechanical exception to the strategic guideline of avoiding switching to sleeping Pokémon.

## B. Tile Mechanics & Traversal (Verified & In-Progress)
- `ground` / `grass`: Standard traversable tiles.
- `impassable` / `unknown`: Cannot be entered. Must be navigated around.
- `water`: Requires Surf to traverse.
- `ledge`: Can be jumped down (from Y-1 to Y+2 in one step), but not climbed up. Impassable from below and sides.
- `steps`: Allows movement between `ground` and `elevated_ground`.
- `elevated_ground`: Walkable ground at a different elevation, only accessible from `steps` or other `elevated_ground` tiles. One-way drops to adjacent `ground` tiles are possible.
- `cleared_boulder_barrier`: Functions as a one-way ramp. Allows upward movement from an adjacent `ground` tile to the `cleared_bolder_barrier` tile (which acts as `elevated_ground`). Downward movement from `cleared_boulder_barrier` to `ground` is prohibited.
- `boulder_barrier`: Impassable tile that can be cleared by a `boulder_switch`.
- `boulder_switch`: Floor switch for boulders. Activating it changes `boulder_barrier` to `cleared_boulder_barrier`.
- `spinner_*`: Forces movement in the specified direction.
- `ladder_up` / `ladder_down`: Function as warps but are traversable tiles.
- `hole`: A tile that a boulder can be pushed into, usually causing it to fall to a lower floor. The player can also walk into the hole after the boulder.
- **Boulder Pushing:** A single button press can both turn the player and push an adjacent boulder one tile. The player's position does not change during the push. Boulders CANNOT be pushed onto 'steps' tiles.
- **Context is Key:** The behavior of a specific tile type might not be universal. I must test tile mechanics in each new area rather than assuming they will always work the same way.

## C. Elite Four Mechanics (Verified)
- **Room Progression:** After defeating an Elite Four member, the northern door is unlocked by walking towards the southern entrance of the room.
- **Defeated Trainers:** Become impassable obstacles after their defeat speech.

# II. Battle Data & Strategy

## A. Type Effectiveness Chart (Verified In-Game)
- **Super Effective (2x):** Water > Rock, Ground, Fire; Electric > Water; Ground > Fire, Electric, Rock, Poison, Psychic (Hypothesized), Ground; Ice > Ground, Grass, Flying, Dragon; Flying > Fighting, Grass, Bug; Fighting > Normal, Rock, Ice; Grass > Ground, Rock, Water; Psychic > Ghost.
- **Not Very Effective (0.5x):** Normal !> Rock; Flying !> Rock; Ice !> Fighting (Ice-type moves are NOT super-effective against Fighting-types); Psychic !> Psychic.
- **Immune (0x):** Normal immune to Ghost; Ground immune to Electric; Flying immune to Ground; Ghost immune to Ground.

## B. Strategic Notes & Hypotheses
- **Opponent Coverage:** Always assume opponents, especially high-level ones like the Elite Four, have coverage moves for their weaknesses. Do not rely solely on primary typing for strategy.
- **Hypothesis (Agatha's Gengar):** A fast, high-level Psychic-type is essential. My Lv36 Kadabra was too underleveled. I need a faster solution or a bulkier Pokémon that can survive Gengar's attacks.
- **Assumption Under Review:** A high-level Pokémon with a type advantage is not a guaranteed win. Elite Four members have coverage moves (e.g., Lance's Aerodactyl with Earthquake). I must plan for worst-case scenarios.

## C. Battle Logs (Elite Four)
### Lorelei (Observed Roster)
  - Slowbro (Lv 56) - Known Moves: Psychic
  - Cloyster (Lv 55) - Known Moves: Explosion
  - Dewgong (Lv 56) - Moves unknown.
  - Jynx (Lv 59) - Known Moves: Lovely Kiss, Blizzard, Psychic, Bubblebeam (lowers Speed).
  - Lapras (Lv 60) - Moves unknown.

### Bruno (Observed Roster)
  - Hitmonchan (Lv 57) - Known Moves: Dizzy Punch, Thunderpunch, Ice Punch
  - Poliwrath (Lv 56) - Known Moves: Hydro Pump, Ice Beam
  - Hitmonlee (Lv 57) - Known Moves: Jump Kick
  - Onix (Lv 56) - Known Moves: Rock Slide
  - Machamp (Lv 58) - Known Moves: Earthquake, Rock Slide

### Agatha (Observed Roster - Last Attempt)
  - Gengar (Lv 57) - Known Moves: Night Shade, Mega Drain, Hypnosis, Dream Eater
  - Golbat (Lv 58) - Moves unknown.
  - Marowak (Lv 57) - Known Moves: Rock Slide, Earthquake
  - Arbok (Lv 58) - Known Moves: Glare, Substitute
  - Gengar (Lv 59) - Known Moves: Psychic

# III. Meta-Progression & Lessons Learned

## A. Core Methodological Failures (Self-Correction Log - Consolidated after Turn 144065 Critique)
- **Primary Failure (Immediate Action Mandate):** I have repeatedly violated the Immediate Action Mandate by deferring tool maintenance instead of performing it immediately upon failure. This includes attempting to use broken tools across multiple turns and getting stuck in a debugging loop by resubmitting an already-applied fix. I must trust system feedback and prioritize tool maintenance above all else.
- **Confirmation Bias & Data Integrity:** I have a tendency to become fixated on a single hypothesis (e.g., a path is possible) and fail to falsify my own assumptions or trust my tools' outputs. I must be more proactive in using my `puzzle_solver_agent` and basing all strategies only on verified data.
- **Victory Road Trainers:** Defeated trainers in Victory Road become impassable obstacles, similar to the Elite Four. This can permanently block paths.

# IV. Current Plan & Puzzles

## A. Victory Road 2F/3F Multi-Floor Puzzle (Corrected Plan)
1.  **Objective: Reach the northern section of Victory Road 2F.**
    - **Current State:** I am in the southern section of 2F. This section is disconnected from the northern section containing the ladder to western 3F at (2, 2).
    - **Insight (Turn 144360):** The `generate_path_plan` tool's debug logs have confirmed that there is no walkable path between these two sections on 2F.
    - **Action:** I must find an alternate route. This likely involves ascending to 3F and finding a different ladder or hole leading down to the correct area.
    - **Immediate Step:** Go to the ladder at (24, 8) on 2F and ascend to 3F.
2.  **Once on 3F, re-evaluate the map to find a path to the northern section of 2F.**
3.  **Long-term puzzle goals (to be re-evaluated after reaching northern 2F):**
    - Clear barrier on 3F by pushing boulder to switch at (4, 6).
    - Solve 2F puzzle by pushing boulder from 3F into a hole to land on the switch at (10, 17).

## B. Victory Road 2F/3F Multi-Floor Puzzle (New Insight)
- **Conclusion (Turn 144047):** My `boulder_path_planner` has confirmed that neither boulder currently on 2F can reach the switch at (10, 17). The critical directive allows for a multi-floor solution. Therefore, the puzzle requires me to push a boulder from 3F down a hole onto 2F.
- **Conclusion (Turn 144266):** Verified with `boulder_path_planner` that neither boulder on 2F can reach the switch at (10, 17). The multi-floor solution is confirmed as the only path forward.
- **Confirmation Bias Lesson (Victory Road 2F):** I repeatedly assumed my `generate_path_plan` tool was bugged when it returned "no path found." The debug logs eventually proved the tool was correct and my understanding of the map's segmented layout was wrong. I must trust my tool's outputs and use them to falsify my own assumptions about reachability, rather than trying to force the tool to confirm my biased beliefs.

## D. Future Development & Testing
- **Agent Monitoring (`battle_strategist_agent`):** The agent made a minor error in type-effectiveness reasoning (Turn 144315). While the recommended action was still sound, I need to monitor its performance for any further inaccuracies.
- **Player-Hole Interaction:** Need to verify if the player can walk into a `hole` tile after a boulder has been pushed into it.

# V. Self-Assessment (Turn 144543)
- **Immediate Action Mandate Failure:** I violated this mandate by not immediately fixing the faulty `boulder_path_planner` tool in turn 144527. This is a critical error in my methodology and must not be repeated.
- **Untested Assumption:** Need to verify if the player can walk into a `hole` tile after a boulder has been pushed into it. The system directive suggests this is possible, but I must confirm it myself.