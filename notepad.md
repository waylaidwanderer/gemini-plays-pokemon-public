# Suicune Quest
- Objective: Trigger sighting in Cianwood City at the northern shore.
- Strategy: The Middle-West Route
    1. Walk West to (12, 30).
    2. Walk North to (12, 28).
    3. Surf North from (12, 28) to land at (12, 19).
    4. Walk West along Row 19 to (5, 19).
    5. Walk North to (5, 18), then West to (2, 18).
    6. Walk North along X=2 to Y=4.
    7. Walk East to (7, 4) to trigger the sighting.
- Note: Ledge jumps at (6, 34), (12, 50), and (23, 46) are confirmed IMPASSABLE from the north. The internal land mass is divided by walls. The corridor at X=2 is the primary north-south thoroughfare.
- Suicune sighting count = 1.

# Tile Mechanics (Verified)
- FLOOR: Standard walkable ground.
- WATER: Traversable only while Surfing (requires HM03).
- BUOY: Impassable water obstacle.
- WALL: Impassable obstacle.
- FLOOR_UP_WALL / LEDGE_HOP_DOWN: In Cianwood, these function as standard WALL tiles from the north (cannot jump down).
- Interaction: To Surf, face WATER from an adjacent FLOOR tile and press A. Stepping onto FLOOR from WATER automatically ends Surfing.

# Lessons Learned
- Cianwood's ledges do not allow jumping from the north.
- Internal walls at X=9, 12, 17 divide the city into vertical strips.
- Buoy lines block the eastern sea. Use Row 19/18 and Row 30 for horizontal movement.
- Do not trust pathfinders that assume 'unseen' tiles are passable. Reveal tiles manually.