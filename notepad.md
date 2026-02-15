# Underground Warehouse
- **Goal:** Rescue Director / Get Card Key.
- **Config [OFF, OFF, ON] (Failed):**
  - **Result:** (2,6) Open, (12,8) Open. (16,6) Closed.
  - **Analysis:** Sw3 ON opens the destination but closes the entry.
- **Config [OFF, OFF, OFF] (Confirmed):**
  - **Result:** (16,6) Open, (6,8) Open, (12,8) Closed.
  - **Trap Effect:** Entering (15,4) CLOSED (16,6) and (6,8). (12,8) remained Closed.
  - **Conclusion:** Trap closes gates or toggles them.
- **Hypothesis:** Need to open (12,8) first (closing 16,6), then use Trap to re-open (16,6).
- **Plan:**
  1. Turn Sw2 ON -> [OFF, ON, OFF]. (Opens 12,8, Closes 16,6).
  2. Trigger Trap (15,4).
  3. Hope (16,6) Opens.
- **Config [OFF, ON, ON] (Confirmed):**
  - **Result:** (2,6) Open, (12,8) Open. (16,6) Closed.
  - **Analysis:** Sw3 ON opens Dest (12,8) but closes Entry (16,6).