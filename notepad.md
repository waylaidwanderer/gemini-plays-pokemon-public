Location: Warehouse (3_54).
Objective: Test State 0-1-1 (Sw1 OFF, Sw2 ON, Sw3 ON).
Status:
- State 0-1-1.
- Tool Results:
  - G1 (Left): OPEN.
  - G2 (Middle): OPEN.
  - G3 (Right): OPEN.
  - G4 (Inner Left): CLOSED.
  - (12,8) Middle Path: WALL/CLOSED.
Hypothesis:
- Sw1 determines if Col 12 (ON) or Col 16 (OFF) is open.
- Sw1 is OFF, so Col 16 should be Floor.
- Sw3 ON might open the end of Col 16?
Plan:
1. Check end of Right Path (16, 10).
2. If blocked, check Middle Gate (10, 6).
3. Update Matrix.