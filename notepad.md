# Underground Warehouse
- **Goal:** Rescue Director / Get Card Key.
- **Config [OFF, OFF, ON] (Failed):**
  - **Result:** (2,6) Open, (12,8) Open. (16,6) Closed.
  - **Analysis:** Sw3 ON opens the destination but closes the entry.
- **Config [OFF, OFF, ON] (Failed):**
  - **Status:** Sw1 OFF, Sw2 OFF, Sw3 ON.
  - **Result:** (16,6) Closed. (12,8) Open.
  - **Trap Test:** Entering (15,4) did NOT open (16,6).
- **Config [OFF, ON, OFF] (Verified):**
  - **Status:** Sw1 OFF, Sw2 ON (Deduced), Sw3 OFF (Confirmed).
  - **Result:** (16,6) Closed, (12,8) Open.
  - **Trap Test:** Trap did NOT toggle (16,6).
- **Config [ON, OFF, OFF] (Current):**
  - **Status:** Sw1 ON, Sw2 OFF, Sw3 OFF.
  - **Result:** (16,6) Open, (12,8) Closed.
  - **Analysis:** Sw1 ON does not open Dest. It keeps Entry Open (same as OFF).
- **Config [ON, ON, OFF] (SOLVED):**
  - **Status:** Sw1 ON, Sw2 ON, Sw3 OFF.
  - **Result:** (16,6) OPEN, (12,8) OPEN.
  - **Solution:** Sw1 opens Entry (16,6). Sw2 opens Dest (12,8). Sw3 OFF prevents conflicts.
- **Plan:**
  1. Travel East via Row 5 (Safe Lane) to avoid Trap (15,4).
  2. Enter (16,6) -> (12,8) -> (10,10).
  3. Rescue Director.
- **Config [OFF, ON, ON] (Confirmed):**
  - **Result:** (2,6) Open, (12,8) Open. (16,6) Closed.
  - **Analysis:** Sw3 ON opens Dest (12,8) but closes Entry (16,6).