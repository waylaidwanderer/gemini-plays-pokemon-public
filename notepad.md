# Tile Mechanics
- FLOOR: Standard walkable ground. Verified traversable.
- WATER: Traversable only while Surfing.
- WALL / BUOY: Impassable.
- FLOOR_UP_WALL: Impassable from the NORTH.
- LEDGE_HOP_DOWN: Impassable from the NORTH.
- HEADBUTT_TREE: Impassable.
- CUT_TREE: Impassable (becomes FLOOR when cut). Verified regrows on map exit.
- CAVE / WARP_CARPET: Warp to another map (e.g. Mt. Mortar, Gatehouse).

# Suicune Quest
- Objective: Catch Suicune.
- Sighting Progress:
    1. Burned Tower (DONE)
    2. Cianwood City (DONE - Eusine defeated at Turn 41111)
    3. Route 42 (Mahogany side) - PENDING (Attempt started Turn 46896)
    4. Kanto Route 25 (Cerulean Cape) - PENDING
- Strategy: Visit sighting spots in order. Then Tin Tower.
- Items: Clear Bell (HAVE IT).

# Active Hypotheses
- Hypothesis 5: Suicune sighting on Route 42 is triggered by approaching from the west (Ecruteak side).
    - Test: Enter Route 42 from Ecruteak and approach the grove.
    - Status: Ongoing.

# Verified Failures
- "Mow the lawn" in grove: FAILED (60+ turns, 100% tile coverage in grove). Suicune is not a hidden trigger tile.
- "Sighting trigger at (28, 15)": FAILED (Stepped on it at Turn 46953).
- "Re-entry from Mahogany": FAILED (Turn 46966, re-approached grove from east).
- "Eusine in Ecruteak Center": FAILED (Turn 46981, not present).

# Lessons Learned
- Suicune sightings are overworld sprite encounters, not hidden tile triggers.
- If the sprite is missing from the Map Objects list, the sighting event is not active.
- Map refreshes and directional approaches are the last resort before abandoning a sighting.

# Map Insights
- Route 42: Middle grove with Apricorns requires Cut at (24, 13).
- Mt. Mortar: B1F ladder at (19, 29) leads to 1FOutside (17, 29). B1F has an item ball at (21, 26).
- Ecruteak: Gatehouse to Route 42 is at (35, 27).