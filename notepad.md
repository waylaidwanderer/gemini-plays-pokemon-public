# Underground Warehouse
- **Goal:** Rescue Director.
- **Hypothesis:** Order matters ("Switch on the end first") OR Simple Single Switch.
- **Failed Tests:**
  - Sequences: `3->2->1`, `1->2->3`.
  - Combos: `[1, 1, 0]`, `[1, 0, 1]`, `[1, 1, 1]`, `[0, 1, 0]`.
- **Current Test:** `[0, 0, 1]` (Switch 3 Only).
- **Status:**
  - Sw3: ON (Just now).
  - Sw2: ON (Assumed). Heading to turn OFF.
  - Sw1: ON (Assumed). Will turn OFF next.
Turn 45858: Turned Switch 2 OFF. State: [1, 0, 1]. Moving to Switch 1 to turn OFF.
Turn 45859: Moving to Switch 1 to turn OFF. Target State: [0, 0, 1].
Turn 45860: Turned Switch 1 OFF. State: [0, 0, 1]. Checking Gate 1.
Turn 45862: Recovered from menu. Confirmed Switch 1 OFF. State [0, 0, 1]. Moving to Gate 1.