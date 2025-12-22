# Suicune Hunt Strategy & Status
- Strategy: Repel Trick (Lead KIMCHI Lv 21 vs Wild Lv 13-16).
- Method: Pacing (Grass Dance) in grass.
- Battle Plan: Turn 1 Sleep Powder. Use `suicune_capture_analyst_v2`.
- Active Status: Repel active (Turn #12610). Steps: 20/100.
- Safeguard: Re-verify location via Pokédex after every map boundary crossing, battle, or Repel expiration.
- Tracking: Start Turn #12542. Suicune confirmed on Route 38 (Turn #12584).

## Roaming Pokémon Reference
- Tracking: Do NOT use Fly to chase (randomizes location). Walk across map boundaries (gatehouses/warp carpets) to shift position predictably.
- Encountering: Repel Trick + pacing in grass.
- Capture: Sleep status on Turn 1.
- Movement: Shift routes ONLY when player crosses a map boundary (warp carpet, gatehouse) or after a battle with the roamer. Phone calls and other events do NOT move roamers.
- Trackable via Pokédex "AREA" map if previously seen.

## Tile Mechanics
- TALL_GRASS: Traversable. Triggers wild encounters.
- FLOOR: Traversable. Standard ground.
- WALL: Impassable. Collision blocking.
- HEADBUTT_TREE: Impassable. Can be interacted with from adjacent tile if player has Headbutt.
- LEDGE_HOP_DOWN: One-way traversable (South/Down only).
- LEDGE_HOP_LEFT: One-way traversable (West/Left only).
- LEDGE_HOP_RIGHT: One-way traversable (East/Right only).
- WARP_CARPET: Traversable. Triggers map transition.

# Route 37 Specific Notes
- TALL_GRASS at (8, 2), (9, 2), (7, 2): Pacing spot.
- LEDGE_HOP_DOWN at (12, 3), (13, 3), (4, 7), (5, 7), (8, 7), (9, 7).

# PC Storage (Box 1)
- ROCKY (Onix Lv 6), EGG (Cleffa Lv 5), XFDW (Meowth Lv 16), FRITTATA (Togepi Lv 5), SHUCKIE (Shuckle Lv 15).

# General Lessons Learned
- Navigation Buffer: After using a warp, move 3+ tiles away before starting a new path.
- Repel Refresh: If game incorrectly claims Repel is active after wearing off, move 1 step to reset state.
- Phone Calls: Interrupt gameplay but do not affect Repel count or Roamer location.

# Menu Navigation
- Circular Menu: Unreliable fixed Up/Down counts. Verify cursor position.
- Pokédex AREA: Press 'A' on entry -> move to 'AREA' -> press 'A'.