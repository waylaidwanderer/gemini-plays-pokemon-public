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
- Johto League Champion: Confirmed.
- Kanto Badges: 16/16.
- Red Defeated: Turn 44045.

# Task: Legendary Hunt
- Start Turn: 44154
- Current Turn: 44183
- Objective: Capture Raikou, Entei, and Suicune.
- Priority: Raikou (Master Ball).
- Method: Ecruteak Shuffle (Route 37).

# Time Tracking
- Legendary Hunt Start: Turn 44154
- Current Progress: Navigating Fly Map to Ecruteak City.

# Mt. Silver Completion
- Note: Hypothesis: Entrance lobby at (9, 33) appears isolated from the rest of the room by ledges and barriers. Unseen tiles (0, 35) and (19, 35) were unreachable from this entrance in tested paths. Pathing via Room 2 or other warps remains unverified.

# Legendary Hunt Strategy
- Priority: Raikou (Speed).
- Method: Cycle between Ecruteak City and Route 37 gates.
- Ball: MASTER BALL.
- Lead: XENON (Haunter) for Hypnosis (if needed).

# Lessons Learned
- Precise menu navigation is critical; verify menu state before long sequences.
- FLOOR_UP_WALL tiles block movement North (Up) AND block entry from the North (Down).
- Silver Cave Outside has only two main warps (Poke Center and Room 1 entrance).
- Mt. Silver Room 1 has an isolated entrance area; the rest of the room must be accessed via Room 2 or another unknown path.
- PC Storage: Parties must have space before withdrawing; always deposit first if at 6/6.
- Fly Usage: Must be outdoors to use Fly.
- Menu Memory: The menu remembers the last selected option (e.g., PACK instead of POKEMON). Verify cursor position.
- Map Navigation: Mt. Silver is at the far west of Johto. Flying to Ecruteak requires moving East on the Town Map.