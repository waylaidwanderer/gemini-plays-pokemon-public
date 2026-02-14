# Warehouse Switch Puzzle - Solution Testing
- State: Sw1 ON, Sw2 OFF, Sw3 ON.
- Status: Checking Shutter (3, 6).
- Logic:
  - Sw1 ON keeps (6, 8) open (Target).
  - Sw2 OFF *might* keep (3, 6) open (Hypothesis).
  - Sw3 ON triggers the "First Switch" mechanic.
- Expectation: (3, 6) should be OPEN.

## Plan
1. Move to (3, 5).
2. Check Shutter (3, 6).
3. If Open, go South to (3, 8) -> (6, 8).
4. If Closed, panic (just kidding, re-evaluate).