# Suicune Quest
- Start Turn: 46650
- Objective: Trigger sighting in Cianwood City at the northern shore.
- Strategy: The Waterway Bypass
    1. Surf at (19, 30).
    2. Surf North to Y=21, then East to X=23.
    3. Surf North along X=23 to Y=11 (bypasses Y=15 buoy line).
    4. Surf West to (17, 11) and land at (16, 11).
    5. Walk West along Row 11 to (7, 11), then North to (7, 4).
- Note: Land routes are heavily blocked by ledges and walls. The waterway is the only confirmed efficient path to the northern shore. Suicune sighting count = 1.

# Roaming Beast Data
- Raikou: Unknown
- Entei: Unknown
- Suicune Sightings: 1 (Ecruteak), 2 (Cianwood - Pending)

# Strategy: Capture all Legendary Pokemon
- Requirements: Clear Bell (Owned), 16 Badges (Owned).
- Plan: Complete sightings -> Tin Tower -> Capture Suicune (Lv 40).

# Tile Mechanics
- FLOOR: Standard walkable ground.
- WATER: Traversable only while Surfing (requires HM03).
- BUOY: Impassable water obstacle.
- WALL: Impassable obstacle.
- FLOOR_UP_WALL: One-way barrier (Ledge). Blocks movement Up (North) and allows jumping Down (South). Land 2 tiles away when jumping.
- LEDGE_HOP_DOWN: One-way jump South. Entering from the side (Left/Right) is blocked.
- Interaction: To Surf, face WATER from an adjacent FLOOR tile and press A. Stepping onto FLOOR from WATER automatically ends Surfing.

# Lessons Learned
- Verify "gaps" in walls and buoy lines using tools like run_code or pathfinders before committing to long detours.
- Cianwood's internal geography is extremely restrictive; use the coastline for north-south travel.
- BUOY tiles at X=16 and X=18 create a channel at X=17, but it is blocked at Y=25. X=15 is clear for North/South travel between Y=16 and Y=31.