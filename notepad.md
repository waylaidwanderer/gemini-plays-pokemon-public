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
Objective: Open Gate 1 (2, 6) to access the South area.
Status:
- State 1-0-1 (Sw1 ON, Sw2 OFF, Sw3 ON): Gate 1 CLOSED.
- State 1-1-1 (All ON): Gate 1 CLOSED.
Hypothesis: Switch 1 (currently ON) is keeping Gate 1 closed.
Plan:
1. Go to Switch 1 (16, 1). Turn OFF.
2. Resulting State: 0-0-1 (Sw1 OFF, Sw2 OFF, Sw3 ON).
3. Check Gate 1 (2, 6). It should be OPEN.
4. If Open, check Wall (2, 10). If open, proceed East along Row 12 to find the Grunt.