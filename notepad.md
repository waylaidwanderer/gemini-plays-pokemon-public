# Underground Warehouse Strategy
- **Clue:** "The switch on the end is the one to press first."
- **Tested Sequences & Results:**
  - `3 -> 1 -> 2` (All ON): (10, 6) CLOSED.
  - `1 -> 3` (Sw2 OFF): (10, 6) CLOSED.
  - **Goal State:** Sw1 ON, Sw2 OFF, Sw3 OFF. (Historical note says this opens (10, 6)).
- **Current Execution:**
  - Current State: Sw1 ON, Sw2 OFF, Sw3 OFF (Just turned OFF).
  - Next Step: Check Gate at (10, 6).

# Switch Status (After this turn)
- Sw1: ON (Verified)
- Sw2: OFF (Verified)
- Sw3: OFF (Just turned OFF)
- Goal: Check if (10, 6) is OPEN.