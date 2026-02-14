# Warehouse Switch Puzzle - Solution Testing
- Observation: Switch 2 ON closed (3, 6) (changed 3fe2->2889).
- Observation: Switch 1 ON closed (12, 8) (Trap) and opened (6, 8) (Target).
- Current State: Sw1 ON, Sw2 ON, Sw3 ON.
- Problem: All paths South (3, 6), (6, 6) are closed.
- Hypothesis: Switch 2 OFF opens (3, 6).
- Plan: Set state to [Sw1 ON, Sw2 OFF, Sw3 ON].
- Route: Go down (3, 6) -> (3, 8) -> (6, 8) -> Director.

## Plan
1. Turn Switch 2 OFF.
2. Move to (3, 6).
3. If Open, go South to Row 8.
4. Go East to (6, 8) and check if still Open.
5. Proceed to Director.