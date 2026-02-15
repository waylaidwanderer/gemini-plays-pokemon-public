# Underground Warehouse
- **Goal:** Rescue Director.
- **Config [ON, OFF, OFF] (Winning?):**
  - **Status:** Sw1 ON. Sw2 OFF. Sw3 OFF.
  - **Discovery:** System reported (10,6) OPENED!
  - **Implication:** Entrance to Middle Room is open from the Top!
  - **Plan:** Enter (10,6). Go South.
  - **Check:** Is (10,10) Open? (It was open in Baseline).
  - **Goal:** Walk straight to Director.
- **Verified Configurations:**
  - **[OFF, ON, OFF]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed. -> Dead End (Left).
  - **[ON, ON, OFF]:** Same as above.
  - **[OFF, ON, ON]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed. -> Dead End (Left).
  - **[OFF, OFF, ON]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed?? (12,8) Open.
    - *Note:* If (6,8) is closed, this is also a Dead End in Left Room.
- **Testing Plan:**
  1. **[ON, OFF, OFF]:** Turn Sw2 OFF. Check (16,6) and (12,8).
  2. **[OFF, OFF, OFF]:** Turn Sw1 OFF. Check if "Reset" opens everything.