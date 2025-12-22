# Suicune Hunt Strategy & Status
- Status: Roaming. Last confirmed on Route 37 (Turn #12425).
- Strategy: Repel Trick. Lead with KIMCHI (Gloom Lv 21) which is > local wild levels (Lv 13-16) but < Suicune (Lv 40).
- Method: Pacing (Grass Dance) at (8, 2) on Route 37.
- Battle Plan: Use Sleep Powder on Turn 1 to prevent fleeing. Use `suicune_capture_analyst_v2` for catch odds.
- Active Status: Repel active (Turn #12444). Steps: 60/100.
- Safeguard: Re-verify location via Pokédex after every map boundary crossing, battle, Repel expiration, phone call, or suspected location change.
- Tool Usage: `grass_dance_tool` for pacing. **Avoid SWEET SCENT**.

# Route 37 Tile Mechanics
- TALL_GRASS at (8, 2), (9, 2), (7, 2): Traversable, triggers wild encounters.
- WALL at (10, 2), (10, 3): Impassable.
- FLOOR at (9, 1), (10, 1): Traversable.
- HEADBUTT_TREE at (9, 0): Impassable.
- LEDGE_HOP_DOWN at (12, 3), (13, 3), (4, 7), (5, 7), (8, 7), (9, 7): Traversable only from above (Down).

# PC Storage (Box 1)
- ROCKY (Onix Lv 6), EGG (Cleffa Lv 5), XFDW (Meowth Lv 16), FRITTATA (Togepi Lv 5), SHUCKIE (Shuckle Lv 15).

# Roaming Mechanics
- Move routes when player crosses a boundary (gatehouse, warp carpet).
- Fly causes them to move to a random location.
- Flee immediately in battle. Use status (Sleep). 
- Trackable via Pokédex "AREA" map if seen.

# General Lessons Learned
- Navigation Buffer: After using a warp, move at least 3 tiles away before starting a new path to prevent re-entry loops.
- Repel Trick: Leading with a Pokemon lower level than the target but higher than local wild Pokemon filters out non-targets.
- Tool Timing: Menu-heavy tools like Pokédex tracking require significant 'sleep' delays (600ms+) to account for UI transitions.
- Repel Refresh: Verified. If the game incorrectly claims a Repel is "still in effect" after it wears off, take one step of movement to reset the internal state.
- Ledge Mechanics: LEDGE_HOP_DOWN tiles are one-way (Down/South only). They act as walls when approached from the South.
- Phone Calls: NPCs like Arnie can call and interrupt gameplay. This does not change the Repel count but can be a distraction.

# Menu Navigation
- Lesson: The main menu is circular. Using a fixed number of 'Up' or 'Down' presses is unreliable. Always verify cursor position or use relative movement.
- Pokédex: To see the 'AREA' map, first press 'A' on the list entry, then move the cursor to 'AREA' and press 'A' again.