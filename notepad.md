# Strategy: Suicune Hunt (Crystal)
- Sequence: 1. Burned Tower (Done) -> 2. Cianwood (Done) -> 3. Route 42 (Done) -> 4. Route 38 -> 5. Route 14 -> 6. Tin Tower.
- Battle Plan (Tin Tower): 1. Hypnosis, 2. Night Shade (Fixed 21 dmg), 3. Catch.

# Side Quests & Resources
- Quick Claw: National Park (34, 12). Lady in NE. Only present Mon/Wed/Fri/Sun. (Unavailable Thurs/Tues/Sat due to Contest).
- Phone Contacts: Arnie (Bug Catcher) wants Snubbull.
- Clear Bell: In Key Items.
- Sick Miltank: Needs Berries.
- Arthur (Hard Stone): Route 36. Thursday only. (Today!)

# Suicune Sighting Logic
- Observed Sightings: 1. Burned Tower -> 2. Cianwood City -> 3. Route 42 -> 4. Route 38 (Current).
- Trigger Condition: Approach Suicune in the overworld.
- Route 38 Potential Locations: 
  - Eastern end near Ecruteak Gatehouse (Targeting unseen tiles).
  - (1, 3) - Western Pocket (Isolated, requires investigation of access).
  - Ledge area near farm: (6, 13) or (7, 10-12).

# Tile Mechanics (Global)
- FLOOR: Standard traversable tile.
- WALL / FENCE: Impassable collision.
- LEDGE_HOP_DOWN: One-way jump South.
- LEDGE_HOP_LEFT: One-way jump West.
- LEDGE_HOP_RIGHT: One-way jump East.
- TALL_GRASS: Traversable; triggers wild encounters.
- HEADBUTT_TREE: Impassable; can be interacted with using Headbutt.
- WARP_CARPET: Triggers map transition.

# Game Mechanics & Systems
- Day/Night Cycle: Affects Pokemon spawns and NPC availability.
- Bug Catching Contest: Tues/Thurs/Sat in National Park. Replaces NPCs; Quick Claw unavailable.
- Fly Mechanics: Only usable in cities/towns.
- Money Management: Current ¥373.

# Route 38/39 Mechanics & Exploration
- Verified Map Connections:
  - Southern Path (Row 14-16) is reachable from North via Row 13 ledges. Exit North at (9, 14).
  - Western Pocket (X=0-2, Row 1-6) on Route 38 is isolated by walls at X=3 and Row 7.
  - Route 39 North-South: Row 7 wall has a gap at X=12.
  - Route 39 East-West: Row 6 wall at X=16 blocks travel. Bypass via Row 5 or 8.

# Lessons Learned
- Tool Hygiene: Trust find_path_v2 failures as evidence of obstructions.
- Exploration: Check all reachable unseen tiles before declaring a dead end.
- Hallucination Note: Stopped obsessing over Western Pocket; focusing on route perimeter and ledges.