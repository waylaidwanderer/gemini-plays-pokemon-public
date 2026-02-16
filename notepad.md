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
- Successfully traversed (9, 4) - Trap seems inactive in this state.
Plan:
1. Navigate to Gate 1 (2, 6) via Row 5.
2. Check if Gate 1 is OPEN.
3. If Open, explore. If Closed, rethink logic (maybe Sw1 needs to be OFF?).