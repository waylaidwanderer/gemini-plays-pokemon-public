# Ice Path Strategy
- **Primary Goal:** Reach Blackthorn City.
- **Status:** Solving Ice Puzzle (South/East Route).
- **Location:** (19, 21). Sliding Down to (19, 23).
- **Critical Test:** Must test the ledge at **(19, 24)**.
  - (20, 24) confirmed blocked.
  - (18, 24) confirmed blocked.
  - If (19, 24) works, I reach the South Area.
  - If (19, 24) fails, I am running out of options on this screen.
- **East Corridor Note:** Column x=28 is blocked at y=21, meaning the East path loops back to (20, 23). The only way out is Row 24.
- **Items:** Item Balls at (32, 23) and (35, 9).

# Mechanics & Lessons
- **Ice Physics:** Sliding continues until collision.
- **Ledges:** `FLOOR_UP_WALL` tiles at (7,18), (8,18), (9,18), (10,18), (14,22), (20,24) are **IMPASSABLE WALLS**. Do not attempt to jump them.
- **Map Structure:** Map appears split into West (Goal?), Center (Start/Hub), and East (Dead ends/Item Balls).

# Map Notes
- **East Corridor:** Accessible via (20,23) -> (25,23) -> (25,19) -> (28,19).
- **Dead Ends:**
  - North-East Loop (Row 11-18) connects to nothing but the East Corridor.
  - West Row 16 is blocked.
  - Row 18 Ledges are walls.
  - (25, 11) is a dead end.
- **Hypothesis:** Deep South-East (x=28, y>20) holds the key to progression (Ladder or West Path).
- **Turn 16442:** Verified East Corridor is a loop. Returning to (20, 23).
- **Hypothesis:** The exit to the West/South side must be via the ledges at Row 24 (x=18, 19).
- **Test Plan:**
  1. Go to (19, 23) [Ice]. Press Down to test (19, 24).
  2. If fail, go to (18, 23) [Ice]. Press Down to test (18, 24).
- **Turn 16444:** Sliding Left to (18, 23). Will test ledge (18, 24) next.
- **Turn 16445:** Testing ledge at (18, 24).
- **Turn 16446:** Testing (18, 24). If wall, escaping to Start to try (15, 17) -> Up.