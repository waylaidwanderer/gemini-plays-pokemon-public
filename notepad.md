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
- Sighting 3: Route 42 Central Island. Suicune should flee when approached.
- Sighting 4: Route 36 (Sudowoodo junction).
- Sighting 5: Tin Tower 1F (Final Battle). Requires Clear Bell and defeating the Wise Trio.
- Sequence: Burned Tower -> Cianwood -> Route 42 -> Route 36 -> Tin Tower.
- Note: If Route 42 fails to trigger, check Route 36 or Tin Tower directly. Sages at Tin Tower Gatehouse (4_1) were passive at Turn 22052.

# Tested Hypotheses & Coordinates
- Route 42 Central Island: Explored thoroughly (Turns 22061-22112). Sighting did NOT trigger.
- Mt. Mortar Refresh: Entered/Exited to refresh map (Turn 22105). No change.

# Lessons Learned
- Suicune Sequence: Scripted sightings are NOT visible in the Pokedex.
- Verification: Always check "Map Objects On Screen" before asserting a sprite's presence. Avoid hallucinations.
- Stagnation: Pivot quickly if a trigger fails after 20+ turns of exploration.

# PC Storage Inventory
- Box 1: RICOTTA (RATICATE), CINNABAR (GOLDEEN), VORTEX (POLIWAG), INTERCEPT (YANMA), ROCKY (ONIX), EGG (CLEFFA), XFDW (MEOWTH), FRITTATA (TOGEPI), SHUCKIE (SHUCKLE), Blarney (SUDOWOODO).