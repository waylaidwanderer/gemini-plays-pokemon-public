# Underground Warehouse
- **Goal:** Rescue Director.
- **Hypothesis:** "Switch on the end first" (Order 1->2? or 3->2?).
- **Gate Status:**
  - Gate 1 (2, 6): Opens with `[1, 0, 1]`? Closed at `[0, 1, 1]`.
  - Gate 2 (10, 6): Opens with `[0, 1, 0]`, `[0, 1, 1]`. Blocked by wall at (11, 10).
  - Gate 3 (16, 6): CLOSED at `[1, 1, 0]` (Order `2->1`). OPENS at `[1, 1, 0]` (Order `1->2`).
- **Plan:** Go to Sw2. Turn OFF, then ON. This creates sequence `1 -> 2`.
- **Current State:** `[1, 1, 0]` (Sw1 ON, Sw2 ON).
- **Next Step:** Check Gate 2, then toggle Sw2.