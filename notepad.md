# Blackthorn Gym (Puzzle Progress)
- Start Turn: 34501
- Pits (2F): P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Default Boulders (2F): B6 (3, 3), B7 (6, 1), B8 (8, 14).
- Floor Reset: Using a ladder or falling into a pit resets all boulder positions on 2F.
- Push Mechanic: Player stays in the same tile after pushing a boulder.

# Connectivity & Obstacle Log
- (4, 13): Verified FLOOR (Turn 34723). Acts as a 4-way intersection.
- (4, 12): Verified WALL (Turn 34724).
- (8, 9): Labeled WALL. Testing passability next.
- (8, 8): Labeled WALL.
- Fran (4, 11): Verified Impassable (Turn 34709).
- Cody (4, 1): Labeled FLOOR but has NPC. Testing passability later.

# Strategy
- Step 1: Navigate to (8, 15) and push B8 (8, 14) north.
- Step 2: Test passability of (8, 9) and (8, 8).
- Step 3: If blocked, explore the column 9 corridor (9, 5-11).

# Tile Mechanics (Global)
- FLOOR: Walkable.
- WALL: Impassable collision.
- PIT: Impassable on 2F; fills gap on 1F.
- LADDER: Warp between floors.
- BOULDER: Pushable object (requires Strength).

# Resource Locations
- Route 45: Good training spot for Haunter.