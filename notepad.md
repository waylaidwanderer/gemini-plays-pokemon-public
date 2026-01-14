# Suicune Quest
- Start Turn: 46650
- Objective: Trigger sighting in Cianwood City at (7, 4).
- Strategy: The West Side Jump
    1. Walk West to (6, 44), then South to (6, 45).
    2. Jump South over the ledge at (6, 46) to land at (6, 47).
    3. Walk West along Row 47 to the corridor at X=2.
    4. Walk North along X=2 corridor to Y=4.
    5. Walk East along Row 4 to (7, 4) to trigger the sighting.
- Note: Row 43 is blocked at (7, 43). The ledge at (6, 46) is the key to reaching the western corridor. Suicune sighting count = 1.

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
- FLOOR_UP_WALL (ledges) can be jumped south from the adjacent northern tile. Side entry is blocked. Jumping lands you 2 tiles away from the start tile.
- BUOY tiles at X=16 and X=18 create a channel at X=17, but it is blocked at Y=25. X=15 is clear for North/South travel between Y=16 and Y=31.