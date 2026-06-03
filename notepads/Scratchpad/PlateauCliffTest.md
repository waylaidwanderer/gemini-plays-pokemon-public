# Plateau Cliff North-Jump Empirical Test (Turn 44351)
- **Hypothesis**: The player can walk/jump North (Up) from the high plateau edge at (21, 12) (TYPE_2770) down to the northern ground level at (21, 11) (TYPE_3fe2).
- **Rationale**: If true, this will bypass the eastern stairs and save ~30-40 steps, placing us directly adjacent to the overworld item at (21, 10).
- **Methodology**:
  1. From (21, 13) facing Down, walk Up to (21, 12).
  2. Press Up to attempt to step/jump onto (21, 11).
  3. Verify position and screen:
     - Success: Position is (21, 11).
     - Failure: Position remains (21, 12) (blocked).