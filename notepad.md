# Underground Warehouse Strategy
- **Status:** Switch 1 (Unknown), Switch 2 (OFF), Switch 3 (ON).
- **Goal:** Reach Switch 1 (Right).
- **Route:** Row 5 to avoid Trap at (15,4).
- **Gate Data (from error log):**
  - [OFF, OFF, ON]: (2,6) OPEN, (6,8) OPEN. Others CLOSED.
  - [OFF, ON, ON]: (2,6) OPEN. (10,6) CLOSED.
- **Hypothesis:** Switch 2 doesn't control (2,6). Maybe Switch 1 controls (16,6)?
- **Plan:** Turn Switch 1 ON. Test [ON, OFF, ON].
- **Reflection:** Avoiding "Trap Room" by sticking to Row 5.