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
- State 0-1-1 (Sw1 OFF, Sw2 ON, Sw3 ON).
- Checking Gate 1.
- Trap (10, 4) should be SAFE with Sw2 ON.
Plan:
1. Navigate to Gate 1 (2, 6).
2. Check if Gate 1 is OPEN.
3. If Closed, the only remaining reasonable combination is 0-1-0 (Sw1 OFF, Sw2 ON, Sw3 OFF) or 1-0-0 (Sw1 ON, Sw2 OFF, Sw3 OFF).