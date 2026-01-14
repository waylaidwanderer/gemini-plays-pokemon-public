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
    1. Walk to (13, 16).
    2. Surf north/east to reach (18, 11).
    3. Land at (16, 11) (via unseen (17, 11)).
    4. Walk west along Y=11 to (7, 11), then north to (7, 4).
- Note: Ledge at (6, 34) failed manual verification (impassable from north). Suicune sightings count = 1.

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