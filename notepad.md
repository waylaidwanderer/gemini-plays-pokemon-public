# Underground Warehouse
- **Goal:** Rescue Director.
- **Hypothesis:** Order matters ("Switch on the end first") OR Simple Single Switch.
- **Failed Tests:**
  - Sequences: `3->2->1`, `1->2->3`.
  - Combos: `[1, 1, 0]`, `[1, 0, 1]`, `[1, 1, 1]`, `[0, 1, 0]`.
- **Current Test:** Sequence `1 -> 2` (Sw1 ON, then Sw2 ON).
- **Status:**
  - Sw3: OFF.
  - Sw2: ON (Just turned ON).
  - Sw1: ON.
Turn 45967: Turned Switch 2 ON (Sequence 1->2). Checking Gate 3.