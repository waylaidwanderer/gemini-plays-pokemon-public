# Underground Warehouse Switch Puzzle

**Goal:** Open Gate 3 (16, 6) to find the Director.

**Confirmed Mechanics:**
- **Gate 1 (2, 6):** Opens with **Switch 3 ON** (State 0-0-1).
- **Gate 2 (10, 6):** Opens with **Switch 3 ON + Switch 1 ON** (State 1-0-1). Also opened with Seq 3->2->1 (State 1-1-1).
- **Gate 3 (16, 6):** Confirmed CLOSED with Seq 1->2 (State 1-1-0).
- **Gate 3 (16, 6):** Confirmed CLOSED with Seq 1->2->3 (State 1-1-1).
- **Inner Wall (11, 10):** Confirmed CLOSED with Seq 1->2->3.

**Current Status (Based on Markers):**
- Switch 1 (Right): **OFF** (Verified)
- Switch 2 (Middle): **ON** (Verified - Previous Step)
- Switch 3 (Left): **ON** (Verified - Step 2 of Sequence)
- Global State: 0-0-0 (Reset Complete).

**Plan: Test Sequence 3 -> 2 (State 0-1-1)**
1. Turn Switch 2 **OFF** (Reset).
2. Turn Switch 3 **OFF** (Reset).
3. Turn Switch 3 **ON** (Step 1).
4. Turn Switch 2 **ON** (Step 2).
5. Check Gate 3. (Do NOT press Switch 1).

**Key Locations:**
- Switch 1: (16, 1) [Right]
- Switch 2: (10, 1) [Middle]
- Switch 3: (2, 1) [Left]
- Gate 2: (10, 6)
- Gate 3: (16, 6)
- **Gate 3 (16, 6):** Confirmed CLOSED with Seq 3->1->2 (State 1-1-1).
- **Gate 3 (16, 6):** Confirmed CLOSED with Seq 1->3->2 (State 1-1-1).