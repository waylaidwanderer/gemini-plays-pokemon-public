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
Objective: Find the "missed trigger".
Status: Stuck at (17, 9) due to navigation error (treated walls as walkable).
Correction: Walls are TYPE_2889. Floor is TYPE_3fe2.
Plan: Navigate to Rocket Grunt F at (19, 12) using valid floor tiles. Target position (20, 12) or (19, 13).
Path likely involves going North to Row 5, then East, then South.