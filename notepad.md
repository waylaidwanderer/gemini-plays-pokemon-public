# Suicune Quest (Crystal) - PROGRESS
- Milestone 1-4: Sightings complete (Burned Tower, Cianwood, Route 42, Route 36).
- Milestone 5: Tin Tower battle engaged. Suicune is now roaming.
- Status: Roaming. Goal: Catch Suicune.

# General Mechanics
- Tile Mechanics:
    - FLOOR, TALL_GRASS, CAVE, GRASS, SAND, STAIRS, DOCK, WARP, STAIRCASE, ICE, WHIRLPOOL, WATER (with Surf), DIRT, PATH, DOOR, WARP_CARPET_DOWN: Traversable.
    - WALL, COUNTER, MART_SHELF: Impassable.
    - LEDGE: One-way (hop down).
- Navigation:
    - Paths are often wider than one tile; navigate around NPCs/objects.
    - Interacting with clerks: Face the counter tile in front of them and press A.
    - Phone calls: Wait for "Click!" or "……" before resuming movement.
    - Always verify collision types (e.g., MART_SHELF, COUNTER) in pathfinding tools.
- Goldenrod Dept. Store: 2F (Basic), 3F (Battle items), 4F (Vitamins), 5F (TMs).

# Suicune Hunt Strategy
- **Objective**: Catch Suicune (Level 40).
- **Battle Plan**:
    - Lead with XENON (Gastly, Lv21).
    - Turn 1: MEAN LOOK (prevents fleeing).
    - Turn 2+: HYPNOSIS (Sleep), then chip damage and ULTRA BALLS.
    - Note: Mean Look must hit before Suicune acts.
- **Encounter Loop**:
    1. Check Pokedex AREA map.
    2. Transition between a city and a route (e.g., Ecruteak and Route 38).
    3. Suicune relocates every time you cross a map boundary.
    4. When Suicune is on your current route, use a Super Repel and search the grass.
- **Inventory Check**: Need Super Repels (available at Goldenrod Dept. Store).

# PC Storage (Box 1)
- RICOTTA (RATICATE 16), CINNABAR (GOLDEEN 21), VORTEX (POLIWAG 22), INTERCEPT (YANMA 12), ROCKY (ONIX 6), EGG (CLEFFA 5), XFDW (MEOWTH 16), FRITTATA (TOGEPI 5), SHUCKIE (SHUCKLE 15), Blarney (SUDOWOODO 20).

# Lessons Learned
- Cannot use FLY from inside buildings; must be outdoors.
- Roaming Pokemon (Suicune) relocate upon EVERY map transition.
- FLYING forces roaming Pokemon to a completely random location in Johto.
- Poké Mart inventories scale with Badge progress; Super Repels NOT available at Ecruteak Mart even with 7 badges. Checking Goldenrod Dept. Store.
- Interacting with clerks behind counters: Face the counter tile, not the NPC.
- City Navigation: Buildings create complex layouts; use pathfinding tools to find non-obvious routes.

# Menu Mechanics
- Gen 2 menus remember the last selected item. Use "homing" (pressing Up 8 times) to reset the cursor to the top before navigating.

# Suicune Speed Concern
- Suicune (Lv 40) is likely faster than XENON (Lv 21). Mean Look only works if we move first. Need to level up XENON or use items/strategy to boost Speed.