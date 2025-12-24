# Ice Path Strategy
- **Current State:** At (15, 17).
- **Plan:** Slide Down to (15, 21), then Right to (19, 21).
- **Goal:** Explore central ice node (19, 21). Check neighbors (19, 19) and (20, 21) for secret paths.
- **Backup:** If no exit from (19, 21), re-explore SE Floor for missed branches.

# Map Structure
- **Hub (13, 16):** Connected to Entrance (4, 19).
- **North Wall:** Seems solid at Row 14.
- **West Wall:** Seems solid at x=3 (Dead End).
- **South Ledges:** Confirmed impassable.
- **East Path:** Via (15, 21) -> (19, 21). This is the only way forward.

# Item Locations
- **Item Ball (32, 23):** Surrounded by walls/ledges. Access likely from North (Row 21 Ice).

# Map Structure
- **West Corridor (x=0):** Connected to SW area (Row 22+).
- **Hub:** Connecting point.
- **South Loop:** Dead end.

# Mechanics
- **Ledges:** `FLOOR_UP_WALL` *should* be jumpable from North. Previous test at `(10, 18)` and `(14, 22)` failed. Retrying adjacent tiles.