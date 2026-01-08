# Blackthorn Gym (Puzzle Progress)
- Pits (2F): P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders (2F): B6 (3, 2), B7 (6, 1), B8 (8, 14) [Current Positions].
- Reset Mechanic: Ladders (1, 7) and (7, 9) reset 2F boulders. (Verified Turn 34678).
- Push Mechanic: Player stays in tile after push. (Verified Turn 34644).
- Status: Strength is ACTIVE. B6 is at (3, 2). (Turn 34752).

# Verified Obstacles (2F)
- (4, 1): COOLTRAINER_M Cody. Impassable (Attempt Turn 34737).
- (4, 11): COOLTRAINER_F Fran. Impassable (Attempt Turn 34709).
- (4, 12): WALL. Impassable (Attempt Turn 34724).
- (7, 11): WALL. Impassable (Attempt Turn 34732).
- (8, 9): WALL. Impassable (Attempt Turn 34721).
- (9, 12): WALL. Impassable (Attempt Turn 34691).

# Verified Connections (2F)
- (4, 13): FLOOR. Gap connecting Left (x=0-3) and Right (x=5-9) sections.

# Strategy: Blackthorn Gym 2F
- Goal: Find a passable 'wall' that allows boulder movement.
- Step 1: Reach (3, 3) and test (4, 3).
- Step 2: Reach (8, 13) and test (9, 13).
- Step 3: Reach (5, 5) and test (4, 5) and (6, 5).

# Tile Mechanics (Global)
- FLOOR: Walkable.
- WALL: Impassable collision.
- PIT: Impassable on 2F; fills gap on 1F.
- LADDER: Warp between floors.
- BOULDER: Pushable object (requires Strength).

# Resource Locations
- Route 45: Good training spot for Haunter (Night Shade).