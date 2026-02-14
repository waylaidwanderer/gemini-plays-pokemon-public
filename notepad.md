# Warehouse Switch Puzzle - Solution (Final)
- Logic:
  - Switch 1 ON opens `(6, 6)` and `(10, 2)`. (Essential for movement).
  - Switch 2 ON opens `(6, 8)`. (Essential for destination).
  - Switch 3 ON (Already ON).
- Conclusion: ALL SWITCHES MUST BE ON.
- Current State: Sw1 ON, Sw2 OFF, Sw3 ON.
- Action: Turn Switch 2 ON.

## Plan
1. Move to Switch 2 (10, 2).
2. Turn Switch 2 ON.
3. Verify `(6, 8)` opens.
4. Go through `(6, 8)` to Director.