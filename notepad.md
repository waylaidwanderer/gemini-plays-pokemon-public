# Blackthorn Gym (Puzzle Progress)
- Start Turn: 34763
- Pits: P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders: B6 (3, 3), B7 (6, 1), B8 (8, 14).
- Status: Strength ACTIVE.

# Scientific Verification of "Walls" (2F)
- Hypothesis: Some tiles marked "WALL" are actually passable floor tiles or statues.
- Test 1: Cody (4, 1) -> Confirmed WALL (Turn 34880).
- Test 2: Fran (4, 11) -> Confirmed WALL (Turn 34865).
- Test 3: (4, 10) -> Confirmed WALL (Turn 34863).
- Test 4: (4, 9) -> Confirmed WALL (Turn 34883).
- Test 5: (6, 2) -> Confirmed WALL (Turn 34887). (6, 3) -> Confirmed WALL (Turn 34885).
- Test 6: (7, 10) and (7, 11) -> Confirmed WALLs (Turn 34796, 34868).
- Test 7: (8, 8) and (8, 9) -> Pending.
- Test 8: (2, 9) and (2, 13) gaps -> Pending.

# Verified Obstacles (2F)
- Column 4: (4, 1), (4, 9), (4, 10), (4, 11), (4, 12) are WALLs.
- Column 6: (6, 3) is WALL.
- Column 7: (7, 10), (7, 11) are WALLs.
- Column 9: (9, 13) is WALL.

# Strategy: Blackthorn Gym 2F
- Step 1: Systematically walk into every "WALL" tile adjacent to boulder paths.
- Step 2: Update map based on findings.
- Step 3: Use BFS solver (run_code) with corrected map.

# Verified Obstacles (2F)
- Column 4: (4, 1), (4, 10), (4, 11), (4, 12) are WALLs.
- Column 8: (8, 8, 9) are likely WALLs (Seen=true).
- Column 9: (9, 13) is WALL.