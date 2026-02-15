# Underground Warehouse
- **Goal:** Rescue Director / Get Card Key.
- **Config [OFF, OFF, ON] (Failed):**
  - **Result:** (2,6) Open, (12,8) Open. (16,6) Closed.
  - **Analysis:** Sw3 ON opens the destination but closes the entry.
- **Config [OFF, OFF, OFF] (Trapped):**
  - **Status:** Sw1 OFF, Sw2 OFF, Sw3 OFF + Trap Triggered.
  - **Result:** ALL GATES CLOSED (except 10,10).
  - **Insight:** Trap (15,4) toggles/closes (16,6).
- **New Strategy:** Use Trap to our advantage.
  1. Set [OFF, OFF, ON]. (Sw3 ON opens Dest (12,8), closes Entry (16,6)).
  2. Trigger Trap (15,4). (Hypothesis: Re-opens Entry (16,6)).
  3. Walk (16,6) -> (12,8) -> Director.
- **Immediate Goal:** Turn Sw3 ON.
- **Config [OFF, ON, ON] (Confirmed):**
  - **Result:** (2,6) Open, (12,8) Open. (16,6) Closed.
  - **Analysis:** Sw3 ON opens Dest (12,8) but closes Entry (16,6).