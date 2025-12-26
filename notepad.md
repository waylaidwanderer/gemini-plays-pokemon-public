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
- Sighting 3 (Hypothesis): Defeating the Wise Trio in Ecruteak City is required to trigger the Route 42 sighting if the Clear Bell is already in the inventory. [Turn 21977]
- Sighting 3 (Goal): Route 42 Central Island grove. 
  - HOW: Step on trigger tiles (approx 26, 14) AFTER defeating Wise Trio.
- Sighting 4 (Hypothesis): Route 36 (Sudowoodo junction).
  - HOW: Approach the junction after Sighting 3.
- Sighting 5 (Hypothesis): Tin Tower 1F (Final Battle).
  - Prerequisite: Clear Bell (Obtained).
  - Prerequisite: All 4 scripted sightings must be triggered.
- Note: Sequence is Burned Tower -> Cianwood -> Route 42 -> Route 36 -> Tin Tower.

# Lessons Learned
- PC Mechanics: "MOVE PKMN W/O MAIL" is best for inventory checks.
- Interaction: Never mix directional inputs and action buttons in the same turn.
- Suicune Sequence: Crystal sequence is fixed: Burned Tower -> Cianwood -> Route 42 -> Route 36 -> Tin Tower.
- Navigation: If stuck in a menu loop, verify cursor position and manual button indices.
- [Turn 21931] Mistake: Assumed Suicune sighting existed on Route 36 before 42. Correction: Sequence is 42 then 36. [Turn 21973]
- [Turn 21957] Mistake: Mixed directional and action buttons. Result: Action stripped.
- [Turn 21976] Mystery: Suicune not appearing on Route 42 despite prerequisites. Troubleshooting: NPC Troubleshooter confirmed Wise Trio must be defeated first when Clear Bell is held. [Turn 21985]
- [Turn 21991] Stagnation: Attempting to Fly to Ecruteak since Turn 21977 due to menu navigator failure. [Turn 21994]

# Tasks & Progress
- Goal: Travel to Ecruteak City to confront the Wise Trio. [Start Turn 21977, Timestamp: Friday, Dec 26, 2025 at 12:03 AM]
- Badges Obtained: Zephyr, Hive, Plain, Fog, Mineral, Storm, Glacier. (7/8 Johto Badges).

# PC Storage Inventory
- Box 1: RICOTTA (RATICATE), CINNABAR (GOLDEEN), VORTEX (POLIWAG), INTERCEPT (YANMA), ROCKY (ONIX), EGG (CLEFFA), XFDW (MEOWTH), FRITTATA (TOGEPI), SHUCKIE (SHUCKLE), Blarney (SUDOWOODO).