# Underground Warehouse State [Sw3 OFF, Sw2 OFF, Sw1 OFF]
- **Gates:**
  - OPEN: (2, 6), (10, 6), (6, 8).
  - CLOSED: (12, 8), (16, 6), (2, 10).
- **Result:** "All OFF" did NOT open (16, 6). It closed (12, 8).
- **Hypothesis:** Sw3 ON + Sw2 OFF might open (16, 6).
- **Plan:** Go to Switch 3 (2, 1). Toggle ON.