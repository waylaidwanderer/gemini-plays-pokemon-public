# Tile Mechanics (Global)
- FLOOR: Traversable in all directions. (Verified)
- WALL: Impassable solid obstacle. (Verified)
- TALL_GRASS: Traversable. Triggers wild encounters. (Verified)
- WATER: Impassable without Surf. Traversable with Surf. (Verified)
- HEADBUTT_TREE: Impassable. Interacts with Headbutt move. (Verified)
- CUT_TREE: Impassable. Requires Cut move to clear. Regrows on map reload. (Verified)
- FRUIT_TREE: Impassable. Interacts with A button to provide items once per day. (Verified)
- LEDGE_HOP_LEFT: One-way ledge (East to West). (Verified)
- FLOOR_UP_WALL: One-way barrier (Southward). Impassable from the South. (Verified)
- WARP / CAVE / WARP_CARPET: Map transition points. (Verified)

# Roamer Tracking Data
- Raikou/Entei Neighbors: Route 42 (2_5) connects to Ecruteak City (1_3) and Mahogany Town (2_4).

# Suicune Tracking & Strategy
- Status: Scripted Overworld Encounters (Crystal Version). (Verified by Pokedex check at Turn 16958)
- Sightings: Burned Tower (fled), Cianwood City (fled).
- Next Target: Route 42 (Middle area near Apricorn trees). (Confirmed by Pokedex)
- Trigger: Walking to a specific tile on the middle island.
- Failed Hypotheses:
  - Interaction with Apricorn trees triggers encounter. (1 attempt)
  - Standing at (30, 16) or (28, 15) triggers encounter. (Failed)

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
- Route 42 middle area (Apricorn trees) for Suicune sighting.
- Unseen tiles on Route 42: (33, 15), (24, 17).

# Lessons Learned
- Roamer vs. Scripted: In Pokemon Crystal, Suicune is NOT a roamer like Raikou/Entei. It has fixed overworld locations. Trying to "intercept" it with a Repel trick is a waste of time. (Turn 16921)

# Task History
- Scripted Suicune Hunt: Started Turn 16921. Pivot from roamer strategy.

# Progress Update (Turn 16951)
- Reached the middle island of Route 42.
- Collected Apricorns from the trees.
- Suicune not yet triggered.
- Strategy: Explore the remaining reachable tiles on the island to find the trigger tile.