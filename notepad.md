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
    1. Surf through the eastern water corridor to Row 51.
    2. Land at (23, 51).
    3. Walk West to (4, 51), then North to (7, 4).

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
- Land route to West Cianwood is partitioned by FLOOR_UP_WALL lines. 
- Entry to the southern land mass is only possible from the eastern water at Row 51.
- Northern land mass landing zone is at (7, 10).