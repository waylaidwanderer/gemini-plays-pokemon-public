# Tile Mechanics
- FLOOR: Walkable.
- WALL: Impassable. (Visual confirmation: pillars at (7, 10), (7, 11), etc. are solid walls).
- PIT: Warp to same coordinates on 1F. Can be filled by pushing a boulder into it.
- LADDER: Two-way warp between floors. Located at (1, 7) and (7, 9).
- BOULDER: Pushable object requiring STRENGTH. Acts as a wall for movement.

# Game Mechanics & Systems
## Blackthorn Gym Boulder Puzzle (2F)
- Goal: Push 3 boulders into pits on 2F to bridge gaps on 1F.
- Verified Pits (2F): P0 (2, 5), P1 (8, 3), P2 (8, 7).
- Original Boulder Positions: B6 (3, 3), B7 (6, 1), B8 (8, 14).

## Solution Strategy [Turn 34276]
### Boulder 7 -> Pit (8, 3)
1. At (5, 1), push B7 (6, 1) Right to (7, 1).
2. Move to (6, 1).
3. Push B7 (7, 1) Right to (8, 1).
4. Move to (7, 1).
5. Push B7 (8, 1) Down to (8, 2).
6. Move to (8, 1).
7. Push B7 (8, 2) Down into (8, 3) PIT.

### Boulder 6 -> Pit (2, 5)
1. Move to (3, 4). Push Up to move B6 to (3, 2).
2. Move to (3, 3). Push Left to move B6 to (2, 3).
3. Move to (2, 2). Push Down to move B6 to (2, 4).
4. Move to (2, 3). Push Down to move B6 into (2, 5) PIT.

### Boulder 8 -> Pit (8, 7)
1. Push B8 (8, 14) to (8, 12).
2. Push B8 Left into column 6 at (6, 12).
3. Push B8 Up column 6 to (6, 7).
4. Push B8 Right into (8, 7) PIT.

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

# Hypotheses to Test
1. Cody (4, 1) is a wall even after defeat. (Likely True).
2. Boulders can be pushed into Trainers. (Likely False).
3. Row 0 walls are all impassable. (Tested (5, 0), need to test others).
4. Column 8/9 Row 4 walls are impassable. (Visual confirmation).
5. B8 can be moved to the left side via Row 11 if (7, 11) is actually walkable. (Tested (7, 11), it was WALL).

# Boulder 7 Plan (Revised)
1. Move to (9, 1) via (7, 1) -> (7, 2) -> (8, 2) -> (9, 2).
2. Push B7 (8, 1) Left to (7, 1).
3. Push B7 (7, 1) Left to (6, 1).
4. Push B7 (6, 1) Left to (5, 1).
5. See if B7 can be pushed into Cody at (4, 1).
6. If not, B7 MUST go Down Column 5. (Requires (5, 0) to be walkable, but tested it as WALL).
7. RE-TEST (5, 0) carefully. Maybe I hit a corner?
- Turn 34288: Confirmed Cody (4, 1) is a solid obstacle for boulders. Pushing B7 into him fails (snaps back).
- Hypothesis: Boulders cannot be pushed into NPCs. (Confirmed).
- Test 4: Attempt to push B7 from (5, 2) into (5, 0). (Verifying Row 0 wall).