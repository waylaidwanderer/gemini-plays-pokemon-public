# Underground Warehouse
- **Goal:** Rescue Director.
- **Hypothesis:** Order matters ("Switch on the end first") OR Simple Single Switch.
- **Failed Tests:**
  - Sequences: `3->2->1`, `1->2->3`.
  - Combos: `[1, 1, 0]`, `[1, 0, 1]`, `[1, 1, 1]`, `[0, 1, 0]`.
- **Current Test:** Transitioning to `[1, 0, 1]` (Sw1=ON, Sw3=ON, Sw2=OFF).
- **Status:**
  - Sw3: OFF -> Will turn ON.
  - Sw2: ON -> Turning OFF.
  - Sw1: ON.
- **Goal:** Check Back Gate at (2, 10).
Turn 45978: Turning Switch 2 OFF. Moving to Switch 3.