# Rocket Hideout Elevator Cabin (Map 0_203) Testing Log
- Turn 36781: Stand at (3, 2). Hypothesize that (2, 2) is walkable floor. Testing by pressing 'Left'.
- Goal: Determine the exact boundary of the walkable area and locate the control panel to select the floor.
- Turn 36782: Pressed 'Left' from (3, 2). Moved successfully to (2, 2). (2, 2) is 100% walkable!
- Turn 36783: Stand at (2, 2). Hypothesize that (2, 1) is walkable and does not contain a warp. Testing by pressing 'Up' to step onto (2, 1).
- Turn 36787: Pressed 'Up' to step onto (2, 1). Warped back to Map 0_200 (25, 19). This proves that (2, 1) is ALSO an active exit warp tile!
- Breakthrough Discovery: Row 1 consists entirely of exit warp tiles. We cannot stand on row 1.
- Solution to Face UP at (3, 2):
  1. Enter elevator from B2F (25, 19) by pressing 'Down'. We spawn at Map 0_203 (3, 1) and automatically walk down to (3, 2), facing DOWN.
  2. Walk Left to (2, 2).
  3. Walk Down to (2, 3).
  4. Walk Right to (3, 3).
  5. Walk Up to (3, 2) - this leaves us at (3, 2) facing UP!
  6. Press 'A' to interact with the control panel at (3, 1) / (3, 0) and open the elevator menu!
- Turn 36804: Pressed 'A' while standing at (3, 2) facing UP, but no menu opened.
- Hypothesis 2: The elevator control panel is at (2, 1), requiring us to stand at (2, 2) facing UP and press 'A'.
- Path to stand at (2, 2) facing UP:
  1. Walk Left from (3, 2) to (2, 2) (facing Left).
  2. Walk Down from (2, 2) to (2, 3) (facing Down).
  3. Walk Up from (2, 3) to (2, 2) (facing UP!).
  4. Press 'A'.