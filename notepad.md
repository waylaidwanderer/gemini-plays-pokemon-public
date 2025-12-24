# Ice Path Strategy
- **Current State:** At Hub (9, 16).
- **Goal:** Explore North/East Ice Area for Ladder to B1F.
- **Reachability:** West Corridor (Column 0) confirmed unreachable from Hub (bfs failed). Ladder must be in NE or accessed differently.
- **Plan:**
  1. Check North Alcove (9, 15).
  2. Return to Ice Entrance (13, 16).
  3. Slide Right -> Down -> Right to reach (19, 21).
  4. Explore paths from (19, 21) (Up or Right).

# Map Structure
- **Hub:** Isolated loop.
- **West Corridor:** Accessed via SW Floor (Row 22+).
- **Access Point:** Likely a ledge at Row 18 or Row 22. (14, 22) failed. Row 18 is the best bet.
- **Critical Insight:** Previously blocked at (5, 16) despite it looking like FLOOR. This suggests a barrier separating the Hub from the West Corridor.
- **Hypothesis:** The "South Ledges" or the Ice Puzzle are the only ways to cross this barrier.
- **Current Action:** Testing Ledge at (9, 18). If blocked, the West Corridor must be accessed via a different route (possibly a hole from the floor above?).
- **Note:** Check for any "Holes" or "Ladders" I might have missed in the layout.