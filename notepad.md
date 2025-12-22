# Suicune Hunt Strategy & Status
- Strategy: Repel Trick (Lead KIMCHI Lv 21 vs Wild Lv 13-16).
- Method: Pacing (Grass Dance) in grass at (28, 7) on Route 38.
- Battle Plan: Turn 1 Sleep Powder. Use `suicune_capture_analyst_v2`.
- Active Status: Super Repel active (Turn #12893). 6 left.
- Task Timestamp: Grass Dance task started Turn #12861.

# Roaming Pokémon Reference
- Tracking: Use Pokédex AREA map. Access: Pokedex -> Entry -> AREA.
- Movement: Roamers shift routes ONLY when the player crosses a map boundary (warp/carpet) or after a battle with the roamer.
- Note: Flying counts as crossing boundaries. Pacing in grass does NOT move them. Phone calls do NOT move them.
- Capture: Status (Sleep/Paralysis) and HP damage are permanent between encounters. Sleep is highly recommended to prevent fleeing on Turn 1.

# Tile Mechanics (Route 38)
- TALL_GRASS: Traversable. Triggers wild encounters. Repel Trick works here.
- FLOOR: Traversable. Standard ground.
- WALL / HEADBUTT_TREE: Impassable.
- LEDGE_HOP_DOWN / LEFT / RIGHT: One-way traversable in the indicated direction.
- WARP_CARPET_RIGHT: Traversable. Triggers map transition to Ecruteak Gatehouse.

# PC Storage (Box 1)
- ROCKY (Onix Lv 6), EGG (Cleffa Lv 5), XFDW (Meowth Lv 16), FRITTATA (Togepi Lv 5), SHUCKIE (Shuckle Lv 15).

# General Lessons Learned
- Tool Reliability: Custom tools for menu navigation (like `check_suicune_location_v2`) must explicitly handle the 'menu_already_open' state and initial cursor position to avoid sequence breaks.
- Repel Refresh: If a Repel wears off, the game may still block encounters for 1 step. Move to reset the state.
- Roamer Logic: Roamers only move when you change maps. You can safely pace in one area indefinitely once they are trapped there.

# Suicune Capture Strategy Detail
- Lead: Gloom (KIMCHI) Lv 21. Move: Sleep Powder (Acc: 75%).
- Odds: ~0.59% with Great Ball at full HP. Status (Sleep) is the priority.