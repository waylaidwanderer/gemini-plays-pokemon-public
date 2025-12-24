# Ice Path Strategy
- **Primary Goal:** Reach Blackthorn City.
- **Status:** At (8, 17). Confirmed (8, 18) is a wall.
- **Plan:**
  1. Move to (9, 17).
  2. Test `(9, 18)` by pressing Down.
  3. Continue testing ledges (10, 18) through (12, 18) if necessary.
  4. If ALL fail, I am missing a fundamental path (possibly hidden ladder or North-West access).

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