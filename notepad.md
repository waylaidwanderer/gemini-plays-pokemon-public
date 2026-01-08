# Tile Mechanics (Global)
- FLOOR: Standard walkable tile.
- WALL: Impassable collision (pillars, statues, rocks).
- LADDER: Two-way warp between floors. (1, 7) and (7, 9).
- PIT: A hole that leads to 1F. Boulders fall through to fill gaps on 1F. Empty pits are impassable/warp; filled pits on 1F become walkable.
- BOULDER: Pushable object. Requires STRENGTH. Pushing moves it one tile. Player STAYS in original tile.

# Blackthorn Gym (2F) Puzzle
- Start Turn: 34501 (Current Attempt: 34547)
- Goal: Push three boulders into pits to bridge gaps to Gym Leader Clair on 1F.
- Boulder 5: DOES NOT EXIST (Verified at (3, 7))
- Boulder 6: (3, 3) - SEEN
- Boulder 7: (6, 1) - PENDING VERIFICATION (Post-reset)
- Boulder 8: (8, 14) - SEEN
- Pit A: (8, 3)
- Pit B: (2, 5)
- Pit C: (8, 7)
- NPC Obstacles: Cody (4, 1), Fran (4, 11), Lola (9, 2), Paul (1, 15) are solid and block player/boulders.

# Strategy & Progress
- Lead Pokémon: XENON (Haunter, Lv36). Target Lv40 on Route 45.
- Gym Leader Clair: Dragonair x3 (Lv37), Kingdra (Lv40).

# Puzzles & Solutions
## Blackthorn Gym 2F Boulder Puzzle
- Status: Resetting floor to default state. Strength active.
- Verified: Boulder 5 does not exist. Only 3 boulders (6, 7, 8).
- Mechanics: Pushing a boulder into a pit removes it from 2F. Empty pits are impassable/warp for player.
- Strategy: Use BFS to find the sequence of pushes.
- Failed Attempts: 4 (BFS returned no solution due to incorrect grid or search limits).

# Resource Locations
- Route 45: Good training spot for Haunter (Night Shade).