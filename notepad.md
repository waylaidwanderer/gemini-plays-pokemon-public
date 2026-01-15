# Tile Mechanics
- FLOOR_UP_WALL: Blocks SOUTH movement. PASSABILITY FROM SOUTH TO NORTH UNVERIFIED. Found at (4, 20), (16, 10), (8, 34).
- LEDGE_HOP_DOWN: Blocks NORTH movement. Found at (10, 15).
- Vertical Walls: X=3, 5, 7, 9, 11, 17, 20.

# Suicune Quest (Cianwood)
- Start Turn: 49771
- Start Time: 3:29 PM

## Strategy: The Great Southern Loop (v2)
The city is a maze of walls and ledges. Row 51 is the only clear East-West path.
1. Land at (23, 32). (Completed)
2. Navigate to (10, 51) via Row 33 and the X=12 ledge gap:
   - Up to (23, 33), then Left to (18, 33).
   - Up to Row 32 to bypass Pokefan M at (17, 33).
   - Left to (12, 32), then Down to (12, 33).
   - Down to (12, 49), then Left to (10, 49).
   - Down through Row 50 gap to (10, 51).
3. Walk West to (2, 51) to enter the Western Corridor.
4. Walk North to (2, 12).
5. Walk East to (14, 12).
6. Walk North to (14, 10) to trigger Suicune sighting.

# Progress Notes
- Discovered: Central Pool is blocked by buoys at X=16 and X=18.
- Note: No wild encounters on land in the city. Out of Repels.
- Hypothesis: (14, 10) is the trigger point for the Suicune sighting.
- Hypothesis: FLOOR_UP_WALL allows landing from the East/West (Testing required).
- Verification Task: Test North/South passability of FLOOR_UP_WALL at (12, 50).