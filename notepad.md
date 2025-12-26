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
- WARP_CARPET_RIGHT: Traversable. Transition between maps/gatehouses. [Verified]
- WARP_CARPET_LEFT: Traversable. Transition between maps/gatehouses. [Verified]

# General Lessons
- Scripted Events: Sightings are sprite-based. If a sprite is missing, the event cannot trigger. [Turn 22217]
- Ecruteak Geography: NW = Burned Tower; NE = Barrier Station (leads to Tin Tower). Wise Trio is in Barrier Station (Map 4_2) or Tin Tower 1F. [Turn 22217]
- Root Hypothesis Failure: If a scripted sequence stalls (e.g., Suicune sightings), the assumed order or prerequisite might be wrong. Pivot to the next major hurdle (Wise Trio battle) instead of looping. [Turn 22321]

# Strategy: Suicune Hunt (Crystal Version)
- Sighting 1: Burned Tower (Complete)
- Sighting 2: Cianwood City (Complete)
    - Note: Observed Suicune at (10, 14) and defeated Eusine. [Verified]
- Sighting 3 (Current Goal): Route 42 Central Island.
    - How: Surf from the mainland (e.g., from (13, 8)) to the island. Use Cut at (24, 13) to enter the grove. Approach the three Apricorn trees. Suicune should appear as a sprite and flee.
- Sighting 4: Route 36 (Sudowoodo junction).
    - How: Approach the junction at (35, 9) after the Route 42 sighting.
- Sighting 5: Tin Tower 1F (Final Battle).
    - Requirement: Must defeat the Wise Trio (Sages) in the Barrier Station/Tin Tower 1F. They appear after Sightings 3 and 4 are complete.

# Suicune Battle Strategy (Crystal)
- Location: Tin Tower 1F.
- Status: Stationary encounter. Level 40.
- Strategy: induced sleep (KIMCHI/XENON), weaken (GNEISS/Calcifer). Mean Look NOT required.
- Prerequisite: Defeat Wise Trio.

# PC Storage Inventory
- Box 1: RICOTTA (RATICATE), CINNABAR (GOLDEEN), VORTEX (POLIWAG), INTERCEPT (YANMA), ROCKY (ONIX), EGG (CLEFFA), XFDW (MEOWTH), FRITTATA (TOGEPI), SHUCKIE (SHUCKLE), Blarney (SUDOWOODO).

# Timestamps
- Suicune Hunt (Route 42/36 Phase): Started Turn 22256 (Dec 26, 2:00 AM). Stalled at Turn 22315. Pivoting to Wise Trio/Tin Tower.