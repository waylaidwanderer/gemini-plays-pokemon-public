# Blackthorn Gym (Puzzle Progress)
- Start Turn: 34501
- Pits (2F): P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders (2F): B6 (3, 3), B7 (6, 1), B8 (8, 14) [Default Positions].
- Floor Reset: Using a ladder or falling into a pit resets all boulder positions on 2F. (Verified Turn 34678).
- Push Mechanic: Player stays in the same tile after pushing a boulder. (Verified Turn 34644).

# Verified Obstacles
- (4, 12), (5, 10), (5, 12), (6, 6), (7, 11), (8, 9) are WALLs.
- Fran (4, 11) is an impassable NPC (Verified Turn 34709).
- Cody (4, 1) is an NPC. Testing passability.

# Verified Connections
- (4, 13) is a FLOOR (gap).

# Strategy: Blackthorn Gym 2F
- Step 1: Test passability of suspected fake walls: (8, 8), (9, 12), (9, 13), (7, 10).
- Step 2: Use `solve_puzzle_v5` once a path is found.

# Tile Mechanics (Global)
- FLOOR: Walkable.
- WALL: Impassable collision.
- PIT: Impassable on 2F; fills gap on 1F.
- LADDER: Warp between floors.
- BOULDER: Pushable object (requires Strength).

# Resource Locations
- Route 45: Good training spot for Haunter (Night Shade).