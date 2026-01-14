# Tile Mechanics
- FLOOR: Standard walkable ground.
- WATER: Traversable only while Surfing (requires HM03).
- BUOY: Impassable water obstacle.
- WALL: Impassable obstacle.
- FLOOR_UP_WALL: One-way barrier (Ledge). Blocks movement Up (North) and usually allows jumping Down (South).
- LEDGE_HOP_DOWN: One-way jump South.
- Interaction: To Surf, face WATER from an adjacent FLOOR tile and press A. Stepping onto FLOOR from WATER automatically ends Surfing.

# Suicune Quest
- Status: Tracking sightings in Johto.
- Current Objective: Cianwood City sighting at (7, 4).
- Start Turn: 46373.
- Strategy (The "How"):
    1. Walk to Surf Point: (11, 19) -> (11, 16) -> (13, 16).
    2. Surf Point: Face Right at (13, 16) and launch into WATER at (14, 16).
    3. Eastern Loop: Surf South to Y=30 to bypass the buoy wall at X=16.
    4. Land Gap: Land at (15, 30), walk to (19, 30), then Surf again at (20, 30).
    5. Northern Reach: Surf Right to X=23, North to Y=8, then Left to (19, 8).
    6. Landing: Surf Down to (19, 11) and land at (16, 11).
    7. Sighting: Walk from (16, 11) to (7, 4) to trigger cutscene.
- Note: This is a sighting event, not a battle. Suicune will run away.

# Strategy: Capture all Legendary Pokemon
- Requirements: Clear Bell (Owned), 16 Badges (Owned).
- Plan: Complete sightings -> Tin Tower -> Capture Suicune (Lv 40).

# Pokemon Movesets
- XENON (Haunter): Hypnosis, Confuse Ray, Night Shade, Dream Eater.
- Calcifer (Typhlosion): Flamethrower, Return, Smokescreen, Thunderpunch.
- KIMCHI (Gloom): Flash, Petal Dance, Cut, Sleep Powder.
- GNEISS (Graveler): Earthquake, Defense Curl, Strength, Rollout.
- GORP (Snorlax): Surf, Rest, Body Slam, Rollout.
- ICARUS (Pidgeotto): Fly, Sand-Attack, Gust, Quick Attack.

# Lessons Learned
- Tool Over-engineering: Avoid spending excessive turns refining pathfinding tools for clear routes. Prioritize manual movement.
- Sighting vs Battle: Always verify if an encounter is a static battle or a scripted sighting to avoid unnecessary preparation.