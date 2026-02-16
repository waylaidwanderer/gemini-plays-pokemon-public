# Underground Warehouse Switch Puzzle

**Goal:** Open Gate 3 (16, 6) to find the Director.

**Confirmed Mechanics:**
- **Gate 1 (2, 6):** **OPEN** with **Switch 3 ON** (State 0-0-1).
- **Gate 2 (10, 6):** Opens with **Switch 3 ON + Switch 1 ON** (State 1-0-1).
- **Gate 3 (16, 6):** **OPEN** with **Switch 1 ON** (State 1-0-0).
- **Wall at (2, 10):** Confirmed BLOCKING with Switch 3 ON.
- **Hypothesis:** Need State 1-0-1 (Sw1+Sw3) to open Gate 2? Or maybe it affects (2, 10)?
- **Plan:** Go to Switch 1. Turn ON. Test State 1-0-1.
- **Navigation:** Traversing Row 4 traps (Sw2 OFF) to reach Switch 1.

**Current Status:**
- Switches: 1 OFF, 2 OFF, 3 ON.
- Position: Moving to Gate 1 (2, 6).

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