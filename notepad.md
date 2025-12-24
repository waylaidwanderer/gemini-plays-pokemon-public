# Ice Path Strategy
- **Current Action:** Backtracking from East Floor.
- **Goal:** Find Ladder to B1F.
- **Status:** Found **HM07 (Waterfall)** at (31, 7).

# Ice Path Strategy
- **Current Action:** Returning to West Ice Room.
- **Goal:** Find Ladder to B1F (likely in SW area).
- **Status:** Found HM07. Escaped Ice Rooms.
- **Location:** At (23, 24) (Dead End).
- **Plan:**
  1. Navigate to West Ice Room Entrance (15, 14). [NEXT]
  2. Enter Ice and navigate to (7, 3).
  3. Slide **Down** from (7, 3) to (7, 14) [Exit to SW Area].
  4. Explore SW Area for Ladder.
- **Hypothesis:** The SW area (x<13, y>19) is only accessible via the West Ice Room vertical slide.
- **Items:** Item Balls at (32, 23), (35, 9) [Inaccessible].

# Mechanics & Lessons
- **Ice Physics:** Sliding continues until collision.
- **Ledges:** `FLOOR_UP_WALL` tiles are impassable walls.

# Map Structure
- **West:** Ice Room (Puzzle solved).
- **Center:** Hub.
- **East:** Winding corridors.
- **South:** Unexplored SW area.