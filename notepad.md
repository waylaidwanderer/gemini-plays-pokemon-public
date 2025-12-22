# Suicune Hunt Strategy & Status
- Strategy: Repel Trick (Lead KIMCHI Lv 21 vs Wild Lv 13-16).
- Method: Pacing (Grass Dance) in grass at (28, 7) on Route 38.
- Battle Plan: Turn 1 Sleep Powder. Use `suicune_capture_analyst_v2`.
- Active Status: Super Repel active (Turn #12835). 8 left.
- Safeguard: Re-verify Suicune location via Pokédex after crossing map boundaries.
- Tracking: Suicune last confirmed on Route 38 (Turn #12804). Re-verifying now due to stagnation (Turn #12845).
- Strategy: Use `check_suicune_location_v2` -> Confirm Route -> Resume Grass Dance or Boundary Dance.

# Route 38 Specific Notes
- TALL_GRASS at (28, 7): Pacing spot for Suicune.
- Gatehouse to Ecruteak City: Warp at (35, 8).

## Roaming Pokémon Reference
- Tracking: Walk across map boundaries to shift position predictably. Do NOT fly.
- Encountering: Repel Trick + pacing in grass.
- Capture: Sleep status on Turn 1. HP and Status are preserved between encounters.
- Movement: Shift routes ONLY when player crosses a map boundary or after a battle with the roamer. Phone calls do NOT move roamers.

## Tile Mechanics
- TALL_GRASS: Traversable. Triggers wild encounters. Repel Trick works here.
- FLOOR: Traversable.
- WALL: Impassable.
- LEDGE_HOP: One-way traversable (Down/Left/Right).
- WARP_CARPET: Traversable. Triggers map transition.

# PC Storage (Box 1)
- ROCKY (Onix Lv 6), EGG (Cleffa Lv 5), XFDW (Meowth Lv 16), FRITTATA (Togepi Lv 5), SHUCKIE (Shuckle Lv 15).

# General Lessons Learned
- Repel Refresh: If game incorrectly claims Repel is active after wearing off, move 1 step to reset state.
- Menu Navigation: Pokédex AREA: Press 'A' on entry -> move to 'AREA' -> press 'A'.
- Menu Scrolling: Scrolling is not always linear; verify cursor position visually.

# Suicune Capture Strategy Detail
- Lead: Gloom (KIMCHI) with Sleep Powder.
- Status: Sleep is best.
- Analyst: Use `suicune_capture_analyst_v2` for catch odds.