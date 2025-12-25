# Strategy: Suicune Hunt (Crystal)
- Sequence: 1. Burned Tower (Done) -> 2. Cianwood (Done) -> 3. Route 42 (Done) -> 4. Route 38 -> 5. Route 14 -> 6. Tin Tower.
- Battle Plan (Tin Tower): 1. Hypnosis, 2. Night Shade (Fixed 21 dmg), 3. Catch.
- Hunt started Turn 20250.
- Fly attempt to Ecruteak started Turn 20482.

# Side Quests & Resources
- Quick Claw: National Park (34, 12). NE section lady. Only present Mon/Wed/Fri/Sun. (Unavailable Thurs/Tues/Sat due to Contest).
- Phone Contacts: Arnie (Bug Catcher) wants Snubbull.
- Clear Bell: In Key Items.
- Sick Miltank: Needs Berries.
- Thunderstone: Obtained Turn 20360.

# Suicune Sighting Logic
- Observed Sightings: 1. Burned Tower -> 2. Cianwood City -> 3. Route 42 -> 4. Route 38 (Current).
- Trigger Condition: Approach Suicune in the overworld to trigger flee.
- Route 38 Potential Locations: 
  - (31, 15) - Eastern Ledge (Checked).
  - (1, 3) - Western Pocket (Target).
  - (5, 8) - Near farm (Checked).

# Tile Mechanics (Verified)
- FLOOR: Traversable.
- WALL / FENCE: Impassable.
- LEDGE_HOP_DOWN: One-way South.
- LEDGE_HOP_LEFT: One-way West.
- LEDGE_HOP_RIGHT: One-way East. (Confirmed at 21, 12).
- TALL_GRASS: Traversable, encounters.
- HEADBUTT_TREE: Impassable.
- WARP_CARPET: Map transition.

# Route 38/39 Mechanics & Exploration
- Pathing Insights:
  - Southern Path (Row 14-16) is reachable from the North via ledges (Row 13) and has an exit North at (9, 14).
  - Top Lane Western Pocket (X=0-2) is isolated from the rest of Route 38 by walls at Row 7 and X=3. 
  - Route 39 Wall: A wall at (16, 6) blocks east-west travel on Row 6.

# Lessons Learned
- Fly Mechanics: Fly can only be used in towns or cities. Cannot be used on Routes.
- LEDGE_HOP_DOWN is one-way South. Do not plan North paths through them.
- If an area seems isolated, check adjacent maps for alternative entrances.
- Thursday/Tuesday/Saturday: Bug Catching Contest active. National Park NPCs are replaced.
- Markers: Always keep markers for physical constraints (e.g., ledge pockets) to assist pathfinding tools.