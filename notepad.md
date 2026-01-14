# Suicune Quest
- Objective: Trigger sighting in Cianwood City at the northern shore.
- Strategy: The Great Northern Sea Loop
    1. Surf East at (19, 30) to X=23.
    2. Surf North along X=23 to Row 8.
    3. Surf West along Row 8 to X=19.
    4. Surf South to Row 11.
    5. Surf West to land at (16, 11).
    6. Walk to (7, 4) to trigger sighting.
- Note: Internal land routes and ledge jumps are blocked. The buoy wall at X=22 has a gap at Row 8. Suicune sighting count = 1.

# Tile Mechanics (Verified)
- FLOOR: Standard walkable ground.
- WATER: Traversable only while Surfing (requires HM03).
- BUOY: Impassable water obstacle.
- WALL: Impassable obstacle.
- FLOOR_UP_WALL / LEDGE_HOP_DOWN: In Cianwood, these function as standard WALL tiles from the north (cannot jump down).
- Interaction: To Surf, face WATER from an adjacent FLOOR tile and press A. Stepping onto FLOOR from WATER automatically ends Surfing.

# Lessons Learned
- Cianwood's ledges are impassable from the north.
- Internal walls divide the city into inaccessible strips on land.
- Zig-zag buoy lines block the eastern sea. Gap found at (22, 8).
- Reveal 'unseen' tiles manually before planning long routes.