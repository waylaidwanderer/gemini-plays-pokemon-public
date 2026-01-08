# Blackthorn Gym (Puzzle Progress)
- Start Turn: 34501
- Current Turn: 34711
- Pits (2F): P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders (2F): B6 (3, 3), B7 (6, 1), B8 (8, 11).
- Floor Reset: Using a ladder or falling into a pit resets all boulder positions on 2F.
- Push Mechanic: Player stays in the same tile after pushing a boulder.

# Puzzle Observations
- B8 (8, 14) has been pushed to (8, 11).
- Corridor 4 (x=8) is blocked north of y=10 by WALLs at (8, 8) and (8, 9).
- Row 13 gap (4, 13) connects Left and Right sections.

# Current Test: Passability of NPCs
- Objective: Determine if defeated trainers (Fran at 4, 11 and Cody at 4, 1) are passable.
- Test 1 (Fran): Move to (5, 11) and attempt to walk left into (4, 11).
- Result: Impassable (Verified Turn 34709).

# Verified Connections & Obstacles
- (5, 10) and (5, 12) are WALL tiles.
- (6, 6) is a WALL tile.
- Fran at (4, 11) is impassable.
- Cody at (4, 1) is likely impassable.

# Strategy: Blackthorn Gym 2F
- Step 1: Map out a path for B8 to P3 (8, 7) that avoids WALLs at (8, 8-9).
- Step 2: Determine if B8 can be pushed into Corridor 3 (x=5, 6).

# Tile Mechanics (Global)
- FLOOR: Walkable.
- WALL: Impassable collision (pillars, statues, rocks).
- PIT: Impassable on 2F; fills gap on 1F.
- LADDER: Warp between floors.
- BOULDER: Pushable object (requires Strength).

# Resource Locations
- Route 45: Good training spot for Haunter (Night Shade).