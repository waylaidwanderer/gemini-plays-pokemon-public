# Tile Mechanics (Global)
- FLOOR: Standard walkable tile.
- WALL: Impassable collision (pillars, statues, rocks, NPCs).
- LADDER: Two-way warp between floors. (1, 7) and (7, 9).
- PIT: A hole that leads to 1F. Boulders fall through to fill gaps on 1F. Empty pits are impassable/warp for player on 2F.
- BOULDER: Pushable object. Requires STRENGTH. Pushing moves it one tile. Player STAYS in original tile. (Verified Turn 34566)

# Blackthorn Gym (2F) Puzzle
- Goal: Push three boulders into pits to bridge gaps to Gym Leader Clair on 1F.
- Boulder 6: (3, 3)
- Boulder 7: (6, 1)
- Boulder 8: (8, 14)
- Pit 1: (8, 3)
- Pit 2: (2, 5)
- Pit 3: (8, 7)
- NPC Obstacles: Cody (4, 1), Fran (4, 11), Lola (9, 2), Paul (1, 15) are solid and block movement.

# Strategy & Progress
- Lead Pokémon: XENON (Haunter, Lv36).
- Status: Strength active. Player at (3, 1).
- Plan: Solve the puzzle using BFS.

# Resource Locations
- Route 45: Good training spot for Haunter (Night Shade).