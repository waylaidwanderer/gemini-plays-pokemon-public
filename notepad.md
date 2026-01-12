# Tile Mechanics
- FLOOR: Standard ground. Traversable.
- WALL: Collision block. Impassable.
- Grass: Encounter area. Traversable.
- Water: Requires Surf to traverse.
- Ledge: One-way jump. Traversable from specific direction.
- FLOOR_UP_WALL: Floor tile with a wall boundary to the north. Blocks movement North (exit). Entry from North (Down) needs testing.
- LEDGE_HOP_DOWN: One-way ledge. Jump Down only.
- LEDGE_HOP_RIGHT: One-way ledge. Jump Right only.
- LEDGE_HOP_LEFT: One-way ledge. Jump Left only.

# Pokemon Information (Movesets)
- KIMCHI (Gloom): Flash, Petal Dance, Cut, Sleep Powder.
- XENON (Haunter): Hypnosis, Confuse Ray, Night Shade, Dream Eater.
- Calcifer (Typhlosion): Flamethrower, Return, Smokescreen, Thunderpunch.
- GORP (Snorlax): Surf, Rest, Body Slam, Rollout.
- GNEISS (Graveler): Earthquake, Defense Curl, Strength, Rollout.
- ICARUS (Pidgeotto): Fly, Sand-Attack, Gust, Quick Attack.

# Major Achievements
- Johto League Champion: Turn 38104.
- Kanto Badges: 16/16.
- Red Defeated: Turn 44045.

# Task: Legendary Hunt
- Start Turn: 44154
- Ecruteak Shuffle Start: Turn 44185
- Objective: Capture Raikou, Entei, and Suicune.
- Priority: Raikou (Master Ball).
- Method: Ecruteak Shuffle (Route 37).
- Note: Need to encounter Raikou/Entei once in the wild for them to appear on the Pokegear Map.
- Suicune Strategy: Static encounter at Tin Tower in Crystal. Requires Clear Bell (in inventory).

# Legendary Hunt Strategy
- Priority: Raikou (Speed).
- Method: Cycle between Ecruteak City and Route 37 gates.
- Ball: MASTER BALL.
- Lead: ICARUS (Lv 19) with Repel to filter for Lv 40 Roamers.
- Backup Lead: XENON (Haunter) for Hypnosis (if Master Ball is saved).
- Observed Roamer Movesets: (None yet)

# Lessons Learned
- Precise menu navigation is critical; verify menu state before long sequences.
- FLOOR_UP_WALL tiles block movement North (Up) AND block entry from the North (Down).
- PC Storage: Parties must have space before withdrawing; always deposit first if at 6/6.
- Fly Usage: Must be outdoors to use Fly.
- Menu Memory: The menu remembers the last selected option (e.g., PACK instead of POKEMON). Verify cursor position.
- Suicune (Crystal): Suicune is NOT a roamer in Crystal; it is found at Tin Tower. Route 37 is for Raikou/Entei.
- Repel Trick: Use a lead Pokémon with a level between the local wild encounters and the target legendary (e.g., Lv 19 Pidgeotto for Lv 40 Roamers on Route 37).
- Menu Order: POKEDEX, POKEMON, PACK, POKEGEAR, GEM, SAVE, OPTION, EXIT. Up from GEM is POKEGEAR.