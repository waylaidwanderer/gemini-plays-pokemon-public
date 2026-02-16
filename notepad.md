# Underground Warehouse Switch Puzzle (SOLVED)

**Solution:** Gate 3 (16, 6) opens with **Switch 1 ON** and **Switch 2 ON** (State 1-1-0). Switch 3 OFF.

**Mechanics Summary:**
- **Switch 2 (ON):** Opens Entrance (11, 6).
- **Switch 1 (ON):** Opens Exit (11, 10).
- **Switch 3 (ON):** Closes Entrance (11, 6) & Opens Gate 1.
- **Gate 3:** Closed if Switch 3 is ON. Open if Sw1 & Sw2 ON.

**Current Location:** Warehouse (3_54).
**Objective:** Open Gate 3.

Location: Warehouse (3_54).
Objective: Open Gate 1 (2, 6).
Status:
- State 0-0-1 (Sw1 OFF, Sw2 OFF, Sw3 ON): Gate 1 CLOSED.
- Next Test: State 0-1-1 (Sw1 OFF, Sw2 ON, Sw3 ON).
Plan:
1. Go to Switch 2 (10, 1). Turn ON.
2. Check Gate 1.
3. If still closed, I might need to try the "Only Switch 1 ON" or "Only Switch 3 ON" strategies again, carefully checking the *inner* walls.