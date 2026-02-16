# Underground Warehouse Switch Puzzle

**Goal:** Open Gate 3 (16, 6) to find the Director.

**Confirmed Mechanics:**
- **Gate 1 (2, 6):** **OPEN** with **Switch 3 ON** (State 0-0-1). **CLOSED** with **Switch 3 OFF**.
- **Gate 3 (16, 6):** **OPEN** with **Switch 1 ON** (State 1-0-0). **CLOSED** with **Switch 1 & 3 ON** (State 1-0-1).
- **Gate 3 (16, 6):** **OPEN** with **State 1-1-0**.
- **Wall at (16, 10):** **BLOCKING** with **State 1-1-0**.
- **Conclusion:** State 1-1-0 is NOT the solution for Gate 3.
- **Next Test:** **State 0-1-0** (Switch 2 Only) and **State 0-1-1** (Switch 2 & 3).
- **Hypothesis:** Summary suggested Switch 2 opens Gate 2.
- **Reference:** Log 46573 says Switch 1 opens wall at (11, 10) behind Gate 2. I might need a complex sequence or state to access that.

**Current Status:**
- Switches: 1 OFF, 2 ON, 3 ON. (State 0-1-1).
- Position: At Switch 3 (2, 1). Turned ON.
- Next Action: Check Gate 2 (10, 6).
- **Hypothesis:** State 0-1-1 opens Gate 2 AND the wall behind it.

**Key Locations:**
- Switch 1: (16, 1) [Right] - ON
- Switch 2: (10, 1) [Middle] - OFF
- Switch 3: (2, 1) [Left] - ON
- Gate 2: (10, 6)
- Gate 3: (16, 6)
- **Gate 3 (16, 6):** Confirmed CLOSED with Seq 3->1->2 (State 1-1-1).
- **Gate 3 (16, 6):** Confirmed CLOSED with Seq 1->3->2 (State 1-1-1).
**Reflection & Lessons:**
- **Tool Limitation:** Remote scanning (XML) fails for dynamic tiles (Gates) that are off-screen. The Mental Map only updates when tiles are seen. Manual verification is required for puzzle states.
- **Puzzle Progress:** Systematically ruled out "All ON" and "1-0-1". "0-0-1" (Switch 3 Only) is the current best candidate.