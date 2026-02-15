# Underground Warehouse
- **Goal:** Rescue Director / Get Card Key.
- **Config [OFF, OFF, ON] (Failed):**
  - **Result:** (2,6) Open, (12,8) Open. (16,6) Closed.
  - **Analysis:** Sw3 ON opens the destination but closes the entry.
- **Config [OFF, ON, OFF] (Target):**
  - **Status:** Sw1 OFF, Sw2 ON, Sw3 OFF.
  - **Hypothesis:** Sw2 ON might open (12,8) without Sw3?
  - **Prediction:** (16,6) Open (Sw3 OFF), (12,8) Open (Sw2 ON?), (2,6) Closed (XOR).
  - **Goal:** Exit via (16,6) -> (12,8).