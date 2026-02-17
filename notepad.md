Location: Warehouse (2, 6) - Checking Gate 1.
Objective: Access Switch 3 (2, 1).
Current State: 0-1-0 (S1 OFF, S2 ON, S3 OFF).
- Wall (2, 10): CLOSED.
- Gate 1 (2, 6): Checking...
Plan:
1. Move Up to (2, 6).
2. If Gate 1 Open -> Go to Switch 3.
3. If Gate 1 Closed -> Backtrack to Switch 2 (10, 1).
   - Try S2 OFF (0-0-0) -> S1 ON (1-0-0) -> Try S3?
   - Or maybe find Card Key elsewhere?
Path: Up -> Up.