=== ELEVATION & BOUNDARY TESTS ===
Turn 58982:
- Context: Overwatch warned me about making unverified assumptions regarding tile color boundaries and ladder destinations.
- Hypothesis 1: The boundary between Dark Red tiles (Level 1) and Dark Purple tiles (Level 2) acts as a solid wall preventing upward movement.
- Test 1: I am at (3,5) [Dark Red]. I will press 'Up' to attempt to walk onto (3,4) [Dark Purple].
- Expected Result: If I bump and stay at (3,5), upward movement across this boundary is blocked.
- Result 1 (Turn 58983): Pressed 'Up', visited 0 tiles, remained at (3,5). Hypothesis 1 is SUPPORTED for this specific boundary.

Turn 58983:
- Hypothesis 2: Movement between tiles of the same color is unobstructed.
- Test 2: Move 'Right' from (3,5) [Dark Red] to (4,5) [Dark Red].
- Expected Result: Player successfully moves to (4,5).