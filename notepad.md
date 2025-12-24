# Ice Path Strategy
- **Current State:** At Hub (14, 16).
- **Goal:** Find path to West Corridor (x=0) or North Ice Area.
- **Reachability Analysis:** System reports 383 reachable tiles, implying an exit from the Hub exists.
- **Observation:** (12, 18) and (11, 18) are Walls. South Ledges are likely all impassable.
- **Plan:** Return to Ice Entrance (13, 16).
- **Route:**
  1. Slide **Right** to (15, 16).
  2. Slide **Down** to (15, 21).
  3. Slide **Right** to (19, 21).
  4. **Explore:** Slide **Up** or **Right** from (19, 21).
- **Hypothesis:** The path to the North/East Ice Area starts from the central ice nodes (x=19), not the Hub ledges.
- **Reachability:** System says 383 tiles reachable. This confirms access to the large East/North sections exists.

# Map Structure
- **West Corridor (x=0):** Connected to SW area (Row 22+).
- **Hub:** Connecting point.
- **South Loop:** Dead end.

# Mechanics
- **Ledges:** `FLOOR_UP_WALL` *should* be jumpable from North. Previous test at `(10, 18)` and `(14, 22)` failed. Retrying adjacent tiles.