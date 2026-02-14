# Underground Warehouse Strategy
- **Clue:** "The switch on the end is the one to press first."
- **Tested Sequences:**
  - `3 -> 1 -> 2`: Failed.
  - `1 -> 3 -> 2`: Failed.
  - `3 -> 2 -> 1`: Failed. Result: (2, 6) OPEN, (12, 8) OPEN. Others CLOSED.
- **Next Sequence:** `1 -> 2 -> 3` (Right End Start).
  1. Reset Sw1 to OFF (Current).
  2. Reset Sw2 to OFF.
  3. Reset Sw3 to OFF.
  4. Turn Sw1 ON.
  5. Turn Sw2 ON.
  6. Turn Sw3 ON.
  7. Check Gate (2, 10).

# Switch Status (Current)
- Sw1: OFF (Verified)
- Sw2: OFF (Verified)
- Sw3: ON
- Goal: Reset all to OFF. Next: Turn Sw3 OFF.