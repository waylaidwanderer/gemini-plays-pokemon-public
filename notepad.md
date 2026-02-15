# Underground Warehouse
- **Goal:** Rescue Director.
- **Hypothesis: [ON, OFF, ON]**
  - **Reasoning:**
    - [OFF, OFF, ON] had (6,8) & (10,10) Open, but (2,6) Closed.
    - [ON, OFF, ON] previously showed (2,6) Open.
    - If Sw1 ON opens (2,6) and doesn't close the others, this is the path!
  - **Plan:**
    1. Turn Sw1 ON.
    2. Go to Sw3 -> Turn ON.
    3. Check Gates.
    4. Path: (2,6) -> (6,8) -> (10,10).
- **Verified Configurations:**
  - **[OFF, ON, OFF]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed. -> Dead End (Left).
  - **[ON, ON, OFF]:** Same as above.
  - **[OFF, ON, ON]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed. -> Dead End (Left).
  - **[OFF, OFF, ON]:** Left(2,6) Open. Right(16,6) Closed. Cross(6,8) Closed?? (12,8) Open.
    - *Note:* If (6,8) is closed, this is also a Dead End in Left Room.
- **Testing Plan:**
  1. **[ON, OFF, OFF]:** Turn Sw2 OFF. Check (16,6) and (12,8).
  2. **[OFF, OFF, OFF]:** Turn Sw1 OFF. Check if "Reset" opens everything.