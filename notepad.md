# Underground Warehouse Strategy
- **Clue:** "The switch on the end is the one to press first."
- **Tested & Failed Sequences:**
  - `3 -> 1 -> 2` (All ON) -> (10, 6) CLOSED.
  - `3 -> 2 -> 1` (All ON) -> (10, 6) CLOSED.
  - `1 -> 2 -> 3` -> (10, 6) CLOSED.
  - `1 Only` -> (10, 6) CLOSED.
  - `3 Only` -> (10, 6) CLOSED.
- **Current Plan:** Test Sub-sequences.
  - Theory: Maybe the sequence is just 2 steps?
  - Current State: All ON.
  - Step 1: Turn Sw1 OFF. (Result: Sw3 ON, Sw2 ON).
  - Step 2: Check Gates.
  - Step 3: If closed, go to Sw3 and Turn OFF (Result: Sw2 Only).

# Switch Status
- Sw1: ON (Turning OFF)
- Sw2: ON (Verified)
- Sw3: ON (Verified)
- **Goal:** Test State [3 ON, 2 ON, 1 OFF].