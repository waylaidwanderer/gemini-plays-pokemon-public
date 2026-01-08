# Blackthorn Gym (Puzzle Progress)
- Start Turn: 34501
- Pits (2F): P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders (2F): B6 (3, 3), B7 (6, 1), B8 (8, 14) [Default Positions].
- Floor Reset: Using a ladder or falling into a pit resets all boulder positions on 2F. (Verified Turn 34678).
- Push Mechanic: Player stays in the same tile after pushing a boulder. (Verified Turn 34644).

# Verified Obstacles
- (4, 1), (4, 2), (4, 11), (4, 12) are Impassable (NPCs or WALLs).
- (5, 10), (5, 12), (6, 6) are WALLs (pillars).
- (7, 10), (7, 11) are WALLs.
- (8, 9) is a WALL.
- (2, 17) is a WALL.

# Verified Connections
- (4, 13) is a FLOOR (gap).
- (7, 12), (7, 13) are FLOORs.

# Investigation Plan (Turn 34740)
- Goal: Find a hidden path through the segmented corridors.
- Test 1: Move to (5, 5) and test passability of (4, 5) and (6, 5).
- Test 2: Test (6, 4) and (6, 6).
- Test 3: Test (8, 8).

# Tile Mechanics (Global)
- FLOOR: Walkable.
- WALL: Impassable collision.
- PIT: Impassable on 2F; fills gap on 1F.
- LADDER: Warp between floors.
- BOULDER: Pushable object (requires Strength).

# Resource Locations
- Route 45: Good training spot for Haunter (Night Shade).