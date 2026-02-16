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
- State 1-0-1 (Sw1 ON, Sw2 OFF, Sw3 ON).
- Trap (10, 4) CONFIRMED SAFE in this state.
- Proceeding to Switch 1 (16, 1) to Turn OFF.
Hypothesis: Switch 1 OFF + Switch 2 OFF + Switch 3 ON = Gate 1 OPEN.
Plan:
1. Navigate to Switch 1 (16, 2).
2. Turn Switch 1 OFF.
3. Return to Gate 1 (2, 6) via Row 2 (Safe).