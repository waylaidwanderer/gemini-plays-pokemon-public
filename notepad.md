# Tile Mechanics (Global)
- FLOOR: Traversable in all directions. (Verified)
- WALL: Impassable solid obstacle. (Verified)
- TALL_GRASS: Traversable. Triggers wild encounters. (Verified)
- WATER: Impassable without Surf. To enter water from land, face the water tile and press A to initiate Surf. (Verified)
- HEADBUTT_TREE: Impassable. Interacts with Headbutt move. (Verified)
- CUT_TREE: Impassable. Requires Cut move to clear. Regrows on map reload. (Verified)
- FRUIT_TREE: Impassable. Interacts with A button to provide items once per day. (Verified)
- LEDGE_HOP_LEFT/RIGHT/UP/DOWN: One-way movement. (Verified)
- FLOOR_UP_WALL: One-way barrier (Southward). Impassable from the South. (Verified)
- WARP / CAVE / WARP_CARPET: Map transition points. (Verified)

# Suicune Tracking & Strategy
- Status: Scripted Overworld Encounters (Crystal Version).
- Sightings: Burned Tower (fled), Cianwood City (fled), Route 42 (fled - Flagged by Sage permission).
- Goal: Capture/Defeat Suicune at Tin Tower 1F.
- Strategy: Speak to all three Sages in Tin Tower 1F to trigger the encounter.
- Team Lead: XENON (Gastly) for Hypnosis/Night Shade.

# Sage Lore (Tin Tower 1F)
1. Sage (11, 11): Ho-Oh resurrected Entei, Raikou, and Suicune after the Brass Tower fire. (Spoken)
2. Sage (5, 9): Legend says Ho-Oh descends when souls of Pokemon and humans commune. (Spoken)
3. Sage (14, 6): Towers built for friendship 700 years ago. (Spoken)
- All three Sages have shared their lore. Heading to center (9, 9) to trigger Suicune.

# HM/TM Knowledge
- HM01 Cut: KIMCHI (Gloom)
- HM02 Fly: ICARUS (Pidgey)
- HM03 Surf: Ravioli (Krabby)
- HM04 Strength: GNEISS (Graveler)

# PC Storage (Box 1)
- VORTEX (Poliwag): Lv22, Male.
- INTERCEPT (Yanma): Lv12, Female.
- ROCKY (Onix): Lv6, Male.
- EGG (Cleffa): Lv5, Female.
- XFDW (Meowth): Lv16, Male.
- FRITTATA (Togepi): Lv5, Male.
- SHUCKIE (Shuckle): Lv15, Female.
- Blarney (SUDOWOODO): Lv20, Male.

# General Lessons
- Sage Permission Flag: Sage at (4, 6) in Ecruteak building (4_1) is the definitive indicator for Route 42 event completion.
- Roamer vs. Scripted: Suicune is NOT a roamer in Crystal. Don't rely on Pokedex 'Area' for movement.
- Surf Initiation: Face water and press A.
- Scripted Event Logic: If a legendary isn't appearing where expected, verify all prerequisite NPC interactions and game-state flags (like the Sage's permission).