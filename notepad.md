# Tile Mechanics
- FLOOR_UP_WALL: Hypothesis: Blocks entry from North, allows entry from South. (Test pending).
- BUOY: Impassable water obstacle.
- LEDGE_HOP_DOWN: One-way jump South.
- LEDGE_HOP_RIGHT: One-way jump East.

# Suicune Quest
- Status: Tracking sightings in Johto.
- Current Objective: Cianwood City sighting at (7, 4).
- Start Turn: 46373.
- Repel Status: Super Repel active (Turn 46460).
- Strategy (The "How"):
    1. From (12, 27), Surf North to (12, 20).
    2. Land at (11, 20).
    3. Walk North to (11, 12), then West to (4, 12), then North to (4, 4), then East to (7, 4).

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

# Navigation Notes
- Land route to West Cianwood is a maze of one-way walls and building blockades.
- Water route requires navigating gaps in BUOY lines at (16, 24), (23, 15), and (20, 9).
- Northern land mass at Row 10 is the intended landing zone for reaching (7, 4).

# Navigation Log
- Turn 46477: Arnie's phone call interrupted movement. Identified bug in find_path_v7_robust (is_surfing boolean parsing). Fixed. Resuming trek to (7, 4).