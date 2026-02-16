# Underground Warehouse
- **Goal:** Rescue Director.
- **Hypothesis:** "Switch on the end first" (Order 1->2? or 3->2?).
- **Verified Mechanics:**
  - **Order Matters:** `1 -> 2` vs `2 -> 1` produces different results.
  - **Gate 2 (10, 6):** OPENS with `2 -> 1`. CLOSED with `1 -> 2`.
  - **Gate 3 (16, 6):** CLOSED with `2 -> 1`. OPENS with `1 -> 2`.
  - **Gate 1 (2, 6):** CLOSED with `1 -> 3` (State `[1, 0, 1]`).
- **Current State:** `[1, 0, 1]` (Sw1 ON, Sw2 OFF, Sw3 ON).
- **Hypothesis:** Gate 1 opens with `3 -> 1` or `3 -> 2`.
- **Plan:**
  1. Go to Sw1. Turn OFF -> `[0, 0, 1]`.
  2. Turn Sw1 ON -> `[1, 0, 1]` (Sequence `3 -> 1`).
  3. If Gate 1 still closed: Turn Sw1 OFF, Go to Sw2, Turn ON (`3 -> 2`).
- **Goal:** Rescue Director.