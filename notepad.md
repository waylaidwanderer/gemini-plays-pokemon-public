# Underground Warehouse Strategy
- **Clue:** "The switch on the end is the one to press first."
- **Tested Sequences & Results:**
  - `3 -> 1 -> 2` (All ON): (10, 6) CLOSED.
  - `1 -> 3` (Sw2 OFF): (10, 6) CLOSED.
  - `1 Only`: (12, 8) OPEN, (10, 6) CLOSED.
  - `1 -> 2 -> 3`: Failed (History Turn 42988).
- **New Plan:** Test `3 -> 2 -> 1`.
  - Evidence: Summary Turn 43029 says this opened (10, 6).
  - Step 1: Turn Sw1 OFF (Reset).
  - Step 2: Turn Sw3 ON.
  - Step 3: Turn Sw2 ON.
  - Step 4: Turn Sw1 ON.

# Switch Status
- Sw1: ON (Verified)
- Sw2: OFF (Verified)
- Sw3: OFF (Verified)
- Goal: Reset Sw1 to OFF.