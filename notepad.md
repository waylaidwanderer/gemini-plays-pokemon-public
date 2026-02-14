# Underground Warehouse Strategy
- **Clue:** "The switch on the end is the one to press first."
- **Tested & Failed Sequences:**
  - `3 -> 1 -> 2` (All ON) -> (10, 6) CLOSED.
  - `3 -> 2 -> 1` (All ON) -> (10, 6) CLOSED.
  - `1 -> 2 -> 3` -> (10, 6) CLOSED.
  - `1 Only` -> (10, 6) CLOSED.
  - `3 Only` -> (10, 6) CLOSED.
- **Current Plan:** Test Sub-sequences.
  - Current State: Sw2 ON, Sw3 ON. Sw1 Status Uncertain.
  - Check (12, 8):
    - OPEN = Sw1 ON (Need to turn OFF).
    - CLOSED = Sw1 OFF (Proceed to next test).
  - Next Test: If (10, 6) Closed, turn Sw3 OFF -> Test Sw2 Only.

# Switch Status
- Sw1: UNKNOWN (Verifying)
- Sw2: ON (Verified)
- Sw3: ON (Verified)
- **Goal:** Find the combination that opens (10, 6).