# Suicune Hunt Strategy & Status
- Status: Roaming. Last confirmed on Route 37 (Turn #12293).
- Strategy: Repel Trick. Lead with KIMCHI (Gloom Lv 21) which is > local wild levels (Lv 13-16) but < Suicune (Lv 40).
- Method: Pacing (Grass Dance) at (8, 2) on Route 37.
- Grass Dance Start Turn: #12301.
- Battle Plan: Use Sleep Powder on Turn 1 to prevent fleeing. Use `suicune_capture_analyst` for catch odds.
- Active Status: Using Super Repel (Turn #12301). Steps taken: 60.
- Safeguard: Re-verify location via Pokédex after every map boundary crossing or battle.
- Tool Usage: `grass_dance_tool` for pacing, `check_suicune_location` for tracking. **Avoid SWEET SCENT**.

# Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL/COUNTER/MART_SHELF/HEADBUTT_TREE: Impassable.
- STAIRCASE/WARP/DOOR/WARP_CARPET: Map transition.
- WATER: HM03 Surf required.
- TALL_GRASS: Traversable. Triggers wild encounters.
- LEDGE_HOP_DOWN: Traversable only from above (Down).
- CUT_TREE: HM01 Cut required.

# PC Storage (Box 1)
- ROCKY (Onix Lv 6), EGG (Cleffa Lv 5), XFDW (Meowth Lv 16), FRITTATA (Togepi Lv 5), SHUCKIE (Shuckle Lv 15).

# Roaming Mechanics
- Move routes when player crosses a boundary.
- Fly causes them to move to a random location.
- Flee immediately in battle. Use status (Sleep).
- Trackable via Pokédex "AREA" map if seen.

# General Lessons Learned
- Navigation Buffer: After using a warp, move at least 3 tiles away before starting a new path to prevent re-entry loops.
- Repel Trick: Leading with a Pokemon lower level than the target but higher than local wild Pokemon filters out non-targets.
- Sweet Scent Interaction: SWEET SCENT bypasses REPEL filtering. Use pacing for the Repel trick.