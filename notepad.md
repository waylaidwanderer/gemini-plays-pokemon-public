# Blackthorn Gym (Puzzle Progress)
- Start Turn: 34763
- Pits: P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders (Found): B6 (3, 3), B7 (6, 1), B8 (8, 14).
- Status: Strength ACTIVE.

# Puzzle Analysis (2F)
- Problem: B8 is currently trapped in Column 8. B6 and B7 are clear.
- Pushing: Player MOVES into boulder's old tile. (Verified Turn 34814, 34816, 34854).
- Problem: B8 is trapped in Column 8.
- Goal: Verify if (4, 10) and (7, 10) statues are passable floors.
- Test: Walk Right from (3, 10).

# Tile Mechanics (2F)
- WALL: (4, 0, 2-10, 12), (2, 8), (3, 8), (4, 8), (8, 8, 9), (7, 10, 11, 14, 15), (9, 12-17).
- GAP: (4, 1) and (4, 13-17) are passable.

# Strategy: Blackthorn Gym 2F
- Step 1: Explore Column 0 and 1 in the southern half.
- Step 2: Solve B6 and B7.
- Step 3: Re-evaluate B8.