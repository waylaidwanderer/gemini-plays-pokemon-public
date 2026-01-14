# Tile Mechanics
- FLOOR: Standard walkable ground. Verified traversable.
- TALL_GRASS: Walkable, may trigger wild battles. Verified.
- WATER: Traversable only while Surfing. 
- WALL / BUOY: Impassable.
- FLOOR_UP_WALL: Impassable from the NORTH.
- LEDGE_HOP_DOWN: Impassable from the NORTH.
- HEADBUTT_TREE: Impassable.
- CUT_TREE: Impassable (becomes FLOOR when cut). Verified regrows on map exit.
- FRUIT_TREE: Impassable. Interact to obtain Apricorns. Verified.
- CAVE / WARP_CARPET: Warp to another map (e.g. Mt. Mortar, Gatehouse).
- COUNTER: Impassable. Used to interact with NPCs from an adjacent tile.

# Suicune Quest
- Status: 16 Badges, Clear Bell in inventory.
- Start Turn (Route 42 Grove): 47288.
- Sighting Progress:
    1. Burned Tower (DONE)
    2. Cianwood City (DONE - Eusine defeated)
    3. Route 42 (Middle Grove) - IN PROGRESS.
    4. Kanto Route 14 (East of Fuchsia) - LOCKED.
    5. Kanto Route 25 (Cerulean Cape) - LOCKED.
- Strategy & Lessons:
    - Visit sighting spots in order. Quest is strictly linear.
    - Lesson: Suicune is a static land sprite; water sweeps are ineffective.
    - Lesson: Missing a Johto sighting (e.g., Route 42) blocks all subsequent sightings in Kanto and the Tin Tower event.
- Backtracking Plan (HOW):
    - Head East to the grove near the 3 Apricorn trees on Route 42.
    - Ensure KIMCHI has Cut for the tree at (24, 13).
    - Trigger the sighting in the grove using 'suicune_sweep' tool.
    - Return to Kanto (Fuchsia City) after Johto sighting.