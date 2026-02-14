# Underground Warehouse Strategy
- **Clue:** "The switch on the end is the one to press first."
- **Interpretation:** Could be Switch 3 (Left End) or Switch 1 (Right End).
- **Tested Sequences:**
  - `3 -> 1 -> 2`: Result: Gate (2, 10) Closed, Gate (10, 6) Open. (Failed).
- **Current Plan:** Test `1 -> 3 -> 2`.
  1. Reset all to OFF. (Current Step: Turn Sw3 OFF, then Sw1 OFF).
  2. Press Switch 1.
  3. Press Switch 3.
  4. Press Switch 2.
  5. Check Gate (2, 10) or (16, 10).

# Switch Status (Current)
- Sw1: ON
- Sw2: OFF
- Sw3: ON (About to turn OFF)