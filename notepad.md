# Underground Warehouse
- **Status:**
  - Sw1: ON.
  - Sw2: ON.
  - Sw3: ON.
  - Gate (2, 10): CLOSED (Verified via XML).
  - Gate (12, 8): CLOSED (XML).
  - Gate (16, 10): CLOSED (XML).
  - Gate (2, 6): Unverified visual (XML says Closed, but logic suggests Open).
- **Next Plan:**
  1. Check Gate (2, 6).
  2. If Open, go to Switch 3 (Reset).
  3. If Closed, go to Switch 2.
  4. Goal: Reset all to OFF, then try Sequence 1 -> 3 -> 2.