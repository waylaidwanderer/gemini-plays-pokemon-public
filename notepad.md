# Suicune Quest
- Objective: Trigger sighting in Cianwood City at the northern shore.
- Strategy: The Secret Land Path (Verified)
    1. Land at (19, 30).
    2. Walk West to (12, 30), then South to (12, 34).
    3. Walk West to (10, 34), then North to (10, 33).
    4. Walk West to (8, 33), then South to (8, 35).
    5. Walk West to the West Coast corridor at (2, 35).
    6. Walk North along X=2 to Row 4.
    7. Walk East to (7, 4) to trigger the sighting.
- Note: This path uses confirmed gaps in the city's internal walls (Row 33, 34, 35) and avoids all ledges. X=2 is the primary north-south thoroughfare.
- Suicune sighting count = 1.

# Tile Mechanics (Verified)
- FLOOR: Standard walkable ground.
- WATER: Traversable only while Surfing (requires HM03).
- BUOY: Impassable water obstacle.
- WALL: Impassable obstacle.
- FLOOR_UP_WALL / LEDGE_HOP_DOWN: In Cianwood, these function as standard WALL tiles from the north (cannot jump down).
- Interaction: To Surf, face WATER from an adjacent FLOOR tile and press A. Stepping onto FLOOR from WATER automatically ends Surfing.

# Lessons Learned
- Cianwood's ledges are impassable from the north.
- Internal walls divide the city into strips. Gaps exist at Row 33 (X=9), Row 34 (X=11, X=3), and Row 35 (X=7, X=5).
- The West Coast corridor (X=2) is the only clear path to the northern shore.
- Do not trust pathfinders that assume 'unseen' tiles are passable. Reveal tiles manually.