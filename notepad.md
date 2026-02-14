# Warehouse Strategy
- Objective: Rescue Director (Underground Warehouse 3_54).
- Puzzle Status:
  - Switch 3 (2, 1): ON (Verifying).
  - Switch 2 (10, 1): ON.
  - Switch 1 (16, 1): ON.
- Observations:
  - Switch 1+2 ON -> (3, 6) is OPEN.
  - Switch 3 ON -> Expect (3, 10) to OPEN.
- Strategy (Right End First):
  1. Reset All to OFF (Done).
  2. Switch 1 ON (Done).
  3. Switch 2 ON (Done).
  4. Switch 3 ON (Done).
  5. Check if (3, 10) opens.
- Next Action:
  - Walk South through (3, 6) to (3, 10).
  - If open, proceed to Director at (9, 12).