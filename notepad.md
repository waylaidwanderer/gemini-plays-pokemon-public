# Tile Mechanics
- FLOOR_UP_WALL: Blocks SOUTH movement. Passable from SOUTH to NORTH. Found at (6-8, 34), (10, 48), (12, 50).
- LEDGE_HOP_DOWN: Blocks NORTH movement. One-way ledge jumping South. Found at (10, 15).
- Vertical Walls: X=3, 5, 7, 9, 11, 17, 20.

# Suicune Quest (Cianwood)
- Start Turn: 49771
- Start Time: 3:29 PM

## Strategy: The Row 34 Western Bypass (Confirmed)
The northern plateau (Row 10-12) is accessible via the Western Corridor (X=0-2). Row 34 is the key East-West transit corridor.
1. Surf South from (24, 16) to (24, 32). (In Progress)
2. Land at (23, 32).
3. Walk to (12, 33) via Row 32 (to bypass Pokefan M).
4. Walk to (10, 33), then Down to (10, 35).
5. Walk West to (8, 35), then North to (8, 34) (Ledge jump North).
6. Walk West along Row 34 to (2, 34) to enter the Western Corridor.
7. Walk North through the corridor to (2, 14).
8. Walk East to (8, 14), then North to (8, 10).
9. Walk East to (14, 10) to trigger Suicune sighting.

# Progress Notes
- Verified: FLOOR_UP_WALL blocks entry from the North (Turn 49811).
- Verified: Row 34 (X=2-5) is a clear corridor to the Western Corridor.
- Note: Out of Repels. No wild encounters on land in the city.
- Hypothesis: (14, 10) is the trigger point for the Suicune sighting.

# Reflection Turn (49828)
- Immediate Execution: Re-pivoting to the Row 34 land route. By entering Row 34 from the South at X=8, I can bypass the ledges and use the corridor to reach the Western Corridor. This is the most efficient path through the city maze.
- Notepad Hygiene: Strategy updated to the definitive land route.
- Error Analysis: Root cause of delay was misinterpreting the directional blocking of FLOOR_UP_WALL.