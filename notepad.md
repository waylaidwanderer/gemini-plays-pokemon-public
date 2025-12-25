# Strategy: Suicune Hunt (Crystal)
- Sequence: 1. Burned Tower (Done) -> 2. Cianwood (Done) -> 3. Route 42 (Done) -> 4. Route 38 -> 5. Route 14 -> 6. Tin Tower.
- Battle Plan (Tin Tower): 1. Hypnosis, 2. Night Shade (Fixed 21 dmg), 3. Catch.
- Hunt Progress: Searching Route 38 for scripted sighting.

# Side Quests & Resources
- Arthur (Hard Stone): Route 36. Thursday only. Attempted, dialogue looped. Re-evaluate if needed.
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

# Game Mechanics & Systems
- Day/Night Cycle: Affects spawns and NPCs.
- Bug Catching Contest: Tues/Thurs/Sat in National Park. Replaces NPCs.
- Fly Mechanics: Only usable in cities/towns.
- Money Management: Current ¥373.

# Route 38/39 Mechanics & Exploration
- Southern Path (Row 14-16) reachable via Row 13 ledges. Exit North at (9, 14).
- Route 39 North-South: Row 7 wall has a gap at X=12.
- Suicune Trigger: Scripted overworld sighting. Search northern fence line and ledges.

# Lessons Learned
- Tool Hygiene: Trust find_path_v2 failures as evidence of obstructions.
- Exploration: Check all reachable unseen tiles before declaring a dead end.
- Arthur: Dialogue loops if gift criteria not met.
- Suicune: Scripted sighting, not a random roam yet.

# Time Tracking
- Suicune Hunt (Route 38): Started Turn 20250.
- Arthur Hunt: Started Turn 20530.