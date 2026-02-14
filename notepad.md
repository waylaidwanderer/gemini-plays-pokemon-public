# Underground Warehouse Strategy
- **Clue:** "The switch on the end is the one to press first."
- **Tested & Failed Sequences:**
  - `3 -> 1 -> 2` (All ON) -> (10, 6) CLOSED.
  - `1 -> 2 -> 3` -> (10, 6) CLOSED.
  - `1 Only` -> (10, 6) CLOSED.
  - `3 Only` -> (10, 6) CLOSED.
- **Current Plan:** Test `3 -> 2 -> 1`.
  - Step 1: Reset All to OFF. (Done).
  - Step 2: Turn Sw3 ON. (Done).
  - Step 3: Turn Sw2 ON. (Done).
  - Step 4: Turn Sw1 ON. (Done).

# Switch Status
- Sw1: ON (Just turned ON)
- Sw2: ON (Verified)
- Sw3: ON (Verified)
- **State:** All ON.
- **Goal:** Check if (10, 6) opens with this specific order.