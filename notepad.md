# Underground Warehouse
- **Goal:** Rescue Director.
- **Hypothesis:** Order matters ("Switch on the end first") OR Simple Single Switch.
- **Failed Tests:**
  - Sequences: `3->2->1`, `1->2->3`.
  - Combos: `[1, 1, 0]`, `[1, 0, 1]`, `[1, 1, 1]`, `[0, 1, 0]`.
- **Current Test:** `[1, 0, 1]` (Sequence 3 -> 1).
- **Status:**
  - Sw3: ON.
  - Sw2: OFF.
  - Sw1: ON.
Turn 45925: Turned Switch 1 ON. Checking Gate 3.