# Underground Warehouse
- **Goal:** Rescue Director.
- **Action:** Turning Sw3 ON.
- **Correction:** Path blocked by Grunt at (3,2). Detouring via Row 3.
- **Path:** (4,2) -> Down -> Left -> Left -> Up -> (2,2).
- **Strategy: The "Full Power" (Testing [ON, ON, ON])**
  - **Status:** Sw1 ON, Sw2 OFF, Sw3 ON.
  - **Result for [ON, OFF, ON]:** 2-6 Open, 16-10 Open. All internal paths Closed. Dead End.
  - **Hypothesis:** Maybe turning EVERYTHING on opens the main path?
  - **Plan:**
    1. Navigate to Switch 2 (10,1).
    2. Turn Sw2 ON.
    3. Check Gate States.
    4. If failure, proceed to Sw3 to start testing "OFF" variants.