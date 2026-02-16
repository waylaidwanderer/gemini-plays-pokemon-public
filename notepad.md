# Underground Warehouse
- **Goal:** Rescue Director.
- **Hypothesis:** Order matters ("Switch on the end first") OR Simple Single Switch.
- **Failed Tests:**
  - Sequences: `3->2->1`, `1->2->3`.
  - Combos: `[1, 1, 0]`, `[1, 0, 1]`, `[1, 1, 1]`, `[0, 1, 0]`.
- **Current Test:** `[0, 1, 1]` (Sw1=ON, Sw2=ON, Sw3=OFF).
- **Status:**
  - Sw3: OFF.
  - Sw2: ON -> Toggle OFF/ON (Sequence `1 -> 2`).
  - Sw1: ON.
- **Result:** Gate 3 CLOSED (Correction from Turn 45963).
- **Plan:** Toggle Switch 2 to simulate `Sw1 -> Sw2` sequence.
Turn 45965: Moving to Switch 2 to toggle.