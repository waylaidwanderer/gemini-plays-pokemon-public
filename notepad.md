# Blackthorn Gym (Puzzle Progress)
- Start Turn: 34763
- Pits (2F): P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders (2F): B6 (3, 3), B7 (6, 1), B8 (8, 15).
- Status: Strength is ACTIVE.

# Tile Mechanics (2F)
- WALL: Impassable. (4, 0-10, 12), (2, 8), (3, 8), (4, 8), (8, 8, 9).
- NPC: Impassable (Cody 4,1, Fran 4,11).
- Gap: (4, 13) is the only FLOOR tile connecting the left (Cols 0-3) and right (Cols 5-9) sides.
- Horizontal Path (Row 13): (3,13) <-> (8,13) is clear.

# Puzzle Analysis (2F)
- P1 (8, 3) entry: (8, 2) DOWN. Stand at (8, 1).
- P2 (2, 5) entry: (1, 5) RIGHT. Stand at (0, 5).
- P3 (8, 7) entry: (8, 6) DOWN. Stand at (8, 5).
- B6 (3, 3) -> P2 (2, 5) via (3, 3) -> (3, 7) -> (0, 7) -> (0, 5) -> (1, 5) -> P2.
- B8 (8, 15) -> P3 (8, 7) via (8, 15) -> (8, 11) -> (9, 11) -> (9, 5) -> (8, 5) -> (8, 6) -> P3.
- B7 (6, 1) -> P1 (8, 3) via (6, 1) -> (8, 1) -> (8, 2) -> P1.

# Strategy: Blackthorn Gym 2F
- Step 1: Reach (8, 16) to push B8 UP.
- Step 2: Push B8 to (8, 11).
- Step 3: Push B8 to P3.
- Step 4: Push B6 to P2.
- Step 5: Push B7 to P1.

# Failed Hypotheses
- H1: Cody is passable. (Failed, Turn 34770)
- H2: B6 can reach P2 from the left side. (Failed, Turn 34775 - Col 4 blocks)
- H3: B8 must cross the gap to reach P2. (Possible, but B6 can do it via Row 7).