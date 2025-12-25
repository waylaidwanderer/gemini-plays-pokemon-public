# Strategy: Suicune Hunt (Crystal)
- Sequence: 1. Burned Tower (Done) -> 2. Cianwood (Done) -> 3. Route 42 (Done) -> 4. Route 38 -> 5. Route 14 -> 6. Tin Tower.
- Battle Plan (Tin Tower): 1. Hypnosis, 2. Night Shade (Fixed 21 dmg), 3. Catch.
- Hunt started Turn 20250.

# Side Quests & Resources
- Quick Claw: National Park (34, 12). NE section lady. Only present Mon/Wed/Fri/Sun. (Unavailable today, Thursday).
- Phone Contacts: Arnie (Bug Catcher) wants Snubbull.
- Clear Bell: In Key Items.
- Sick Miltank: Needs Berries.
- Thunderstone: Obtained Turn 20360.

# Suicune Sighting Logic
- Observed Sightings: 1. Burned Tower -> 2. Cianwood City -> 3. Route 42 -> 4. Route 38 (Current).
- Trigger Condition: Suicune will be visible in the overworld at a specific coordinate. Approaching it triggers a flee and updates the tracker.
- Route 38 Potential Locations: 
  - (31, 15) - Ledge area (Checked).
  - (1, 3) - Western Pocket (Unexplored).
  - (5, 8) - Near farm (Checked).

# Tile Mechanics (Verified)
- FLOOR: Traversable.
- WALL / FENCE: Impassable.
- LEDGE_HOP_DOWN: One-way South.
- LEDGE_HOP_LEFT: One-way West.
- LEDGE_HOP_RIGHT: One-way East.
- TALL_GRASS: Traversable, encounters.
- HEADBUTT_TREE: Impassable.
- WARP_CARPET: Map transition.

# Route 38/39 Mechanics & Exploration
- Pathing Insights:
  - Southern Path (Row 14-16) is reachable from the North via ledges (Row 13) and has an exit North at (9, 14).
  - Top Lane Western Pocket (X=0-2) is isolated from the rest of Route 38 by walls at Row 7 and X=3. Entry point is Route 39 (19, 6) -> Route 38 (0, 6).
  - Middle Lane (Row 8-11) is the main thoroughfare.
- Exploration Status:
  - Western Pocket (X=0-2): Unexplored. Entry point: Route 39 (13, 8) -> (13, 6) -> (19, 6) -> Route 38 (0, 6).
  - Southern Path (Row 14-16, X=22-29): Unexplored. Isolated by ledge at Row 13.
- Current Plan: 
  1. Return to Route 39.
  2. Detour around the wall at (19, 7) by walking to (13, 8), then Up to Row 6.
  3. Walk East to (19, 6) and enter Route 38 (0, 6).
  4. Search Western Pocket (X=0-2) for Suicune sighting.
  5. Search Southern Path extension (X=22-29) if Suicune not found.
  6. Return to Ecruteak for Tin Tower (if flee triggered).