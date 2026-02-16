# Underground Warehouse
- **Goal:** Rescue Director.
- **Hypothesis:** Order matters ("Switch on the end first") OR Simple Single Switch.
- **Failed Tests:**
  - Sequences: `3->2->1`, `1->2->3`.
  - Combos: `[1, 1, 0]`, `[1, 0, 1]`, `[1, 1, 1]`, `[0, 1, 0]`.
- **Current Test:** `[1, 0, 1]` (Sequence 1 -> 3).
- **Status:**
  - Sw3: OFF -> turning ON.
  - Sw2: OFF.
  - Sw1: ON.
Turn 45892: Turning Switch 3 ON. Testing Gate 1 next.