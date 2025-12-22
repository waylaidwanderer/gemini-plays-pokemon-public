# Suicune Hunt Strategy & Status
- Status: Roaming. Last confirmed on Route 37 (Turn #12346).
- Strategy: Repel Trick. Lead with KIMCHI (Gloom Lv 21) which is > local wild levels (Lv 13-16) but < Suicune (Lv 40).
- Method: Pacing (Grass Dance) at (8, 2) on Route 37.
- Battle Plan: Use Sleep Powder on Turn 1 to prevent fleeing. Use `suicune_capture_analyst_v2` for catch odds.
- Active Status: Repel expired (Turn #12352). Steps: 100/100.
- Safeguard: Re-verify location via Pokédex after every map boundary crossing, battle, Repel expiration, phone call, or suspected location change.
- Tool Usage: `grass_dance_tool` for pacing, `check_suicune_location_v3` for tracking. **Avoid SWEET SCENT**.

# Route 37 Tile Mechanics
- TALL_GRASS at (8, 2), (9, 2), (7, 2): Traversable, triggers wild encounters.
- WALL at (10, 2), (10, 3): Impassable.
- FLOOR at (9, 1), (10, 1): Traversable.
- HEADBUTT_TREE at (9, 0): Impassable.
- LEDGE_HOP_DOWN at (12, 3), (13, 3), (4, 7), (5, 7), (8, 7), (9, 7): Traversable only from above (Down).

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

# Ledge Test Plan (Route 37)
- Observation: Ledges at (12, 3), (13, 3), (4, 7), (5, 7), (8, 7), (9, 7). Potential ledges at (14, 14), (15, 14).
- Hypothesis: LEDGE_HOP_DOWN is a one-way jump South.
- Test: 1. Move to (12, 2). 2. Walk Down. 3. Attempt to walk Up.
- Conclusion: Pending.