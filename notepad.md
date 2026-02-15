# Underground Warehouse
- **Goal:** Rescue Director.
- **Current State:** [1,0,1] (Sw1 ON, Sw2 OFF, Sw3 ON).
- **Hypothesis:** Testing [1,0,1].
- **Plan:**
  1. Check Gates via tool (Target: Exit (16,10) == 3fe2).
  2. If Exit is OPEN, navigate to it.
  3. If Closed, try [1,1,1] again and check Exit with tool.