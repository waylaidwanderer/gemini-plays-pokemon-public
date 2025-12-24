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
- Strategy: Methodically sweep the middle island of Route 42. Suicune appears as a static sprite once the trigger tile is stepped on.
- Team Lead: XENON (Gastly) for Hypnosis/Night Shade.
- Next Sightings (Crystal): Route 36 (near Violet), Route 25 (near Bill's house).

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
- Pathfinding Shorelines: find_path_v2 can struggle with water entry points. Manual navigation to (40, 11) or (33, 10) is more reliable for starting Surf.