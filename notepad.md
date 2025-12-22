# Suicune Hunt Strategy & Status
- Status: Roaming. Location may have changed due to boundary crossing (Turn #12523). Pending Pokédex check.
- Strategy: Repel Trick (Lead Lv 21 vs Wild Lv 13-16).
- Method: Pacing (Grass Dance) in Route 42 grass patch at (46, 12).
- Battle Plan: Turn 1 Sleep Powder. Use `suicune_capture_analyst_v2`.
- Active Status: Repel active (Turn #12519). Steps: 4/100.
- Safeguard: Re-verify location via Pokédex after every map boundary crossing, battle, Repel expiration, phone call, or suspected location change.
- Tool Usage: `grass_dance_tool` for pacing. **Avoid SWEET SCENT**.
- Tracking: Start Turn #12524. Navigate to grass patch.

## Roaming Pokémon Reference
- Tracking: Do NOT use Fly to chase (randomizes location). Walk across map boundaries (gatehouses/warp carpets) to shift position predictably.
- Encountering: Repel Trick + pacing in grass.
- Capture: Sleep status on Turn 1.
- Movement: Shift routes when player crosses a map boundary (warp carpet, gatehouse).
- Trackable via Pokédex "AREA" map if previously seen.

## Global Tile Mechanics
- TALL_GRASS: Traversable. Triggers wild encounters.
- FLOOR: Traversable. Standard ground.
- WALL: Impassable. Collision blocking.
- HEADBUTT_TREE: Impassable. Can be interacted with from adjacent tile if player has Headbutt.
- LEDGE_HOP_DOWN: One-way traversable (South/Down only). Impassable from other directions.
- WARP: Traversable. Triggers map transition.

# Route 37 Specific Notes
- TALL_GRASS at (8, 2), (9, 2), (7, 2): Pacing spot.
- LEDGE_HOP_DOWN at (12, 3), (13, 3), (4, 7), (5, 7), (8, 7), (9, 7).

# PC Storage (Box 1)
- ROCKY (Onix Lv 6), EGG (Cleffa Lv 5), XFDW (Meowth Lv 16), FRITTATA (Togepi Lv 5), SHUCKIE (Shuckle Lv 15).

# General Lessons Learned
- Navigation Buffer: After using a warp, move at least 3 tiles away before starting a new path to prevent re-entry loops.
- Repel Trick: Leading with a Pokemon lower level than the target but higher than local wild Pokemon filters out non-targets.
- Tool Timing: Menu-heavy tools like Pokédex tracking require significant 'sleep' delays (600ms+) to account for UI transitions.
- Repel Refresh: Verified. If the game incorrectly claims a Repel is "still in effect" after it wears off, take one step of movement to reset the internal state.
- Ledge Mechanics: LEDGE_HOP_DOWN tiles are one-way (Down/South only). They act as walls when approached from the South.
- Phone Calls: NPCs like Arnie can call and interrupt gameplay.

# Menu Navigation
- Lesson: The main menu is circular. Using a fixed number of 'Up' or 'Down' presses is unreliable. Always verify cursor position or use relative movement.
- Pokédex AREA: Press 'A' on entry -> move to 'AREA' -> press 'A'.