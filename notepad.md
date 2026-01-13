# Tile Mechanics
- FLOOR_UP_WALL: Blocks entry from North, allows entry from South (Verified Row 50 blocks south entry).
- BUOY: Impassable water obstacle.
- LEDGE_HOP_DOWN: One-way jump South.
- LEDGE_HOP_RIGHT: One-way jump East.

# Suicune Quest
- Status: Tracking sightings in Johto.
- Current Objective: Cianwood City sighting at (7, 4).
- Timeline: Started Turn 46373. Current Turn 46463.
- Repel Status: Super Repel active (Turn 46460).

# Legendary Battle Strategy: Suicune
- Lead: XENON (Haunter, Lv 44).
- Strategy: Use Hypnosis immediately. Chip with Night Shade x2 (fixed 88 dmg). Maintain Sleep.
- Analysis: Suicune (~140 HP) will be in red/yellow after 2 Night Shades. 
- Backup: KIMCHI (Gloom) for Sleep Powder. GORP (Snorlax) as tank with Body Slam (paralysis) / Rest.
- Catch: Ultra Balls (32) while asleep.

# Strategy: Capture all Legendary Pokemon
- Requirements: Clear Bell (Owned), 16 Badges (Owned).
- Plan: Complete sightings -> Tin Tower -> Capture Suicune.

# Pokemon Movesets
- XENON (Haunter): Hypnosis, Confuse Ray, Night Shade, Dream Eater.
- Calcifer (Typhlosion): Flamethrower, Return, Smokescreen, Thunderpunch.
- KIMCHI (Gloom): Flash, Petal Dance, Cut, Sleep Powder.
- GNEISS (Graveler): Earthquake, Defense Curl, Strength, Rollout.
- GORP (Snorlax): Surf, Rest, Body Slam, Rollout.
- ICARUS (Pidgeotto): Fly, Sand-Attack, Gust, Quick Attack.

# Reflection Turn 46463
1. Immediate Execution: Super Repel active. Pathfinder fixed for surfing.
2. Notepad Hygiene: Cleaned up redundant logs per overwatch.
3. Map Hygiene: Suicune sighting marker at (7, 4).
4. Automation Strategy: Using updated pathfinder to navigate BUOY gaps.
5. Goal Clarity: Reach (7, 4).
6. Error Analysis: Looping at (23, 10) caused by pathfinder ignoring BUOYs due to 'unseen' logic. Fixed.

# Navigation Log
- Turn 46463: Surfing at (27, 4). Zig-zagging through BUOY gaps to (7, 4).