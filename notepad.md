# Underground Warehouse
- **Goal:** Rescue Director (Real one).
- **Status:**
  - Sw3: OFF (Likely).
  - Sw2: OFF.
  - Sw1: ON.
- **Plan:**
  1. Turn Sw1 OFF (Reset).
  2. Verify Sw3 is OFF.
  3. Execute Sequence: Sw3 ON -> Sw2 ON.
  4. Check Gate (2, 10).
- **Hypothesis:** Sw1 ON might be keeping (2, 10) closed? Or Order matters.
- **Mechanics:**
  - Sw3 ON: Opens (16, 10), Opens (6, 8).
  - Sw3 OFF: (2, 10) is CLOSED.
  - Sw2 ON: Opens (2, 6), (3, 6). Closes (16, 6).
  - Sw2 OFF: Opens (16, 6).
  - Sw1 ON: Opens (16, 7) & (12, 8).