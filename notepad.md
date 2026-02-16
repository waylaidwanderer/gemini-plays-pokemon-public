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
- State 1-1-1 (All ON): Gate 1 CLOSED.
- State 1-1-0 (Sw1, Sw2 ON): Gate 3 OPEN (Dead End).
Hypothesis: Gate 1 might require Sw3 ON and Sw2 OFF (State 1-0-1) or Sw1 OFF (State 0-1-1).
Plan:
1. Go to Switch 2 (10, 1). Turn OFF. (State 1-0-1).
2. Check Gate 1.
3. If Closed, Turn Sw2 ON, then try Sw3 OFF... wait, I've tried Sw3 OFF.
4. Maybe Turn Sw1 OFF? (Requires crossing to right side).