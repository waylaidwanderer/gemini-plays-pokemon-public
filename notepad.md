# Underground Warehouse
- **Goal:** Rescue Director.
- **Verification: Left Room Connectivity**
  - **Goal:** Verify if I can travel from (6,8) to Sw3 (2,1).
  - **Plan:**
    1. Check (12,9) (Wall?).
    2. Go West through Gate (6,8).
    3. Navigate to Sw3 (2,1).
  - **Logic:** If I can reach Sw3 from inside, I can set [OFF, OFF, ON] from the inside.
    - [OFF, OFF, ON] opens (6,8) and (10,10).
    - Entering from (2,6) [OFF, OFF, OFF], then toggling Sw3 ON is the key.
- **Verified Configurations:**
  - **[OFF, ON, OFF]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed. -> Dead End (Left).
  - **[ON, ON, OFF]:** Same as above.
  - **[OFF, ON, ON]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed. -> Dead End (Left).
  - **[OFF, OFF, ON]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed?? (12,8) Open.
    - *Note:* If (6,8) is closed, this is also a Dead End in Left Room.
- **Testing Plan:**
  1. **[ON, OFF, OFF]:** Turn Sw2 OFF. Check (16,6) and (12,8).
  2. **[OFF, OFF, OFF]:** Turn Sw1 OFF. Check if "Reset" opens everything.