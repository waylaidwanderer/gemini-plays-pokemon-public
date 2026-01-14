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
- Strategy: Southern Crossing
    1. Move Right to X=12.
    2. Move South along X=12 to Y=49.
    3. Jump South over the ledge at (12, 50) to land at (12, 51). (Mechanic Verification: Test ledge jumping).
    4. Move West along Y=51 to the corridor at X=2.
    5. Move North along X=2 to Y=4.
    6. Move East to (7, 4) to trigger the sighting.
- Note: The city center is a maze. The southern crossing and west corridor (X=2) are the most reliable path. Suicune sighting count = 1.
- Progress: Turn 46706, currently at (12, 49). Jumping ledge to reach Y=51 corridor.

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