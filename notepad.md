# Ice Path Strategy
- **Current State:** At Hub (14, 16).
- **Goal:** Find path to West Corridor (x=0) or North Ice Area.
- **Reachability Analysis:** System reports 383 reachable tiles, implying an exit from the Hub exists.
- **Observation:** (12, 18) is a Wall.
- **Plan:** Test remaining ledges: (11, 18), (9, 18), (8, 18), (7, 18).
- **Reasoning:** Row 18 ledges are the only potential access to the West Corridor (x=0), which is the likely route to the North Ice Area (Row 13). Hub is otherwise isolated.
- **Hypothesis:** One of the `FLOOR_UP_WALL` tiles is a valid ledge. Markers might be stale/incorrect.

# Map Structure
- **West Corridor (x=0):** Connected to SW area (Row 22+).
- **Hub:** Connecting point.
- **South Loop:** Dead end.

# Mechanics
- **Ledges:** `FLOOR_UP_WALL` *should* be jumpable from North. Previous test at `(10, 18)` and `(14, 22)` failed. Retrying adjacent tiles.