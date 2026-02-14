# Underground Warehouse
- **Goal:** Rescue Director (requires opening shutter at (12, 8)).
- **Current State:** [Sw3=ON, Sw2=OFF, Sw1=ON] -> Shutter (6, 8) OPEN (Dead End).
- **Target State:** [Sw3=OFF, Sw2=ON, Sw1=ON] -> Shutter (12, 8) OPEN (Path to Director).
- **Plan:**
  1. Turn Sw3 OFF.
  2. Turn Sw2 ON.
  3. Verify Sw1 ON.
  4. Go through (12, 8) -> South to Director.