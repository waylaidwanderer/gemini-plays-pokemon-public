# Ice Path Strategy
- **Current Test:** Verifying if `FLOOR_UP_WALL` at (14, 22) is a jumpable ledge from the North.
- **Hypothesis:** It acts as a one-way ledge allowing access to the southern corridor (Row 23).
- **Execution:** Slide Down to (15, 21), Left to (14, 21), then Down.

# Map Structure
- **West Edge (x=0):** Open floor corridor N-S.
- **Hub (y=16):** Isolated floor area.
- **South Loop:** SE Floor (Row 23) leads to Exit Ledge (29, 11).
- **Access to West:** Potentially via Ledge at (14, 22).

# Items
- **Item Ball at (32, 23):** Access via East Ice Puzzle.
- **Item Ball at (35, 9):** Access via NE area.

# Mechanics & Lessons
- **Ice Physics:** Sliding continues until collision.
- **Ledges:** `FLOOR_UP_WALL` tiles are impassable from South (Wall). Testing navigability from North (Ledge).