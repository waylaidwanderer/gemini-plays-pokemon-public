# Suicune Hunt Strategy
- Strategy: Repel Trick (Lead KIMCHI Lv 21 vs Wild Lv 13-16).
- Method: Pacing (Grass Dance) in grass at (28, 7) on Route 38.
- Battle Plan: Turn 1 Sleep Powder. Use `suicune_capture_analyst_v2`.

# Roaming Pokémon Reference
- Tracking: Use Pokédex AREA map.
- Movement: Suicune shifts routes ONLY when the player crosses a map boundary (warp, carpet, or edge), uses Fly, or after a battle with the roamer.
- Note: Pacing in grass, phone calls, or battling OTHER wild Pokemon on the same route do NOT move it.
- Capture: Status and HP damage are permanent. Sleep prevents fleeing on Turn 1.
- Catch Odds: ~5.66% with Sleep + Great Ball at 1 HP. Suicune is Lv 40.
- Johto Map Dots: Pokedex shows roamers as red dots. Route 38 is at Johto map (5, 5).

# Global Tile Mechanics
- TALL_GRASS / LONG_GRASS: Traversable. Triggers wild encounters. Repel Trick works here.
- FLOOR: Traversable. Standard ground.
- WALL / HEADBUTT_TREE: Impassable.
- LEDGE_HOP_DOWN / LEFT / RIGHT: One-way traversable in the indicated direction.
- WARP_CARPET_RIGHT: Traversable. Triggers map transition.
- MART_SHELF: Impassable.
- COUNTER: Impassable. Used for interaction with clerks.
- OLIVINE_CITY (18, 17): WALL (Impassable). Avoid when pathing.

# Route 38/39 Boundary Reference
- Route 38 (0, 8) <-> Route 39 (20, 8)
- Route 38 (0, 10) <-> Route 39 (19, 10)
- Crossing this line shifts roamer locations.

# PC Storage (Box 1)
- ROCKY (Onix Lv 6), EGG (Cleffa Lv 5), XFDW (Meowth Lv 16), FRITTATA (Togepi Lv 5), SHUCKIE (Shuckle Lv 15).

# Lessons Learned & Error Analysis
- Tool Reliability: Custom tools for roamer tracking must handle the full sequence and reset the menu cursor.
- Navigation: Paths are often wider than one tile. Analyze adjacent tiles before assuming a path is blocked.
- State Sync: Always verify inventory and money against Game State Information.

# Pokedex Navigation Sequence (Verified)
1. Press Start to open Menu.
2. Press Up 8 times to reset cursor to POKEDEX.
3. Press A to select POKEDEX.
4. Select Suicune from list and press A.
5. Cursor starts on PAGE. Press Right to select AREA.
6. Press A to view map.
7. Press B multiple times to exit.