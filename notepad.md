# Global Tile Mechanics
- FLOOR: Traversable. Standard ground. [Verified]
- WALL: Impassable. Rock faces and boundaries. [Verified]
- WATER: Traversable via Surf. [Verified]
- HEADBUTT_TREE: Impassable. Interaction only. [Verified]
- CUT_TREE: Impassable. Can be removed with Cut. [Verified]
- FLOOR_UP_WALL: Impassable ledge (one-way down). [Verified]
- CAVE: Traversable. Warp point leading to interiors. [Verified]
- WARP_CARPET: Traversable. Transition between maps/gatehouses. [Verified]
- TALL_GRASS: Traversable. Wild Pokémon encounters. [Verified]
- PC: Standing below (facing up) and pressing A allows access to item and Pokémon storage. [Verified]

# Strategy: Suicune Hunt (Crystal Version)
- Sighting 1: Burned Tower (Complete)
- Sighting 2: Cianwood City (Complete)
- Sighting 3 (Goal): Route 42 Central Island. Suicune should be visible as a sprite and flee when approached.
- Sighting 4: Route 36 (Sudowoodo junction).
- Sighting 5: Tin Tower 1F (Final Battle). Requires Clear Bell and defeating the Wise Trio.
- Sequence: Burned Tower -> Cianwood -> Route 42 -> Route 36 -> Tin Tower.
- Note: If Route 42 sighting fails to trigger, check Route 36 or Tin Tower directly.

# Lessons Learned
- Suicune Sequence: Scripted sightings are NOT visible in the Pokedex.
- Verification: Always check "Map Objects On Screen" before asserting a sprite's presence.
- Stagnation: If an area fails to trigger an event after thorough exploration, pivot to the next likely location.

# PC Storage Inventory
- Box 1: RICOTTA (RATICATE), CINNABAR (GOLDEEN), VORTEX (POLIWAG), INTERCEPT (YANMA), ROCKY (ONIX), EGG (CLEFFA), XFDW (MEOWTH), FRITTATA (TOGEPI), SHUCKIE (SHUCKLE), Blarney (SUDOWOODO).