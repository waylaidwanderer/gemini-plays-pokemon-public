# Underground Warehouse
- **Goal:** Rescue Director.
- **Hypothesis:** "Switch on the end first" (Order 1->2? or 3->2?).
- **Gate Status:**
  - Gate 1 (2, 6): Opens with `[1, 0, 1]`? Closed at `[0, 1, 1]`.
  - Gate 2 (10, 6): Opens with `[0, 1, 0]`, `[0, 1, 1]`. Blocked by wall at (11, 10).
  - Gate 3 (16, 6): Opens with `[1, 1, 0]`. Blocked by walls inside?
- **Plan:** Test `[1, 1, 0]` again to check Gate 2 status and walls.
- **Current State:** `[0, 1, 1]` (Sw2, Sw3 ON).
- **Next Step:** Turn Sw3 OFF -> `[0, 1, 0]`. Then Sw1 ON -> `[1, 1, 0]`.