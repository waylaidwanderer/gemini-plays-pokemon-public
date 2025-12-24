# Ice Path Strategy
- **Current Action:** Backtracking from East Floor.
- **Goal:** Find Ladder to B1F.
- **Status:** Found **HM07 (Waterfall)** at (31, 7).

# Ice Path Strategy
- **Current Action:** Re-entering West Ice Room (Shortcut).
- **Goal:** Access South-West Area via `(7, 3)` -> Down.
- **Location:** At Hub `(20, 23)`.
- **Shortcut Plan:**
  1. Move **Left** to `(19, 23)` (Enter Ice). [NEXT]
  2. Slide **Left** -> Stop at `(18, 23)` (Wall at `17, 23`? Check map).
     - Map says `(16, 23)` is WALL. `(17, 23)` is WALL.
     - So `(18, 23)` is the stop.
  3. Slide **Up** -> Stop at `(18, 20)` (Wall at `18, 19`).
  4. Slide **Left** -> Stop at `(14, 20)` (Wall at `13, 20`).
  5. Slide **Up** -> Stop at `(14, 2)` (Wall at `14, 1`).
  6. Slide **Left** -> `(8, 2)` (Rock at `7, 2`).
  7. Follow puzzle to `(7, 3)` -> Slide **Down** to SW Area.
- **Items:** Item Balls at `(32, 23)`, `(35, 9)` [Inaccessible].

# Mechanics & Lessons
- **Ice Physics:** Sliding continues until collision.
- **Ledges:** `FLOOR_UP_WALL` tiles are impassable from South/Floor.

# Map Structure
- **West:** Ice Room (Puzzle solved).
- **Center:** Hub.
- **East:** Winding corridors.
- **South:** Unexplored SW area.