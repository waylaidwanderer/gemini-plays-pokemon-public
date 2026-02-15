# Underground Warehouse Mechanics
- **Goal:** Rescue Director / Get Card Key.
- **Config [1:ON, 2:OFF, 3:ON]:**
  - OPEN: (2,6), (10,10).
  - CLOSED: (10,6), (16,6), (6,8), (12,8), (2,10), (16,10).
  - **Result:** Left shaft open but dead end. Middle/Right shafts closed.
- **Hypothesis:** Sw2 ON might open (12,8) or (6,8). Sw3 OFF might open (10,6)/(16,6).
- **Plan:** Try Config [1:ON, 2:ON, 3:ON].
- **Action:** Toggle Sw2 (ON). Then check gates via XML.
- **Current Status:** Sw1: ON, Sw2: OFF, Sw3: ON.