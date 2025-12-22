# Suicune Hunt Strategy & Status
- Strategy: Repel Trick (Lead KIMCHI Lv 21 vs Wild Lv 13-16).
- Method: Pacing (Grass Dance) in grass at (28, 7) on Route 38.
- Battle Plan: Turn 1 Sleep Powder. Use `suicune_capture_analyst_v2`.
- Active Status: Super Repel active (Turn #13003). 4 left.
- Current Status: Suicune confirmed on Route 38 (Turn #12992).
- Task Timing: Grass Dance resuming Turn #13006.

# Roaming Pokémon Reference
- Tracking: Use Pokédex AREA map via `check_suicune_location_v3`.
- Movement: Suicune shifts routes ONLY when the player crosses a map boundary (warp, carpet, or edge) or after a battle with Suicune.
- Note: Flying counts as crossing boundaries. Pacing in grass or phone calls do NOT move it.
- Note: Battling OTHER wild Pokemon on the same route does NOT move it (Verified Turn #12992).
- Capture: Status and HP damage are permanent. Sleep prevents fleeing on Turn 1.
- Catch Odds: ~5.66% with Sleep + Great Ball at 1 HP. Suicune is Lv 40.

# Tile Mechanics (Global)
- TALL_GRASS: (x,y) -> (x,y). Traversable. Triggers wild encounters. Repel Trick works here.
- FLOOR: (x,y) -> (x,y). Traversable. Standard ground.
- WALL / HEADBUTT_TREE: Impassable.
- LEDGE_HOP_DOWN / LEFT / RIGHT: One-way traversable in the indicated direction.
- WARP_CARPET_RIGHT: Traversable. Triggers map transition.

# Route 38 Specifics
- Suicune Hunting Spot: (28, 7) tall grass.
- Boundary: Route 38 (0, 10) <-> Route 39 (19, 10). Crossing this shifts Suicune.

# PC Storage (Box 1)
- ROCKY (Onix Lv 6), EGG (Cleffa Lv 5), XFDW (Meowth Lv 16), FRITTATA (Togepi Lv 5), SHUCKIE (Shuckle Lv 15).

# Lessons Learned & Error Analysis
- Tool Reliability: Use `check_suicune_location_v3` for reliable roamer tracking.
- Navigation: Paths are often wider than one tile. Analyze adjacent tiles before assuming a path is blocked.
- Roamer Logic: Roamers only move when you change maps or battle them. Clearing wild encounters is safe.

# Pokedex Navigation Sequence (Verified)
1. Press Start to open Menu.
2. Select POKEDEX (index 0) and press A.
3. Select Suicune from list and press A.
4. Cursor starts on PAGE. Press Right to select AREA.
5. Press A to view map.
6. Press B multiple times to exit.

# Progress Log
- Turn #12992: Confirmed Suicune is still on Route 38 via Pokedex AREA map.
- Turn #12999: Re-applied Super Repel. Resuming Grass Dance.