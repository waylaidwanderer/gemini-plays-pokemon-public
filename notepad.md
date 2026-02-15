# Underground Warehouse
- **Goal:** Rescue Director.
- **Action:** Retrying Switch 1 Toggle (Previous attempt likely cancelled).
- **Target:** Turn Sw1 ON.
- **Current Config Check:** Verify if Sw1 changed state.
- **Then:** Move to Sw3 (2,1) and Turn ON.
- **Goal:** [ON, OFF, ON].
- **Hypothesis:** Opens (2,6) and (6,8).
- **Verified Configurations:**
  - **[OFF, ON, OFF]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed. -> Dead End (Left).
  - **[ON, ON, OFF]:** Same as above.
  - **[OFF, ON, ON]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed. -> Dead End (Left).
  - **[OFF, OFF, ON]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed?? (12,8) Open.
    - *Note:* If (6,8) is closed, this is also a Dead End in Left Room.
- **Testing Plan:**
  1. **[ON, OFF, OFF]:** Turn Sw2 OFF. Check (16,6) and (12,8).
  2. **[OFF, OFF, OFF]:** Turn Sw1 OFF. Check if "Reset" opens everything.