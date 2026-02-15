# Underground Warehouse
- **Goal:** Rescue Director.
- **Config [ON, OFF, ON] (Testing):**
  - **Status:** Sw1 ON. Sw2 OFF. Sw3 OFF (Moving to Turn ON).
  - **Hypothesis:** Opens (2,6) (Left Entry) and (6,8) (Left-to-Middle).
  - **Plan:**
    1. Turn Sw3 ON.
    2. Enter Left Room via (2,6).
    3. Cross to Middle Room via (6,8).
    4. Check for hidden switches/paths in Middle Room.
- **Verified Configurations:**
  - **[OFF, ON, OFF]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed. -> Dead End (Left).
  - **[ON, ON, OFF]:** Same as above.
  - **[OFF, ON, ON]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed. -> Dead End (Left).
  - **[OFF, OFF, ON]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed?? (12,8) Open.
    - *Note:* If (6,8) is closed, this is also a Dead End in Left Room.
- **Testing Plan:**
  1. **[ON, OFF, OFF]:** Turn Sw2 OFF. Check (16,6) and (12,8).
  2. **[OFF, OFF, OFF]:** Turn Sw1 OFF. Check if "Reset" opens everything.