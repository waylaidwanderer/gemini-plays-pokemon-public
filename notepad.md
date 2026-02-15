# Underground Warehouse
- **Goal:** Rescue Director.
- **Action:** Turning Sw3 ON.
- **Correction:** Path blocked by Grunt at (3,2). Detouring via Row 3.
- **Path:** (4,2) -> Down -> Left -> Left -> Up -> (2,2).
- **Strategy: The "Inside Job" (Final Plan)**
  - **Logic:** `[OFF, OFF, ON]` opens the exit path ((6,8) & (10,10)) but closes the entry ((2,6)).
  - **Solution:** I must be INSIDE the Left Room when I trigger the final state.
  - **Plan:**
    1. Turn Sw3 OFF (Current State: [ON, OFF, ON] -> [ON, OFF, OFF]).
    2. Go to Sw1 and Turn OFF ([ON, OFF, OFF] -> [OFF, OFF, OFF]).
    3. Enter Left Room via (2,6) (Open in [OFF, OFF, OFF]).
    4. Turn Sw3 ON (State: [OFF, OFF, ON]).
    5. Exit via (6,8) -> (10,10) -> Director.