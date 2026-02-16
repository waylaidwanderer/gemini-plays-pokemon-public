# Underground Warehouse
- **Goal:** Rescue Director.
- **Hypothesis:** Order matters ("Switch on the end first") OR Simple Single Switch.
- **Failed Tests:**
  - Sequences: `3->2->1`, `1->2->3`.
  - Combos: `[1, 1, 0]`, `[1, 0, 1]`, `[1, 1, 1]`, `[0, 1, 0]`.
- **Current Test:** `[1, 1, 1]` (All ON).
- **Status:**
  - Sw3: ON -> turning OFF.
  - Sw2: ON.
  - Sw1: ON.
Turn 45951: Gate 3 closed with `[1, 1, 1]`. Moving to Switch 3 to test `[0, 1, 1]`.