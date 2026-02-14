# Warehouse Switch Puzzle - Solution Testing
- Observation: Switch 2 ON closed (3, 6).
- Observation: Switch 1 ON closed (12, 8) (Trap) and opened (6, 8) (Target).
- Current State: Sw1 ON, Sw2 OFF, Sw3 ON.
- Status: Moving to check (3, 6).
- Hypothesis: Switch 2 OFF opens (3, 6).

## Plan
1. Move Left to (3, 5).
2. Check (3, 6).
3. If Open, go South to (3, 8) -> (6, 8) -> Director.
4. If Closed, strategy failed. Re-evaluate Switch 3.