# Underground Warehouse Switch Puzzle

**Goal:** Open Gate 3 (16, 6) to find the Director.

**Confirmed Mechanics:**
- **Gate 1 (2, 6):** **OPEN** with **Switch 3 ON** (State 0-0-1).
- **Gate 2 (10, 6):** **CLOSED** with **Switch 3 ON** (State 0-1-1). **OPEN** (implied) with **Switch 2 Only** (State 0-1-0).
- **Column 11 (11, 6):** **CLOSED** with **Switch 3 ON**. **OPEN** with **Switch 2 Only**.
- **Success!** **State 0-1-0** (Switch 2 Only) opened the bypass at **(11, 6)**.
- **Current Position:** (11, 6). Standing on the opened path.
- **Plan:** Walk South through (11, 10) (also expected to be open). Explore the area behind the gates to find the Director.
- **Confirmed Mechanics:** Switch 2 toggles the "Internal Walls" at Col 11. Switch 3 and 1 control the Gates (mostly closed or useless if walls are up).

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