# Blackthorn Gym (Puzzle Progress)
- Pits (2F): P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders (2F): B6 (3, 3), B7 (6, 1), B8 (8, 14) [Default Positions].
- Floor Reset: Using a ladder (1, 7) or (7, 9) resets all boulder positions on 2F. (Verified Turn 34678).
- Push Mechanic: Player stays in the same tile after pushing a boulder. (Verified Turn 34644).
- Status: Strength is INACTIVE. Boulders are RESET. (Verified Turn 34747).

# Verified Obstacles (2F)
- (4, 1): COOLTRAINER_M Cody. Impassable (Attempted move Turn 34737).
- (4, 11): COOLTRAINER_F Fran. Impassable (Attempted move Turn 34709).
- (4, 12): WALL. Impassable (Attempted move Turn 34724).
- (5, 10), (5, 12), (6, 6), (7, 10), (7, 11), (8, 9): WALLs. Impassable.
- (8, 15): FLOOR.
- (9, 12), (9, 13), (9, 14), (9, 15), (9, 16), (9, 17): Labeled WALL.

# Verified Connections (2F)
- (4, 13): FLOOR. Gap connecting Left (x=0-3) and Right (x=5-9) sections.

# Strategy: Blackthorn Gym 2F
- Step 1: Return to 2F and reactivate Strength.
- Step 2: Test passability of (8, 8) and (9, 10-11) if BFS fails.
- Step 3: Use BFS solver ONLY while on 2F map.

# Tile Mechanics (Global)
- FLOOR: Walkable.
- WALL: Impassable collision.
- PIT: Impassable on 2F; fills gap on 1F.
- LADDER: Warp between floors.
- BOULDER: Pushable object (requires Strength).

# Resource Locations
- Route 45: Good training spot for Haunter (Night Shade).