# Underground Warehouse Switch Puzzle

**Goal:** Open Gate 3 (16, 6) to find the Director.

**Confirmed Mechanics:**
- **Gate 1 (2, 6):** **OPEN** with **Switch 3 ON** (State 0-0-1).
- **Gate 3 (16, 6):** **OPEN** with **Switch 1 ON** (State 1-0-0). **CLOSED** with **Switch 1 & 3 ON** (State 1-0-1).
- **Gate 2 (10, 6):** **CLOSED** with **State 1-0-1**.
- **Wall at (2, 10):** BLOCKING with Switch 3 ON.
- **Current Test:** Revert to **State 1-0-0** (Switch 1 Only).
- **Plan:** Turn Switch 3 OFF. Go to Gate 3. Look for "secret passage" to (11, 10).

**Current Status:**
- Switches: 1 ON, 2 OFF, 3 ON.
- Position: At (10, 5). Moving to Switch 3 (2, 1).

**Current Status:**
- Switches: 1 ON, 2 OFF, 3 ON. (State 1-0-1).
- Position: At Switch 1 (16, 2). Moving to check Gate 3.

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