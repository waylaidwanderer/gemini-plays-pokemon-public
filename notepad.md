# Suicune Quest
- Start Turn: 46650
- Objective: Trigger sighting in Cianwood City at the northern shore.
- Strategy: The Southern Promenade
    1. Walk to (23, 44), then South to (23, 52).
    2. Walk West along Row 52 to the corridor at X=2.
    3. Walk North along X=2 corridor to Y=4.
    4. Walk East along Row 4 to (7, 4) to trigger the sighting.
- Note: Ledge jumps at (6, 46) and (12, 50) failed. The southern-most route via Row 52 is the only confirmed clear path to the west side.

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
- FLOOR_UP_WALL: One-way barrier (Ledge). Blocks movement Up (North) and allows jumping Down (South). Land 2 tiles away when jumping. (Note: Manual verification failed for some ledges).
- LEDGE_HOP_DOWN: One-way jump South. Entering from the side (Left/Right) is blocked.
- Interaction: To Surf, face WATER from an adjacent FLOOR tile and press A. Stepping onto FLOOR from WATER automatically ends Surfing.

# Lessons Learned
- Verify "gaps" in walls and buoy lines using tools like run_code or pathfinders before committing to long detours.
- Ledge jumping can be finicky or blocked by invisible triggers. Always look for non-jumping alternates like Row 52 in Cianwood.
- BUOY tiles at X=16 and X=18 create a channel at X=17, but it is blocked at Y=25. X=15 is clear for North/South travel between Y=16 and Y=31.