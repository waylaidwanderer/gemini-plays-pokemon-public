# Ice Path Strategy
- **Current State:** At Hub (14, 16).
- **Goal:** Find path to West Corridor (x=0) or North Ice Area.
- **Reachability Analysis:** System reports 383 reachable tiles, implying an exit from the Hub exists.
- **Candidates:**
  1. South Ledges (Row 18): `(7, 18)` to `(12, 18)`. One MUST be jumpable.
  2. North Alcove (Row 15): `(9, 15)` to `(12, 15)`. Check for hidden path.
- **Plan:** Test South Ledges systematically. If fail, check North.

# Map Structure
- **West Corridor (x=0):** Connected to SW area (Row 22+).
- **Hub:** Connecting point.
- **South Loop:** Dead end.

# Mechanics
- **Ledges:** `FLOOR_UP_WALL` *should* be jumpable from North. Previous test at `(10, 18)` and `(14, 22)` failed. Retrying adjacent tiles.