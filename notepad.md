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
- Soft-locks: Pushing B7 to (5, 1) or B8 to (8, 10) traps the player or the boulder against immovable walls/NPCs.
- Cody (4, 1) and (5, 0) are impassable for boulders.
- Column 5 is the primary vertical artery for the gym.

# Puzzle Reset Strategy
- To reset boulder positions, leave the map (via ladder or pit) and return.
- Current Reset Path: Arrived on 1F via pit at (8, 3). Returning to 2F via ladder at (7, 9).

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