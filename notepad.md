# Tile Mechanics (Global)
- FLOOR: Passable terrain.
- WALL: Impassable silver blocks. Absolute barrier.
- PIT: Player falls to 1F. Boulder destination (forms bridge on 1F).
- LADDER: Warp between floors. Deactivates Strength.
- Strength: Active (Turn 30101). Verified: Pushing B8 worked at Turn 30116.

# Blackthorn Gym 2F State
- Boulders: B6 (3, 3), B7 (6, 1), B8 (8, 10).
- Pits: (2, 5), (8, 3), (8, 7).
- NPCs: Cody (4, 1), Fran (4, 11). Both solid.
- Barriers: Column 4 wall Row 0-12. Column 2 wall Row 10-17. Row 8 wall at (2,8)-(4,8).
- Crossing Points: Row 13 gap at (4, 13) is the primary crossing. Row 1 gap at (2, 1).

# Time Tracking
- Puzzle Start Turn: 29931.
- Current Attempt Start: Turn 30104.

# Strategy: Breaking the Deadlock
- Goal: Drop all boulders into pits.
- Problem: Idealized BFS says puzzle is impossible with current WALL layout.
- Hypothesis: One or more "WALL" tiles are actually passable, or NPCs move.
- Test 1: Talk to Fran at (4, 11). Result: Pending.
- Test 2: Attempt to move onto (4, 3) from (3, 3).
- Test 3: Attempt to move onto (4, 2) from (3, 2).
- Test 4: Attempt to move onto (6, 2) from (7, 2).
- Test 5: Attempt to move onto (6, 3) from (7, 3).