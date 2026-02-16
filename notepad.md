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
- Turning Switch 2 OFF now.
- Testing Gate 1 next.
Truth Table (Gate 1):
- 1-1-1: CLOSED
- 1-0-1: CLOSED
- 0-1-1: CLOSED
- 0-1-0: CLOSED
- 0-0-1: CLOSED
- 1-1-0: OPENED Gate 3. Gate 1 Likely Closed (Not checked).
- 0-0-0: Testing...
- 1-0-0: Untested.
Plan:
1. Confirm Switch 2 OFF.
2. Navigate to Gate 1 (2, 6).
3. Check status.