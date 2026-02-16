# Underground Warehouse
- **Hypothesis:** "Switch on the end first" (Order 1->2? or 3->2?).
- **Verified Mechanics:**
  - **Order Matters:** `1 -> 2` vs `2 -> 1` produces different results.
  - **Gate 2 (10, 6):** OPENS with `2 -> 1`. CLOSED with `1 -> 2`.
  - **Gate 3 (16, 6):** CLOSED with `2 -> 1`. OPENS with `1 -> 2`.
  - **Gate 1 (2, 6):** CLOSED with `1 -> 3`, `3 -> 1`, `3 -> 2`, `2 -> 3`, `2 -> 3 -> 1`.
- **Current State:** `[1, 1, 1]` (All ON). Sequence `2 -> 3 -> 1`.
- **Hypothesis:** "Switch on the end" means `3 -> 2 -> 1`.
- **Plan:**
  1. Turn Sw3 OFF.
  2. Turn Sw2 OFF.
  3. Turn Sw1 OFF. (Clean Slate)
  4. Execute `3 -> 2 -> 1`.
  5. Check Gate 1.