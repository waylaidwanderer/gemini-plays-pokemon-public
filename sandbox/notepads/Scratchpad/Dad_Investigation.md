# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Blockers & Status
- **Metro Turnstile**: Stepping onto (19, 21) triggers "I should find dad first!" and forces Asher 1 step down to (19, 22) (re-verified active Turn 14644).
- **Route 2 Gate**: Stepping onto (52, 19-22) triggers "I can't go yet... I have things to do!" (re-verified active Turn 14647).
- **Jackson Status**: Captured by Team Siara during tremor cutscene (Turn 1666). Marie broadcast radio retreat on Turn 2682. Jackson's whereabouts remain the central progression gate.

## Verified / Settled Locations
- **Sovio Metro Lobby**:
  - Timetable Board (columns 21-23): Verified Turns 7149, 14276-14278 as decorative flavor text ("It's a timetable showing various destinations!").
  - Platform Attendant at (22, 19): Inaccessible behind solid north brick wall at row 23; platform passage gated at turnstile (19, 21).
- **Global Storage Systems (Verified Turns 14291-14315)**: HuPhone Mailbox ('There's no Mail here.'), HuPhone Item Storage ('There are no items.'), and Someone's PC Box 1 (0 Pokémon) audited 100% empty. Party size/composition does not gate turnstile blocker.

## Active Hypotheses & Strategic Focus
- **Hypothesis SS2 (Western Gauntlet & Corridor Boundary Probe - Rows 22-28, Cols 14-19)**:
  - **Start Turn**: 15293
  - **Status**: In Progress
  - **Rationale**: The western gauntlet was the station of Grunt 2 and contains partition walls and corridor extensions south of row 22 that have never been physically probed with collision and 'A' interactions. The previous conclusion that this sector was settled was a scope-of-proof violation based solely on Grunt 2's despawn. Jackson or a detention partition may be located along these unprobed boundaries.
  - **Test Protocol**:
    1. Navigate from Eastern Gangway to Western Gauntlet via bridge, ladder, and stairs to (18, 22) [Completed Turn 15293].
    2. Systematically probe the vertical corridor from row 22 to row 27: test east and west partition walls at rows 22, 23, 24, 25, 26 with directional bumps and 'A' presses.
    3. Audit the row 27-28 horizontal corridor between columns 14 and 19: test north and south wall boundaries.
    4. Record exact collision results and text prompts for every probed tile.
  - **Empirical Results Log**:
    - **Row 22 (Turn 15294)**:
      - (18, 22): Walkable floor (Grunt 2 standing tile).
      - (17, 22): Walkable floor. West boundary (16, 22) is solid black void collision; 'A' interaction inert.
      - (19, 22): Walkable floor. East boundary (20, 22) is solid black void collision; 'A' interaction inert.
    - **Rows 23-25 (Turns 15296-15308)**:
      - (18, 23): Walkable floor.
      - (17, 23): Walkable floor! Column 17 is a clear vertical passage connecting row 22 directly down to row 24.
      - (17, 24): Walkable floor.
      - (16, 24): Solid brick wall collision; 'A' interaction inert.
      - (18, 24): Walkable floor.
      - (19, 24): Walkable floor. East boundary (20, 24) is solid brick wall collision; 'A' interaction inert.
      - (19, 25): Walkable floor. East boundary (20, 25) is solid brick wall collision; 'A' interaction inert.
      - (18, 25): Walkable floor.
      - (17, 25): Walkable floor.
      - (16, 25): Walkable floor! (Wall does not block row 25 at column 16).
    - **Row 26 (Turn 15314-15315)**:
      - (16, 26): Walkable floor.
      - (15, 26): Walkable floor. Arrived at (15, 26).
      - Corridor continues west and south toward row 27 and column 12 stairs.

## Settled Hypotheses
- **Hypothesis SS1 (Sovio Sewers Eastern Storage Room & Platform - 100% SETTLED & ARCHIVED)**:
  - Status: Settled Turn 15261. Executed full 4-step physical protocol. Red mat at (37, 14) confirmed ambient single-line textbox ('Its a simple storage room...') and solid south void collision. Northern expansion (36-38, 12) and eastern boundary (col 39) verified solid walls with inert 'A'. Platform 100% ambient prop.
