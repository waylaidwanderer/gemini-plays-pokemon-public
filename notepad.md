# Underground Warehouse Strategy
- **Logic:** Sequence 3->2 (Sw3 ON then Sw2 ON) failed in Turn 43465.
- **Logic:** Sequence 2->3 (Sw2 ON then Sw3 ON) worked in Turn 43393.
- **Plan:** Execute Sequence 2->3.
  1. Cancel Sw3 (Leave OFF).
  2. Go to Sw2 -> Turn ON.
  3. Return to Sw3 -> Turn ON.
- **Hypothesis:** Starting from All OFF, Sw2 ON keeps Gate (2, 6) OPEN.