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
- State 0-0-0 (All OFF).
- Testing Gate 1.
Plan:
1. Check Gate 1 (2, 6).
2. If Closed, I'm resetting to try a specific sequence starting with "The End Switch".
3. Sequence Hypothesis: Sw3 -> Sw2 -> Sw1? Or Sw1 -> Sw2 -> Sw3?
4. But first, check Gate 1.