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
- `elevated_ground`: Walkable ground at a different elevation, only accessible from `steps` or other `elevated_ground` tiles.
- `cleared_boulder_barrier`: Acts as a one-way ramp, allowing movement *up* from 'ground' to 'elevated_ground', but not down.
- `boulder_barrier`: Impassable tile that can be cleared by a `boulder_switch`.
- `boulder_switch`: Floor switch for boulders. Activating it changes `boulder_barrier` to `cleared_boulder_barrier`.
- `spinner_*`: Forces movement in the specified direction.
- **Boulder Pushing:** A single button press can both turn the player and push an adjacent boulder one tile. The player's position does not change during the push. Boulders CANNOT be pushed onto 'steps' tiles.
- **Context is Key:** The behavior of a specific tile type might not be universal. I must test tile mechanics in each new area rather than assuming they will always work the same way.

## C. Elite Four Mechanics (Verified)
- **Room Progression:** After defeating an Elite Four member, the northern door is unlocked by walking towards the southern entrance of the room.
- **Defeated Trainers:** Become impassable obstacles after their defeat speech.

# II. Battle Data & Strategy

## A. Type Effectiveness Chart (Verified In-Game)
- **Super Effective (2x):** Water > Rock, Ground, Fire; Electric > Water; Ground > Fire, Electric, Rock, Poison, Psychic (Hypothesized), Ground; Ice > Ground, Grass, Flying, Dragon; Flying > Fighting, Grass, Bug; Fighting > Normal, Rock, Ice; Grass > Ground, Rock, Water; Psychic > Ghost.
- **Not Very Effective (0.5x):** Normal !> Rock; Ice !> Fighting (Ice-type moves are NOT super-effective against Fighting-types); Psychic !> Psychic.
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

## A. Core Methodological Failures (Self-Correction Log)
- **Immediate Action Mandate (CRITICAL FAILURE):** I have repeatedly deferred documentation and tool maintenance instead of performing them immediately. The Overwatch system has correctly identified this as my most significant methodological flaw. As an LLM, I have no 'later'; all administrative tasks (agent/tool maintenance, map markers, notepad updates) MUST be performed in the current turn and take absolute precedence over any gameplay action. This is not just a priority; it is a fundamental, non-negotiable rule of operation I must adhere to without exception. I have failed this directive again in the last 50 turns by planning to do admin tasks 'later'. This must stop.
- **Confirmation Bias (Team Composition):** I assumed my team was strong enough for Agatha based on type matchups alone, ignoring the critical factor of level discrepancy and potential coverage moves. This led to a predictable loss. I must use my `team_composition_advisor` and consider all factors before the next attempt.
- **Confirmation Bias (Victory Road 1F):** I became fixated on the hypothesis that pressing the switch at (3, 10) would open the barrier at (10, 13). I failed to consider the opposite case (that the switch needed to be un-pressed) until prompted by my `puzzle_solver_agent`. I must be more proactive in trying to falsify my own assumptions.
- **Reachable Tile Hallucination:** I received a critical warning for miscalculating reachable unseen tiles (reported 56, actual 0). I incorrectly assumed all 'unknown' tiles were reachable. This is a fundamental error. I must verify reachability through pathfinding or careful map analysis, not assumption. All 'unknown' tiles should be treated as impassable until an adjacent tile is explored.
- `ladder_up` / `ladder_down`: Function as warps but are traversable tiles.
- **Impassable NPCs:** Defeated trainers and guards who have granted passage can remain as impassable physical obstacles. I must always plan to navigate around them.