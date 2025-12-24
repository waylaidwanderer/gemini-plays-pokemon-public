# Ice Path Strategy
- **Current Action:** Backtracking from East Floor.
- **Goal:** Find Ladder to B1F.
- **Status:** Found **HM07 (Waterfall)** at (31, 7).

# Ice Path Strategy
- **Current Action:** Looping back to Hub via Entrance.
- **Goal:** Reach West Ice Room Entrance (15, 14).
- **Status:** Shortcut at (19, 23) leads to Entrance (14, 16), not Puzzle.

# Ice Path Strategy
- **Current Action:** Returning to Hub to access SE Area.
- **Goal:** Reach Floor at (20, 23) and explore South.
- **Route:**
  1. Slide **Right** from (14, 17) to (15, 17).
  2. Slide **Down** to (15, 21).
  3. Slide **Right** to (19, 21).
  4. Slide **Down** to (19, 23).
  5. Step **Right** to (20, 23) [Target].

# Mechanics & Lessons
- **Ice Physics:** Sliding continues until collision.
- **Ledges:** `FLOOR_UP_WALL` tiles are impassable walls. `LEDGE_HOP_DOWN` are jumpable ledges.

# Map Structure
- **West:** Ice Room (Puzzle solved).
- **Center:** Hub.
- **East:** Winding corridors.
- **South:** Unexplored SE area (Access via Hub).
- **Items:** Item Balls at (32, 23), (35, 9).