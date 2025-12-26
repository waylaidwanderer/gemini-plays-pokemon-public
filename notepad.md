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
- Sighting 3 (Goal): Route 42 Central Island. Triggered by Surfing to the island with three Apricorn trees. [Next]
- Sighting 4: Route 36 (Sudowoodo junction).
- Sighting 5: Tin Tower 1F (Final Battle).
- Note: Sages in the gatehouse (4_1) are currently passive ("Please, do go on."). They likely only battle after sightings 3 and 4 are complete.
- Sequence: Burned Tower -> Cianwood -> Route 42 -> Route 36 -> Tin Tower.

# Lessons Learned
- PC Mechanics: "MOVE PKMN W/O MAIL" is best for inventory checks.
- Interaction: Never mix directional inputs and action buttons in the same turn.
- Suicune Sequence: Crystal sequence is fixed: Burned Tower -> Cianwood -> Route 42 -> Route 36 -> Tin Tower.
- Navigation: Use manual presses or a robust tool to avoid looping. Fixed menu_navigator_v3_fixed_borders (Turn 22008).
- Multi-map Navigation: find_path_v2 only works on the current map. Use manual planning for paths through warps.

# Tasks & Progress
- Goal: Trigger Suicune sighting on Route 42. [Start Turn 22061]
- Status: Searching for Suicune on Route 42. It hasn't appeared on the central island yet.
- Badges Obtained: Zephyr, Hive, Plain, Fog, Mineral, Storm, Glacier. (7/8 Johto Badges).

# PC Storage Inventory
- Box 1: RICOTTA (RATICATE), CINNABAR (GOLDEEN), VORTEX (POLIWAG), INTERCEPT (YANMA), ROCKY (ONIX), EGG (CLEFFA), XFDW (MEOWTH), FRITTATA (TOGEPI), SHUCKIE (SHUCKLE), Blarney (SUDOWOODO).