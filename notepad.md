# Tile Mechanics
- FLOOR: Walkable.
- WALL: Impassable. (Visual confirmation: pillars/statues at (4,2), (6,2), (4,5), (7,10), (7,11) etc. are solid walls).
- PIT: Warp to same coordinates on 1F. Can be filled by pushing a boulder into it.
- LADDER: Two-way warp between floors. Located at (1, 7) and (7, 9).
- BOULDER: Pushable object requiring STRENGTH. Acts as a wall for movement.

# Game Mechanics & Systems
## Blackthorn Gym Boulder Puzzle (2F)
- Start Turn: 34112 (Current Time: ~200 turns elapsed)
- Goal: Push 3 boulders into pits on 2F to bridge gaps on 1F.
- Verified Pits (2F): P0 (2, 5), P1 (8, 3), P2 (8, 7).
- Original Boulder Positions: B6 (3, 3), B7 (6, 1), B8 (8, 14).
- Mechanics: Pushing a boulder moves it one tile, but the player stays in their original position. Boulders cannot be pushed into NPCs.

# Lessons Learned
- Puzzle Reset: Boulders DO NOT reset when switching floors via pit or ladder. They only reset when leaving the Gym entirely (e.g., exiting the front door).
- Mechanics: Pushing a boulder moves it one tile, but the player stays in their original position. Boulders cannot be pushed into NPCs.
- Current Status [Turn #34318]: B6 at (3, 3), B7 at (7, 1). Heading to B8's last known position (8, 11) to update the XML map. Once all boulders are seen, I will use the corrected solver tool.
- Layout: Row 13 is a safe horizontal crossing between the left and right sides of the gym. Column 5 is the primary vertical artery.

# Pokemon & Party Information
## Strategy for Gym Leader Clair
- Clair's Team: Dragonair x3 (Lv37), Kingdra (Lv40).
- Tactical Plan: Lead Calcifer (Typhlosion, Lv49). Use `battle_advisor_v2`.

# Obstacles & Solutions
- Blackthorn Gym Pit Shifts:
  - 2F (8, 3) -> 1F (7, 6)
  - 2F (2, 5) -> 1F (2, 6)
  - 2F (8, 7) -> 1F (7, 7)

# Puzzle Testing Log
- Turn 34309: Testing walkability of pillar at (6, 3) to find a push path for P1 (8, 3).
- (4, 5), (5, 0), (7, 11), (9, 13) confirmed solid WALL.
- Cody (4, 1) is solid for boulders.
- Turn 34311: Confirmed (6, 3) is a solid WALL.
- Hypothesis: The puzzle is solvable if one specific wall tile is actually floor. I will use code to identify candidates.

# Puzzle Testing Log
- Turn 34313: Testing walkability of pillar at (4, 3).
- Hypothesis: (4, 3) is a fake wall (gap in pillars), which would allow pushing B6 Left from (3, 3).
- Test: Move Left from (5, 3).
- Turn 34314: Confirmed (4, 3) is a solid WALL.
- Turn 34314: Testing walkability of pillar at (4, 4).
- Hypothesis: (4, 4) is a fake wall, allowing the player to stand there to push B6 Left from (3, 4).
- Test: Move Left from (5, 4).