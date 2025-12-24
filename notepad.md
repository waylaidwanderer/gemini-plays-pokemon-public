# Ice Path Strategy
- **Current Action:** Backtracking from East Floor.
- **Goal:** Find Ladder to B1F.
- **Status:** Found **HM07 (Waterfall)** at (31, 7).

# Ice Path Strategy
- **Current Action:** Looping back to Hub via Entrance.
- **Goal:** Reach West Ice Room Entrance (15, 14).
- **Status:** Shortcut at (19, 23) leads to Entrance (14, 16), not Puzzle.

# Ice Path Strategy
- **Current Action:** Accessing South-West Area (Shortcut).
- **Goal:** Find Ladder to B1F.
- **Location:** At `(14, 21)` (approx).
- **Shortcut Plan:**
  1. Slide **Left** from `(19, 21)` to `(14, 21)` (Wall at `13, 21`). [DONE]
  2. Slide **Up** from `(14, 21)`. [NEXT]
     - **Branch A:** Stop at `(14, 16)` (if wall exists) -> Walk Left to SW Ledges.
     - **Branch B:** Slide to `(14, 2)` (if no wall) -> Slide Left to `(8, 2)` -> Puzzle to `(7, 3)` -> Down to SW Area.
- **Items:** Item Balls at `(32, 23)`, `(35, 9)` [Inaccessible].

# Mechanics & Lessons
- **Ice Physics:** Sliding continues until collision.
- **Ledges:** `FLOOR_UP_WALL` tiles are impassable from South, jumpable from North.

# Map Structure
- **West:** Ice Room (Puzzle solved).
- **Center:** Hub.
- **East:** Winding corridors.
- **South:** Unexplored SW area.
  7. Slide **Right** -> (19, 21).
  8. Slide **Down** -> (19, 23).
  9. Slide **Right** -> (20, 23) [Back at Hub].
  10. Walk to (15, 14) via East Corridors.
- **Items:** Item Balls at (32, 23), (35, 9).

# Mechanics & Lessons
- **Ice Physics:** Sliding continues until collision.
- **Ledges:** `FLOOR_UP_WALL` tiles are impassable walls.

# Map Structure
- **West:** Ice Room (Puzzle solved).
- **Center:** Hub.
- **East:** Winding corridors.
- **South:** Unexplored SW area.