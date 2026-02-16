# Underground Warehouse
- **Goal:** Rescue Director.
- **Hypothesis:** Order matters ("Switch on the end first") OR Simple Single Switch.
- **Failed Tests:**
  - Sequences: `3->2->1`, `1->2->3`.
  - Combos: `[1, 1, 0]`, `[1, 0, 1]`, `[1, 1, 1]`, `[0, 1, 0]`.
- **Current Test:** Setting up `[0, 1, 1]` (Sw1=OFF, Sw2=ON, Sw3=ON).
- **Status:**
  - Sw3: OFF -> Will turn ON.
  - Sw2: OFF (Gate 2 closed, inferred OFF). -> Will turn ON.
  - Sw1: ON -> Turning OFF now.
- **Goal:** Check Back Gate at (2, 10).
Turn 45982: Turning Switch 1 OFF. Then moving to Sw2 and Sw3.