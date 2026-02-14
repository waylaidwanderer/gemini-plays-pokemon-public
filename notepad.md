# Underground Warehouse Strategy
- **Clue:** "The switch on the end is the one to press first."
- **Tested Sequences & Results:**
  - `3 -> 1 -> 2`: (10, 6) OPEN. (Most promising).
  - `1 -> 3 -> 2`: (10, 6) CLOSED.
  - `3 -> 2 -> 1`: (2, 6) & (12, 8) OPEN.
  - `1 -> 2 -> 3`: (2, 6) & (12, 8) OPEN.
- **Current Execution:**
  - Found Sw2 unexpectedly ON.
  - Action: Turn Sw2 OFF, then turn Sw2 ON to simulate the final step of `3 -> 1 -> 2`.
  - Current State: Sw3 ON, Sw1 ON, Sw2 ON (Transitioning to OFF).

# Switch Status (Current)
- Sw1: ON (Verified)
- Sw2: ON (Unexpected - Correcting to OFF)
- Sw3: ON (Verified)
- Effect of Sw3 ON: Opens Gate (2, 6).
- Effect of Sw3+Sw1 ON: Opens Gate (12, 8). Gate (10, 6) CLOSED.
- Goal: Toggle Sw2 (OFF -> ON).