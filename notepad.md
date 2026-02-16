# Underground Warehouse
- **Goal:** Rescue Director.
- **Hypothesis:** Order matters ("Switch on the end first") OR Simple Single Switch.
- **Failed Tests:**
  - Sequences: `3->2->1`, `1->2->3`.
  - Combos: `[1, 1, 0]`, `[1, 0, 1]`, `[1, 1, 1]`, `[0, 1, 0]`.
- **Current Test:** `[1, 1, 1]` (All ON).
- **Status:**
  - Sw3: ON.
  - Sw2: ON.
  - Sw1: OFF -> turning ON.
- **Recent Results:**
  - `[1, 1, 0]` failed to open Gate 3.
  - `[1, 0, 1]` opened Gate 1.
  - `[0, 1, 0]` opened Gate 2.
Turn 45947: Gate 3 closed with `[1, 1, 0]`. Trying `[1, 1, 1]`.