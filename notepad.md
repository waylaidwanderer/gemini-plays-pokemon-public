# Blackthorn Gym (Global Mechanics)
- Start Turn: 34501 (Puzzle Start)
- Current Turn: 34681
- Pits (2F): (8, 3), (2, 5), (8, 7).
- Boulders (2F): B6 (3, 3), B7 (6, 1), B8 (8, 14).
- Floor Reset: Using a ladder (1, 7) or (7, 9) resets all boulder positions on 2F.
- Push Mechanic: Player stays in the same tile after pushing a boulder.
- Obstacles: Pillars (WALL tiles) and Cooltrainers (Objects) are impassable.
- Corridor Connectivity: Corridors are narrow. Movement between corridors is only possible at specific gaps (Row 1, Row 5, Row 12/13).

# Strategy for Beating Blackthorn Gym
- Goal: Fill the three pits on 2F to bridge gaps on 1F.
- Manual Strategy Hypothesis:
    1. B8 (8, 14) -> P2 (2, 5) via Row 13 gap. (Requires x=9 to be passable or a way to get behind B8).
    2. B6 (3, 3) -> P3 (8, 7) via Row 13 gap and Corridor 3.
    3. B7 (6, 1) -> P1 (8, 3).
- Verification: Testing passability of (7, 11) and (7, 10) to see if B8 can be pushed out of its corridor.

# Tile Mechanics (Global)
- FLOOR: Standard walkable tile.
- WALL: Impassable collision.
- PIT: Impassable on 2F; fills a gap on 1F when a boulder is pushed in.
- LADDER: Warp between 1F and 2F.
- BOULDER: Pushable object (requires Strength).

# Resource Locations
- Route 45: Good training spot for Haunter (Night Shade).