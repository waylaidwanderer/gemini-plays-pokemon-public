# Underground Warehouse Switch Puzzle

**Goal:** Open Gate 3 (16, 6) to find the Director.

**Confirmed Mechanics:**
- **Gate 1 (2, 6):** Opens with **Switch 3 ON** (State 0-0-1).
- **Gate 2 (10, 6):** Opens with **Switch 3 ON + Switch 1 ON** (State 1-0-1). Also opened with Seq 3->2->1 (State 1-1-1).
- **Gate 3 (16, 6):** Opens with State 1-1-0 (1 ON, 2 ON, 3 OFF). Wall behind it is blocked.
- **Trap (16, 8):** Disabled by Sequence 3->2->1.
- **Hypothesis:** Execute 3->2->1 to disable trap, then turn 3 OFF to open Gate 3.

**Plan:**
1. Reset Switch 2 to OFF.
2. Turn Switch 2 ON (Sequence Step 2).
3. Turn Switch 1 ON (Sequence Step 3).
4. Go to Switch 3 and turn OFF.
5. Check Gate 3.

**Key Locations:**
- Switch 1: (16, 1) [Right]
- Switch 2: (10, 1) [Middle]
- Switch 3: (2, 1) [Left]
- Gate 2: (10, 6)
- Gate 3: (16, 6)
- **Gate 3 (16, 6):** Confirmed CLOSED with Seq 3->1->2 (State 1-1-1).
- **Gate 3 (16, 6):** Confirmed CLOSED with Seq 1->3->2 (State 1-1-1).