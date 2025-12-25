# Suicune Hunt Strategy (Crystal)
- Status: SCRIPTED (Route 38). Sighting #4. Suicune is stationary near the Miltank farm and will not move until approached.
- Lead: XENON (Gastly Lv21). Moves: Mean Look, Hypnosis.
- Strategy: Trigger flee on Route 38 (Northern strip), then battle at Tin Tower.
- Battle Plan: 1. Hypnosis, 2. Night Shade (Fixed 21 dmg), 3. Catch.

# Quick Claw Quest
- NPC: Teacher sitting on a bench.
- Hypothesis: NPC located at (16, 12) in National Park (Source: expert agent).
- Time: Present at all times (Morning, Day, Night).
- Note: Return during the day to verify hypothesis.

# Swarms & Rematches
- Yanma Swarm: Route 35 (Arnie). Triggered Turn 19540.
- Schoolboy Alan: Route 36 (Rematch).

# Tile Mechanics (Verified)
- FLOOR: Traversable.
- WALL: Impassable.
- LONG_GRASS: Traversable, low encounter rate.
- TALL_GRASS: Traversable, higher encounter rate.
- WARP_CARPET: Traversable, map transition.
- LEDGE_HOP_DOWN: Traversable, one-way (Down).
- LEDGE_HOP_LEFT: Traversable, one-way (Left).
- LEDGE_HOP_RIGHT: Traversable, one-way (Right).
- HEADBUTT_TREE: Impassable, Headbutt for encounters.
- DOOR: Traversable, map transition.

# Lessons Learned
- NPC Verification: Never trust agent coordinates over the Game State 'Map Objects On Screen' list.
- Loop Prevention: If stuck in a pathing loop, re-verify collision data and NPC presence manually.
- Suicune Mechanics: In Crystal, Suicune follows a fixed scripted path and only roams after the Tin Tower event.

# Resources & PC Inventory
- Poke Balls: 1 Ultra, 23 Great, 2 Poke.
- Items: 3 Super Repels, 1 Max Ether, 1 Max Revive, 2 Lemonades.
- Key Items: Clear Bell (Required for Suicune at Tin Tower).
- PC Box 1 (10/20): RICOTTA, CINNABAR, VORTEX, INTERCEPT, ROCKY, EGG, XFDW, FRITTATA, SHUCKIE, Blarney.

# Suicune Route 38 Investigation
- Observation: Route 38 has an isolated western pocket (x=0-2, Row 0-2) blocked by a wall at x=3.
- Hypothesis: Suicune is hiding in this pocket.
- Test: Enter Route 38 (0, 6) from Route 39 (19, 6) and check (2, 2).
- Current Status: Finding path to Route 39 (19, 6).