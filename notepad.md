# Warehouse Strategy
- Objective: Rescue Director (Underground Warehouse 3_54).
- Puzzle Status:
  - Switch 3 (2, 1): OFF.
  - Switch 2 (10, 1): OFF -> Turn ON (Step 2).
  - Switch 1 (16, 1): ON.
- Observations (Switch 1 ON):
  - (12, 8): OPEN (Floor).
  - (6, 8): CLOSED (Wall).
  - (3, 6): CLOSED (Wall).
- Strategy (Right End First):
  1. Reset All to OFF (Done).
  2. Switch 1 ON (Done).
  3. Switch 2 ON (Executing).
  4. Verify shutters.
  5. Switch 3 ON.