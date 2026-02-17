Location: Warehouse (2, 9) - Wall (2, 10) is CLOSED.
Objective: Check Gate 1 (2, 6).
Current State: 0-1-0 (S1 OFF, S2 ON, S3 OFF).
- Wall (2, 10): CLOSED (Bumped).
- Gate 1 (2, 6): Checking now.
Plan:
1. Move Up to (2, 6).
2. If Gate 1 Open -> Access Switch 3 (2, 1).
3. If Gate 1 Closed -> Backtrack to Switch 2 (10, 1).
   - Try turning S2 OFF (0-0-0) -> Cross (15,4) -> S1 ON (1-0-0).
   - Or Try S3? (Need access).
Path: Up -> Up -> Up.