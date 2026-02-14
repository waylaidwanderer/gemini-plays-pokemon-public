# Underground Warehouse
- **Goal:** Rescue Director (Real one).
- **Status:**
  - Sw3: Unknown (Inferred OFF).
  - Sw2: OFF.
  - Sw1: OFF (Toggled).
- **Plan:**
  1. Verify Switch 1 is OFF (Gate (16, 7) should close).
  2. Go to Switch 3 (2, 1). Ensure it is OFF.
  3. Execute Sequence: Switch 3 ON -> Switch 2 ON -> Switch 1 ON.
  4. Check Gate (2, 10).
- **Mechanics:**
  - Sw3 ON: Opens (16, 10), Opens (6, 8).
  - Sw2 ON: Opens (2, 6), (3, 6). Closes (16, 6).
  - Sw2 OFF: Opens (16, 6).
  - Sw1 ON: Opens (16, 7) & (12, 8).