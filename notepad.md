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
- Sighting 3: Route 42 Central Island. [Start Turn 21950]
  - HOW: Step on the trigger tiles in the grove (approx 26, 14).
  - Note: Harvesting Apricorns does NOT trigger the sighting. Must step on the specific tile.
- Sighting 4: Tin Tower 1F (Final Battle).
  - Prerequisite: Clear Bell (Obtained).
  - Prerequisite: All 3 scripted sightings (Burned Tower, Cianwood, Route 42) must be triggered.
- Note: Crystal sequence is Burned Tower -> Cianwood -> Route 42 -> Tin Tower. No sightings on Route 36 or Fuchsia City.

# Gym Progress
- Rising Badge (Clair): Next Gym Badge required. Need to travel to Blackthorn City.
- Badges Obtained: Zephyr, Hive, Plain, Fog, Mineral, Storm, Glacier. (7/8 Johto Badges).

# PC Storage Inventory
- Box 1: RICOTTA (Raticate), CINNABAR (Goldeen), VORTEX (Poliwag), INTERCEPT (Yanma), ROCKY (Onix), EGG (Cleffa), XFDW (Meowth), FRITTATA (Togepi), SHUCKIE (Shuckle), Blarney (Sudowoodo).

# NPC & Interaction Lessons
- PC "MOVE PKMN W/O MAIL" is the most reliable way to check stored items.
- Check held items if an NPC dialogue loops or item seems missing.
- Menu Navigation: Use menu_navigator_v3_fixed_borders to handle borders.
- Lesson: Moving NPCs like Arthur can be difficult to interact with. Use `stun_npc` to freeze them in place.
- Lesson: Never mix directional inputs and the A button in the same turn; the system will strip the A button to prevent errors. Move first, then interact.

# Error Analysis Log
- [Turn 21931] Mistake: Assumed a Suicune sighting existed on Route 36. Root Cause: Confused Crystal mechanics with other games. Correction: Suicune Tracker confirmed sequence is Burned Tower -> Cianwood -> Route 42 -> Tin Tower.
- [Turn 21931] Mistake: Assumed harvesting Apricorns on Route 42 triggered Sighting 3. Root Cause: Sprite didn't appear but I assumed it happened off-screen. Correction: Must return and step on the trigger tile.
- [Turn 21957] Mistake: Mixed directional and action buttons (Down, A, A). Result: Only Down was executed. Correction: Move first, then perform action.