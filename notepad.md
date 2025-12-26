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
- Scripted Events: Sightings are sprite-based. If a sprite is missing, the event cannot trigger. [Turn 22217]
- Ecruteak Geography: NW = Burned Tower; NE = Barrier Station (leads to Tin Tower). Wise Trio is in Barrier Station (Map 4_2) or Tin Tower 1F. [Turn 22217]
- Root Hypothesis Failure: If a scripted sequence stalls (e.g., Suicune sightings), the assumed order or prerequisite might be wrong. Pivot to the next major hurdle (Wise Trio battle) instead of looping. [Turn 22321]

# Strategy: Suicune Hunt (Crystal Version)
- Sighting 1: Burned Tower (Complete)
- Sighting 2: Cianwood City (Complete)
    - Note: Observed Suicune at (10, 14) and defeated Eusine. [Verified]
- Overworld Sightings (Stalled): Route 42 & Route 36.
    - Failed Attempts: Thorough sweeps of Route 42 island and Route 36 junction [Turns 22256-22315]. Sprites did not appear.
    - Strategy Shift: Proceeding directly to Tin Tower to engage the Wise Trio. Hypothesis: The sages or the tower itself may trigger the remaining sequence or the sightings were somehow bypassed. [Turn #22336]
- Sighting 5 (Goal): Tin Tower 1F (Final Battle).
    - How: Enter Tin Tower 1F via the NE entrance in Ecruteak City (37, 7). Requires Clear Bell and defeating the Wise Trio.
- Sequence: Burned Tower -> Cianwood -> Route 42 -> Route 36 -> Tin Tower.

# Suicune Battle Strategy (Crystal)
- Location: Tin Tower 1F (Final Sighting).
- Status: Stationary encounter (does not flee).
- Level: 40.
- Strategy: Use KIMCHI (Sleep Powder) or XENON (Hypnosis) to induce sleep. Weaken with GNEISS or Calcifer.
- Note: Mean Look is NOT required for this specific battle.
- Requirement: Must defeat the Wise Trio first.

# PC Storage Inventory
- Box 1: RICOTTA (RATICATE), CINNABAR (GOLDEEN), VORTEX (POLIWAG), INTERCEPT (YANMA), ROCKY (ONIX), EGG (CLEFFA), XFDW (MEOWTH), FRITTATA (TOGEPI), SHUCKIE (SHUCKLE), Blarney (SUDOWOODO).

# Timestamps
- Suicune Hunt (Route 42/36 Phase): Started Turn 22256 (Dec 26, 2:00 AM). Stalled at Turn 22315. Pivoting to Wise Trio/Tin Tower.