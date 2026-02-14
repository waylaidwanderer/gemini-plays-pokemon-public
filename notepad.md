# Underground Warehouse Strategy
- **Clue:** "The switch on the end is the one to press first."
- **Tested Sequences & Results:**
  - `3 -> 1 -> 2`: (10, 6) OPEN. (Most promising).
  - `1 -> 3 -> 2`: (10, 6) CLOSED.
  - `3 -> 2 -> 1`: (2, 6) & (12, 8) OPEN.
  - `1 -> 2 -> 3`: (2, 6) & (12, 8) OPEN.
- **Current Execution:**
  - Sequence: 3 (ON) -> 1 (ON) -> 2 (OFF -> ON)
  - Current State: Sw3 ON, Sw1 ON, Sw2 ON (Just turned ON).
  - Next Step: Check Gate at (10, 6).

# Switch Status (Current)
- Sw1: ON (Verified)
- Sw2: ON (Just turned ON)
- Sw3: ON (Verified)
- Effect of Sw3 ON: Opens Gate (2, 6).
- Effect of Sw3+Sw1 ON: Opens Gate (12, 8). Gate (10, 6) CLOSED.
- Goal: Verify if (10, 6) is OPEN.