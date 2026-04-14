# Fuchsia City Routing
Goal: Find path from South Fuchsia (Y > 25) to North Fuchsia (Y < 25).

Tested Vertical Columns (South to North):
- X=22: Blocked by inner corner ledge at Y=25.
- X=18: Blocked by Pokemon Center building at Y=27.
- X=3: Blocked by rock cliff at Y=25.

Plan: Trace the southern path (around Y=30-32) and test other columns (e.g., X=8, X=13, X=15).
- Test: At (3,30). Vertical ledge at X=2 blocks West. Horizontal ledge at Y=31 blocks North from Y=32. Plan is to jump South over Y=31, land at (3,32), walk West to X=1 (bypassing the vertical ledge), and then walk North.
- Test Result (Turn 27738): Walked North along X=1. Reached Y=16. The path North is blocked by a horizontal row of cuttable trees spanning from X=0 to at least X=6 at Y=15. Cutting a tree here will grant access to the Northern half of the city (where the Poke Mart is).