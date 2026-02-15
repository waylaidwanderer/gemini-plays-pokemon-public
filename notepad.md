# Underground Warehouse Strategy
- **Status:** Switch 1 (ON), Switch 2 (OFF), Switch 3 (ON).
- **Gate Data (verified by code):**
  - [ON, OFF, ON]: (2,6) OPEN. (12,8) CLOSED. Others CLOSED.
  - [OFF, OFF, ON]: (2,6) OPEN, (12,8) OPEN.
- **Analysis:** Switch 1 ON closes (12,8).
- **Hypothesis:** Try Switch 1 as "End Switch" ALONE.
- **Plan:** Go to Switch 3. Turn OFF. Test [ON, OFF, OFF].
- **Route:** Down to Row 5, then Left to avoid Traps at (15,4) and (15,1).