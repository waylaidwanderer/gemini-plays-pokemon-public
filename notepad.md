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
- Current Objective: Trigger the Route 42 encounter. Started Turn 16921.
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

# Island Sweep Plan (Turn 16996)
- Objective: Step on every reachable tile on the middle island to trigger Suicune.
- Starting Point: (24, 13)
- Grid:
  - Row 1: (24, 14) to (28, 14)
  - Row 2: (30, 15) to (25, 15)
  - Row 3: (26, 16) to (30, 16)
  - Row 4: (30, 17) to (26, 17)
- Progress:
  - Row 1 (24, 14 to 27, 14): Done.
  - Row 2 (30, 15 to 25, 15): Done.
  - Row 3 (26, 16) and (30, 16): In Progress.
  - Row 4 (26, 17) to (30, 17): Pending.