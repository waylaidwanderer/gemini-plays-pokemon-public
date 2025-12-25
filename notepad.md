# Strategy: Suicune Hunt (Crystal)
- Sequence: 1. Burned Tower (Done) -> 2. Cianwood (Done) -> 3. Route 42 (Done) -> 4. Route 38 -> 5. Route 14 -> 6. Tin Tower.
- Battle Plan (Tin Tower): 1. Hypnosis, 2. Night Shade (Fixed 21 dmg), 3. Catch.
- Hunt Progress: Searching Route 38 central/ledge area.

# Side Quests & Resources
- Arthur (Hard Stone): Route 36. Thursday only. (Today!) - PRIORITY
- Quick Claw: National Park (34, 12). Lady in NE. Only present Mon/Wed/Fri/Sun.
- Phone Contacts: Arnie (Bug Catcher) wants Snubbull.
- Clear Bell: In Key Items.
- Sick Miltank: Needs Berries.

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
  - Route 39 North-South: Row 7 wall has a gap at X=12.
  - Route 38 Suicune Event: Scripted proximity trigger near the farm/ledge area. (Approach row 8-12 near X=5-10). NO isolated pocket.

# Lessons Learned
- Tool Hygiene: Trust find_path_v2 failures as evidence of obstructions.
- Exploration: Check all reachable unseen tiles before declaring a dead end.
- Arthur (Hard Stone): Dialogue loops intro if item not given. Check bag space (15/20) and positioning.
- Suicune Trigger: Walk along the northern fence line/ledge on Route 38.

# Time Tracking
- Suicune Hunt (Route 38 sighting): Started Turn 20250. Current Turn 20588. 
- Arthur (Hard Stone) Hunt: Started Turn 20530. Current Turn 20588.