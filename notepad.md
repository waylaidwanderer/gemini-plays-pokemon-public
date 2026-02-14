# Warehouse Switch Puzzle - Solution Testing
- State: Sw1 ON, Sw2 OFF (Toggling NOW), Sw3 ON.
- Hypothesis: [Sw1 ON, Sw2 OFF, Sw3 ON] is the solution.
- Logic:
  - Sw1 ON opens (6, 8) (Target).
  - Sw3 ON closes (12, 8) (Trap)?
  - Sw2 OFF opens (6, 6) (Path).
- Plan: Toggle Sw2 OFF. Check (6, 6).

## Plan
1. Turn Switch 2 OFF (Press A x3).
2. Move to (6, 5).
3. Check Shutter (6, 6).
4. If Open, proceed to (6, 8) and Director.