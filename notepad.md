# Underground Warehouse Switch Puzzle

**Goal:** Open Gate 3 (16, 6) to find the Director.

**Confirmed Mechanics:**
- **Gate 1 (2, 6):** Opens with **Switch 3 ON** (State 0-0-1).
- **Gate 2 (10, 6):** Opens with **Switch 3 ON + Switch 1 ON** (State 1-0-1). Also opened with Seq 3->2->1 (State 1-1-1).
- **Gate 3 (16, 6):** **OPEN** with **Switch 1 ON** (State 1-0-0).
- **Correction:** Switch 2 was ON. State 1-1-1 (All ON) confirmed Gate 1 CLOSED.
- **Observation:** Gate 1 CLOSED in State 0-0-1 (Only Switch 3 ON). Previous note was wrong.
- **Goal:** Find combination for Gate 1.
- **Remaining Combinations:** 0-0-0 (All OFF), 0-1-0 (Only 2), 0-1-1 (2 & 3), 1-1-0 (1 & 2).
- **Plan:** Turn Switch 3 OFF (All OFF). Check Gate 1. Then try Switch 2 ON.

**Current Status:**
- Switches: 1 OFF, 2 OFF, 3 ON.
- Position: Moving to Switch 3.

**Key Locations:**
- Switch 1: (16, 1) [Right]
- Switch 2: (10, 1) [Middle]
- Switch 3: (2, 1) [Left]
- Gate 2: (10, 6)
- Gate 3: (16, 6)
- **Gate 3 (16, 6):** Confirmed CLOSED with Seq 3->1->2 (State 1-1-1).
- **Gate 3 (16, 6):** Confirmed CLOSED with Seq 1->3->2 (State 1-1-1).
**Reflection & Lessons:**
- **Tool Limitation:** Remote scanning (XML) fails for dynamic tiles (Gates) that are off-screen. The Mental Map only updates when tiles are seen. Manual verification is required for puzzle states.
- **Puzzle Progress:** Systematically ruled out "All ON" and "1-0-1". "0-0-1" (Switch 3 Only) is the current best candidate.