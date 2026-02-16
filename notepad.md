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
Correction: Navigation error previously (treated walls as walkable).
Current Plan:
1. Turn Switch 2 OFF (State 1-0-1: Sw1 ON, Sw2 OFF, Sw3 ON).
2. Check Gate 1 (2, 6).
3. Important: Exit Switch 2 area via (9, 2) to avoid Trap at (10, 4).