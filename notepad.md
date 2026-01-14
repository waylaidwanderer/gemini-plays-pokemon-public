# Tile Mechanics
- FLOOR: Standard walkable ground.
- WATER: Traversable only while Surfing (requires HM03).
- BUOY: Impassable water obstacle.
- WALL: Impassable obstacle.
- FLOOR_UP_WALL: One-way barrier (Ledge). Blocks movement Up (North) and allows jumping Down (South). Land 2 tiles away when jumping.
- LEDGE_HOP_DOWN: One-way jump South. Entering from the side (Left/Right) is blocked.
- Interaction: To Surf, face WATER from an adjacent FLOOR tile and press A. Stepping onto FLOOR from WATER automatically ends Surfing.

# Suicune Quest
- Start Turn: 46650
- Objective: Trigger sighting in Cianwood City at (7, 4).
- Strategy:
    1. Walk to (12, 29).
    2. Surf North to (12, 19) and land.
    3. Walk West to (4, 19).
    4. Jump South over the ledge at (4, 20) to land at (4, 22).
    5. Walk West to the corridor at X=2.
    6. Walk North along X=2 to Y=4.
    7. Walk East to (7, 4) to trigger the sighting.
- Note: The inner city is a maze. The ledge at (4, 20) is the gateway to the West Coast corridor (X=2), which is the only clear path to the northern shore. Suicune sighting count = 1.

# Roaming Beast Data
- Raikou: Unknown
- Entei: Unknown
- Suicune Sightings: 1 (Ecruteak), 2 (Cianwood - Pending)

# Strategy: Capture all Legendary Pokemon
- Requirements: Clear Bell (Owned), 16 Badges (Owned).
- Plan: Complete sightings -> Tin Tower -> Capture Suicune (Lv 40).

# Lessons Learned
- Verify "gaps" in walls and buoy lines using tools like run_code or pathfinders before committing to long detours. My assumption of a solid wall led to a 100+ turn detour that was unnecessary.
- FLOOR_UP_WALL (ledges) can be jumped south from the adjacent northern tile. Side entry is blocked.
- BUOY tiles at X=16 and X=18 create a channel at X=17, but it is blocked at Y=25. X=15 is clear for North/South travel between Y=16 and Y=31.