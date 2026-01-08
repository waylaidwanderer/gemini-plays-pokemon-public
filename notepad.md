# Blackthorn Gym (Puzzle Progress)
- Start Turn: 34501
- Pits (2F): P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Default Boulders (2F): B6 (3, 3), B7 (6, 1), B8 (8, 14).
- Floor Reset: Using a ladder or falling into a pit resets all boulder positions on 2F.
- Push Mechanic: Player stays in the same tile after pushing a boulder.

# Puzzle Investigation (Turn 34721)
- Problem: BFS and manual analysis suggest all boulders are blocked from all pits by WALLs.
- Hypothesis: One or more tiles marked as WALL are actually passable FLOORs.
- Target 1: (8, 9) - If passable, B8 can reach P3 (8, 7) directly. (Verified Turn 34721: Impassable).
- Target 2: (4, 13) - Potential gap connecting Left (x=0-3) and Right (x=5-9) sections.
- Target 3: (4, 1) NPC Cody - If passable, B6 can reach P2 (2, 5).

# Verified Obstacles
- (5, 10), (5, 12), (6, 6) are WALL tiles.
- (8, 9) is a WALL tile.
- NPC Fran (4, 11) is impassable.
- Corridor 4 (x=9) is blocked at (9, 4) and (9, 12).

# Verified Connections
- None yet. Testing (4, 13).

# Strategy
- Test passability of suspected walls and gaps.
- Use `gym_strategist` agent for high-level planning once connectivity is known.

# Tile Mechanics (Global)
- FLOOR: Walkable.
- WALL: Impassable collision.
- PIT: Impassable on 2F; fills gap on 1F.
- LADDER: Warp between floors.
- BOULDER: Pushable object (requires Strength).

# Resource Locations
- Route 45: Good training spot for Haunter (Night Shade).