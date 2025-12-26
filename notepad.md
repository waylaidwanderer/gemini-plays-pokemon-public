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
- Prerequisite: Defeat Wise Trio in Ecruteak City (Required because Clear Bell is in bag). [Turn 21985]
- Sighting 3: Route 42 Central Island grove.
  - HOW: Step on trigger tiles (approx 26, 14) AFTER defeating Wise Trio.
- Sighting 4: Route 36 (Sudowoodo junction). [Verified mandatory by Critique Turn #21960]
  - HOW: Approach the junction after Sighting 3.
- Sighting 5: Tin Tower 1F (Final Battle).
  - Prerequisite: Clear Bell (Obtained).
  - Prerequisite: All 4 scripted sightings must be triggered.
- Note: Sequence is Burned Tower -> Cianwood -> Route 42 -> Route 36 -> Tin Tower. Fuchsia City and Kanto routes are NOT in Crystal's sequence.

# Gym Progress
- Rising Badge (Clair): Next Gym Badge required. Travel to Blackthorn City.
- Badges Obtained: Zephyr, Hive, Plain, Fog, Mineral, Storm, Glacier. (7/8 Johto Badges).

# PC Storage Inventory
- Box 1: RICOTTA (RATICATE), CINNABAR (GOLDEEN), VORTEX (POLIWAG), INTERCEPT (YANMA), ROCKY (ONIX), EGG (CLEFFA), XFDW (MEOWTH), FRITTATA (TOGEPI), SHUCKIE (SHUCKLE), Blarney (SUDOWOODO).

# NPC & Interaction Lessons
- PC "MOVE PKMN W/O MAIL" is the most reliable way to check stored items.
- Menu Navigation: Use menu_navigator_v3_fixed_borders to handle borders.
- Lesson: Moving NPCs like Arthur can be difficult to interact with. Use `stun_npc` to freeze them in place.
- Lesson: Never mix directional inputs and the A button in the same turn.

# Error Analysis Log
- [Turn 21931] Mistake: Assumed Suicune sighting existed on Route 36 before 42. Correction: Sequence is 42 then 36. [Turn 21973]
- [Turn 21957] Mistake: Mixed directional and action buttons. Result: Action stripped.
- [Turn 21976] Mystery: Suicune not appearing on Route 42 despite prerequisites. Troubleshooting: NPC Troubleshooter confirmed Wise Trio must be defeated first when Clear Bell is held. [Turn 21985]