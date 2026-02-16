# Underground Warehouse
- **Goal:** Rescue Director.
- **Hypothesis:** Order matters ("Switch on the end first") OR Simple Single Switch.
- **Failed Tests:**
  - Sequences: `3->2->1`, `1->2->3`.
  - Combos: `[1, 1, 0]`, `[1, 0, 1]`, `[1, 1, 1]`, `[0, 1, 0]`.
- **Current Test:** `[1, 1, 0]` (Sw3=ON, Sw2=ON, Sw1=OFF) - based on clue "110".
- **Status:**
  - Sw3: ON.
  - Sw2: ON (Just turned ON).
  - Sw1: ON -> turning OFF next.
Turn 45934: Turning Switch 2 ON. Moving to Switch 1 to turn OFF.