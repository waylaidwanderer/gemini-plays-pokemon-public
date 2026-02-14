# Underground Warehouse
- **Goal:** Rescue Director (Real one).
- **Status:**
  - Sw3: ON.
  - Sw2: OFF.
  - Sw1: OFF (Just turned off).
- **Observation:**
  - Sw3 ON + Sw2 OFF + Sw1 ON -> (16, 10) CLOSED.
- **Plan:**
  1. Verify Switch 1 is OFF.
  2. Check if (16, 6) is still open.
  3. Go check/reset Switch 3 to OFF (Full Reset).
  4. Try Sequence: 3 -> 2 -> 1 (or 1 -> 2 -> 3).
  5. Check Gates (16, 10) and (2, 10).
- **Mechanics:**
  - Sw3 ON: Opens (16, 10), Opens (6, 8).
  - Sw3 OFF: (2, 10) is CLOSED.
  - Sw2 ON: Opens (2, 6), (3, 6). Closes (16, 6).
  - Sw2 OFF: Opens (16, 6).
  - Sw1 ON: Opens (16, 7) & (12, 8).