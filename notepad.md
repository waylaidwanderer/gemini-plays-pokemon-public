- Status: ROAMING. Snapshot via Pokedex 'Area'. Fly triggers a roaming move.
- Lead: XENON (Gastly Lv21). Moves: Mean Look, Hypnosis.
- Strategy: Boundary cycling between Route 38 and Ecruteak City.

# Suicune Battle Plan
- Turn 1: MEAN LOOK.
- Turn 2+: HYPNOSIS. (Priority: Keep asleep).
- Turn 3+: NIGHT SHADE. (Fixed damage 21).

# Quick Claw Quest
- NPC: Woman on a bench in the northeast section of National Park.
- Coordinates: Northeast corner. Conflicting info: (19,10) or (17,12). Trust agent's map bounds (20x27).
- Path: Enter National Park from Route 35 (3, 5). Head north through grass, then east along fence.

# Fly Map List (Order from New Bark Town)
1. New Bark Town, 2. Cherrygrove City, 3. Violet City, 4. Azalea Town, 5. Goldenrod City, 6. Ecruteak City, 7. Olivine City, 8. Cianwood City, 9. Mahogany Town, 10. Lake of Rage.

# Tile Mechanics (Verified)
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Surf required.
- TALL_GRASS: Encounters.
- HEADBUTT_TREE: Headbutt for encounters.
- LEDGE_HOP_DOWN: One-way (Down).
- CUT_TREE: Cut to remove.
- DOOR / WARP_CARPET: Map transition.

# Resources & PC Inventory
- Poke Balls: 1 Ultra, 23 Great, 2 Poke.
- Items: 3 Super Repels, 1 Max Ether, 1 Max Revive, 2 Lemonades.
- PC Box 1 (10/20): RICOTTA, CINNABAR, VORTEX, INTERCEPT, ROCKY, EGG, XFDW, FRITTATA, SHUCKIE, Blarney.

# Swarms & Rematches
- Yanma Swarm: Route 35 (Arnie, Turn 19540).
- Schoolboy Alan: Route 36 (Rematch).

# Reflection Turn 19627
- Immediate Execution: Recovered from 100-turn menu loop in Olivine. Corrected hallucinated coordinates (34,12) -> northeast area.
- Notepad Hygiene: Major reorganization performed. Removed meta-rules and redundant logs.
- Map Hygiene: Route 35 markers are up to date.
- Automation Strategy: find_path_v2 used for gatehouse exit. Will continue using for overworld.
- Goal Clarity: Objectives are outcome-focused. Method is to enter National Park, then find NPC.
- Error Analysis: Menu loops were caused by cursor persistence. Lesson: Always use "B-mash" and verify state. Coordinate hallucination identified and corrected.