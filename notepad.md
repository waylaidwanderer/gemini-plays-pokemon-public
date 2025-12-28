# Tile Mechanics - Global
- FLOOR: Standard walkable tile.
- WALL: Impassable boundary.
- WATER: Traversable only with Surf.
- BUOY: Impassable boundary in water.
- WARP_CARPET: Triggers map transition when walked off the map edge.
- HEADBUTT_TREE: Can be interacted with using Headbutt.
- CUT_TREE: Blocking object; requires HM01 Cut and interaction from adjacent tile to remove.
- CAVE: Map transition entry point.
- TALL_GRASS: Walkable; triggers wild battles.
- LEDGE_HOP_DOWN: One-way jump down; impassable from below.

# Suicune Quest Strategy (Crystal)
- Phase Start: Turn 27180
- Exploration Phase Start: Turn 27390
- Tracking Wild Suicune Phase Start: Turn 27442 (Dec 27, 2025)
- Key Items: Clear Bell (Acquired)
- Prerequisite Strategy: Eusine must be defeated at Cianwood City north shore before wild sightings on Route 42 and 36 will trigger.
- Route 42 Trigger: (26, 15) - Small clearing with 3 Apricorn trees.
- Route 36 Trigger: Location TBD.
- Final Encounter: Tin Tower (static battle) after all wild sightings.

## Battle Strategy (Eusine - Cianwood)
- Eusine's Team: Drowzee Lv23, Haunter Lv23, Electrode Lv25.
- Strategy: Lead with Calcifer (Typhlosion) Lv45. Flame Wheel for Drowzee/Haunter, Thunderpunch for Electrode.
- Note: Xenon (Lv21 Gastly) is too weak to lead.

## Battle Strategy (Wise Trio)
- Trio will only battle after Route 42 and 36 sightings are complete.
- Lead: GNEISS (Graveler) Lv44 (Earthquake, Rollout).

## Capture Strategy (Suicune)
- Suicune is a static encounter in Tin Tower (Crystal). 
- Lead: XENON (Gastly) Lv21 (Hypnosis, Night Shade).
- Items: 43 Great Balls, 1 Ultra Ball.

## Lessons Learned
- Suicune Quest (Crystal): The quest is strictly gated. Eusine must be defeated in Cianwood before the Route 42 sighting triggers. Missing this battle is a common cause of progress stalling.
- Navigation (Cianwood): The northern shore is reachable on foot via a western detour (X=2) to bypass the Y=15-18 walls, then heading north to Y=14, east to X=8, and north through the gap at (8, 13).
- Tool Hygiene: Refined find_path_v9 to handle Objects, Ledges, Warps, and 'seen' tiles. Outdated tools deleted.

## Task Log
- Verifying Eusine status in Cianwood City: Started Turn 27474. (Turn 27559: Back on land at (5, 18) heading for north shore).