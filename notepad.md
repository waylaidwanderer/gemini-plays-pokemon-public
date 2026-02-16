# Underground Warehouse Switch Puzzle (SOLVED)

**Solution:** Gate 3 (16, 6) opens with **Switch 1 ON** and **Switch 2 ON** (State 1-1-0). Switch 3 OFF.

**Mechanics Summary:**
- **Switch 2 (ON):** Opens Entrance (11, 6).
- **Switch 1 (ON):** Opens Exit (11, 10).
- **Switch 3 (ON):** Closes Entrance (11, 6) & Opens Gate 1.
- **Gate 3:** Closed if Switch 3 is ON. Open if Sw1 & Sw2 ON.

**Current Location:** Director's Room (3_53).
**Objective:** Rescue Director.

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
- Switch 1: (16, 1) [Right] - ON (Just Turned ON)
- **State Analysis:** Tool shows Secret Door (11, 6) OPEN. Suspicion: Switch 2 might still be ON.
- **Wall (16, 10):** CLOSED with All Switches ON.
- Switch 2: (10, 1) [Middle] - ON (Just Turned ON for Safe Crossing)
- Switch 3: (2, 1) [Left] - OFF (Just Turned OFF for Reset)
- Gate 2: (10, 6)
- Gate 3: (16, 6)
- **Gate 3 (16, 6):** CLOSED with All Switches ON (State 1-1-1).
- **Gate 3 (16, 6):** OPEN with Sw1 & Sw2 ON (State 1-1-0).
- **Hypothesis:** Switch 2 closes Gate 3. Trying State 1-0-0 (Sw1 ON only).
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
**Confirmed:** Trap (10, 4) is SAFE with Switch 2 ON.
**Hypothesis:** State 1-1-0 (Sw1 & Sw2 ON) should open **Entrance (11, 6)** (via Sw2) and **Exit (11, 10)** (via Sw1). Checking this path now.
- **Current State:** 0-1-1 (Sw1 OFF, Sw2 ON, Sw3 ON).
- **Hypothesis:** Testing if this opens Gate 3 or the walls.
- **Next Step:** Check Gate 3. If closed, try turning Switch 2 OFF (State 0-0-1).
Location: Director's Room (3_53).
Objective: Rescue Director.
Status: Puzzle Solved. In room with Silver and Rocket Grunt.
Interact with Grunt and Silver to find the Director.