# Tile Mechanics (Global)
- FLOOR: Standard walkable tile.
- WALL: Impassable collision (pillars, statues, rocks).
- LADDER: Two-way warp between floors. (1, 7) and (7, 9).
- PIT: A hole that leads to 1F. Boulders fall through to fill gaps on 1F. Empty pits are impassable/warp; filled pits on 1F become walkable.
- BOULDER: Pushable object. Requires STRENGTH. Pushing moves it one tile. Player STAYS in original tile. (Verified Turn 34566)

# Blackthorn Gym (2F) Puzzle
- Goal: Push three boulders into pits to bridge gaps to Gym Leader Clair on 1F.
- Boulder 6: (3, 3)
- Boulder 7: (6, 1)
- Boulder 8: (8, 14)
- Pit A: (8, 3)
- Pit B: (2, 5)
- Pit C: (8, 7)
- NPC Obstacles: Cody (4, 1), Fran (4, 11), Lola (9, 2), Paul (1, 15) are solid and block player/boulders.

# Strategy & Progress
- Lead Pokémon: XENON (Haunter, Lv36). Target Lv40 on Route 45.
- Gym Leader Clair: Dragonair x3 (Lv37), Kingdra (Lv40).

# Puzzles & Solutions
## Blackthorn Gym 2F Boulder Puzzle
- Status: Resetting floor to default state. Verified mechanic: player stays in place.
- Failed Attempts: 4 (BFS returned no solution due to incorrect mechanic or grid assumptions).
- Plan: Use refined solve_blackthorn_boulders_v3 from reset state.

# Resource Locations
- Route 45: Good training spot for Haunter (Night Shade).

## Push Mechanic Test (Turn 34565)
- Observation: Standing at (3, 4) facing Boulder 6 at (3, 3). Strength active.
- Hypothesis: Pushing a boulder moves it one tile, and the player stays in their original tile.
- Test: Press 'Up' to push Boulder 6 to (3, 2).
- Conclusion: CONFIRMED. Player stayed at (3, 4) while boulder moved to (3, 2). (Turn 34566)