# Tile Mechanics
- FLOOR: Walkable.
- WALL: Impassable (statues, pillars, rocks).
- PIT: Warp to same coordinates on 1F. Filled by pushing a boulder into it. Player falls if walking on an empty pit.
- LADDER: Two-way warp between floors. (1, 7) and (7, 9).
- BOULDER: Pushable object. Acts as a wall for movement.

# Game Mechanics & Systems
## Blackthorn Gym Boulder Puzzle (2F)
- Current Attempt Start Turn: 34441
- Goal: Push 3 boulders into pits on 2F to bridge gaps on 1F.
- Verified Pits (2F): P0 (2, 5), P1 (8, 3), P2 (8, 7).
- Mechanics Verification:
  - Attempt 1: Pushing B6 Up from (3, 4). (Pending)
- Reset: Leaving the floor resets all boulder positions and Strength.

## Boulder Positions (2F)
- Boulder 6: (3, 3)
- Boulder 7: (6, 1)
- Boulder 8: (8, 14)

# Strategy & Progress
- Lead Pokémon: XENON (Haunter, Lv36).
- Gym Leader Clair's Team: Dragonair x3 (Lv37), Kingdra (Lv40).

# Obstacles & Solutions
- Blackthorn Gym Pit Shifts (2F -> 1F):
  - (8, 3) -> (7, 6)
  - (2, 5) -> (2, 6)
  - (8, 7) -> (7, 7)

# Lessons Learned
- Puzzle Mechanics: Foundational assumptions must be explicitly tested.
- Map Analysis: Boulder 8 at (8, 14) is blocked from a straight-up path to (8, 7) by walls at (8, 9).
- Tool Hygiene: Commit to one verified mechanic and use a single refined tool.