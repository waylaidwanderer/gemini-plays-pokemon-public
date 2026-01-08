# Blackthorn Gym (Puzzle Progress)
- Start Turn: 34501
- Current Turn: 34707
- Pits (2F): P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders (2F): B6 (3, 3), B7 (6, 1), B8 (8, 11).
- Floor Reset: Using a ladder or falling into a pit resets all boulder positions on 2F.
- Push Mechanic: Player stays in the same tile after pushing a boulder.

# Puzzle Observations
- B8 (8, 14) has been pushed to (8, 11).
- Corridor 4 (x=8) is blocked north of y=10 by WALLs at (8, 8) and (8, 9).
- Corridor 3 (x=5, 6) seems to be the main path north.
- Row 13 gap (4, 13) connects Left and Right sections.
- Hypothesis: Defeated trainers (Cody at 4, 1 and Fran at 4, 11) might be passable.

# Strategy: Blackthorn Gym 2F
- Step 1: Verify passability of defeated trainers.
- Step 2: Re-run BFS solver with updated passability data.
- Step 3: Execute manual push sequence.

# Tile Mechanics (Global)
- FLOOR: Walkable.
- WALL: Impassable.
- PIT: Impassable on 2F; fills gap on 1F.
- LADDER: Warp between floors.
- BOULDER: Pushable (requires Strength).

# Resource Locations
- Route 45: Good training spot for Haunter (Night Shade).