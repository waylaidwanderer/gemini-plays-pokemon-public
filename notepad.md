# Ice Path Strategy
- **Primary Goal:** Reach Blackthorn City.
- **Status:** At (8, 17). Testing ledge (8, 18).
- **Critical Info:**
  - `(7, 18)` is confirmed IMPASSABLE.
  - Gyarados is low HP (11). Machoke (Lv57) is backup.
- **Plan:**
  1. Test `(8, 18)` by pressing Down.
  2. If it's a ledge, jump to Row 19 and head West.
  3. If it's a wall, mark it and try `(9, 18)`.
  4. If ALL Row 18 ledges fail, pivot to **Ice Puzzle -> Slide UP from (15, 17)**.

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