# Underground Warehouse
- **Goal:** Rescue Director.
- **Strategy: The "Reset & Trap"**
  - **Current Action:** Turning Sw3 OFF. Next: Turn Sw1 OFF.
  - **Target State:** [OFF, OFF, OFF].
  - **Check:** Verify (16,6) and (2,6) are Open/Closed.
  - **Trap Experiment:** Once in [OFF, OFF, OFF], step on (15,4).
  - **Goal:** Open (16,6).
- **Verified Configurations:**
  - **[OFF, ON, OFF]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed. -> Dead End (Left).
  - **[ON, ON, OFF]:** Same as above.
  - **[OFF, ON, ON]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed. -> Dead End (Left).
  - **[OFF, OFF, ON]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed?? (12,8) Open.
    - *Note:* If (6,8) is closed, this is also a Dead End in Left Room.
- **Testing Plan:**
  1. **[ON, OFF, OFF]:** Turn Sw2 OFF. Check (16,6) and (12,8).
  2. **[OFF, OFF, OFF]:** Turn Sw1 OFF. Check if "Reset" opens everything.