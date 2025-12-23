# Suicune Hunt Strategy (Started Turn #13189)
- Lead: KIMCHI (Lv 21 Gloom).
- Method: Repel Trick. Wild Pokemon on Route 38 are Lv 13-16 (verified Lv 16 Magnemite). Leading with Lv 21 KIMCHI + Super Repel filters out all wild encounters except Suicune (Lv 40).
- Repel Tracking:
  - Super Repel #1: Turn #13364 (Wore off Turn #13387).
  - Super Repel #2: Turn #13391 (Expected to wear off ~Turn #13411).
- Location: Pacing (Grass Dance) at (28, 7) on Route 38.
- Tracking: Use Pokedex AREA map.
- Battle Plan: Turn 1 Sleep Powder. Use `suicune_capture_analyst_v2`.
- Capture Notes: Status and HP damage are permanent. Sleep prevents fleeing on Turn 1. Suicune is Lv 40.
- Roamer Logic: Roamers only move when map boundaries are crossed, Fly is used, or after a battle with the roamer. Pacing or regular wild battles do not move them.

# Roaming Pokémon Reference
- Movement: Suicune shifts routes ONLY when the player crosses a map boundary (warp, carpet, or edge), uses Fly, or after a battle with the roamer.
- Logic: Pacing in grass, phone calls, or battling OTHER wild Pokemon on the same route do NOT move it.
- Tracking: Suicune's location is verified visually via Pokedex AREA map. It is currently on Route 38 (west of Ecruteak City).

# Global Tile Mechanics
- TALL_GRASS: Traversable. Triggers wild encounters. Repel Trick works here.
- FLOOR: Traversable. Standard ground.
- WALL / HEADBUTT_TREE / MART_SHELF / COUNTER: Impassable.
- LEDGE_HOP_DOWN / LEFT / RIGHT: One-way traversable in the indicated direction.
- WARP_CARPET: Traversable. Triggers map transition.
- Mechanism: To interact with NPCs behind COUNTER tiles, face the counter and press A.

# Route 38/39 Boundary Reference
- Route 38 (0, 8) <-> Route 39 (19, 8)
- Route 38 (0, 10) <-> Route 39 (19, 10)
- Crossing this line shifts roamer locations.

# PC Storage (Box 1)
- ROCKY (Onix Lv 6), EGG (Cleffa Lv 5), XFDW (Meowth Lv 16), FRITTATA (Togepi Lv 5), SHUCKIE (Shuckle Lv 15).

# Lessons Learned & Error Analysis
- Tool Reliability: Roamer tracking tools must handle menu state carefully.
- Navigation: Paths are often wider than one tile. Analyze adjacent tiles before assuming a path is blocked.
- State Sync: Always verify inventory and money against Game State Information.
- Map Limits: Route 39 is 20 tiles wide (X=0 to 19). (20, 8) is out of bounds.
- Input Hygiene: Avoid mixing directional and action buttons in a single `press_buttons` call.