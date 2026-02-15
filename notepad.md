# Underground Warehouse
- **Goal:** Rescue Director.
- **Action:** Turning Sw3 ON.
- **Correction:** Path blocked by Grunt at (3,2). Detouring via Row 3.
- **Path:** (4,2) -> Down -> Left -> Left -> Up -> (2,2).
- **Strategy: The "Combo Search" (Testing [OFF, ON, ON])**
  - **Status:** Sw1 OFF, Sw2 OFF, Sw3 ON.
  - **Results for [OFF, OFF, ON]:**
    - Entry: 2-6 (OPEN), 10-6 (OPEN), 16-6 (CLOSED).
    - Cross: 6-8 (OPEN), 12-8 (CLOSED).
    - Exit: 2-10 (CLOSED), 10-10 (CLOSED), 16-10 (OPEN).
    - *Problem:* 16-10 is Open but unreachable (Need 16-6 or 12-8).
  - **Hypothesis:** Turning Sw2 ON might open 12-8 or 10-10.
  - **Plan:**
    1. Navigate to Switch 2 (10,1).
    2. Turn Sw2 ON.
    3. Check Gate States.