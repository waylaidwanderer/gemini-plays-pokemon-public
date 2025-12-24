# Ice Path Strategy
- **Primary Goal:** Reach Blackthorn City.
- **Status:** At Start (13, 16). Preparing to test Row 18 ledges.
- **Critical Info:**
  - `(7, 18)` is confirmed IMPASSABLE.
  - `(8, 18)` is UNTESTED (despite previous confusion).
  - Gyarados is low HP (11). Must be careful.
- **Plan:**
  1. Walk to `(8, 17)`.
  2. Test `(8, 18)` by pressing Down.
  3. If it's a ledge, jump to Row 19/22 and head West.
  4. If it's a wall, mark it and try `(9, 18)`.
  5. If ALL Row 18 ledges fail, the "West Corridor" must be accessed via the **Ice Puzzle** -> **Sliding UP from (15, 17)** path (The "Box" hypothesis).

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