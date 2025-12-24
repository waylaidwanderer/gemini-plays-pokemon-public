# Ice Path Strategy
- **Navigation Analysis:**
  - The "East Corridor" shifts columns.
  - North Part: x=30 (Row 12 to 18).
  - Connection: Row 18/19.
  - South Part: x=28 (Row 18 down to ??).
- **Plan:**
  1. Walk to (28, 20).
  2. Explore South along x=28.
  3. Look for a ladder or a path West at the bottom (Row 27+).
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