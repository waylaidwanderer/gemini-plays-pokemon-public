# Blackthorn Gym (Puzzle Progress)
- Start Turn: 34501
- Pits (2F): P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Default Boulders (2F): B6 (3, 3), B7 (6, 1), B8 (8, 14).
- Floor Reset: Using a ladder or falling into a pit resets all boulder positions on 2F.
- Push Mechanic: Player stays in the same tile after pushing a boulder.

# Verified Obstacles
- (5, 10), (5, 12), (6, 6) are WALL tiles.
- NPCs Fran (4, 11) and Cody (4, 1) are impassable.
- Corridor 4 (x=8) is blocked north of y=10 by WALLs at (8, 8) and (8, 9).
- Corridor 4 (x=9) is blocked at (9, 4) and (9, 12).

# Verified Connections
- Row 13 gap at (4, 13) and (5, 13) is passable.
- Corridor 3 (x=5, 6) is segmented: (5, 10) and (5, 12) block vertical movement in column 5.
- Corridor 3 (x=6) allows movement from (6, 11) up to (6, 7). (6, 6) is a WALL.

# Strategy: Blackthorn Gym 2F
- Step 1: Reset boulders to default positions using Ladder at (7, 9). (In progress)
- Step 2: Use `solve_puzzle_v5` from (7, 9) on 2F to find the solution.
- Step 3: Execute the sequence.

# Tile Mechanics (Global)
- FLOOR: Walkable.
- WALL: Impassable collision.
- PIT: Impassable on 2F; fills gap on 1F.
- LADDER: Warp between floors.
- BOULDER: Pushable object (requires Strength).

# Resource Locations
- Route 45: Good training spot for Haunter (Night Shade).