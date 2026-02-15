# Underground Warehouse
- **Goal:** Rescue Director.
- **Investigation: Middle Room Trap**
  - **Action:** Step on Trap (12,9).
  - **Reason:** It is reachable. Might be a useful warp or trigger.
  - **Backup Plan:** If warped out, reset to [OFF, OFF, OFF] and try Trap (15,4) to open (16,6).
  - **Logic:** [OFF, OFF, OFF] opens the internal path to Director, but locks the main entry. Trap (15,4) might unlock entry.
- **Verified Configurations:**
  - **[OFF, ON, OFF]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed. -> Dead End (Left).
  - **[ON, ON, OFF]:** Same as above.
  - **[OFF, ON, ON]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed. -> Dead End (Left).
  - **[OFF, OFF, ON]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed?? (12,8) Open.
    - *Note:* If (6,8) is closed, this is also a Dead End in Left Room.
- **Testing Plan:**
  1. **[ON, OFF, OFF]:** Turn Sw2 OFF. Check (16,6) and (12,8).
  2. **[OFF, OFF, OFF]:** Turn Sw1 OFF. Check if "Reset" opens everything.