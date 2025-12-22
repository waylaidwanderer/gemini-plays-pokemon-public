# Suicune Tracking & Strategy
- Status: Roaming. Confirmed on Route 37 (Turn #12216).
- Strategy: Lead with KIMCHI (Gloom Lv 21). Use Super Repel to filter encounters (Repel filters < Lv 21, Suicune is Lv 40).
- Encounter Method: Pacing (Grass Dance). Note: SWEET SCENT ignores REPEL and pulls low-level Pokemon.
- Battle Plan: Sleep Powder (Turn 1) -> Switch/Ball (Turn 2+). Use `suicune_capture_analyst` for capture optimization.

# Active Hunt Status
- Super Repel active: Started Turn #12222. Expired Turn #12259.
- Current Location: Route 37 tall grass (8, 2).
- Pacing count: ~170 steps taken before expiration.
- Safeguard: Re-verify Suicune's location via Pokédex after every battle and every 50 steps.
- Encounter Strategy: Use pacing (Grass Dance) with Repel trick. Avoid SWEET SCENT.
- Battle Plan: Sleep Powder (Turn 1) -> Switch/Ball (Turn 2+). Use `suicune_capture_analyst` for capture optimization.

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