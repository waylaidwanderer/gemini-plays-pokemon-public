# Ice Path Strategy
- **Current Action:** Backtracking from East Floor.
- **Goal:** Find Ladder to B1F.
- **Status:** Found **HM07 (Waterfall)** at (31, 7).

# Ice Path Strategy
- **Current Action:** Looping back to Hub via Entrance.
- **Goal:** Reach West Ice Room Entrance (15, 14).
- **Status:** Shortcut at (19, 23) leads to Entrance (14, 16), not Puzzle.

# Ice Path Strategy
- **Current Action:** Exploring South-East Floor Area.
- **Goal:** Retrieve Item Ball at (32, 23).
- **Route:**
  1. Step **Right** to (20, 23) [Current].
  2. Walk South/East on the floor tiles.
  3. Find path to Item Ball (32, 23).

# Mechanics & Lessons
- **Ice Physics:** Sliding continues until collision.
- **Ledges:** `FLOOR_UP_WALL` tiles are impassable walls. `LEDGE_HOP_DOWN` are jumpable ledges.

# Map Structure
- **West:** Ice Room (Puzzle solved).
- **Center:** Hub.
- **East:** Winding corridors.
- **South:** SE Floor Area (Current Location).
- **Items:** Item Balls at (32, 23), (35, 9).