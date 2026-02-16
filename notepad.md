# Underground Warehouse Switch Puzzle

**Goal:** Open Gate 3 (16, 6) to find the Director.

**Confirmed Mechanics:**
- **Gate 1 (2, 6):** Confirmed CLOSED with All Switches OFF (Reset Successful).
- **Puzzle Progress:** Starting Sequence: 3 (Left) -> 2 (Middle) -> 1 (Right).
- **Gate 2 (10, 6):** **CLOSED** with **Switch 3 ON** (State 0-1-1). **OPEN** (implied) with **Switch 2 Only** (State 0-1-0).
- **Column 11 (11, 6):** **CLOSED** with **Switch 3 ON**. **OPEN** with **Switch 2 Only**.
- **Puzzle Logic:**
    - **Switch 2 (ON):** Opens **Entrance (11, 6)**.
    - **Switch 1 (ON):** Opens **Exit (11, 10)**.
    - **Switch 3 (ON):** Closes Entrance (11, 6) (and opens Gate 1).
- **Observation:** `(11, 10)` is a Wall with State 1-1-0.
- **Hypothesis:** "The switch on the end is the one to press first" implies a **SEQUENCE**, not just a state.
- **Plan:**
    1. Exit Middle Room via `(11, 6)` or `(12, 9)` (if open).
    2. Reset all switches to **OFF**.
    3. Try Sequence: **Switch 3 -> Switch 2 -> Switch 1** (Left to Right).
    4. Try Sequence: **Switch 1 -> Switch 2 -> Switch 3** (Right to Left).

# Underground Warehouse Truth Table

**Goal:** Find the state that opens **Exit Wall (11, 10)**.

**State Analysis:**
- **0-0-1 (Sw3):** Gate 1 OPEN. Walls CLOSED.
- **1-0-0 (Sw1):** Gate 3 OPEN. Walls CLOSED.
- **0-1-0 (Sw2):** Gate 3 OPEN (Tool). **Entrance (11, 6) OPEN**. Exit (11, 10) CLOSED.
- **1-1-0 (Sw1+2):** Gate 3 OPEN. **Entrance (11, 6) OPEN**. Exit (11, 10) CLOSED.
- **0-1-1 (Sw2+3):** Entrance (11, 6) CLOSED. Gate 2 CLOSED.
- **1-0-1 (Sw1+3):** Gate 2 CLOSED. Gate 3 CLOSED.
- **1-1-1 (All ON):** **UNTESTED on Walls**.

**Hypothesis:**
- State **1-1-1** might be the key.
- Or "End Switch First" implies a specific order for 1-1-1 (e.g. 3->2->1).

**Plan:**
1. Go to **Switch 1**. Turn **ON**. (Result: State 1-1-1).
2. Check **(11, 10)** and **(11, 6)**.
3. If fail, reconsider "Sequence".

**Key Locations:**
- Switch 1: (16, 1) [Right] - ON (Seq Step 3: 3->2->1 Complete)
- **Wall (16, 10):** CLOSED with All Switches ON.
- Switch 2: (10, 1) [Middle] - OFF (Resetting)
- Switch 3: (2, 1) [Left] - ON (Seq Step 1)
- Gate 2: (10, 6)
- Gate 3: (16, 6)
- **Gate 3 (16, 6):** CLOSED with All Switches ON (State 1-1-1).
- **Gate 3 (16, 6):** OPEN with State 1-1-0 (Sw1 & Sw2 ON, Sw3 OFF).
- **Gate 3 (16, 6):** Confirmed CLOSED with Seq 3->1->2 (State 1-1-1).
- **Gate 3 (16, 6):** Confirmed CLOSED with Seq 1->3->2 (State 1-1-1).
**Reflection & Lessons:**
- **Tool Limitation:** Remote scanning (XML) fails for dynamic tiles (Gates) that are off-screen. The Mental Map only updates when tiles are seen. Manual verification is required for puzzle states.
- **Puzzle Progress:** Systematically ruled out "All ON" and "1-0-1". "0-0-1" (Switch 3 Only) is the current best candidate.
- **Trap Update:** Attempted Column 8 traverse (Sw2 OFF) and warped back to start. **(8, 4)** is likely a Trap when Sw2 is OFF.
- **Navigation:** Trying Column 6 traverse.
- **Trap Analysis:** Stuck in Middle Pocket (Cols 8-11). Cols 8, 9, 10 are traps with Sw2 OFF. Walls block Left (Col 6/7) and Right (Col 12).
- **Escape Plan:** Attempting escape via **Column 11** traverse. If this fails, navigation logic needs a rethink (or Sw2 must be ON to move).
**Discovery:** Walking over (10, 4) with Switch 2 ON did NOT trigger the warp. Trap (10, 4) is disabled by Switch 2.