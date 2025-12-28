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
- Verifying Eusine status in Cianwood City: Started Turn 27474.
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
- Navigation (Cianwood): The northern shore is segmented by walls and buoys. Surfing far east is required to bypass the buoy barrier and reach the northernmost edge.
- Tool Hygiene: Fixed find_path_v8 to handle XML root being the Map element.

# Navigation - Path to Tin Tower
1. Ecruteak City (18, 11) -> Enter Gatehouse (4_1).
2. Gatehouse (5, 3) [Ladder] -> Gatehouse (17, 15).
3. Gatehouse (17, 3) [Warp] -> Wise Trio Room (4_2) (1, 4).
4. Wise Trio Room (7, 4) [Warp] -> Ecruteak Restricted Area (20, 2).
5. Restricted Area (20, 2) -> Walk East to (35, 6) -> Tin Tower Area (37, 7).
6. Enter Tin Tower 1F at (37, 7).