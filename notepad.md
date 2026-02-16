# Underground Warehouse
- **Hypothesis:** "Switch on the end first" (Order 1->2? or 3->2?).
- **Verified Mechanics:**
  - **Order Matters:** `1 -> 2` vs `2 -> 1` produces different results.
  - **Gate 2 (10, 6):** OPENS with `2 -> 1`. CLOSED with `1 -> 2`.
  - **Gate 3 (16, 6):** CLOSED with `2 -> 1`. OPENS with `1 -> 2`.
  - **Gate 1 (2, 6):** CLOSED with `1 -> 3`, `3 -> 1`, `3 -> 2`, `2 -> 3`.
- **Current State:** `[1, 1, 1]` (Sw1 ON, Sw2 ON, Sw3 ON). Sequence `2 -> 3 -> 1`.
- **Hypothesis:** Gate 1 requires all three switches or a specific "End" start.
- **Plan:**
  1. Check Gate 1.
  2. If fail: Reset all to OFF. Try `3 -> 2 -> 1`.