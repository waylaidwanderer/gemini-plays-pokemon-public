# Ice Path Strategy
- **Primary Goal:** Reach Blackthorn City.
- **Status:** Executing Ice Puzzle Solution.
- **Current Plan (East Corridor):**
  1. Move from (9, 17) to (13, 17).
  2. **Sequence:** Right -> (15, 17) -> Down -> (15, 21) -> Right -> (19, 21) -> Down -> (19, 23) -> Right -> (20, 23).
  3. Navigate to (30, 12).
  4. Explore South down x=30.
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