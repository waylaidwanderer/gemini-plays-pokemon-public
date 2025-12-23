# Suicune Hunt Strategy & Status
- Strategy: Repel Trick (Lead KIMCHI Lv 21 vs Wild Lv 13-16).
- Method: Pacing (Grass Dance) in grass at (28, 7) on Route 38.
- Battle Plan: Turn 1 Sleep Powder. Use `suicune_capture_analyst_v2`.
- Active Status: Super Repel expired (Turn #13075). 0 left in bag.
- Current Status: Suicune confirmed on Route 38 (Turn #13076).

# Roaming Pokémon Reference
- Tracking: Use Pokédex AREA map via `check_suicune_location_v5`.
- Movement: Suicune shifts routes ONLY when the player crosses a map boundary (warp, carpet, or edge) or after a battle with Suicune.
- Note: Flying counts as crossing boundaries. Pacing in grass or phone calls do NOT move it.
- Note: Battling OTHER wild Pokemon on the same route does NOT move it (Verified Turn #12992).
- Capture: Status and HP damage are permanent. Sleep prevents fleeing on Turn 1.
- Catch Odds: ~5.66% with Sleep + Great Ball at 1 HP. Suicune is Lv 40.

# Global Tile Mechanics
- TALL_GRASS / LONG_GRASS: Traversable. Triggers wild encounters. Repel Trick works here.
- FLOOR: Traversable. Standard ground.
- WALL / HEADBUTT_TREE: Impassable.
- LEDGE_HOP_DOWN / LEFT / RIGHT: One-way traversable in the indicated direction.
- WARP_CARPET_RIGHT: Traversable. Triggers map transition.

# Restock Task (Started Turn #13076)
- Goal: Buy 20 Super Repels (10,000 yen).
- Current Funds: 10,821 yen.
- TM Selling Progress:
  - TM01 (DynamicPunch): Sold for 1500 yen.
  - TM08 (Rock Smash): Sold for 500 yen.
  - TM12 (Sweet Scent): Sold for 500 yen.
  - TM16 (Icy Wind): Sold for 1500 yen.
  - TM35 (Sleep Talk): Sold for 500 yen.
  - TM45 (Attract): Sold for 1500 yen.
  - TM33 (Ice Punch): Sold for 1500 yen.
  - TM48 (Fire Punch): Sold for 1500 yen.
  - TM49 (Fury Cutter): Pending (Optional).
  - TM50 (Nightmare): Pending (Optional).
- Revenue Goal Met: Yes.
- Time Tracking: 50 turns elapsed since task start.

# Olivine Mart Tile Mechanics
- MART_SHELF: Impassable. (Visual confirmation: Attempted movement blocked).
- COUNTER: Impassable. Used for interaction with clerks. (Verified: Interaction with Clerk at (1, 3) successful while facing Counter at (2, 3) from (3, 3)).

# Route 38 Specifics
- Suicune Hunting Spot: (28, 7) tall grass.
- Boundary: Route 38 (0, 10) <-> Route 39 (19, 10). Crossing this shifts Suicune.

# PC Storage (Box 1)
- ROCKY (Onix Lv 6), EGG (Cleffa Lv 5), XFDW (Meowth Lv 16), FRITTATA (Togepi Lv 5), SHUCKIE (Shuckle Lv 15).

# Lessons Learned & Error Analysis
- Tool Reliability: Custom tools for roamer tracking must handle the full sequence from overworld to overworld and reset the menu cursor.
- Navigation: Paths are often wider than one tile. Analyze adjacent tiles before assuming a path is blocked.
- Roamer Logic: Roamers only move when you change maps or battle them. Clearing wild encounters is safe.

# Pokedex Navigation Sequence (Verified)
1. Press Start to open Menu.
2. Press Up 8 times to reset cursor to POKEDEX.
3. Press A to select POKEDEX.
4. Select Suicune from list and press A.
5. Cursor starts on PAGE. Press Right to select AREA.
6. Press A to view map.
7. Press B multiple times to exit.

# Encounter Tracking (Route 38)
- Current Repel: Applied Turn #13062. Expired Turn #13075.
- Steps Taken: 200 (Repel Duration).
- Status: Suicune confirmed here Turn #13076.