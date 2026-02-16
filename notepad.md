# Underground Warehouse
- **Hypothesis:** "Switch on the end first" (Order 1->2? or 3->2?).
- **Verified Mechanics:**
  - **Order Matters:** `1 -> 2` vs `2 -> 1` produces different results.
  - **Gate 2 (10, 6):** OPENS with `2 -> 1`. CLOSED with `1 -> 2`.
  - **Gate 3 (16, 6):** CLOSED with `2 -> 1`. OPENS with `1 -> 2`.
  - **Gate 1 (2, 6):** CLOSED with `1 -> 3` and `3 -> 1`.
- **Current State:** `[0, 1, 0]` (Sw1 OFF, Sw2 ON, Sw3 OFF).
- **Hypothesis:** Gate 1 opens with `2 -> 3` (Sequence `Switch 2 then Switch 3`).
- **Plan:**
  1. Turn Sw2 OFF (Reset to `[0, 0, 0]`).
  2. Turn Sw2 ON (Start Sequence).
  3. Turn Sw3 ON (Finish Sequence).
  4. Check Gate 1.