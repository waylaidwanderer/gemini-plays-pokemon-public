# Underground Warehouse Switch Puzzle

**Goal:** Open Gate 3 (16, 6) to find the Director.

**Confirmed Mechanics (Revised):**
- **Gate 1 (2, 6):** Opens with **Switch 3 ON** (State 0-0-1).
- **Gate 2 (10, 6):** Opens with **Switch 3 ON + Switch 1 ON** (State 1-0-1). Also opened with Seq 3->2->1 (State 1-1-1).
- **Gate 3 (16, 6):** Opened with Seq 1->2 (State 0-1-1? or 1-1-0? No, 1->2 means 1 ON, then 2 ON. State 1-1-0).
- **Inner Wall (10, 10) or (11, 10):** Currently the main obstacle behind Gate 2.

**Current Hypothesis:**
- Different combinations of switches open different gates/walls.
- State 1-0-1 opened Gate 2. Checking if it opens the Inner Wall.

**Next Steps:**
1. Check Inner Wall at (10, 10)/(11, 10).
2. If blocked, try **State 1-1-1** (Turn Switch 2 ON).
3. If blocked, try **State 0-1-1** (Turn Switch 1 OFF).

**Key Locations:**
- Switch 1: (16, 1) [Right]
- Switch 2: (10, 1) [Middle]
- Switch 3: (2, 1) [Left]
- Current Status: Switch 1 ON, Switch 2 ON, Switch 3 OFF (State: 1-1-0).
- Sequence: 1 -> 2.
- Observation: Gate 2 (10, 6) definitely OPENED (Tile changed).
- Action: Moving to check Gate 3 (16, 6).
- Path: (8, 4) -> Down to (8, 5) -> Right to (16, 5) -> Down to Gate 3.
- Logic: If Gate 3 is closed, the sequence 1->2 opens Gate 2, not 3.