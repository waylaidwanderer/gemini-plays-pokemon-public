=== ELEVATION & BOUNDARY TESTS ===
Turn 58987:
- Hypothesis 3: Horizontal movement from Dark Red to Dark Purple is blocked.
- Result 3 (Turn 58988): Player moved successfully to (1,5). Hypothesis 3 is FALSE. Color boundaries DO NOT block horizontal movement unless there's a drawn ledge!

Turn 58988:
- Hypothesis 4: The ladder at (1,1) on 2F connects to 3F and is accessible from the South.
- Test 4: Walk Up 4 times from (1,5) to (1,1).
- Result 4 (Turn 58989): Bumped immediately. Visited 0 tiles. Y=4 has a continuous South-facing ledge from X=0 to X=4 blocking Northward movement.

Turn 58989:
- Hypothesis 5: The X=5 trench (which is Dark Red) is the ONLY break in the Y=4 ledge. Boulder 2F-B at (5,5) blocks it. Pushing the boulder RIGHT to (6,5) will clear the trench.
- Test 5: Walk Right to (4,5) and push the boulder Right to (6,5).