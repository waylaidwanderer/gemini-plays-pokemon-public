# Underground Warehouse Switch Puzzle

**Goal:** Open Gate 3 (16, 6) to find the Director.

**Confirmed Mechanics:**
- **Gate 1 (2, 6):** **OPEN** with **Switch 3 ON** (State 0-0-1).
- **Gate 2 (10, 6):** **CLOSED** with **Switch 3 ON** (State 0-1-1). **OPEN** (implied) with **Switch 2 Only** (State 0-1-0).
- **Column 11 (11, 6):** **CLOSED** with **Switch 3 ON**. **OPEN** with **Switch 2 Only**.
- **Puzzle Logic:**
    - **Switch 2 (ON):** Opens **Entrance (11, 6)**.
    - **Switch 1 (ON):** Opens **Exit (11, 10)**.
    - **Switch 3 (ON):** Closes Entrance (11, 6) (and opens Gate 1).
- **Solution:** **State 1-1-0** (Sw1 ON, Sw2 ON, Sw3 OFF).
- **Plan:**
    1. Verify (11, 10) is CLOSED (confirming Sw1 is needed).
    2. Go to Switch 1 (16, 1). Turn **ON**.
    3. Return to (11, 6) and pass through to (11, 10).
- **Current Status:**
- Switches: 1 ON, 2 ON, 3 OFF. (State 1-1-0).
- Position: Moving to (11, 6) via Row 5.
- **Hypothesis:** State 1-1-0 opens BOTH (11, 6) and (11, 10).
- **Goal:** Reach the Director through the Column 11 bypass.

**Key Locations:**
- Switch 1: (16, 1) [Right] - OFF
- Switch 2: (10, 1) [Middle] - ON
- Switch 3: (2, 1) [Left] - OFF
- Gate 2: (10, 6)
- Gate 3: (16, 6)
- **Gate 3 (16, 6):** Confirmed CLOSED with Seq 3->1->2 (State 1-1-1).
- **Gate 3 (16, 6):** Confirmed CLOSED with Seq 1->3->2 (State 1-1-1).
**Reflection & Lessons:**
- **Tool Limitation:** Remote scanning (XML) fails for dynamic tiles (Gates) that are off-screen. The Mental Map only updates when tiles are seen. Manual verification is required for puzzle states.
- **Puzzle Progress:** Systematically ruled out "All ON" and "1-0-1". "0-0-1" (Switch 3 Only) is the current best candidate.