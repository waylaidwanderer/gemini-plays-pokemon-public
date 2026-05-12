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

Turn 58995:
- Hypothesis 6: The ladder visible at (1,1) is on Level 2 (Dark Purple) and warps to 3F.
- Test 6: Walk from (4,5) to (0,5), North to (0,1), then Right to step onto the ladder at (1,1). Observe the destination.
Turn 59003:
- Context: Level 2 East is blocked by walls at X=22. Level 1 Y=16 is a dead end. The only remaining path to the 3F ladder is Level 1 East (Y=8 to Y=11).
- Hypothesis: I can walk horizontally from Level 2 to Level 1 if there is no drawn ledge. Specifically, from (15,11) [Dark Purple] to (16,11) [Dark Red].
- Test: Walk Left to (15,12), Up to (15,11), then Right to attempt to step onto (16,11).