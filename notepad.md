# Tile Mechanics
- FLOOR: Standard walkable ground. Verified traversable.
- WATER: Traversable only while Surfing. 
- WALL / BUOY: Impassable.
- FLOOR_UP_WALL: Impassable from the NORTH.
- LEDGE_HOP_DOWN: Impassable from the NORTH.
- HEADBUTT_TREE: Impassable.
- CUT_TREE: Impassable (becomes FLOOR when cut). Verified regrows on map exit.
- CAVE / WARP_CARPET: Warp to another map (e.g. Mt. Mortar, Gatehouse).
- COUNTER: Impassable. Used to interact with NPCs from an adjacent tile.

# Suicune Quest
- Status: 16 Badges, Red Defeated, Clear Bell in inventory.
- Timestamps:
    - Tin Tower Investigation Started: Turn #47028
    - Route 42 Re-investigation Started: Turn #47046
- Sighting Progress:
    1. Burned Tower (DONE)
    2. Cianwood City (DONE - Eusine defeated)
    3. Route 42 (Middle Grove) - PENDING (MANDATORY).
    4. Kanto Route 14 (East of Fuchsia) - PENDING
    5. Kanto Route 25 (Cerulean Cape) - PENDING
- Strategy: Visit sighting spots in order. The Wise Trio in Ecruteak are non-interactable until Route 42 is cleared.
- Expert Advice: Suicune must be found in the grove near the middle of Route 42 (requires Cut or Surf).

## Route 42 Hypothesis Testing
- Hypothesis 1: Sighting triggers by walking on every tile in the grove.
    - Test: "Mowed the lawn" (Turns 46897-47000).
    - Result: FAILED (from Mahogany side).
- Hypothesis 2: Sighting triggers by entering from Ecruteak instead of Mahogany.
    - Test: Entered from Ecruteak (Turn 47056).
    - Result: FAILED (Swept floor: Turns 47072-47078).
- Hypothesis 3: Sighting triggers by standing at the water's edge *inside* the grove.
    - Target Tiles: (24, 15) through (30, 15).
    - Result: FAILED (Swept on Turn 47077).
- Hypothesis 4: Suicune is in the water.
    - Result: FAILED (Expert and Overwatch confirm it is on land).
- Hypothesis 5: Sighting triggers on the northern land strip or unvisited grove tiles.
    - Target Area: Row 11 (20, 11 to 33, 11) and Row 12 inside grove.
    - Result: PENDING.

# Verified Failures (Route 42)
- "Sighting trigger at (28, 15)": FAILED.
- "Re-entry from Mt. Mortar": FAILED (Turn 46939).
- "Eusine in Ecruteak Center": FAILED (Turn 46981).
- Wise Trio Interaction (Ecruteak): FAILED (Turn 47043).

# Map Insights
- Route 42: Middle grove with Apricorns requires Cut at (24, 13).
- Mt. Mortar: B1F ladder at (19, 29) leads to 1FOutside (17, 29). B1F has an item ball at (21, 26).
- Ecruteak: Gatehouse to Route 42 is at (35, 27).
- Tin Tower: Located in Ecruteak City. Requires Clear Bell.
- Ecruteak Courtyard (Tin Tower grounds): Enclosed area reachable only through the entrance building at (18, 11). Warps at (20, 2) and (20, 3) lead back inside. No direct path to the rest of the city.