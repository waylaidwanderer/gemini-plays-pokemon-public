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
    3. Route 42 (Mahogany side) - PENDING (Started Turn 46896, Attempt #1)
    4. Kanto Route 25 (Cerulean Cape) - PENDING
- Strategy: Visit sighting spots in order. Then Tin Tower.
- Items: Clear Bell (HAVE IT).

# Map Insights (Route 42)
- Middle grove with Apricorns requires Cut at (24, 13).
- Island is reachable via western pond (Surf) or Mt. Mortar middle entrance.
- Entrances at (10, 5), (28, 9), (46, 7).

# Systematic Search Plan (Route 42 Island)
- Phase 1: Grove (X=24-31, Y=13-17). Status: COMPLETED (No sighting).
- Phase 2: Upper Island (X=20-33, Y=4-12). Status: STARTING.
- Start Turn: 46896.

# Hypotheses & Tests
- Hypothesis 1: Trigger is a specific tile in the (26, 15) or (27, 15) grove.
    - Test: Walk onto (26, 15) and (27, 15).
    - Status: FAILED (Walked all tiles in grove).
- Hypothesis 2: Trigger is on the upper island near the cave entrance or eastern pond.
    - Test: Walk all floor tiles from Y=4 to Y=12.
    - Status: Pending.

# Failed Hypotheses
- "The Sea Loop" (Surfing around buoys): Denied. Buoy walls at Row 15 and Row 9 are too restrictive.
- "Sighting trigger at (26, 15) only": Denied (Initial pass at (26, 15) failed; requires systematic sweep).

# Lessons Learned
- Eusine battle confirms sighting completion.
- Buoy walls are highly restrictive; land routes often safer.
- Multimodal pathfinding fails on water-to-land transitions; use manual navigation or chunks.
- [Lesson] Always verify 'Surrounding tiles' in GameState before executing a manual movement sequence to avoid hitting obstacles like trees.

# Map Insights (Mt. Mortar)
- B1F ladder at (19, 29) leads to 1FOutside (17, 29).
- B1F has an item ball at (21, 26).