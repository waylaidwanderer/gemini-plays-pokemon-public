# Underground Warehouse Switch Puzzle

**Goal:** Open Gate 3 (16, 6) to find the Director.

**Confirmed Mechanics:**
- **Gate 1 (2, 6):** Opens with **Switch 3 ON** (State 0-0-1).
- **Gate 2 (10, 6):** Opens with **Switch 3 ON + Switch 1 ON** (State 1-0-1). Also opened with Seq 3->2->1 (State 1-1-1).
- **Gate 3 (16, 6):** **OPEN** with **Switch 1 ON** (State 1-0-0).
- **Gate 1 (2, 6):** CLOSED (State 1-0-0).
- **Gate 2 (10, 6):** CLOSED (State 1-0-0).
- **Trap (16, 8):** Status Unknown for State 1-0-0. (Disabled in 1-1-1).
- **Hypothesis:** Switch 1 opens Gate 3. Need to check if trap is active.

**Current Status:**
- Switches: Switch 1 ON, others OFF.
- Plan: Enter Gate 3 and test trap.

**Key Locations:**
- Switch 1: (16, 1) [Right]
- Switch 2: (10, 1) [Middle]
- Switch 3: (2, 1) [Left]
- Gate 2: (10, 6)
- Gate 3: (16, 6)
- **Gate 3 (16, 6):** Confirmed CLOSED with Seq 3->1->2 (State 1-1-1).
- **Gate 3 (16, 6):** Confirmed CLOSED with Seq 1->3->2 (State 1-1-1).