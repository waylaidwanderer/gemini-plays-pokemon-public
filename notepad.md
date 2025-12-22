# Suicune Hunt Strategy & Status
- Strategy: Repel Trick (Lead KIMCHI Lv 21 vs Wild Lv 13-16).
- Method: Pacing (Grass Dance) in grass at (28, 7) on Route 38.
- Battle Plan: Turn 1 Sleep Powder. Use `suicune_capture_analyst_v2`.
- Active Status: Repel wore off (Turn #12979). Encountered Tauros (Turn #12982).
- Current Status: Checking Suicune location after battle.
- Task Timing: Grass Dance interrupted by battle (Turn #12982).

# Roaming Pokémon Reference
- Tracking: Use Pokédex AREA map. (Start -> POKEDEX -> Select Suicune -> AREA).
- Movement: Suicune shifts routes ONLY when the player crosses a map boundary (warp, carpet, or edge) or after a battle.
- Note: Flying counts as crossing boundaries. Pacing in grass or phone calls do NOT move it.
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
- Tool Failure (check_suicune_location_v2): The tool failed due to incorrect menu indexing and handling of the Pokedex entry state. Manual navigation is safer until refined.
- Stagnation (Turn 12921-12930): Attempting to reuse a broken tool leads to loops. Fix tools immediately or switch to manual.
- Navigation: Paths are often wider than one tile. Analyze adjacent tiles before assuming a path is blocked.

# Pokedex Navigation Sequence (Verified)
1. Press Start to open Menu.
2. Select POKEDEX (index 0) and press A.
3. Select Suicune from list and press A.
4. Cursor starts on PAGE. Press Right to select AREA.
5. Press A to view map.
6. Press B multiple times to exit.

# Roamer Movement Verified (Crystal)
- Rule: Roamers (Suicune) do NOT move if you battle a different wild Pokemon on the same route.
- Rule: Roamers ONLY move when you cross a map boundary (Route/City), use Fly, or after battling the roamer itself.
- Conclusion: Once trapped on a route, you can safely clear wild encounters or pace indefinitely.

# Progress Log
- Turn #12992: Confirmed Suicune is still on Route 38 via Pokedex AREA map. Exit sequence initiated.