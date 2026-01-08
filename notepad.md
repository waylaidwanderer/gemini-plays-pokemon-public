# Blackthorn Gym (Puzzle Progress)
- Start Turn: 34763
- Pits: P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders: B6 (3, 3), B7 (6, 1), B8 (8, 10).
- Status: Strength is ACTIVE. Boulder 8 is STUCK at (8, 10).

# Game Mechanics
- Strength: Deactivated when changing maps or using ladders. Must be re-activated on a boulder.
- Pushing: After a push, the player moves into the boulder's old tile. (Confirmed Turn 34833).
- Ladders: (1, 7) and (7, 9) reset boulder positions on 2F.

# Tile Mechanics (2F)
- WALL: Impassable. (4, 0, 2-10, 12), (2, 8), (3, 8), (4, 8), (8, 8, 9), (7, 10, 11), (9, 12-17).
- GAP: (4, 1) and (4, 13-17) are passable.
- B8 Trap: Column 8 is a dead end for boulders north of Row 10. (8, 9) is a WALL.

# Strategy: Blackthorn Gym 2F
- Step 1: Reach ladder at (7, 9) to reset boulders.
- Step 2: Push B7 (6, 1) to P2 (2, 5) via Row 1 and Column 0.
- Step 3: Push B6 (3, 3) to P1 (8, 3) via Row 1.
- Step 4: Push B8 (8, 14) to P3 (8, 7) via Row 13 and Column 6.

# Failed Hypotheses
- H1: Boulder 8 can reach pits via Column 8. (Denied, Turn 34833 - (8, 9) is WALL).
- H2: Player stays in tile after push. (Denied, Turn 34833).