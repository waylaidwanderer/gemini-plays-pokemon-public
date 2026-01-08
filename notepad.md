# Blackthorn Gym (Puzzle Progress)
- Start Turn: 34501 (Entered Gym)
- Puzzle Phase Start: 34671
- Pits (2F): P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders (2F): B6 (3, 3), B7 (6, 1), B8 (8, 14).
- Reset Mechanic: Ladders (1, 7) and (7, 9) reset 2F boulders.
- Push Mechanic: Player stays in tile after push.

# Connectivity & Obstacle Log
- (4, 13): Verified FLOOR (Turn 34723).
- (8, 9): Verified WALL (Turn 34721).
- Fran (4, 11): Verified Impassable (Turn 34709).
- (5, 10), (5, 12), (6, 6): Labeled WALL.
- Corridor 4 (x=9): Labeled WALL at (9, 4), (9, 12), (9, 13), (9, 14).

# Hypothesis Testing
- Hypothesis: Some tiles labeled WALL in the x=4 column are passable, allowing cross-corridor pushes.
- Test 1: Walk Up from (4, 13) to (4, 12).
- Result: Pending.

# Strategy
- Systematically test "walls" that block boulder-to-pit paths.
- Once connectivity is confirmed, use `solve_puzzle_v5` to calculate the push sequence.

# Tile Mechanics (Global)
- FLOOR: Walkable.
- WALL: Impassable collision.
- PIT: Impassable on 2F; fills gap on 1F.
- LADDER: Warp between floors.
- BOULDER: Pushable (requires Strength).

# Resource Locations
- Route 45: Good training spot for Haunter.