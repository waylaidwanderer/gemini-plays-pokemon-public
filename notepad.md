# Underground Warehouse Switch Puzzle

**Goal:** Open Gate 3 (16, 6) to find the Director.

**Confirmed Mechanics:**
- **Gate 1 (2, 6):** Opens with **Switch 3 ON** (State 0-0-1).
- **Gate 2 (10, 6):** Opens with **Switch 3 ON + Switch 1 ON** (State 1-0-1). Also opened with Seq 3->2->1 (State 1-1-1).
- **Gate 3 (16, 6):** Confirmed CLOSED with Seq 1->2 (State 1-1-0).
- **Gate 3 (16, 6):** Confirmed CLOSED with Seq 1->2->3 (State 1-1-1).
- **Inner Wall (11, 10):** Confirmed CLOSED with Seq 1->2->3.

**Current Status (Based on Markers):**
- Switch 1 (Right): **ON**
- Switch 2 (Middle): **ON**
- Switch 3 (Left): **OFF**
- Global State: 0-1-1 (if order is 3-2-1).

**Plan: Reset & Retry**
1. Turn Switch 2 **OFF**. (Moving there now)
2. Turn Switch 1 **OFF**.
3. Confirm Switch 3 is OFF.
4. Execute Sequence: **Switch 3 (ON) -> Switch 1 (ON) -> Switch 2 (ON)**.
5. Check results (Gate 3, Inner Walls).

**Key Locations:**
- Switch 1: (16, 1) [Right]
- Switch 2: (10, 1) [Middle]
- Switch 3: (2, 1) [Left]
- Gate 2: (10, 6)
- Gate 3: (16, 6)