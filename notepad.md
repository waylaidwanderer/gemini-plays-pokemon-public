# Underground Warehouse
- **Goal:** Rescue Director.
- **Hypothesis:** Order matters ("Switch on the end first") OR Simple Single Switch.
- **Failed Tests:**
  - Sequences: `3->2->1`, `1->2->3`.
  - Combos: `[1, 1, 0]`, `[1, 0, 1]`, `[1, 1, 1]`, `[0, 1, 0]`.
- **Current Test:** `[0, 1, 1]` (Sw1=ON, Sw2=ON, Sw3=OFF).
- **Status:**
  - Sw3: OFF.
  - Sw2: ON.
  - Sw1: ON.
- **Result:** Gate 3 (16, 6) OPENED.
- **Conclusion:** The clues are swapped. Left Room "110" opens Right Room. The bit order is Sw1-Sw2-Sw3.
Turn 45962: Entering Right Room. Fingers crossed the trap at (16, 8) is disabled.