# Blackthorn Gym (Puzzle Progress)
- Pits (2F): P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders (2F): B6 (3, 3), B7 (6, 1), B8 (8, 14) [Default Positions].
- Reset Mechanic: Ladders (1, 7) and (7, 9) reset 2F boulders. (Verified Turn 34678).
- Push Mechanic: Player stays in tile after push. (Verified Turn 34644).
- Status: Strength is ACTIVE. B6 moved to (3, 2). (Turn 34752).

# Verified Obstacles (2F)
- (4, 1): COOLTRAINER_M Cody. Impassable (Attempted move Turn 34737).
- (4, 11): COOLTRAINER_F Fran. Impassable (Attempted move Turn 34709).
- (4, 12): WALL. Impassable (Attempted move Turn 34724).
- (7, 11): WALL. Impassable (Attempted move Turn 34732).
- (8, 9): WALL. Impassable (Attempted move Turn 34721).
- (9, 12): WALL. Impassable (Attempted move Turn 34691).

# Verified Connections (2F)
- (4, 13): FLOOR. Gap connecting Left (x=0-3) and Right (x=5-9) sections.

# Strategy: Blackthorn Gym 2F
- Step 1: Reach B6 (3, 3) and reactivate Strength.
- Step 2: Test passability of (8, 8) and (6, 4).
- Step 3: Run comprehensive solve script with high state limit.

# Tile Mechanics (Global)
- FLOOR: Walkable.
- WALL: Impassable collision.
- PIT: Impassable on 2F; fills gap on 1F.
- LADDER: Warp between floors.
- BOULDER: Pushable object (requires Strength).

# Resource Locations
- Route 45: Good training spot for Haunter (Night Shade).