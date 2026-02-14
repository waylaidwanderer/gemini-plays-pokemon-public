# Underground Warehouse Strategy
- **Clue:** "The switch on the end is the one to press first."
- **Tested Sequences & Results:**
  - `3 -> 1 -> 2` (All ON): (10, 6) CLOSED.
  - `1 -> 3` (Sw2 OFF): (10, 6) CLOSED.
  - **Goal State:** Sw1 ON, Sw2 OFF, Sw3 OFF. (Historical note says this opens (10, 6)).
- **Current Execution:**
  - Current State: Sw1 ON, Sw2 ON, Sw3 ON.
  - Step 1: Turn Sw2 OFF. (Doing now).
  - Step 2: Turn Sw3 OFF.
  - Final State: Sw1 ON Only.

# Switch Status (After this turn)
- Sw1: ON (Verified)
- Sw2: OFF (Just turned OFF)
- Sw3: ON (Verified)
- Goal: Reach Sw1 ON Only state.