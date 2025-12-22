# Suicune Hunt Strategy & Status
- Status: Roaming. Last confirmed on Route 37 (Turn #12293).
- Strategy: Repel Trick. Lead with KIMCHI (Gloom Lv 21) which is > local wild levels (Lv 13-16) but < Suicune (Lv 40).
- Method: Pacing (Grass Dance) at (8, 2) on Route 37.
- Grass Dance Start Turn: #12301.
- Battle Plan: Use Sleep Powder on Turn 1 to prevent fleeing. Use `suicune_capture_analyst_v2` for catch odds.
- Active Status: Super Repel Wore Off (Turn #12309). Total steps this session: 200.
- Safeguard: Re-verify location via Pokédex after every map boundary crossing, battle, Repel expiration, or phone call.
- Tool Usage: `grass_dance_tool` for pacing, `check_suicune_location_v2` for tracking. **Avoid SWEET SCENT**.

## Failed Attempt Log
- Attempt #1: Super Repel (200 steps) on Route 37. Result: No encounter.
- Attempt #2: Repel (100 steps) on Route 37. Result: Interrupted by Arnie at Turn #12326. Repel status uncertain (Game says 'in effect' at #12324).

# Route 37 Tile Mechanics
- TALL_GRASS at (8, 2), (9, 2), (7, 2): Traversable, triggers wild encounters.
- WALL at (10, 2), (10, 3): Impassable.
- FLOOR at (9, 1), (10, 1): Traversable.
- HEADBUTT_TREE at (9, 0): Impassable.

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
- Move routes when player crosses a boundary (gatehouse, warp carpet).
- Fly causes them to move to a random location.
- Flee immediately in battle. Use status (Sleep).
- Trackable via Pokédex "AREA" map if seen.

# General Lessons Learned
- Navigation Buffer: After using a warp, move at least 3 tiles away before starting a new path to prevent re-entry loops.
- Repel Trick: Leading with a Pokemon lower level than the target but higher than local wild Pokemon filters out non-targets.
- Sweet Scent Interaction: SWEET SCENT bypasses REPEL filtering. Use pacing for the Repel trick.
- Tool Timing: Menu-heavy tools like Pokédex tracking require significant 'sleep' delays (600ms+) to account for UI transitions.
## Attempt #2
- Status: Repel status uncertain. Game said "still in effect" at #12324 despite "wore off" at #12309. Possibly requires one step of movement to reset.
- Start Turn: #12318.
- Interrupted by Arnie at #12326.
- Goal: Verify Suicune's location and resume Grass Dance.