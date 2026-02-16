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
  1. Reset Complete (All OFF).
  2. Turn Sw3 ON.
  3. Turn Sw2 ON.
  4. Turn Sw1 ON.
  5. Check Gate 1.
- **SOLVED:** Gate 1 (2, 6) OPENS with State `[0, 0, 1]` (Switch 3 ON, others OFF).
- **Current State:** `[0, 0, 1]`.
- **Plan:**
  1. Enter Gate 1.
  2. Rescue Director.
- **Encounter:** Rival Silver at (4, 8) says "There's nothing down there" and doesn't battle.
- **Action:** Bypassing Silver to explore the rest of the warehouse. Heading to Burglar Duncan (9, 12).