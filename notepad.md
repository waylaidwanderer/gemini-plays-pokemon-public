# Underground Warehouse
- **Goal:** Rescue Director.
- **Current State:**
  - Sw1: OFF (Action taken).
  - Sw2: OFF (Verified previously).
  - Sw3: OFF (Verified previously).
- **Strategy:** Baseline Established [OFF, OFF, OFF].
  - **Action:** Check Gates.
  - **Hypothesis:** Determine "Zero State".
- **Next Step:**
  - If (16,6) Open: Enter.
  - If Closed: Toggle Sw3 ON -> [OFF, OFF, ON] (Previous Winning State??).
- **Verified Configurations:**
  - **[OFF, ON, OFF]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed. -> Dead End (Left).
  - **[ON, ON, OFF]:** Same as above.
  - **[OFF, ON, ON]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed. -> Dead End (Left).
  - **[OFF, OFF, ON]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed?? (12,8) Open.
    - *Note:* If (6,8) is closed, this is also a Dead End in Left Room.
- **Testing Plan:**
  1. **[ON, OFF, OFF]:** Turn Sw2 OFF. Check (16,6) and (12,8).
  2. **[OFF, OFF, OFF]:** Turn Sw1 OFF. Check if "Reset" opens everything.