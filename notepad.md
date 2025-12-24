# Ice Path Strategy
- **Current State:** At South Hub (14, 21).
- **Test Result:** `FLOOR_UP_WALL` at (14, 22) is IMPASSABLE from North. It is a Wall, not a Ledge.
- **Conclusion:** West Corridor is not accessible via this route.
- **Plan:** Return to Hub Entrance (13, 16) and explore North/East for the main path.

# Map Structure
- **West Corridor (x=0):** Likely isolated from this Hub. Access probably via fall/ladder.
- **Hub (y=16):** Central Safe Zone.
- **South Loop:** Dead end (Exit only).
- **East Ice Puzzle:** The likely path forward (North/East).

# Items
- **Item Ball at (32, 23):** Access via East Ice Puzzle.
- **Item Ball at (35, 9):** Access via NE area.

# Mechanics & Lessons
- **Ice Physics:** Sliding continues until collision.
- **Ledges:** `FLOOR_UP_WALL` tiles here are WALLS, not ledges.
- **Dead Ends:** South Hub leads only to exits or walls. Go North.