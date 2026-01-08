# Tile Mechanics (Global)
- FLOOR: Standard walkable tile.
- WALL: Impassable collision (pillars, statues, rocks, NPCs).
- LADDER: Two-way warp between floors. (1, 7) and (7, 9).
- PIT: A hole that leads to 1F. Boulders fall through to fill gaps on 1F. Empty pits are impassable/warp for player on 2F.
- BOULDER: Pushable object. Requires STRENGTH. Pushing moves it one tile. Player STAYS in original tile. (Verified Turn 34566)

# Blackthorn Gym (2F) Puzzle
- Goal: Push three boulders into pits to bridge gaps to Gym Leader Clair on 1F.
- Boulder positions (Starting): B6 (3, 3), B7 (6, 1), B8 (8, 14).
- Pits: (8, 3), (2, 5), (8, 7).
- Connectivity: Cody (4, 1) and Fran (4, 11) are solid obstacles. Sections are connected by ladders via 1F.

# Strategy & Progress
- Status: B6 at (3, 5). Strength active. Player at (3, 3).
- Plan: Verify walkability of Fran at (4, 11), then use refined solver.

# Resource Locations
- Route 45: Good training spot for Haunter (Night Shade).