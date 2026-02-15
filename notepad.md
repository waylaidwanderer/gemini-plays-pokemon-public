# Underground Warehouse
- **Goal:** Rescue Director.
- **Strategy: The "Reset & Trap"**
  - **Status:** Moving to Sw1 (16,2).
  - **Next:** Turn Sw1 OFF.
  - **Test:** Verify `[OFF, OFF, OFF]` keeps (12,8) and (10,10) Open.
  - **Experiment:** Step on (15,4). If it opens (16,6), path is clear: (16,6)->(12,8)->(10,10).
  - **Goal:** Reach Director.
- **Verified Configurations:**
  - **[OFF, ON, OFF]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed. -> Dead End (Left).
  - **[ON, ON, OFF]:** Same as above.
  - **[OFF, ON, ON]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed. -> Dead End (Left).
  - **[OFF, OFF, ON]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed?? (12,8) Open.
    - *Note:* If (6,8) is closed, this is also a Dead End in Left Room.
- **Testing Plan:**
  1. **[ON, OFF, OFF]:** Turn Sw2 OFF. Check (16,6) and (12,8).
  2. **[OFF, OFF, OFF]:** Turn Sw1 OFF. Check if "Reset" opens everything.