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

# Strategy: Suicune Hunt (Johto)
- Sighting 1: Burned Tower (Complete)
- Sighting 2: Cianwood (Complete)
- Sighting 3: Route 42 (Pending). Approach Suicune on the center island (requires Surf and Cut).
- Sighting 4: Route 36 (Next). Triggered at the Sudowoodo junction after Route 42.
- Sighting 5: Fuchsia City (Kanto).
- Final Battle: Tin Tower 1F (Requires Clear Bell).
- Primary Goal HOW: Complete all 5 sightings. Enter Tin Tower 1F. Use Xenon (Gastly) for Hypnosis and Mean Look. Use Ultra/Great Balls.
- Hypothesis: The Pokedex status "Route 38" refers to Raikou/Entei, not Suicune.

# Week Siblings Strategy
- Arthur (Thursday): Route 36. Provides Hard Stone.
- Arthur Note: If dialogue intro loops, the flag is likely set. Check PC and party held items.
- Lesson: Moving NPCs like Arthur can be difficult to interact with. Use `stun_npc` to freeze them in place.
- Lesson: Never mix directional inputs and the A button in the same turn; the system will strip the A button to prevent errors. Move first, then interact.

# Gym Progress
- Rising Badge (Clair): Next Gym Badge required. Need to travel to Blackthorn City.
- Badges Obtained: Zephyr, Hive, Plain, Fog, Mineral, Storm, Glacier. (7/8 Johto Badges).

# PC Storage Inventory
- Box 1: RICOTTA (Raticate), CINNABAR (Goldeen), VORTEX (Poliwag), INTERCEPT (Yanma), ROCKY (Onix), EGG (Cleffa), XFDW (Meowth), FRITTATA (Togepi), SHUCKIE (Shuckle), Blarney (Sudowoodo).
- PC Check: Item Storage and Box 1 (all 10 Pokémon) confirmed empty of items (Turns 21844-21861).
- Party Check: XENON, ICARUS, and GNEISS have item icons in the party menu. Checking Gneiss first (Turn 21867).
- Suicune Strategy: Proceed to Route 42 center island. Use Surf and Cut.
- Lesson: PC "MOVE PKMN W/O MAIL" is the most reliable way to check stored items.
- Lesson: Menu navigation tools must handle border characters (│, ┌, └) correctly. Fix applied in menu_navigator_v2_fixed_v2.