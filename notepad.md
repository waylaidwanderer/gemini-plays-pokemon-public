# Ice Path Strategy
- **Current Action:** Backtracking from East Floor.
- **Goal:** Find Ladder to B1F.
- **Status:** Found **HM07 (Waterfall)** at (31, 7).

# Ice Path Strategy
- **Current Action:** Looping back to Hub via Entrance.
- **Goal:** Reach West Ice Room Entrance (15, 14).
- **Status:** Shortcut at (19, 23) leads to Entrance (14, 16), not Puzzle.
- **Loop Plan:**
  1. Slide **Up** -> (18, 20). [DONE]
  2. Slide **Left** -> (14, 20). [DONE]
  3. Slide **Up** -> (14, 16). [DONE]
  4. Walk to (13, 17). [DONE]
  5. Slide **Right** -> (15, 17). [DONE]
  6. Slide **Down** -> (15, 21). [NEXT]
  7. Slide **Right** -> (19, 21).
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