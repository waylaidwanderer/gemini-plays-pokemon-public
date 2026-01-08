# Tile Mechanics (Global)
- FLOOR: Standard walkable tile.
- WALL: Impassable collision (pillars, statues, rocks, NPCs).
- LADDER: Two-way warp between floors. (1, 7) and (7, 9).
- PIT: A hole that leads to 1F. Boulders fall through to fill gaps on 1F. Empty pits are impassable for player on 2F.
- BOULDER: Pushable object. Requires STRENGTH. Pushing moves it one tile. Player STAYS in original tile. (Verified Turn 34566)

# Blackthorn Gym Puzzle Analysis
- Start Turn: 34501
- Goal: Fill three pits on 2F to bridge gaps on 1F.
- Boulders: B6 (3, 3), B7 (6, 1), B8 (8, 14) [Default Positions].
- Pits: P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Critical Mechanic: Changing floors (using ladders) RESETS all boulder positions on 2F. (Verified Turn 34592).
- Push Mechanic: Player stays in place after push (Verified Turn 34644).
- Passability: Cody (4, 1), Fran (4, 11), Paul (1, 15), and Lola (9, 2) are walls.
- Corridor Connectivity:
    - Left (x=0-3) and Right (x=5-8) connected only at Row 13-17.
    - Right (x=5-6) and Right (x=8-9) connected at Row 1, 3, 5, 7 and Row 12.
    - Corridor 4 (x=8, 9) is split by walls at (8, 8) and (8, 9).

# Strategy & Progress
- Lead Pokémon: XENON (Haunter, Lv36).
- Strategy:
    1. B8 (8, 14) -> P2 (2, 5) via Row 13 gap.
    2. B7 (6, 1) -> P1 (8, 3).
    3. B6 (3, 3) -> P3 (8, 7) via Row 13 gap and Corridor 3.
- Note: If BFS fails, re-examine map for hidden paths or incorrect wall data.

# Resource Locations
- Route 45: Good training spot for Haunter (Night Shade).