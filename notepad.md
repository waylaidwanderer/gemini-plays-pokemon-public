# Strategy: Suicune Hunt (Johto)
- Status: Suicune confirmed on Route 42 via Pokedex (Turn 21433).
- Strategy: Systematic floor sweep of the central island (X=24-30, Y=14-17) to trigger Sighting 3 flee event.
- Progress:
    - Island sweep started: Turn 21455 (Thursday, Dec 25, 2025).
    - Current Task: Verify blinking location in Pokedex. Sweep of floor tiles complete (Turn 21492).
- Lessons Learned:
    - Pokedex: Alphabetical (A-Z). Suicune follows Sudowoodo.
    - Scripted: Sighting sequence is fixed. Pokedex AREA map tracks current scripted location.
    - Animation: Sprite flees with a visible jump. If no jump seen, event is not complete.
    - Trigger: Suicune on Route 42 is a tile trigger on the southern Apricorn island.

# Tile Mechanics
- FLOOR: Traversable. Standard ground. [Verified]
- WALL: Impassable. [Verified]
- WATER: Traversable via Surf. [Verified]
- HEADBUTT_TREE: Impassable. Interaction triggers Headbutt. [Verified]
- CUT_TREE: Impassable. Interaction triggers Cut. [Verified]
- FRUIT_TREE: Impassable. Interaction gives Apricorn/Berry. [Verified]
- TALL_GRASS: Traversable. Wild encounters. [Verified]
- CAVE: Warp. [Verified]
- WARP_CARPET_LEFT: Warp. [Verified]
- WARP_CARPET_DOWN: Warp. [Verified]
- LADDER: Warp. [Verified]
- FLOOR_UP_WALL: Impassable. Ledge that can be jumped over from above. [Verified]