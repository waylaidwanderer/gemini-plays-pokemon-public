# Tile Mechanics
- FLOOR_UP_WALL: Blocks entry from North, allows entry from South.
- BUOY: Impassable water obstacle.
- LEDGE_HOP_DOWN: One-way jump South.
- LEDGE_HOP_RIGHT: One-way jump East.

# Suicune Quest
- Status: Tracking sightings in Johto.
- Current Objective: Cianwood City sighting at (7, 4).
- Timeline: Started Turn 46373. Current Turn 46437. (Attempted land route 46375-46395; surfing since 46396).

# Major Milestones & Discoveries
- [Turn 46375-46395]: Land route to West Cianwood blocked by rocks and ledges.
- [Turn 46396-46408]: Switched to Surfing strategy. Accessed water at (27, 45) and (12, 28).

# Legendary Battle Strategy: Suicune
- Lead: XENON (Haunter, Lv 44).
- Strategy: Use Hypnosis immediately. Chip with Night Shade x2 (fixed damage). Maintain Sleep. Throw Ultra Balls.
- Backup: KIMCHI (Gloom) for Sleep Powder. GORP (Snorlax) as tank with Body Slam/Rest.

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

# Navigation Lessons
- Turn 46431: Phone calls can interrupt movement from `find_path_v7_robust` with `autopress_buttons: true`.
- Tile Mechanics: Stepping onto land (FLOOR) from WATER immediately stops the Surfing state.

# Strategy: Navigation Stagnation Mitigation
- Observation: Wild Tentacool and phone calls are interrupting the long Surf trek to (7, 4).
- Action: Use Super Repel before surfing.
- Status: Super Repel x18 in inventory.

# Tile Mechanics Test: FLOOR_UP_WALL
- Hypothesis: Blocks entry from North, allows entry from South.
- Test Plan: Attempt to walk North from (12, 51) to (12, 50) (South to North) and South from (12, 50) to (12, 51) (North to South).
- Conclusion: Pending.