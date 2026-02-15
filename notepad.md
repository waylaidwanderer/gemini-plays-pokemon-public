# Underground Warehouse
- **Goal:** Rescue Director.
- **Action:** Turning Sw3 ON.
- **Correction:** Path blocked by Grunt at (3,2). Detouring via Row 3.
- **Path:** (4,2) -> Down -> Left -> Left -> Up -> (2,2).
- **Strategy: The "Exhaustive Search" (Testing [ON, ON, OFF])**
  - **Status:** Sw1 ON, Sw2 ON, Sw3 ON.
  - **Result for [ON, ON, ON]:** Entry 2-6/10-6 Open. Exit 16-10 Open. Cross 6-8/12-8 CLOSED.
  - **Hypothesis:** Maybe Sw3 needs to be OFF?
  - **Plan:**
    1. Turn Sw3 OFF (State: [ON, ON, OFF]).
    2. Check Gate States.
    3. If fail, try [ON, OFF, OFF] (Sw2 OFF).