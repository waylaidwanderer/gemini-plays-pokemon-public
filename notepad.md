# Underground Warehouse
- **Goal:** Rescue Director.
- **Hypothesis:** "Switch on the end first" (Order 1->2? or 3->2?).
- **Verified Mechanics:**
  - **Order Matters:** `1 -> 2` vs `2 -> 1` produces different results.
  - **Gate 2 (10, 6):** OPENS with `2 -> 1`. CLOSED with `1 -> 2`.
  - **Gate 3 (16, 6):** CLOSED with `2 -> 1`. OPENS with `1 -> 2`.
  - **Gate 1 (2, 6):** Likely involves Switch 3.
- **Current State:** `[1, 0, 0]` (Sw1 ON, Sw2 OFF, Sw3 OFF->ON).
- **Plan:**
  1. Toggle Sw3 ON -> `[1, 0, 1]`.
  2. Check Gate 1 (2, 6).
- **Goal:** Rescue Director.