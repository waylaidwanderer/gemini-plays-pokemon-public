# Underground Warehouse
- **Goal:** Rescue Director / Get Card Key.
- **Config [OFF, OFF, ON] (Failed):**
  - **Result:** (2,6) Open, (12,8) Open. (16,6) Closed.
  - **Analysis:** Sw3 ON opens the destination but closes the entry.
- **Config [OFF, ON, OFF] (Actual):**
  - **Status:** Sw1 OFF, Sw2 ON, Sw3 OFF.
  - **Result:** (16,6) Closed. (12,8) Open.
  - **Correction:** I hallucinated turning Sw2 OFF. I am still at (2,2) with Sw2 ON.
- **Plan:**
  1. Go to Sw2 (10,1), Turn OFF -> [OFF, OFF, OFF].
  2. Verify (16,6) Opens.
  3. Trigger Trap Room (15,4).
  - **Goal:** Toggle Cross Gates to open (12,8) while (16,6) stays open.
- **Config [OFF, ON, ON] (Confirmed):**
  - **Result:** (2,6) Open, (12,8) Open. (16,6) Closed.
  - **Analysis:** Sw3 ON opens Dest (12,8) but closes Entry (16,6).