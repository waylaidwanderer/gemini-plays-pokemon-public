# Tile Mechanics - Global
- FLOOR: Standard walkable tile. Verified traversable.
- WALL: Impassable boundary. Verified impassable.
- WATER: Traversable only with Surf. Verified traversable with HM03.
- BUOY: Impassable boundary in water. Verified impassable.
- WARP_CARPET: Triggers map transition when walked off the map edge. Verified functional.
- HEADBUTT_TREE: Blocking object; can be interacted with using Headbutt. Verified impassable.
- CUT_TREE: Blocking object; requires HM01 Cut. Verified impassable until cut. Regrows on map reload.
- COUNTER: Impassable barrier often found in shops or gatehouses; allows interaction with NPCs behind it. Verified impassable.
- CAVE: Map transition entry point. Verified functional.
- TALL_GRASS: Walkable; triggers wild battles. Verified traversable.
- LEDGE_HOP_DOWN: One-way jump down; impassable from below. Verified one-way movement.

# Suicune Quest Strategy (Crystal)
- Sequence: Burned Tower (DONE) -> Cianwood North Shore (DONE) -> Route 42 (Middle Island) -> Route 36 (Sudowoodo area) -> Tin Tower (Wise Trio + Suicune Battle).
- Current Status: Wise Trio Room (4_2) is EMPTY. Sightings are NOT complete.
- Plan: 
  1. Reach Route 42 island (24, 12) to cut the tree at (24, 13).
  2. Step on (26, 15) on foot to trigger sighting.
  3. Travel to Route 36 (35, 9) on foot to trigger final sighting.
- Clear Bell: Required for final encounter. (Status: Acquired).

## Battle Strategy (Wise Trio)
- Sage Gaku: Noctowl (32), Flareon (32). Counter: GNEISS (Rollout/Earthquake).
- Sage Masa: Noctowl (32), Vaporeon (32). Counter: KIMCHI (Sleep Powder) or Calcifer (Thunderpunch).
- Sage Koji: Noctowl (32), Jolteon (32). Counter: GNEISS (Earthquake).

## Capture Strategy (Suicune)
- Static Lv40 encounter in Tin Tower.
- Lead: XENON (Gastly) Lv21 (Hypnosis). Risk: Underleveled.
- Plan: Use Night Shade for fixed damage, Hypnosis for status.
- Items: 43 Great Balls, 1 Ultra Ball.

# Lessons Learned
- Suicune Sighting Sequence: Strictly sequential. Eusine battle in Cianwood is a mandatory flag.
- Tin Tower Sages: Dialogue "Tin Tower shook" (Turn 27084) is triggered by Clear Bell, NOT by sighting completion. Do not use as a progress indicator.
- Wise Trio Room: If empty, sightings are incomplete.
- Strategy Pivot: Empty Wise Trio room overrides previous assumptions of completion. Return to wild sightings.
- Route 42 Trigger: (26, 15) is the clearing with three Apricorn trees. Must be reached on foot.
- Lesson: In Crystal, all outdoor sightings must be triggered before the Wise Trio appears.
## Suicune Sighting Attempt - Route 42
- Turn 27838: Arrived at (26, 15). Walking around the island to trigger cutscene.
- Systematic Patrol: (26, 15) -> (27, 14) -> (28, 15) -> (29, 15) -> (30, 15).
- Observation: Suicune not currently in Map Objects. Expecting scripted spawn.
- Turn 27843: Attempted sighting at Route 42 (26, 15). No cutscene triggered after walking over the coordinates. Moving to Route 36 to check for sighting there.
- Path: Fly to Ecruteak City -> Walk south to Route 36 Sudowoodo spot.