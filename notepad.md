# Tile Mechanics
- FLOOR_UP_WALL: Blocks SOUTH movement. Hypothesis: Passable from SOUTH to NORTH (one-way ledge jumping North). Found at (4, 30), (4, 20), (6-8, 34), (10, 48), (12, 50).
- LEDGE_HOP_DOWN: Blocks NORTH movement. One-way ledge jumping South. Found at (10, 15).
- Vertical Walls: X=3, 5, 7, 9, 11, 17, 20.

# Suicune Quest (Cianwood)
- Start Turn: 49771
- Start Time: 3:29 PM

## Strategy: The Ultimate Land Route (Definitive)
1. Walk West along Row 32 to (12, 32). (In Progress)
2. Walk South along X=12 to (12, 44).
3. Walk West through gap at (9, 44) to (8, 44).
4. Walk North along X=8 to (8, 35).
5. Walk West through gap at (5, 35) to (4, 35).
6. Walk North along X=4 to (4, 30). Test Northward passability of FLOOR_UP_WALL.
7. IF PASSABLE: Continue North to (4, 12), then East to (14, 12), then North to (14, 10).
8. IF BLOCKED: Walk South to (4, 51), then West to (2, 51), then North to (2, 12), then East to (14, 12), then North to (14, 10).

# Battle Preparation: Eusine
- Expected Roster: Drowzee (Lv23), Haunter (Lv23), Electrode (Lv25).
- Counter-Strategy: Lead with Calcifer (Lv64). Flamethrower for Drowzee/Haunter, Thunderpunch for Electrode.
- Status: Party fully healthy.

# Progress Notes
- Verified: FLOOR_UP_WALL blocks entry from the North (Turn 49811).
- Verified: X=9 wall has a gap at Row 44. X=5 wall has a gap at Row 35.
- Note: Out of Repels. No wild encounters on land in the city.
- Hypothesis: (14, 10) is the trigger point for the Suicune sighting.
- Hypothesis: FLOOR_UP_WALL is passable from South to North.