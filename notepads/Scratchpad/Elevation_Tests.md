=== ELEVATION & BOUNDARY TESTS ===
Turn 58982:
- Context: Overwatch warned me about making unverified assumptions.
- Test 1: I am at (4,5) [Dark Red]. Pressed 'Up' towards (4,4) [Dark Purple].
- Result 1: Visited 0 tiles, bumped. Upward movement from Dark Red to Dark Purple is BLOCKED.

Turn 58986:
- Hypothesis 2: Movement between tiles of the same color is unobstructed.
- Test 2: Move 'Left', 'Left' from (4,5) [Dark Red].
- Result 2: Player moved successfully to (2,5). Hypothesis 2 is SUPPORTED.

Turn 58987:
- Hypothesis 3: Horizontal movement from Dark Red (Level 1) to Dark Purple (Level 2) is blocked.
- Test 3: I am at (2,5) [Dark Red]. Press 'Left' towards (1,5) [Dark Purple].
- Expected Result: Bump (0 tiles visited).