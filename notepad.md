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
    3. Route 42 (Mahogany side) - PENDING (Started Turn 46896)
    4. Kanto Route 25 (Cerulean Cape) - PENDING
- Strategy: Visit sighting spots in order. Then Tin Tower.
- Items: Clear Bell (HAVE IT).

# Map Insights (Route 42)
- Middle grove with Apricorns requires Cut at (24, 13).
- Island is reachable via western pond (Surf) or Mt. Mortar middle entrance.
- Entrances at (10, 5), (28, 9), (46, 7).

# Hypotheses & Tests
- Hypothesis 1: Trigger is a specific tile in the (26, 15) or (27, 15) grove.
    - Test: Walk onto all floor tiles in the grove (X=24-31, Y=13-17).
    - Status: FAILED (Walked all tiles as of Turn 46953, no sighting triggered).
- Hypothesis 2: Trigger is on the upper island near the cave entrance or eastern pond.
    - Test: Walk all floor tiles from Y=4 to Y=12.
    - Status: PARTIALLY COMPLETED.
- Hypothesis 3: Suicune appears only when entering the map from a specific side or after re-entering.
    - Test: Exit to Mahogany, then re-enter and approach the grove.
    - Status: FAILED (Re-entered from Mahogany at Turn 46966, no sighting).
- Hypothesis 5: Suicune sighting on Route 42 is triggered by approaching from the west (Ecruteak side).
    - Test: Fly to Ecruteak and enter Route 42 from the west.
    - Status: Ongoing (Landed in Ecruteak).

# Failed Hypotheses
- "Mow the lawn" in grove: FAILED (60+ turns, all tiles stepped on). Suicune is likely a static sprite that isn't currently present.
- "Sighting trigger at (28, 15)": FAILED (Stepped on it at Turn 46953).
- "Re-entry from Mahogany": FAILED (Turn 46966).

# Lessons Learned
- Suicune in Route 42 is likely an overworld sprite; if it's not in the Map Objects list, the sighting event is not active.
- Map refreshes (entering/exiting) are essential when overworld events aren't triggering as expected.

# Map Insights (Mt. Mortar)
- B1F ladder at (19, 29) leads to 1FOutside (17, 29).
- B1F has an item ball at (21, 26).