# Underground Warehouse
- **Goal:** Rescue Director.
- **Hypothesis:** Order matters ("Switch on the end first") OR Simple Single Switch.
- **Failed Tests:**
  - Sequences: `3->2->1`, `1->2->3`.
  - Combos: `[1, 1, 0]`, `[1, 0, 1]`, `[1, 1, 1]`, `[0, 1, 0]`.
- **Current Test:** `[0, 1, 1]` (Sw1=ON, Sw2=ON, Sw3=OFF) -> based on "110" clue (1-2-3 order).
- **Status:**
  - Sw3: OFF.
  - Sw2: ON.
  - Sw1: ON.
- **Recent Results:**
  - `[1, 1, 0]` (Sw3=ON, Sw2=ON, Sw1=OFF) failed Gate 3.
  - `[1, 1, 1]` failed Gate 3.
Turn 45957: Turned Switch 3 OFF. Testing Gate 3.