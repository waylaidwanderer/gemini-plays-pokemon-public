# Suicune Hunt Strategy & Status
- Status: Roaming. Last confirmed on Route 37 (Turn #12293).
- Strategy: Lead with KIMCHI (Gloom Lv 21). Use Super Repel (filters < Lv 21). Suicune is Lv 40.
- Method: Pacing (Grass Dance) on confirmed route. **Avoid SWEET SCENT** (ignores Repel).
- Battle Plan: Sleep Powder (Turn 1). Use `suicune_capture_analyst` for capture optimization.
- Active Status: Super Repel Expired (Turn #12259). Steps taken: ~170.
- Safeguard: Re-verify location via Pokédex after every map boundary crossing or battle.
- Tool Usage: Use `grass_dance_tool` for pacing and `check_suicune_location` for tracking.

# Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL/COUNTER/MART_SHELF/HEADBUTT_TREE: Impassable.
- STAIRCASE/WARP/DOOR/WARP_CARPET: Map transition.
- WATER: HM03 Surf required.
- GRASS: Wild encounters.
- CUT_TREE: HM01 Cut required.
- LEDGE_HOP: One-way jump.

# PC Storage (Box 1)
- ROCKY (Onix Lv 6), EGG (Cleffa Lv 5), XFDW (Meowth Lv 16), FRITTATA (Togepi Lv 5), SHUCKIE (Shuckle Lv 15).

# Roaming Mechanics
- Move routes when player crosses a boundary.
- Fly causes them to move to a random location.
- Flee immediately in battle. Use status (Sleep).
- Trackable via Pokédex "AREA" map if seen.

# General Lessons Learned
- Navigation Buffer: After using a warp, move at least 3 tiles away before starting a new path to prevent re-entry loops.
- Repel Trick: Leading with a Pokemon lower level than the target but higher than local wild Pokemon (e.g. KIMCHI Lv 21 vs Route 37 wild Lv 13-16) filters out non-targets.
- Sweet Scent Interaction: SWEET SCENT bypasses REPEL filtering. Use pacing for the Repel trick.