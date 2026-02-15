# Underground Warehouse Mechanics
- **Hypothesis:** Sw2=ON opens (2,6) but closes (6,8). Sw2=OFF opens (6,8) but closes (2,6).
- **Conflict:** Need both open.
- **Action:** Turn Sw2 ON.
- **Next:** If (2,6) opens but (6,8) closes, go to Sw1 and toggle OFF.
- **Current Status:** Sw1: ON, Sw2: ON, Sw3: ON.