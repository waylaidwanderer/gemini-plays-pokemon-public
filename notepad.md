# Underground Warehouse
- **Goal:** Rescue Director.
- **Hypothesis:** Order matters ("Switch on the end first") OR Simple Single Switch.
- **Failed Tests:**
  - Sequences: `3->2->1`, `1->2->3`.
  - Combos: `[1, 1, 0]`, `[1, 0, 1]`, `[1, 1, 1]`, `[0, 1, 0]`.
- **Current Test:** Sequence `1 -> 2` (Target: Sw1=ON, Sw2=ON, Sw3=OFF).
- **Status:**
  - Sw3: OFF.
  - Sw2: ON -> Turning OFF now -> Will turn ON next.
  - Sw1: ON.
Turn 45966: Turning Switch 2 OFF. Next: Turn ON.