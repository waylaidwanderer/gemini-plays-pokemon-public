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
- Hypothesis: The "Wise Trio" are the Sages in the Tin Tower gatehouse (4_1) at (4, 6), (1, 1), and (1, 15). Defeating them is required to trigger Sighting 3 if the Clear Bell is held. [Turn 22040]
- Sighting 3 (Goal): Route 42 Central Island. Triggered after defeating the Wise Trio.
- Sighting 4 (Hypothesis): Route 36 (Sudowoodo junction).
- Sighting 5 (Hypothesis): Tin Tower 1F (Final Battle).
- Note: Sequence is Burned Tower -> Cianwood -> Route 42 -> Route 36 -> Tin Tower.

# Lessons Learned
- PC Mechanics: "MOVE PKMN W/O MAIL" is best for inventory checks.
- Interaction: Never mix directional inputs and action buttons in the same turn.
- Suicune Sequence: Crystal sequence is fixed: Burned Tower -> Cianwood -> Route 42 -> Route 36 -> Tin Tower.
- Navigation: Use manual presses or a robust tool to avoid looping. Fixed menu_navigator_v3_fixed_borders (Turn 22008).
- Multi-map Navigation: find_path_v2 only works on the current map. Use manual planning for paths through warps.

# Tasks & Progress
- Goal: Defeat the Wise Trio Sages in the Tin Tower gatehouse (4_1). [Start Turn 22040, Timestamp: Friday, Dec 26, 2025 at 12:35 AM]
- Badges Obtained: Zephyr, Hive, Plain, Fog, Mineral, Storm, Glacier. (7/8 Johto Badges).

# PC Storage Inventory
- Box 1: RICOTTA (RATICATE), CINNABAR (GOLDEEN), VORTEX (POLIWAG), INTERCEPT (YANMA), ROCKY (ONIX), EGG (CLEFFA), XFDW (MEOWTH), FRITTATA (TOGEPI), SHUCKIE (SHUCKLE), Blarney (SUDOWOODO).
- Observation: Tin Tower 1F Sages provided lore but no battles. [Turn 22026]
- Observation: Wise Trio Room (4_2) is empty. [Turn 22030]
- Discovery: Three Sages found in gatehouse (4_1) at (4, 6), (1, 1), and (1, 15). Only (4, 6) has been talked to. [Turn 22040]