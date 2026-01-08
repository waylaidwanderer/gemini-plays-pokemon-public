# Blackthorn Gym (Puzzle Progress)
- Start Turn: 34501
- Pits (2F): P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders (2F): B6 (3, 3), B7 (6, 1), B8 (8, 11).
- Floor Reset: Using a ladder or falling into a pit resets all boulder positions on 2F.
- Push Mechanic: Player stays in the same tile after pushing a boulder.

# Verified Obstacles
- (5, 10), (5, 12), (6, 6) are WALL tiles.
- NPCs Fran (4, 11) and Cody (4, 1) are impassable.
- Corridor 4 (x=8) is blocked north of y=10 by WALLs at (8, 8) and (8, 9).

# Connectivity Analysis
- Corridor 4 (x=8, 9) connects to the bottom open area at Row 12/13.
- Corridor 2 (x=2, 3) connects to the bottom open area at Row 13.
- Corridor 3 (x=5, 6) is accessed via the Ladder at (7, 9).

# Verified Connections
- Row 13 gap at (4, 13) is passable.

# Strategy: Blackthorn Gym 2F
- Step 1: Push B8 (8, 11) to a reachable pit.
- Step 2: Push B7 (6, 1) and B6 (3, 3) to pits.

# Tile Mechanics (Global)
- FLOOR: Walkable.
- WALL: Impassable collision.
- PIT: Impassable on 2F; fills gap on 1F.
- LADDER: Warp between floors.
- BOULDER: Pushable object (requires Strength).

# Resource Locations
- Route 45: Good training spot for Haunter (Night Shade).