# Blackthorn Gym (Puzzle Progress)
- Pits (2F): P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders (2F): B6 (3, 3), B7 (6, 1), B8 (8, 14).
- Status: Strength is ACTIVE.

# Verified Obstacles (2F)
- Column 4: Almost all WALL/NPC. Gap at (4, 13).
- Row 8: WALLs at (2, 8), (3, 8), (4, 8).
- Column 9: WALLs in many rows.

# Puzzle Analysis (2F)
- P1 (8, 3) entry: Must be from (8, 2) DOWN (stand 8, 1) or (7, 3) RIGHT (stand 6, 3 WALL) or (9, 3) LEFT (stand 10, 3 VOID).
- P2 (2, 5) entry: (2, 4) DOWN (stand 2, 3), (2, 6) UP (stand 2, 7), (1, 5) RIGHT (stand 0, 5), (3, 5) LEFT (stand 4, 5 WALL).
- P3 (8, 7) entry: (8, 6) DOWN (stand 8, 5), (8, 8) UP (stand 8, 9 WALL), (7, 7) RIGHT (stand 6, 7 WALL), (9, 7) LEFT (stand 10, 7 VOID).

# Strategy: Blackthorn Gym 2F
- Step 1: Push B6 (3, 3) DOWN to (3, 4).
- Step 2: Use run_code to find paths for all boulders to valid entry points.
- Step 3: Execute.

# Failed Hypotheses
- H1: Cody is passable. (Failed, Turn 34770)
- H2: B6 can reach P2 from the right. (Failed, Column 4 is WALL)