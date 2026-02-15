# Underground Warehouse
- **Goal:** Rescue Director.
- **Investigation: Middle Room**
  - **Status:** [ON, OFF, ON].
  - **Gates:** (10,6) OPEN. (10,10) CLOSED.
  - **Plan:** Enter Middle Room via (10,6).
  - **Action:** Explore inside. Check "Trap" at (12,9). Check for hidden switches.
  - **Logic:** Since (10,10) is closed by Sw1 ON (needed for Entry), maybe the solution is INSIDE.
- **Verified Configurations:**
  - **[OFF, ON, OFF]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed. -> Dead End (Left).
  - **[ON, ON, OFF]:** Same as above.
  - **[OFF, ON, ON]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed. -> Dead End (Left).
  - **[OFF, OFF, ON]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed?? (12,8) Open.
    - *Note:* If (6,8) is closed, this is also a Dead End in Left Room.
- **Testing Plan:**
  1. **[ON, OFF, OFF]:** Turn Sw2 OFF. Check (16,6) and (12,8).
  2. **[OFF, OFF, OFF]:** Turn Sw1 OFF. Check if "Reset" opens everything.