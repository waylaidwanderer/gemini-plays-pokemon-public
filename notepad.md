# Underground Warehouse Switch Puzzle

**Goal:** Open Gate 3 (16, 6) to find the Director.

**Confirmed Mechanics:**
- **Gate 1 (2, 6):** Opens with **Switch 3 ON** (State 0-0-1).
- **Gate 2 (10, 6):** Opens with **Switch 3 ON + Switch 1 ON** (State 1-0-1). Also opened with Seq 3->2->1 (State 1-1-1).
- **Gate 3 (16, 6):** **OPEN** with **Switch 1 ON** (State 1-0-0).
- **Gate 1 (2, 6):** **OPEN** with **All Switches ON** (Seq 1->2->3).
- **Gate 2 (10, 6):** CLOSED with All Switches ON. (Was open with 1+3).
- **Gate 3 (16, 6):** **OPEN** with All Switches ON.
- **Wall (2, 10):** **OPEN** with All Switches ON.
- **Wall (11, 10):** **OPEN** with All Switches ON.
- **Plan:** Enter Gate 1. Explore (2, 10).

**Current Status:**
- Switches: All ON (Seq 1->2->3).
- Position: (2, 2). Moving to Gate 1.

**Key Locations:**
- Switch 1: (16, 1) [Right]
- Switch 2: (10, 1) [Middle]
- Switch 3: (2, 1) [Left]
- Gate 2: (10, 6)
- Gate 3: (16, 6)
- **Gate 3 (16, 6):** Confirmed CLOSED with Seq 3->1->2 (State 1-1-1).
- **Gate 3 (16, 6):** Confirmed CLOSED with Seq 1->3->2 (State 1-1-1).