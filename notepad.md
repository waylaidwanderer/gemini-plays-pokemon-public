Location: Warehouse (2, 5) - Checking Gate 1.
Objective: Check Gate 1 (2, 6).
Current State: 1-0-0 (S1 ON, S2 OFF, S3 OFF).
- Testing if Gate 1 is OPEN in 1-0-0.
- If Open: Access Switch 3 (2, 1).
- If Closed:
  - Hypothesis: Need S1+S3? Or maybe S3 alone?
  - Problem: Can't reach S3 if Gate 1 is closed.
  - Check Wall (2, 10) as well.
Plan:
1. Move Left to (2, 5).
2. Move Down to check Gate 1 (2, 6).
3. If blocked, Move Down to check Wall (2, 10).
Path: Left x9 -> Down.