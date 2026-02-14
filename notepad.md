# Underground Warehouse Strategy
- **Clue:** "The switch on the end is the one to press first."
- **Tested & Failed Sequences:**
  - `3 -> 1 -> 2` (All ON) -> (10, 6) CLOSED.
  - `1 -> 2 -> 3` -> (10, 6) CLOSED.
  - `1 Only` -> (10, 6) CLOSED.
  - `3 Only` -> (10, 6) CLOSED.
- **Current Plan:** Test `3 -> 2 -> 1`.
  - Theory: "End (3) First".
  - Step 1: Reset All to OFF. (Current Step: Turn Sw1 OFF).
  - Step 2: Turn Sw3 ON.
  - Step 3: Turn Sw2 ON.
  - Step 4: Turn Sw1 ON.

# Switch Status
- Sw1: ON (Turning OFF now)
- Sw2: OFF (Verified)
- Sw3: OFF (Verified)