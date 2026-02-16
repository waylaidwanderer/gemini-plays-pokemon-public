# Underground Warehouse Switch Puzzle

**Goal:** Open Gate 3 (16, 6) to find the Director.

**Confirmed Mechanics:**
- **Gate 1 (2, 6):** Opens with **Switch 3 ON** (State 0-0-1).
- **Gate 2 (10, 6):** Opens with **Switch 3 ON + Switch 1 ON** (State 1-0-1). Also opened with Seq 3->2->1 (State 1-1-1).
- **Gate 3 (16, 6):** Confirmed CLOSED with Seq 1->2 (State 1-1-0).
- **Gate 3 (16, 6):** Confirmed CLOSED with Seq 1->2->3 (State 1-1-1).
- **Inner Wall (11, 10):** Confirmed CLOSED with Seq 1->2->3.

**Current Status (Based on Markers):**
- Switch 1 (Right): **ON** (Verified - Step 1 of Sequence)
- Switch 2 (Middle): **OFF** (Verified)
- Switch 3 (Left): **OFF** (Verified)
- Global State: 0-0-0 (Reset Complete).

**Plan: Sequence 1 -> 3 -> 2**
1. Turn Switch 1 **ON** (Start).
2. Turn Switch 3 **ON**.
3. Turn Switch 2 **ON**.
4. Check Gate 3.

**Key Locations:**
- Switch 1: (16, 1) [Right]
- Switch 2: (10, 1) [Middle]
- Switch 3: (2, 1) [Left]
- Gate 2: (10, 6)
- Gate 3: (16, 6)
- **Gate 3 (16, 6):** Confirmed CLOSED with Seq 3->1->2 (State 1-1-1).