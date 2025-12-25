# Strategy: Suicune Hunt (Crystal)
- Sequence: 1. Burned Tower (Done) -> 2. Cianwood (Done) -> 3. Route 42 (Done) -> 4. Route 38 -> 5. Route 14 -> 6. Tin Tower.
- Battle Plan (Tin Tower): 1. Hypnosis, 2. Night Shade (Fixed 21 dmg), 3. Catch.
- Hunt started Turn 20250.

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
- LEDGE_HOP_DOWN: One-way jump South.
- LEDGE_HOP_LEFT: One-way jump West.
- LEDGE_HOP_RIGHT: One-way jump East.
- TALL_GRASS: Traversable, encounters.
- HEADBUTT_TREE: Impassable.
- WARP_CARPET: Map transition.

# Game Mechanics & Systems
- Day/Night Cycle: Affects Pokemon spawns and certain NPC events.
- Bug Catching Contest: Active Tues/Thurs/Sat in National Park. Replaces NPCs and restricts movement. Quick Claw lady is absent during contests.
- Fly Mechanics: Only usable in cities/towns.
- Money: Current ¥373.

# Route 38/39 Mechanics & Exploration
- Pathing Insights:
  - Southern Path (Row 14-16) is reachable from the North via ledges (Row 13) and has an exit North at (9, 14).
  - Top Lane Western Pocket (X=0-2) is isolated from the rest of Route 38 by a vertical wall at X=3. Access is ONLY via Route 39 Row 6.
  - Route 39 Wall: A wall at (16, 6) blocks east-west travel on Row 6; bypass via Row 5.
  - Route 39 Wall: A wall at Row 7 (X=16-19) blocks north-south travel; bypass via X=15.

# Lessons Learned
- Reflection Note: navigate_fly_map tool returned 'Down' for Olivine->Ecruteak, which is incorrect (Ecruteak is Right/Up). Tool needs refinement.
- Root Hypothesis Check: Verified that Route 38 Western Pocket is reachable via Route 39 North -> Route 38 West. Previous "isolated" belief was due to ledges; northern path is the way.