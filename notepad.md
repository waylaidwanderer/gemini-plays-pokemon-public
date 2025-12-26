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
- Scripted Events: Scripted encounters (like Suicune sightings) are based on visible sprites in the Map Objects list, not hidden tile triggers. If the sprite is not present, the event cannot be triggered by walking. [Turn 22217]
- Ecruteak Geography: There are two distinct buildings in northern Ecruteak. The NW building leads to the Burned Tower. The NE building (Barrier Station) leads to the Tin Tower. The Wise Trio appears in the Barrier Station after getting the Clear Bell. [Turn 22217]

# Strategy: Suicune Hunt (Crystal Version)
- Sighting 2 (Goal): Cianwood City.
    - How: Walk to the extreme northern edge of Cianwood City (above the Gym). Suicune will be standing there and flee when approached. [Hypothesis: This sighting was missed or didn't trigger correctly.]
- Sighting 3: Route 42 Central Island.
    - How: Surf from the mainland (e.g., from (13, 8)) to the island. Use Cut at (24, 13) to enter the grove. Approach the three Apricorn trees. Suicune will be standing near them and flee when approached.
- Sighting 4: Route 36 (Sudowoodo junction).
    - How: Approach the junction at (35, 9) after the Route 42 sighting. Suicune will appear and flee.
- Sighting 5: Tin Tower 1F (Final Battle).
    - How: Enter Tin Tower 1F via the NE Barrier Station in Ecruteak City. Requires Clear Bell and defeating the Wise Trio.
- Sequence: Burned Tower -> Cianwood -> Route 42 -> Route 36 -> Tin Tower.
- Note: Scripted sightings are sprite-based. If Suicune is not at Route 42, re-verify previous steps or check for missed triggers.
- Current Status: Island grove thoroughly explored. No Suicune sprite found. Checking Route 36 junction. [Turn 22308]

# Suicune Battle Strategy (Crystal)
- Location: Tin Tower 1F (Final Sighting).
- Status: Stationary encounter (does not flee).
- Level: 40.
- Strategy: Use KIMCHI (Sleep Powder) or XENON (Hypnosis) to induce sleep. Weaken with GNEISS or Calcifer.
- Note: Mean Look is NOT required for this specific battle.
- Requirement: Must defeat the Wise Trio in the Wise Trio Room first.

# PC Storage Inventory
- Box 1: RICOTTA (RATICATE), CINNABAR (GOLDEEN), VORTEX (POLIWAG), INTERCEPT (YANMA), ROCKY (ONIX), EGG (CLEFFA), XFDW (MEOWTH), FRITTATA (TOGEPI), SHUCKIE (SHUCKLE), Blarney (SUDOWOODO).

# Timestamps
- Suicune Hunt (Route 42/36 Phase): Started Turn 22256 (Dec 26, 2:00 AM).