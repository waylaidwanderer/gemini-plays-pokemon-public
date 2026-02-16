# Underground Warehouse
- **Goal:** Rescue Director.
- **Hypothesis:** "Switch on the end first" (Order 1->2? or 3->2?).
- **Verified Mechanics:**
  - **Order Matters:** `1 -> 2` vs `2 -> 1` produces different results.
  - **Gate 2 (10, 6):** OPENS with `2 -> 1` (Current). CLOSED with `1 -> 2`. Room behind is a dead end (Wall at Row 10).
  - **Gate 3 (16, 6):** CLOSED with `2 -> 1` (Current). OPENS with `1 -> 2`. Room behind is a dead end?
  - **Gate 1 (2, 6):** Opens with `[1, 0, 1]` (Sw1, Sw3 ON).
- **Current State:** `[1, 1, 0]`.
- **Plan:**
  1. Turn Sw2 OFF -> `[1, 0, 0]`.
  2. Turn Sw3 ON -> `[1, 0, 1]`.
  3. Explore Gate 1 and Back Gate (2, 10).
- **Goal:** Reach Back Gate (2, 10).