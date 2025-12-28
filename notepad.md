# Tile Mechanics - Global
- FLOOR: Standard walkable tile.
- WALL: Impassable boundary.
- WATER: Traversable only with Surf.
- BUOY: Impassable boundary in water.
- WARP_CARPET: Triggers map transition when walked off the map edge.
- HEADBUTT_TREE: Blocking object; can be interacted with using Headbutt.
- CUT_TREE: Blocking object; requires HM01 Cut and interaction from adjacent tile to remove.
- CAVE: Map transition entry point.
- TALL_GRASS: Walkable; triggers wild battles.
- LEDGE_HOP_DOWN: One-way jump down; impassable from below.

# Suicune Quest Strategy (Crystal)
- Phase Start: Turn 27180
- Exploration Phase Start: Turn 27390
- Tracking Wild Suicune Phase Start: Turn 27442 (Dec 27, 2025)
- Route 42 Sighting Attempt: Started Turn 27570.
- Key Items: Clear Bell (Acquired)
- Prerequisite Strategy: Eusine must be defeated at Cianwood City north shore before wild sightings on Route 42 and 36 will trigger. (Status: Verified, Eusine missing from shore).
- Route 42 Trigger: (26, 15) - Small clearing with 3 Apricorn trees outside Mt. Mortar middle entrance.
- Route 36 Trigger: Target location TBD.
- Final Encounter: Tin Tower (static battle) after all wild sightings.

## Battle Strategy (Wise Trio)
- Trio will only battle after Route 42 and 36 sightings are complete.
- Lead: GNEISS (Graveler) Lv44 (Earthquake, Rollout).

## Capture Strategy (Suicune)
- Suicune is a static encounter in Tin Tower (Crystal) at Lv40.
- Lead: XENON (Gastly) Lv21 (Hypnosis, Night Shade).
- **CRITICAL RISK:** Xenon is severely underleveled (Lv21 vs Lv40). Suicune will likely outspeed and KO Xenon before Hypnosis can be used. Consider training a faster/bulkier sleep inducer or using items to boost speed.
- Items: 43 Great Balls, 1 Ultra Ball.

## Lessons Learned
- Suicune Quest (Crystal): The quest is strictly gated. Eusine must be defeated in Cianwood before the Route 42 sighting triggers.
- Event Verification: If Eusine is missing from the Cianwood beach after Suicune flees, the battle flag is likely set.
- Navigation: Entering water costs 3 actions (Face/A, Confirm A, Move).
- Tool Hygiene: find_path_v9 refined to use Dijkstra for accurate cost estimation and 'seen' tile filtering.
- COUNTER: Impassable barrier often found in shops or gatehouses; allows interaction with NPCs behind it.

## Plan for Route 42 Sighting
1. Exit Route 42 Gatehouse at (9, 5).
2. Travel east on Route 42 to (26, 15).
3. Sighting should trigger automatically upon approaching the Apricorn trees.