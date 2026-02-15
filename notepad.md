# Underground Warehouse
- **Goal:** Rescue Director.
- **Strategy: Internal Exploration**
  - **Config:** [ON, OFF, ON].
  - **Why:** Opens (2,6) Entry + (6,8) Cross. Allows access to Left & Middle Rooms.
  - **Plan:**
    1. Turn Sw1 ON.
    2. Turn Sw3 ON.
    3. Enter via (2,6).
    4. Talk to Silver (4,8).
    5. Defeat Duncan (9,12).
    6. Check if new path opens.
- **Verified Configurations:**
  - **[OFF, ON, OFF]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed. -> Dead End (Left).
  - **[ON, ON, OFF]:** Same as above.
  - **[OFF, ON, ON]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed. -> Dead End (Left).
  - **[OFF, OFF, ON]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed?? (12,8) Open.
    - *Note:* If (6,8) is closed, this is also a Dead End in Left Room.
- **Testing Plan:**
  1. **[ON, OFF, OFF]:** Turn Sw2 OFF. Check (16,6) and (12,8).
  2. **[OFF, OFF, OFF]:** Turn Sw1 OFF. Check if "Reset" opens everything.