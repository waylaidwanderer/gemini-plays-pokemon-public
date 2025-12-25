# Suicune Hunt Strategy (Crystal)
- Status: SCRIPTED (Route 38). Start Turn: 19730.
- Lead: XENON (Gastly Lv21). Moves: Mean Look, Hypnosis.
- Strategy: Trigger flee on Route 38 (Northern strip), then battle at Tin Tower.
- Battle Plan: 1. Hypnosis, 2. Night Shade (Fixed 21 dmg), 3. Catch.

# Quick Claw Quest
- NPC: Teacher sitting on a bench.
- Coordinates: (16, 12) in National Park (Source: expert agent).
- Time: Present at all times (Morning, Day, Night).
- Note: If NPC is not visible in 'Map Objects' list at coordinates, they are not present.
- Checked (National Park): (17, 6) - Empty grass, (33, 11) - Empty grass, (35, 12) - Wall.

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

# Lessons Learned
- NPC Verification: Never trust agent coordinates (e.g., item_locator) over the Game State 'Map Objects On Screen' list.
- Loop Prevention: If stuck in a pathing loop, re-verify collision data and NPC presence manually.

# Resources & PC Inventory
- Poke Balls: 1 Ultra, 23 Great, 2 Poke.
- Items: 3 Super Repels, 1 Max Ether, 1 Max Revive, 2 Lemonades.
- Key Items: Clear Bell (Required for Suicune at Tin Tower).
- PC Box 1 (10/20): RICOTTA, CINNABAR, VORTEX, INTERCEPT, ROCKY, EGG, XFDW, FRITTATA, SHUCKIE, Blarney.