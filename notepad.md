# Underground Warehouse
- **Goal:** Rescue Director.
- **Hypothesis:** Order matters ("Switch on the end first") OR Simple Single Switch.
- **Failed Tests:**
  - Sequences: `3->2->1`, `1->2->3`.
  - Combos: `[1, 1, 0]`, `[1, 0, 1]`, `[1, 1, 1]`, `[0, 1, 0]`.
- **Current Test:** Sequence `1 -> 2` (Sw1 ON, then Sw2 ON).
- **Status:**
  - Sw3: OFF.
  - Sw2: ON.
  - Sw1: ON.
- **Result:** Gate 3 (16, 6) OPENED. Trap at (16, 8) DISABLED.
- **Solution:** Switches 1 & 2 ON, Switch 3 OFF. Order `1 -> 2`.
Turn 45971: Safe inside Right Room. engaging Grunt at (19, 12).