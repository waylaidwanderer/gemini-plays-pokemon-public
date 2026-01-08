# Tile Mechanics
- FLOOR: Walkable.
- WALL: Impassable. (Visual confirmation: pillars/statues at (4,2), (6,2), (4,5), (7,10), (7,11) etc. are solid walls).
- PIT: Warp to same coordinates on 1F. Can be filled by pushing a boulder into it.
- LADDER: Two-way warp between floors. Located at (1, 7) and (7, 9).
- BOULDER: Pushable object requiring STRENGTH. Acts as a wall for movement.

# Game Mechanics & Systems
## Blackthorn Gym Boulder Puzzle (2F)
- Start Turn: 34112
- Goal: Push 3 boulders into pits on 2F to bridge gaps on 1F.
- Verified Pits (2F): P0 (2, 5), P1 (8, 3), P2 (8, 7).
- Original Boulder Positions: B6 (3, 3), B7 (6, 1), B8 (8, 14).
- Mechanics: Pushing a boulder moves it one tile, but the player stays in their original position. Boulders cannot be pushed into NPCs.

# Lessons Learned
- Puzzle Status [Turn 34305]: Boulder 8 pushed to (8, 11). Standing at (8, 13) to move to (8, 12).

# Strategy: Test Central Pillars for Hidden Paths
1. Push B8 Up to (8, 10).
2. Move to (9, 10).
3. Attempt to push B8 Left into (7, 10).
4. If successful, (7, 10) is a hidden gap.

# Lessons Learned
- Verified Walls: (4,2), (6,2), (4,5), (5,0), (7,11) are solid.
- Soft-locks: Pushing B7 to (5, 1) or B8 to (8, 10) against a TRUE wall blocks progress.
- Cody (4, 1) is a solid obstacle for boulders.
- Boulders move 1 tile per push; player stays in original position.

# Pokemon & Party Information
## Strategy for Gym Leader Clair
- Clair's Team: Dragonair x3 (Lv37), Kingdra (Lv40).
- Tactical Plan: Lead Calcifer (Typhlosion, Lv49). Use `battle_advisor_v2`.

# Obstacles & Solutions
- Gym Navigation: Ladders (1,7) and (7,9) connect to 1F. Crossing at (4,13) connects Left/Right sides on 2F.
- Blackthorn Gym Pit Shifts:
  - 2F (8, 3) -> 1F (7, 6)
  - 2F (2, 5) -> 1F (2, 6)
  - 2F (8, 7) -> 1F (7, 7)