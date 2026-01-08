# Tile Mechanics (Global)
- FLOOR: Standard walkable tile.
- WALL: Impassable collision (pillars, statues, rocks, NPCs).
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
- Divider: Column 4 is a wall from Row 2 to Row 12. Column 6 is a wall at Row 2, 3, 4, 6.
- Connection: Strips are connected at Row 1 (Top) and Row 13-17 (Bottom).

# Puzzles & Solutions
## Blackthorn Gym 2F Boulder Puzzle
- Status: Strength active. Standing at (3, 4) facing Boulder 6 (3, 3).
- Plan: Run a comprehensive BFS solver with the "stay in place" mechanic and exact grid.

# Resource Locations
- Route 45: Good training spot for Haunter (Night Shade).

## Push Mechanic Test (Turn 34565)
- Observation: Standing at (3, 4) facing Boulder 6 at (3, 3). Strength active.
- Hypothesis: Pushing a boulder moves it one tile, and the player stays in their original tile.
- Test: Press 'Up' to push Boulder 6 to (3, 2).
- Conclusion: CONFIRMED. Player stayed at (3, 4) while boulder moved to (3, 2). (Turn 34566)