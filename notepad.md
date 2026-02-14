# Underground Warehouse Strategy
- **Clue:** "The switch on the end is the one to press first."
- **Tested Sequences & Results:**
  - `3 -> 1 -> 2`: (10, 6) OPEN. (Most promising).
  - `1 -> 3 -> 2`: (10, 6) CLOSED.
  - `3 -> 2 -> 1`: (2, 6) & (12, 8) OPEN.
  - `1 -> 2 -> 3`: (2, 6) & (12, 8) OPEN.
- **Current Execution:**
  - Resetting all switches to OFF to retry `3 -> 1 -> 2` cleanly.
  - Current State: Sw1 ON, Sw2 OFF, Sw3 ON.
  - Immediate Goal: Turn Sw1 OFF.

# Switch Status (Current)
- Sw1: ON (Target: Turn OFF)
- Sw2: OFF (Verified)
- Sw3: ON (Verified)
- Effect of Sw3 ON: Opens Gate (2, 6).
- Effect of Sw3+Sw1 ON: Opens Gate (12, 8). Gate (10, 6) CLOSED.
- Goal: Reset all to OFF.