=== ELEVATION & BOUNDARY TESTS ===
Turn 58986:
- Test 2: Move 'Left', 'Left' from (4,5) [Dark Red].
- Result 2: Player moved successfully to (2,5). Movement between same-color tiles works.

Turn 58987:
- Hypothesis 3: Horizontal movement from Dark Red to Dark Purple is blocked.
- Test 3: I am at (2,5) [Dark Red]. Press 'Left' towards (1,5) [Dark Purple].
- Result 3 (Turn 58988): Player moved successfully to (1,5). Hypothesis 3 is FALSE. Color boundaries DO NOT block horizontal movement unless there's a drawn ledge!

Turn 58988:
- Hypothesis 4: The ladder at (1,1) on 2F connects to 3F.
- Test 4: Walk Up 4 times from (1,5) to (1,1) to take the ladder and observe the destination.