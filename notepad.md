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
- Status: 16 Badges, Red Defeated, Clear Bell in inventory.
- Start Turn (Route 42 Grove): 47288.
- Sighting Progress:
    1. Burned Tower (DONE)
    2. Cianwood City (VERIFYING - North Beach)
    3. Route 42 (Middle Grove) - TRIGGER FAILED (Swept all tiles, no event).
    4. Kanto Route 14 (East of Fuchsia) - LOCKED.
    5. Kanto Route 25 (Cerulean Cape) - LOCKED.
- Strategy & Lessons:
    - Visit sighting spots in order. Quest is strictly linear.
    - Lesson: Suicune is a static land sprite; water sweeps are ineffective.
    - Lesson: Missing a Johto sighting (e.g., Route 42) blocks all subsequent sightings in Kanto and the Tin Tower event.
- Backtracking Plan (HOW):
    - Fly to Cianwood and check the north beach.
    - If Suicune is there, trigger the event and battle Eusine.
    - Then return to Route 42 grove.
- Hypothesis Log (Route 42):
    - H1: Trigger is a specific tile within the grove boundary. (Tested with 'suicune_sweep_v2', Failed Turn 47324).
    - H2: Prerequisite (Cianwood Sighting) is incomplete. (Testing now).