# Blackthorn Gym (Global Mechanics)
- Start Turn: 34501 (Puzzle Start)
- Current Turn: 34671
- Pits (2F): (8, 3), (2, 5), (8, 7).
- Boulders (2F): B6 (3, 3), B7 (6, 1), B8 (8, 14).
- Floor Reset: Using a ladder (1, 7) or (7, 9) resets all boulder positions on 2F.
- Push Mechanic: Player stays in the same tile after pushing a boulder.
- Obstacles: Pillars (WALL tiles) and Cooltrainers (Objects) are impassable.
- Corridor Connectivity: Corridors are narrow. Movement between corridors is only possible at specific gaps (Row 1, Row 5, Row 12/13).

# Strategy for Beating Blackthorn Gym
- Goal: Fill the three pits on 2F to create bridges on 1F.
- Method: Use the `solve_blackthorn_gym_boulders_v4` tool to find the exact push sequence.
- Status: Activating STRENGTH to begin pushing B6.

# Tile Mechanics (Global)
- FLOOR: Standard walkable tile.
- WALL: Impassable collision.
- PIT: Impassable on 2F; fills a gap on 1F when a boulder is pushed in.
- LADDER: Warp between 1F and 2F.
- BOULDER: Pushable object (requires Strength).

# Resource Locations
- Route 45: Good training spot for Haunter (Night Shade).