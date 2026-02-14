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
  - Current State: Sw3 OFF, Sw2 ON, Sw1 OFF.
  - Target State: [Sw2 Only].
  - Next Step: Check Gate (10, 6).

# Switch Status
- Sw1: OFF (Verified)
- Sw2: ON (Verified)
- Sw3: OFF (Just turned OFF)
- **Goal:** Check if (10, 6) opens with Sw2 Only.
- [Sw3 OFF, Sw2 ON, Sw1 OFF] -> (10, 6) CLOSED. (Tested Turn 43390)
- Next Test: Toggle Sw2 OFF. Target State: [Sw3 OFF, Sw2 OFF, Sw1 OFF].