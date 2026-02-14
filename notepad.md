# Warehouse Switch Puzzle - Solution Testing
- State: Sw1 ON, Sw2 OFF, Sw3 OFF (Toggling NOW).
- Hypothesis: Switch 3 OFF opens (3, 6) and/or (6, 6).
- Previous Findings:
  - Sw1 ON opens (6, 8) and (12, 8).
  - Sw2 ON closes (3, 6).
  - Sw3 ON + Sw2 OFF + Sw1 ON = (3, 6) Closed.
- Logic: If Sw3 ON keeps (3, 6) closed, maybe Sw3 OFF opens it?

## Plan
1. Finish toggling Switch 3 to OFF.
2. Check Shutter (3, 6).
3. If Open, proceed South.
4. If Closed, Check Shutter (6, 6).