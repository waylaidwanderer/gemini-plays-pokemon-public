# Ice Path Strategy
- **Primary Goal:** Reach Blackthorn City.
- **Current Plan (Ledge Testing):**
  1. **Navigate:** Walk to (8, 17) from Start (13, 16).
  2. **Test Ledges:** Attempt to jump South at x=8, 9, 10 (Row 18).
  3. **Rationale:** x=7 failed, but x=8-12 are untested. This barrier separates the Start from the West Corridor.
  4. **Backup:** If all ledges fail, commit to the "East Corridor" route (via x=30) which requires solving the main ice puzzle again.
- **East Corridor Route:** (13, 17) -> Solve to (20, 23) -> Go to (30, 12) -> South to (28, 19) -> South to unexplored area.

# Tile Mechanics
- **FLOOR:** Walkable.
- **WALL:** Impassable.
- **FLOOR_UP_WALL:** Acts as a SOLID WALL at (7, 18), (14, 22), (20, 24). Likely all of Row 18 is blocked, but verifying.
- **ICE:** Slides player until collision.

# Key Log
- **Turn 16388:** Escaped ice loop to (13, 16).
- **Turn 16386:** Confirmed (30, 12) leads South.
- **Turn 16381:** Row 18 ledges confirmed impassable (at x=7).