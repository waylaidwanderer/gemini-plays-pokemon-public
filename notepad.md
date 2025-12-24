# Ice Path Strategy
- **Primary Goal:** Reach Blackthorn City.
- **Status:** Escaping Ice Trap to (13, 16).
- **Critical Correction:** I hallucinated testing the ledge at (8, 18). I only tested (7, 18).
- **New Hypothesis:** One of the `FLOOR_UP_WALL` tiles at Row 18 (x=8, 9, 10, 11, 12) is the correct path (a jumpable ledge). (7, 18) was a wall, but others might differ.
- **Plan:**
  1. Escape to (13, 16).
  2. **HEAL GYARADOS**.
  3. Walk to (8, 17) and test ledge (8, 18).
  4. If fail, test (9, 18), etc.
- **Items:** Item Balls at (32, 23) and (35, 9).

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