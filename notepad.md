# Warehouse Strategy
- Objective: Rescue Director (Underground Warehouse 3_54).
- Puzzle Status:
  - Switch 3 (2, 1): OFF.
  - Switch 2 (10, 1): OFF (Verifying).
  - Switch 1 (16, 1): ON -> Target: OFF.
- Strategy (Right End First):
  1. Reset All to OFF.
  2. Sequence: 1 -> 2 -> 3.
  3. Verify shutters at (12, 8) and (6, 8).
- Permutations Tested:
  - 3 -> 2 -> 1 (Fail).
  - 1 -> 3 -> 2 (Fail).
- Reflection (Turn 42008):
  - 50-turn review: Systematic testing is key. Avoid random toggles.
  - Improvement: Creating `toggle_switch` tool if this manual attempt fails.
  - Hygiene: Notepad consolidated. Map markers current.