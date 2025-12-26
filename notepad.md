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
- Suicune Sequence Linearity: Suicune follows a strict order: Burned Tower -> Cianwood City -> Route 42 -> Route 36 -> Tin Tower. Sightings cannot be skipped.
- Event Triggers: Scripted encounters are sprite-based. If the sprite is missing, the event cannot trigger.
- Troubleshooting Stalls: If a scripted event doesn't trigger, re-verify the previous step's completion and ensure all trigger tiles (often directional) are crossed.
- Map Marker Integrity: Markers linked to object IDs will move with those objects. Use static markers for fixed locations like trees.

# Strategy: Suicune Hunt (Crystal Version)
- Sighting 1: Burned Tower (Complete)
- Sighting 2: Cianwood City (Complete)
    - Note: Observed Suicune at (10, 14) and defeated Eusine. [Verified]
- Sighting 3 (Goal): Route 42 Central Island.
    - How: Surf from the mainland (e.g., from (13, 8)) to the island. Use Cut at (24, 13) to enter the grove. Approach the three Apricorn trees. Suicune should appear as a sprite and flee.
- Sighting 4: Route 36 (Sudowoodo junction).
    - How: Approach the junction at (35, 9) after the Route 42 sighting.
- Sighting 5: Tin Tower 1F (Final Battle).
    - Requirement: Must defeat the Wise Trio (Sages) in the Barrier Station/Tin Tower 1F. They appear after Sightings 3 and 4 are complete.

# Suicune Battle Strategy (Crystal)
- Location: Tin Tower 1F.
- Status: Stationary encounter. Level 40.
- Strategy: induce sleep (KIMCHI/XENON), weaken (GNEISS/Calcifer). Mean Look NOT required.
- Prerequisite: Defeat Wise Trio.

# PC Storage Inventory
- Box 1: RICOTTA (RATICATE), CINNABAR (GOLDEEN), VORTEX (POLIWAG), INTERCEPT (YANMA), ROCKY (ONIX), EGG (CLEFFA), XFDW (MEOWTH), FRITTATA (TOGEPI), SHUCKIE (SHUCKLE), Blarney (SUDOWOODO).

# Timestamps
- Suicune Hunt (Route 42/36 Phase): Started Turn 22256 (Dec 26, 2:00 AM). Current Turn: 22372. Goal: Trigger sighting 3.