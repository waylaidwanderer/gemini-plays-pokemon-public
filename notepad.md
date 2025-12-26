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

# General Lessons
- Scripted Events: Scripted encounters (like Suicune sightings) are based on visible sprites in the Map Objects list, not hidden tile triggers. If the sprite is not present, the event cannot be triggered by walking. [Turn 22217]
- Ecruteak Geography: There are two distinct buildings in northern Ecruteak. The NW building leads to the Burned Tower. The NE building (Barrier Station) leads to the Tin Tower. The Wise Trio appears in the Barrier Station after getting the Clear Bell. [Turn 22217]

# Strategy: Suicune Hunt Verification
- Sighting 1: Burned Tower (Complete)
- Sighting 2: Cianwood City (Complete)
- Sighting 3 (Goal): Route 42 Central Island. Suicune appears as a visible sprite.
- Sighting 4: Route 36 (Sudowoodo junction).
- Sighting 5: Tin Tower 1F (Final Battle). Requires Clear Bell and defeating the Wise Trio.
- Current Status: Suicune sprite missing from Route 42 and Route 36.
- Plan:
  1. Visit Morty in Ecruteak Gym to check for quest flags.
  2. Check Burned Tower for Eusine.
  3. Re-verify Route 42 approach from the west.

# Suicune Battle Strategy (Crystal)
- Location: Tin Tower 1F (Final Sighting).
- Status: Stationary encounter (does not flee).
- Level: 40.
- Strategy: Use KIMCHI (Sleep Powder) or XENON (Hypnosis) to induce sleep. Weaken with GNEISS or Calcifer.
- Note: Mean Look is NOT required for this specific battle.
- Requirement: Must defeat the Wise Trio in the Wise Trio Room first.

# PC Storage Inventory
- Box 1: RICOTTA (RATICATE), CINNABAR (GOLDEEN), VORTEX (POLIWAG), INTERCEPT (YANMA), ROCKY (ONIX), EGG (CLEFFA), XFDW (MEOWTH), FRITTATA (TOGEPI), SHUCKIE (SHUCKLE), Blarney (SUDOWOODO).