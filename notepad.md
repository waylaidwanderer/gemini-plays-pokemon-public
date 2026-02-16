# Underground Warehouse Switch Puzzle

**Goal:** Open Gate 3 (16, 6) to find the Director.

**Confirmed Mechanics:**
- **Gate 1 (2, 6):** **OPEN** with **Switch 3 ON** (State 0-0-1). **CLOSED** with **Switch 3 OFF**.
- **Gate 3 (16, 6):** **OPEN** with **Switch 1 ON** (State 1-0-0). **CLOSED** with **Switch 1 & 3 ON** (State 1-0-1).
- **Gate 2 (10, 6):** **CLOSED** with **State 1-1-0**. (Switch 1 & 2 ON).
- **Traps:** Row 4 (10, 4) confirmed SAFE with Switch 2 ON.
- **Current Test:** Checking **Gate 3 (16, 6)** with **State 1-1-0**.
- **Hypothesis:** Switch 1 opens Gate 3. Switch 2 might remove the internal wall at (16, 10) but possibly closes the gate? Or maybe it works!

**Current Status:**
- Switches: 1 ON, 2 ON, 3 OFF. (State 1-1-0).
- Position: At Switch 2 (10, 2). Turned ON.
- Next Action: Check Gate 2 (10, 6) and Gate 3 (16, 6).

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