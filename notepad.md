# Ice Path Strategy
- **Primary Goal:** Reach Blackthorn City.
- **Status:** Solving Ice Puzzle (Again).
- **Ledge Conclusion:** All Row 18 ledges are solid walls.
- **Current Plan (East Corridor):**
  1. **Ice Puzzle:** Right -> Down -> Right -> Down -> Right to `(20, 23)`.
  2. **Navigate:** `(20, 23)` -> East to `(25, 23)` -> North to `(25, 19)` -> East to `(28, 19)` -> North to `(29, 12)` -> East to `(30, 12)`.
  3. **Exploration:** Go South down East Corridor (x=30) to reach the deep South-East area (Row 27).

# Tile Mechanics
- **FLOOR:** Walkable.
- **WALL:** Impassable.
- **FLOOR_UP_WALL:** Acts as a SOLID WALL at (7, 18), (14, 22), (20, 24). Likely all of Row 18 is blocked, but verifying.
- **ICE:** Slides player until collision.

# Key Log
- **Turn 16388:** Escaped ice loop to (13, 16).
- **Turn 16386:** Confirmed (30, 12) leads South.
- **Turn 16381:** Row 18 ledges confirmed impassable (at x=7).
- **Turn 16398:** Ambushed by Golbat while escaping. Gyarados critical (11 HP).
- **Immediate Action:** Flee -> Heal -> Reset to (13, 16).
- **Next Hypothesis:** Check the "Box" at the start ((13,16)-(15,17)). Is sliding UP from (15, 17) a valid move, or just a loop?
- **Turn 16404:** Testing (9, 18). Confirmed path to x=0 is blocked by walls at x=1-2 on Row 17.