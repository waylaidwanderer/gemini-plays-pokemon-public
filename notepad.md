# Tile Mechanics
- FLOOR_UP_WALL: Blocks SOUTH movement. Passable from SOUTH to NORTH. Found at (6-8, 34), (10, 48), (12, 50), (16, 10).
- LEDGE_HOP_DOWN: Blocks NORTH movement. One-way ledge jumping South. Found at (10, 15).
- Vertical Walls: X=3, 5, 7, 9, 11, 17, 20.

# Suicune Quest (Cianwood)
- Start Turn: 49771
- Start Time: 3:29 PM

## Strategy: The Row 34 Western Bypass (Final)
The northern plateau (Row 10-12) is accessible via the Western Corridor (X=0-2). Row 34 provides a clear path to bypass the internal city walls.
1. Walk to (12, 35). (In Progress)
2. Walk to (8, 35), then move North to (8, 34) (Jumping the FLOOR_UP_WALL ledge).
3. Walk West along Row 34 to (2, 34) to enter the Western Corridor.
4. Walk North through the corridor to (2, 12).
5. Walk East along Row 12 to (14, 12).
6. Walk North to (14, 10) to trigger Suicune sighting.

# Progress Notes
- Verified: Row 34 (X=6-8) are FLOOR_UP_WALL, allowing Northward and East-West movement, but blocking Southward entry.
- Verified: X=3 wall has a gap at Row 34.
- Note: Out of Repels. No wild encounters on land in the city.
- Hypothesis: (14, 10) is the trigger point for the Suicune sighting.

# Reflection Turn (49815)
- Immediate Execution: Pivoting to the Row 34 land route after realizing the directional nature of FLOOR_UP_WALL.
- Notepad Hygiene: Cleaned up redundant logs and buoy/gap markers. Strategy updated to the most efficient land route.
- Automation: Python sandbox is currently unavailable; proceeding with manual navigation and logical verification.
- Error Analysis: Root hypothesis that Row 34 was a dead end was based on a single failed 'Down' movement. Re-verified that 'Up' and 'Left/Right' are permitted.