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
- **Boulder Pushing Mechanics (Refined):** Pushing is context-dependent.
- **Adjacent Push:** When standing on a tile directly adjacent to a boulder, a push will move the boulder one tile and the player character will move into the boulder's previous space.
- **Stationary Push:** When standing one tile away from a boulder with an empty space in between, a push will move the boulder one tile, but the player's character will *not* move.
- Boulders CANNOT be pushed onto 'steps' tiles.
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
- **Primary Failure (Immediate Action Mandate):** I have repeatedly violated the Immediate Action Mandate by deferring tool maintenance instead of performing it immediately upon failure. This led to a prolonged debugging loop with my pathfinding tool.
- **Confirmation Bias & Data Integrity:** I have a tendency to become fixated on a single hypothesis (e.g., "my tool is almost working") and fail to falsify my own assumptions or trust my tools' outputs when they indicate a path is blocked. I must be more proactive in basing all strategies only on verified data from my tools.
- **Victory Road Trainers:** Defeated trainers in Victory Road become impassable obstacles, similar to the Elite Four. This can permanently block paths.

# IV. Current Objectives & Hypotheses

## A. Victory Road 2F/3F Multi-Floor Puzzle
- **Objective:** Solve the Victory Road 2F boulder puzzle.
- **Insight (System Directive & Tool Validation):** The puzzle solution is multi-floor. My `boulder_path_planner` confirmed that no boulder on 2F can reach the switch at (10, 17). Therefore, I must ascend to 3F to find a way to drop a boulder onto the switch.