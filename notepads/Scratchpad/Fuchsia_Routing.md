# Fuchsia City Routing
Goal: Find path from South Fuchsia (Y > 25) to North Fuchsia (Y < 25).

Tested Vertical Columns (South to North):
- X=22: Blocked by inner corner ledge at Y=25.
- X=18: Blocked by Pokemon Center building at Y=27.
- X=3: Blocked by rock cliff at Y=25.

Plan: Trace the southern path (around Y=30-32) and test other columns (e.g., X=8, X=13, X=15).