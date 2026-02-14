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
- Sw1: ON (To be verified)
- Sw2: OFF (Verified)
- Sw3: OFF (Verified - kept it OFF)
- Gate (6, 8): Checking status. (If Closed, Sw3 OFF closes it. If Open, Sw3 OFF opens it).