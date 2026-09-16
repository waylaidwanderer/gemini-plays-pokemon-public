# Victory Road 2F Sokoban & Route Plan (Audited Turn 20255)

## Root Cause Diagnostics
- Doorway (5, 4) was plugged by pushing Western Boulder north to (5, 3) on Turn 20203.
- Eastern bypass attempts failed because Column 14 (rows 0-7) and Column 8 (rows 2-7) are continuous solid rock walls.

## Action Plan to Reach 3F:
1. Walk from current position (15, 7) back to ladder (0, 8):
   - East along Row 7 to (20, 7).
   - South along Column 20 to (20, 11).
   - West along Row 11 to (5, 11).
   - Up wooden staircase (5, 10) to (5, 9).
   - North/west along Western Highway (cols 2-3) to ladder (0, 8).
2. Reset Boulder State:
   - Descend ladder (0, 8) to Victory Road 1F.
   - Ascend ladder back to 2F (resets Western Boulder to default at (5, 5)).
3. Clear Doorway (5, 4):
   - Activate Strength with Geodude (ROCKY).
   - Approach (5, 5) from the east at (6, 5), facing West.
   - Push boulder WEST from (5, 5) to (4, 5).
4. Ascend to 3F:
   - Walk into (5, 5), North through doorway (5, 4) into (5, 3).
   - Walk west to ladder at (1, 1) and climb to Victory Road 3F!