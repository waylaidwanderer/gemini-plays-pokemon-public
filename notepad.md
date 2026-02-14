# Underground Warehouse Strategy
- **Clue:** "The switch on the end is the one to press first."
- **Tested Sequences & Results:**
  - `3 -> 1 -> 2`: (10, 6) OPEN. (Most promising).
  - `1 -> 3 -> 2`: (10, 6) CLOSED.
  - `3 -> 2 -> 1`: (2, 6) & (12, 8) OPEN.
  - `1 -> 2 -> 3`: (2, 6) & (12, 8) OPEN.
- **Current Plan:**
  1. Reset Sw2 to OFF (Executing).
  2. Reset Sw1 to OFF.
  3. Re-test `3 -> 1 -> 2` carefully, checking gates at each step.

# Switch Status (Current)
- Sw1: ON
- Sw2: OFF (Verified)
- Sw3: OFF
- Goal: Reset all to OFF. Next: Turn Sw1 OFF.