# Tile Mechanics
- FLOOR: Standard walkable ground. Verified traversable.
- TALL_GRASS: Walkable, may trigger wild battles. Verified.
- WATER: Traversable only while Surfing. 
- WALL / BUOY: Impassable.
- FLOOR_UP_WALL: Impassable from the NORTH.
- LEDGE_HOP_DOWN: Impassable from the NORTH.
- HEADBUTT_TREE: Impassable.
- CUT_TREE: Impassable (becomes FLOOR when cut). Verified regrows on map exit.
- CAVE / WARP_CARPET: Warp to another map (e.g. Mt. Mortar, Gatehouse).
- COUNTER: Impassable. Used to interact with NPCs from an adjacent tile.

# Type Effectiveness (Verified)
- Ghost -> Normal: Immune (Night Shade, Confuse Ray).
- Psychic -> Normal: Effective (Dream Eater). *Note: Hypnosis (Status) missed Aipom on Turn 47189 due to Sand-Attack reducing accuracy; Psychic moves hit Normal types normally.*

# Suicune Quest
- Status: 16 Badges, Red Defeated, Clear Bell in inventory.
- Sighting Progress:
    1. Burned Tower (DONE)
    2. Cianwood City (DONE - Eusine defeated)
    3. Route 42 (Middle Grove) - IN PROGRESS (Searching at (28, 15)).
    4. Kanto Route 14 (East of Fuchsia) - LOCKED (Requires Route 42 sighting).
    5. Kanto Route 25 (Cerulean Cape) - LOCKED (Requires Route 42 sighting).
- Strategy & Lessons:
    - Visit sighting spots in order. Quest is strictly linear.
    - Lesson: Suicune is a static land sprite; water sweeps are ineffective.
    - Lesson: Missing a Johto sighting (e.g., Route 42) blocks all subsequent sightings in Kanto and the Tin Tower event.
- Backtracking Plan (HOW):
    - Head East to the grove near the 3 Apricorn trees on Route 42.
    - Ensure KIMCHI has Cut for the tree at (24, 13).
    - Approach the grove center to trigger Suicune.
    - Return to Kanto (Fuchsia City) after Johto sighting.

# PC Storage (Box 1)
- LARVITAR, SCYTHER, SEEL, MANTINE, KRABBY x2, TENTACOOL, DRATINI, SPINARAK, POLIWAG.
- Suicune Grove Search (Route 42):
    - Attempt 1: Walked around (28, 15), (27, 15), (25, 14), (30, 17). No trigger.
    - Attempt 2: Systematically walking Row 15 (26, 15 to 30, 15) and Row 17 (26, 17 to 30, 17).
    - Hypothesis: Trigger tile is likely (28, 15) or adjacent, approaching the center tree.
    - Result: Pending.