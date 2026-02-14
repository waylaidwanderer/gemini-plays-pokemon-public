# Warehouse Strategy
- Objective: Find the Director in Underground Warehouse (3_54).
- Puzzle Status:
  - Switch 3 (2, 1): OFF.
  - Switch 2 (10, 1): OFF (Verified).
  - Switch 1 (16, 1): ON -> Target: OFF.
- Strategy (Right End First Hypothesis):
  1. Reset All to OFF.
  2. Sequence: Switch 1 -> Switch 2 -> Switch 3.
  3. Verify shutters at (12, 8) and (6, 8) after each step.
- Clues:
  - "End is the one to press first" -> Interpreting as Right End (Switch 1).
  - "Change the order of switching."
- Permutations Tested:
  - 3 -> 2 -> 1 (Fail).
  - 1 -> 3 -> 2 (Fail).
  - Next: 1 -> 2 -> 3.
  - Contingency: 3 -> 1 -> 2.