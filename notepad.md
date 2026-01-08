# Tile Mechanics
- FLOOR: Walkable.
- WALL: Impassable (some statues/pillars in middle are walkable).
- PIT: Warp to same coords on 1F. Boulders fill gaps.
- LADDER: Two-way warp between floors. (1,7) and (7,9).
- BOULDER: Pushable with Strength.
- NPCs: Impassable walls. Cody (4,1) persists after defeat.

# Game Mechanics & Systems
## Blackthorn Gym Boulder Puzzle (2F)
- Goal: Push 3 boulders into pits on 2F to bridge gaps on 1F.
- Verified Pits (2F): (2, 5), (8, 3), (8, 7).
- Original Boulder Positions: B6 (3, 3), B7 (6, 1), B8 (8, 14).
- Strategy: Solve one boulder at a time. Target B8 first.

## Boulder 8 (8, 12) -> Pit (8, 7) Plan
1. Push B8 (8, 12) Up to (8, 11). (Player at 8, 13).
2. Push B8 (8, 11) Up to (8, 10). (Player at 8, 12).
3. Move to (9, 10).
4. Push B8 (8, 10) Left to (7, 10) -> TEST IF WALKABLE.
5. If (7, 10) is WALL, push B8 to (9, 10) and explore column 9.

# Verified Impassable Tiles
- (9, 13): WALL (Tested Turn 34255)
- (8, 9): WALL (Visual)
- (7, 11): WALL (Visual)
- (7, 10): WALL (Visual)

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