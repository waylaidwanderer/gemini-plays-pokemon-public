Location: Warehouse (14, 8) -> Moving to Switch 2 via Row 1.
Objective: Open Secret Door (11, 6) (Target 0-1-0).
Current State: 1-0-0 (S1 ON, S2 OFF, S3 OFF).
- Gate 3 (16, 6) is OPEN.
- Gate 1 (2, 6) is CLOSED.
- Wall (11, 10) is OPEN.
Plan:
1. Move to Switch 1 (16, 1).
2. Attempt to cross Row 1 to Switch 2 (10, 1).
   - Hazard: Trap/Item at (15, 1).
   - If (15, 1) is passable, I reach Switch 2.
   - If (15, 1) warps, navigate from warp point.
3. Turn S2 ON (State -> 1-1-0).
4. Turn S1 OFF (State -> 0-1-0).
   - Access Secret Door.
Path: Right to (16, 8) -> Up to (16, 1) -> Left to (15, 1).