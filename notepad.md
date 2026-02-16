# Underground Warehouse
- **Hypothesis:** "Switch on the end first" (Order 1->2? or 3->2?).
- **Verified Mechanics:**
  - **Order Matters:** `1 -> 2` vs `2 -> 1` produces different results.
  - **Gate 2 (10, 6):** OPENS with `2 -> 1`. CLOSED with `1 -> 2`.
  - **Gate 3 (16, 6):** CLOSED with `2 -> 1`. OPENS with `1 -> 2`.
  - **Gate 1 (2, 6):** CLOSED with `1 -> 3` and `3 -> 1`.
- **Current State:** `[0, 1, 1]` (Sw1 OFF, Sw2 ON, Sw3 ON). Sequence `3 -> 2`.
- **Hypothesis:** Gate 1 opens with `3 -> 2` or `2 -> 3`.
- **Plan:**
  1. Check Gate 1 (2, 6).
  2. If Gate 1 still closed: Turn Sw2 OFF, Sw3 OFF (Reset). Then Sw2 ON -> Sw3 ON (`2 -> 3`).