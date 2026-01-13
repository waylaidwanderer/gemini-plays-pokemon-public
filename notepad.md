# Tile Mechanics
- FLOOR_UP_WALL: Blocks entry from North, allows entry from South (Verified Row 50 blocks south entry).
- BUOY: Impassable water obstacle.
- LEDGE_HOP_DOWN: One-way jump South.
- LEDGE_HOP_RIGHT: One-way jump East.

# Suicune Quest
- Status: Tracking sightings in Johto.
- Current Objective: Cianwood City sighting at (7, 4).
- Timeline: Started Turn 46373. Current Turn 46442.
- Repel Status: Super Repel active (Turn 46441).

# Legendary Battle Strategy: Suicune
- Lead: XENON (Haunter, Lv 44).
- Strategy: Use Hypnosis immediately. Chip with Night Shade x2 (fixed 88 dmg). Maintain Sleep.
- Analysis: Suicune (~140 HP) will be in red/yellow after 2 Night Shades. 
- Backup: KIMCHI (Gloom) for Sleep Powder. GORP (Snorlax) as tank.

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

# Reflection Turn 46442
1. Immediate Execution: Super Repel used. Pathfinding tool fixed.
2. Notepad Hygiene: Removed redundant milestones. Added Repel Status and Reflection section.
3. Map Hygiene: Markers for Surf launch and Suicune area are set.
4. Automation Strategy: Using find_path_v7_robust for long treks.
5. Goal Clarity: Objective is (7, 4). Method is Surfing with Repel.
6. Error Analysis: Stagnation caused by wild encounters and phone calls. Resolved with Repel. Found that stepping on land cancels Surf.

# Navigation Log
- Turn 46441: Used Super Repel (18 left).
- Turn 46442: Heading to (12, 28) to re-initiate Surf.