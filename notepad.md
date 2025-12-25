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
  - Western Pocket (X=0-2): Unexplored. Hypothesize reachability from northern path (Row 0-4) starting from Ecruteak.
  - Southern Path (Row 14-16, X=22-29): Unexplored. Isolated by ledge at Row 13.
- Current Plan: 
  1. Fly to Ecruteak City.
  2. Enter Route 38 and walk west along the northernmost path (Row 0-4).
  3. Search Western Pocket (X=0-2) for Suicune sighting near the farm.
  4. Trigger Suicune flee.
  5. Go to Tin Tower in Ecruteak City.
  6. Return to National Park on Mon/Wed/Fri/Sun for Quick Claw.

# Lessons Learned
- Route 39 Wall: A wall at (16, 6) blocks east-west travel on Row 6. The eastern edge (X=17-19) must be accessed from Route 38.
- Suicune Sighting #4: Located on Route 38, likely in the isolated western pocket near the Moomoo Farm.
- Thursday: Bug Catching Contest active. Standard National Park NPCs (like the Quick Claw teacher) are replaced.
- Navigation Loops: If a pathing tool fails or reports a loop, verify physical obstacles (walls, ledges) and reconsider the entry point for the area.