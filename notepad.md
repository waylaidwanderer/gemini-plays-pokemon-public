# Underground Warehouse Strategy
- **Clue:** "The switch on the end is the one to press first."
- **Tested & Failed Sequences:**
  - `3 -> 1 -> 2` (All ON) -> (10, 6) CLOSED.
  - `3 -> 2 -> 1` (All ON) -> (10, 6) CLOSED.
  - `1 -> 2 -> 3` -> (10, 6) CLOSED.
  - `1 Only` -> (10, 6) CLOSED.
  - `3 Only` -> (10, 6) CLOSED.
  - [3 ON, 2 ON, 1 OFF] -> (10, 6) CLOSED.
- **Current Plan:** Test Sub-sequences.
  - Current State: Sw3 ON, Sw2 ON, Sw1 OFF.
  - Observation: Gate (12, 8) is OPEN even with Sw1 OFF. (Disproves "Gate 12,8 = Sw1" theory).
  - Next Test: Turn Sw3 OFF.
  - Target State: [Sw3 OFF, Sw2 ON, Sw1 OFF] (Only Sw2 ON).

# Switch Status
- Sw1: OFF (Verified by Text)
- Sw2: ON (Verified)
- Sw3: ON (Verified)
- **Goal:** Test State [Sw2 Only].