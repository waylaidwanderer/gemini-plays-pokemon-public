# Underground Warehouse
- **Goal:** Rescue Director.
- **Action:** Turning Sw3 ON.
- **Correction:** Path blocked by Grunt at (3,2). Detouring via Row 3.
- **Path:** (4,2) -> Down -> Left -> Left -> Up -> (2,2).
- **Strategy: The "Correction" (Testing [OFF, OFF, ON])**
  - **Correction:** Switch 1 was ON during previous test! [ON, OFF, ON] failed.
  - **Action:** Turned Switch 1 OFF.
  - **Current Status:** Sw1 OFF, Sw2 OFF, Sw3 ON.
  - **Hypothesis:** [OFF, OFF, ON] might be the key.
  - **Plan:**
    1. Check Gate States immediately.
    2. If (10,10) is open, proceed.
    3. If not, verify Switch 2 state.