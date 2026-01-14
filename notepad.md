# Tile Mechanics
- FLOOR: Standard walkable ground. Verified traversable.
- WATER: Traversable only while Surfing.
- WALL / BUOY: Impassable.
- FLOOR_UP_WALL: Impassable from the NORTH.
- LEDGE_HOP_DOWN: Impassable from the NORTH.
- HEADBUTT_TREE: Impassable.
- CUT_TREE: Impassable (becomes FLOOR when cut). Verified regrows on map exit.

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

# Systematic Search Plan (Route 42 Grove)
- HOW: Use `generate_sweep_path` tool to cover X=24-31, Y=13-17.
- Current Status: Sweeping row 15.
- Start Turn: 46896.

# Hypotheses & Tests
- Hypothesis 1: Trigger is a specific tile in the (26, 15) or (27, 15) grove.
    - Test: Walk onto (26, 15) and (27, 15).
    - Status: Ongoing (Attempt #1).
- Hypothesis 2: Trigger is near the middle Mt. Mortar entrance at (28, 9).
    - Test: Walk around (28, 9) and (28, 10).
    - Status: Pending.

# Failed Hypotheses
- "The Sea Loop" (Surfing around buoys): Denied. Buoy walls at Row 15 and Row 9 are too restrictive.
- "Sighting trigger at (26, 15) only": Denied (Initial pass at (26, 15) failed; requires systematic sweep).

# Lessons Learned
- Eusine battle confirms sighting completion.
- Buoy walls are highly restrictive; land routes often safer.
- Multimodal pathfinding fails on water-to-land transitions; use manual navigation or chunks.
- [Lesson] Always verify 'Surrounding tiles' in GameState before executing a manual movement sequence to avoid hitting obstacles like trees.