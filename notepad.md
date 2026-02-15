# Underground Warehouse
- **Goal:** Rescue Director.
- **Experiment: The "Trap" at (15,4)**
  - **Status:** [ON, OFF, ON].
  - **Observation:** I have been avoiding (15,4) assuming it's bad.
  - **Hypothesis:** Stepping on (15,4) might toggle Gate (16,6) or (10,10).
  - **Plan:** Walk to (15,4). Check Gates.
  - **Reason:** All switch combos lead to dead ends. Need a new variable.
- **Verified Configurations:**
  - **[OFF, ON, OFF]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed. -> Dead End (Left).
  - **[ON, ON, OFF]:** Same as above.
  - **[OFF, ON, ON]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed. -> Dead End (Left).
  - **[OFF, OFF, ON]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed?? (12,8) Open.
    - *Note:* If (6,8) is closed, this is also a Dead End in Left Room.
- **Testing Plan:**
  1. **[ON, OFF, OFF]:** Turn Sw2 OFF. Check (16,6) and (12,8).
  2. **[OFF, OFF, OFF]:** Turn Sw1 OFF. Check if "Reset" opens everything.