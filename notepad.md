# Tile Mechanics
- FLOOR: Walkable.
- WALL: Impassable (statues, pillars, rocks).
- PIT: Warp to same coordinates on 1F. Filled by pushing a boulder into it. Player cannot walk on an empty pit.
- LADDER: Two-way warp between floors. (1, 7) and (7, 9).
- BOULDER: Pushable object. Acts as a wall for movement.

# Game Mechanics & Systems
## Blackthorn Gym Boulder Puzzle (2F)
- Current Attempt Start Turn: 34441
- Goal: Push 3 boulders into pits on 2F to bridge gaps on 1F.
- Verified Pits (2F): P0 (2, 5), P1 (8, 3), P2 (8, 7).
- Mechanics: Pushing a boulder moves it one tile. The player STAYS in their original tile. (Verified Turn 34432).
- Reset: Leaving the floor (via ladder or pit) resets all boulder positions. Strength must be reactivated (A to interact, B to close message, then walk into boulder).

## Boulder Positions (2F)
- Boulder 6: (3, 3) - Verifying
- Boulder 7: (6, 1) - Verifying
- Boulder 8: (8, 14) - Verified

# Strategy & Progress
- Lead Pokémon: XENON (Haunter, Lv36).
- Gym Leader Clair's Team: Dragonair x3 (Lv37), Kingdra (Lv40).

# Obstacles & Solutions
- Blackthorn Gym Pit Shifts (2F -> 1F):
  - (8, 3) -> (7, 6)
  - (2, 5) -> (2, 6)
  - (8, 7) -> (7, 7)

# Lessons Learned
- Puzzle Mechanics: In Blackthorn Gym, the player STAYS in their original tile after a push.
- Map Analysis: Boulder 8 at (8, 14) is blocked from a straight-up path to (8, 7) by walls at (8, 9).
- Tool Hygiene: Always re-verify foundational assumptions (like mechanics) before refining complex tools.