# Tile Mechanics
- FLOOR: Standard walkable ground.
- WATER: Traversable only while Surfing (requires HM03).
- BUOY: Impassable water obstacle.
- WALL: Impassable obstacle.
- FLOOR_UP_WALL: One-way barrier (Ledge). Blocks movement Up (North) and usually allows jumping Down (South).
- LEDGE_HOP_DOWN: One-way jump South.
- LEDGE_HOP_RIGHT: One-way jump East.
- Interaction: To Surf, face WATER from an adjacent FLOOR tile and press A. Stepping onto FLOOR from WATER automatically ends Surfing.

# Suicune Quest
- Status: Tracking sightings in Johto.
- Current Objective: Cianwood City sighting at (7, 4).
- Start Turn: 46373.
- Strategy (The "How"):
    1. Walk to Ledge: (11, 15) -> (11, 28) -> (4, 28) -> (4, 29).
    2. Jump Ledge: (4, 29) -> (4, 31).
    3. Walk to West Coast: (4, 31) -> (2, 31).
    4. Walk to Sighting Area: (2, 31) -> (2, 14) -> (7, 14) -> (7, 4).
- Note: Suicune in Cianwood is a sighting event, not a battle. No need for battle prep. No battle will occur here.

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
- Tool Over-engineering: Spent ~200 turns refining a multi-modal pathfinder for a task that could be solved with simple manual navigation. Prioritize movement over perfect automation when the path is clear.
- Root Hypothesis: Always re-verify connectivity assumptions (e.g., walls vs. ledges) before building complex plans around them.
- Suicune in Cianwood: This is a sighting event, not a battle. Avoid wasting resources on battle prep for this specific objective.