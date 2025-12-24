# Tile Mechanics (Global)
- FLOOR: Traversable in all directions. (Verified)
- WALL: Impassable solid obstacle. (Verified)
- TALL_GRASS: Traversable. Triggers wild encounters. (Verified)
- WATER: Impassable without Surf. To enter water from land, face the water tile and press A to initiate Surf. (Verified)
- HEADBUTT_TREE: Impassable. Interacts with Headbutt move. (Verified)
- CUT_TREE: Impassable. Requires Cut move to clear. Regrows on map reload. (Verified)
- FRUIT_TREE: Impassable. Interacts with A button to provide items once per day. (Verified)
- LEDGE_HOP_LEFT: One-way ledge (East to West). (Verified)
- FLOOR_UP_WALL: One-way barrier (Southward). Impassable from the South. (Verified)
- WARP / CAVE / WARP_CARPET: Map transition points. (Verified)

# Suicune Tracking & Strategy
- Status: Scripted Overworld Encounters (Crystal Version).
- Sightings: Burned Tower (fled), Cianwood City (fled).
- Current Objective: Investigate 'SUICUNE'S NEST' coordinates on Route 42.
- Strategy: Visit red dot and blue square coordinates discovered in the Pokédex AREA map.
- Team Lead: XENON (Gastly) for Hypnosis/Night Shade.
- Next Sightings (Crystal): Route 36 (near Violet), Route 25 (near Bill's house).

# Suicune's Nest Observations (Turn 17031)
- Red Dots: (29, 14), (32, 12), (34, 13), (35, 15), (27, 16), (30, 18).
- Blue Squares: (30, 13), (32, 13), (34, 13), (28, 14), (31, 14), (27, 17), (32, 17), (34, 17), (30, 18).
- Overlap (Red & Blue): (34, 13), (30, 18).
- Investigation Log:
  - (27, 17): Stepped on. No event. (Turn 17035)

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
- Roamer vs. Scripted: Suicune is NOT a roamer in Crystal. Don't rely on Pokedex 'Area' for movement; it only indicates the current route of the scripted event.
- Surf Initiation: Directional buttons won't enter water. Must face water and press A.
- Pathfinding Shorelines: find_path_v2 can struggle with water entry points. Manual navigation is more reliable.
- Pokédex 'Nest' Screen: Rare visual cues in the AREA map may indicate specific event triggers. (Turn 17031)