# Underground Warehouse Switch Puzzle

**Goal:** Open Gate 3 (16, 6) to find the Director.

**Confirmed Mechanics (Revised):**
- **Gate 1 (2, 6):** Opens with **Switch 3 ON** (State 0-0-1).
- **Gate 2 (10, 6):** Opens with **Switch 3 ON + Switch 1 ON** (State 1-0-1). Also opened with Seq 3->2->1 (State 1-1-1).
- **Gate 3 (16, 6):** Confirmed CLOSED with Seq 1->2 (State 1-1-0).
- Visual Confirm: Inner Wall (11, 10) is CLOSED (Type 2889) with State 1-1-1.
- Conclusion: Sequence 1->2->3 is incorrect.
- Action: Stepping on Trap at (10, 9) to fast-reset switches to OFF.
- Next Plan: Try Sequence starting with Switch 3 (Left End).
- Target Sequence: 3 -> 2 -> 1.
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
- Confirmed: State 1-1-0 (Seq 1->2) opens Gate 2 but NOT the Inner Wall at (10, 10).
- Gate 3 remains CLOSED.
- Conclusion: Sequence 1->2 is not the full solution.
- Action: Heading to Switch 3 (2, 1).
- Plan: Turn Switch 3 ON.
- New State: 1-1-1 (Sequence 1->2->3).
- Goal: Check if adding Switch 3 opens the wall or Gate 1.