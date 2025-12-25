# Strategy: Suicune Hunt (Crystal)
- Sequence: 1. Burned Tower (Done) -> 2. Cianwood (Done) -> 3. Route 42 (Done) -> 4. Route 38 -> 5. Route 14 -> 6. Tin Tower.
- Battle Plan (Tin Tower): 1. Hypnosis, 2. Night Shade (Fixed 21 dmg), 3. Catch.

# Side Quests & Resources
- Arthur (Hard Stone): Route 36. Thursday only. (Arthur dialogue looped Turn 20594, Hard Stone not in inventory).
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
- HEADBUTT_TREE: Impassable.
- WARP_CARPET: Triggers map transition.

# Route 38/39 Mechanics & Exploration
- Southern Path (Row 14-16) reachable via Row 13 ledges. Exit North at (9, 14).
- Route 39 North-South: Row 7 wall has a gap at X=12.
- Suicune Trigger: Scripted overworld sighting. Search northern fence line and ledges.

# Reflection (Turn 20608)
- Root Hypothesis Test: The "isolated pocket" theory was a false constraint. Conclusively disproved.
- Lesson: Prioritize mental map connectivity over visual intuition when planning routes around obstacles.
- Maintenance: Tool 'navigate_fly_map_v2' refined.
- Strategy: Walk the northern fence line (rows 8-9) and ledge area (X=5-15) to trigger scripted flee.