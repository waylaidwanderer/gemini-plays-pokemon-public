# Suicune Quest
- Start Turn: 46650
- Objective: Trigger sighting in Cianwood City at the northern shore.
- Strategy: The Southern Promenade (Confirmed Path)
    1. Surf South to (23, 29) and land at (23, 30).
    2. Walk South along X=23 to (23, 45).
    3. Jump South over the ledge at (23, 46) to land at (23, 47).
    4. Walk South to (23, 51).
    5. Walk West along Row 51 to the far west corridor at X=2.
    6. Walk North along X=2 to Y=4.
    7. Walk East to (7, 4) to trigger the sighting.
- Note: Internal city walls at X=9, 12, 17 and buoys at X=16, 18, 19, 22 block direct access. Row 51 is the primary east-west thoroughfare. Suicune sighting count = 1.

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