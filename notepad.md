# Underground Warehouse Mechanics
- **Goal:** Rescue Director / Get Card Key.
- **Config [ON, OFF, ON]:**
  - **Status:** Sw1 ON, Sw2 OFF, Sw3 ON.
  - **Hypothesis:** Sw3 opens (2,6). Sw1 might open (6,8).
  - **Target:** If (2,6) & (6,8) are OPEN -> Path: (2,6) -> (6,8) -> (10,10).
- **Previous Check [OFF, OFF, ON]:** (2,6) Open, (12,8) Open, (10,10) Open. (6,8) Closed.
- **Connections:** Warehouse (23,3) <-> Underground (22,27).
- **NPCs:** Silver (19,24) & Grunt (22,24) in Underground isolated room.