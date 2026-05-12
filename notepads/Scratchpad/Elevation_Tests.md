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
Turn 59006:
- Hypothesis 7: Y=11 is a South-facing ledge blocking Upward movement.
- Test 7: Walk Up from (20,12) [Dark Purple] to (20,11) [Dark Red].
- Result 7 (Turn 59007): Bumped. Visited 0 tiles. Hypothesis 7 is SUPPORTED. Y=11 is a one-way drop. The Y=12 corridor is a trap!

Turn 59011:
- Hypothesis 8: Switch 2F-B at (9,16) removes a barrier in the East, potentially the chasm at (23,14).
- Planned Test: Reset map, push Boulder 2F-A to (9,16), then walk East to check for changes.
Turn 59012:
- Observation: Walked Left from (10,17) [Level 1] towards (9,17) [Level 2]. Visited 0 tiles.
- Conclusion: The boundary at X=9 acts as a solid East-facing cliff. I am trapped on the West side of Level 1 here and must walk East to find stairs back up to Level 2.
Turn 59044: Successfully walked DOWN from (0,8) [Level 2, Dark Purple] to (0,9) [Level 1, Dark Red]. This empirically proves vertical color transitions without drawn ledges DO NOT block movement going South.