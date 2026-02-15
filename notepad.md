# Underground Warehouse Mechanics
- **Goal:** Rescue Director / Get Card Key.
- **Config [1:OFF, 2:ON, 3:ON]:**
  - OPEN: (2,6), (12,8), (10,10).
  - CLOSED: (10,6), (16,6), (6,8), (2,10), (16,10).
- **Analysis:** (2,6) leads to dead end at (2,10). (12,8) is inaccessible due to closed (16,6)/(10,6)/(6,8).
- **Plan:** Try Config [1:ON, 2:OFF, 3:ON]. This supposedly opens (6,8) and (10,10).
- **Hypothesis:** If (6,8) opens, I can cross from left to middle. If (10,10) is open, I can go south to Item/Director.
- **Next Steps:** Toggle Sw2 (OFF), Toggle Sw1 (ON).