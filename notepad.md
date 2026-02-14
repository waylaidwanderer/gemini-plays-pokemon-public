# Underground Warehouse Strategy
- **Clue:** "The switch on the end is the one to press first."
- **Tested & Failed Sequences:**
  - `3 -> 1 -> 2` (All ON) -> (10, 6) CLOSED.
  - `3 -> 2 -> 1` (All ON) -> (10, 6) CLOSED.
  - `1 -> 2 -> 3` -> (10, 6) CLOSED.
  - `1 Only` -> (10, 6) CLOSED.
  - `3 Only` -> (10, 6) CLOSED.
- **Current Plan:** Test Sub-sequences.
  - Current State: Sw2 ON, Sw3 ON. Sw1 ON (Confirmed by Gate 12,8 Open).
  - Action: Turn Sw1 OFF.
  - Target State: [Sw3 ON, Sw2 ON, Sw1 OFF].
  - Check (10, 6).

# Switch Status
- Sw1: ON (Turning OFF)
- Sw2: ON (Verified)
- Sw3: ON (Verified)
- **Goal:** Test State [3 ON, 2 ON, 1 OFF].