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
- Sighting 3 (Hypothesis): Route 42 Central Island. [Turn 21977]
  - Prerequisite: If Clear Bell is held, must defeat Wise Trio in Ecruteak first.
- Sighting 4 (Hypothesis): Route 36 (Sudowoodo junction).
- Sighting 5 (Hypothesis): Tin Tower 1F (Final Battle).
  - Prerequisite: Clear Bell (Obtained).
  - Prerequisite: All 4 scripted sightings must be triggered.
- Note: Sequence is Burned Tower -> Cianwood -> Route 42 -> Route 36 -> Tin Tower.

# Lessons Learned
- PC Mechanics: "MOVE PKMN W/O MAIL" is best for inventory checks.
- Interaction: Never mix directional inputs and action buttons in the same turn.
- Suicune Sequence: Crystal sequence is fixed: Burned Tower -> Cianwood -> Route 42 -> Route 36 -> Tin Tower.
- Navigation: If stuck in a menu loop, verify cursor position and manual button indices. Fixed menu_navigator_v3_fixed_borders (Turn 21992, 22008).
- [Turn 21988] Tool Failure: menu_navigator_v3_fixed_borders overshot POKEMON and selected GEM because it matched status text at the bottom. Fixed in Turn 22008.

# Tasks & Progress
- Badges Obtained: Zephyr, Hive, Plain, Fog, Mineral, Storm, Glacier. (7/8 Johto Badges).

# PC Storage Inventory
- Box 1: RICOTTA (RATICATE), CINNABAR (GOLDEEN), VORTEX (POLIWAG), INTERCEPT (YANMA), ROCKY (ONIX), EGG (CLEFFA), XFDW (MEOWTH), FRITTATA (TOGEPI), SHUCKIE (SHUCKLE), Blarney (SUDOWOODO).
- Observation: Tin Tower 1F Sages (11, 11), (14, 6), and (5, 9) provided lore but no battles. [Turn 22026]
- Strategy: Re-check Wise Trio room (4_2) and gatehouse Sage (4_1) after entering Tin Tower. [Turn 22026]
- Observation: Wise Trio Room (4_2) appears empty at Turn 22030. [Turn 22030]
- Observation: Tin Tower 1F Sage (5, 9) said: "Could it mean the legendary POKéMON are testing us humans?" [Turn 22023]
- Hypothesis: The Wise Trio might appear in 4_2 after a specific trigger, or the battle occurs elsewhere. [Turn 22030]