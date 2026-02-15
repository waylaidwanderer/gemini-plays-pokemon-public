# Underground Warehouse
- **Goal:** Rescue Director.
- **Strategy: The "Reset & Trap"**
  - **Current:** [ON, OFF, ON]. (Verified: Can exit Middle Room via (6,8)).
  - **Plan:**
    1. Navigate to Sw3 (2,2). Turn OFF.
    2. Navigate to Sw1 (16,2). Turn OFF.
    3. Verify [OFF, OFF, OFF] state.
    4. **Critical:** Step on Trap (15,4). Check if (16,6) opens.
  - **Backup:** Test [ON, ON, ON].
  - **Goal:** Find a state where (16,6) is OPEN (to enter Right Room) OR (2,6)+(6,8)+(10,10) is OPEN.
- **Verified Configurations:**
  - **[OFF, ON, OFF]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed. -> Dead End (Left).
  - **[ON, ON, OFF]:** Same as above.
  - **[OFF, ON, ON]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed. -> Dead End (Left).
  - **[OFF, OFF, ON]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed?? (12,8) Open.
    - *Note:* If (6,8) is closed, this is also a Dead End in Left Room.
- **Testing Plan:**
  1. **[ON, OFF, OFF]:** Turn Sw2 OFF. Check (16,6) and (12,8).
  2. **[OFF, OFF, OFF]:** Turn Sw1 OFF. Check if "Reset" opens everything.