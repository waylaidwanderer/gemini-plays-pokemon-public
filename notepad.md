# Ice Path Strategy
- **Primary Goal:** Reach Blackthorn City.
- **Immediate Task:** Heal Gyarados (Critical HP).
- **Status:** At Start (13, 16).
- **Next Hypothesis (Center-North Path):**
  1. From (13, 17), slide Right to (15, 17).
  2. **TEST:** Slide **UP** from (15, 17).
  3. **Rationale:** This path is untested. It might lead to the inaccessible North/West areas.
- **Backup:** If that fails, revert to East Corridor plan.

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