# Underground Warehouse
- **Goal:** Rescue Director.
- **Hypothesis:** Order matters ("Switch on the end first") OR Simple Single Switch.
- **Failed Tests:**
  - Sequences: `3->2->1`, `1->2->3`.
  - Combos: `[1, 1, 0]`, `[1, 0, 1]`, `[1, 1, 1]`, `[0, 1, 0]`.
- **Current Test:** `[1, 0, 0]` (Switch 1 Only).
- **Status:**
  - Sw3: OFF.
  - Sw2: OFF.
  - Sw1: OFF -> turning ON.
Turn 45872: Turned Switch 3 OFF. Moving to Switch 1.