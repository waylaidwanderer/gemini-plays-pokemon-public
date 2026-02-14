# Warehouse Strategy
- Objective: Rescue Director (Underground Warehouse 3_54).
- Puzzle Status:
  - Switch 3 (2, 1): OFF -> Turn ON (Step 3).
  - Switch 2 (10, 1): ON.
  - Switch 1 (16, 1): ON.
- Observations:
  - Switch 1+2 ON -> (3, 6) is OPEN.
  - However, (3, 10) is still CLOSED (Wall). Path blocked.
- Strategy (Right End First):
  1. Reset All to OFF (Done).
  2. Switch 1 ON (Done).
  3. Switch 2 ON (Done).
  4. Switch 3 ON (Next).
  5. Check if (3, 10) opens.