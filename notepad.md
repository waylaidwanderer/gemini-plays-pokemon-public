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

# Roamer Tracking Data
- Raikou/Entei Neighbors: Route 42 (2_5) connects to Ecruteak City (1_3) and Mahogany Town (2_4).

# Suicune Tracking & Strategy
- Status: ROAMING (Confirmed by Pokedex and Roamer Tracker at Turn 16964).
- Sightings: Tin Tower (fled).
- Current Location: Route 42 (Confirmed).
- Strategy: Surf across the pond to reach the eastern tall grass at (46, 12).
- Team Lead: XENON (Gastly) for Mean Look/Hypnosis.
- Failed Hypotheses:
  - Scripted overworld encounter on middle island. (Island is fully explored, Suicune not visible).
  - Walking directly onto water tiles without initiating Surf. (Resulted in being stuck).

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

# Exploration Targets
- Route 42 eastern tall grass for Suicune sighting/encounter.
- Unseen tiles on Route 42: (33, 15), (24, 17).

# Lessons Learned
- Roamer vs. Scripted: In Pokemon Crystal, Suicune is NOT a roamer like Raikou/Entei. It has fixed overworld locations. Trying to "intercept" it with a Repel trick is a waste of time. (Turn 16921)
- Surf Initiation: You cannot move onto a water tile using directional buttons while on land. You must face the water and press A to trigger the "Want to SURF?" prompt. (Turn 16971)

# Task History
- Scripted Suicune Hunt: Started Turn 16921. Pivot from roamer strategy.

# Progress Update (Turn 16971)
- Attempting to cross the pond on Route 42 to reach the eastern tall grass.
- Moving to (33, 10) to face the water and initiate Surf.