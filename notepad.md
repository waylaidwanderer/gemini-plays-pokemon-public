# Tile Mechanics (Global)
- FLOOR: Walkable tile.
- WALL: Impassable collision.
- PIT: Impassable on 2F; fills gap on 1F.
- LADDER: Warp between floors.
- BOULDER: Pushable object (requires Strength). Player stays in place after push.

# Blackthorn Gym (Global Mechanics)
- Start Turn: 34501 (Puzzle Start)
- Pits (2F): P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders (2F): B6 (3, 3), B7 (6, 1), B8 (8, 11).
- Floor Reset: Using a ladder (1, 7) or (7, 9) resets all boulder positions on 2F.

# Manual Strategy: Blackthorn Gym 2F
- Goal: Fill the three pits on 2F to bridge gaps on 1F.
- Step 1: B8 (8, 11) -> P3 (8, 7).
    - Push B8 up to (8, 10).
    - Push B8 right to (9, 10).
    - Push B8 up to (9, 7).
    - Push B8 left into P3 (8, 7).
- Step 2: B7 (6, 1) -> P1 (8, 3).
    - Push B7 right to (8, 1).
    - Push B7 down into P1 (8, 3).
- Step 3: B6 (3, 3) -> P2 (2, 5).
    - Push B6 left to (2, 3).
    - Push B6 down into P2 (2, 5).

# Resource Locations
- Route 45: Good training spot for Haunter (Night Shade).