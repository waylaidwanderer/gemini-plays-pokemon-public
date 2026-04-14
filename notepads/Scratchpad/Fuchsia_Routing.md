# Fuchsia City Routing
Goal: Find path from South Fuchsia (Y > 25) to North Fuchsia (Y < 25).

Tested Vertical Columns (South to North):
- X=22: Blocked by inner corner ledge at Y=25.
- X=18: Blocked by Pokemon Center building at Y=27.
- X=3: Blocked by rock cliff at Y=25.

Plan: Trace the southern path (around Y=30-32) and test other columns (e.g., X=8, X=13, X=15).
- Test: At (3,30). Vertical ledge at X=2 blocks West. Horizontal ledge at Y=31 blocks North from Y=32. Plan is to jump South over Y=31, land at (3,32), walk West to X=1 (bypassing the vertical ledge), and then walk North.
- Test Result (Turn 27738-27745): Walked North along X=1. Reached Y=16. The path North is blocked by dense bushes at Y=15, which cannot be cut. The path East is blocked by a white fence at X=4. X=1 is a dead end for reaching the North half.
- Plan (Turn 27748): Walk South to Y=32, then East to X=11 to visually inspect vertical paths between X=4 and X=15.
- Test Result (Turn 27749-27751): At (1, 29). Walked South to (1, 31). Jumped South over the ledge to (1, 32).
- Test Result (Turn 27753): The area South of Y=31 and West of X=10 is a soft-lock trap. The ledge at Y=31 prevents walking North. The cliff at X=10 prevents walking East. Water/fences prevent walking West/South. I MUST use FLY to escape.
- Hypothesis: To reach the Poke Mart (5, 13) from the Pokemon Center (19, 28), the path North might be at X=17, bypassing the left side of the Pokemon Center building.