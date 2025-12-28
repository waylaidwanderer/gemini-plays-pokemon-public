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
- Sequence: Burned Tower -> Cianwood North Shore (Sighting + Eusine Battle) -> Route 42 (Middle Island) -> Route 36 (Sudowoodo area) -> Tin Tower (Wise Trio + Suicune Battle).
- Status: All sightings (Cianwood, Route 42, Route 36) confirmed completed via Sages' "tower shaking" dialogue (Turn 27084).
- Next Step: Defeat the Wise Trio in the Tin Tower Wise Trio Room (Map 4_2).
- Clear Bell: Required for Wise Trio to appear. (Status: Acquired).

## Battle Strategy (Wise Trio)
- Sage Gaku: Noctowl (32), Flareon (32). Counter: GNEISS (Rollout/Earthquake).
- Sage Masa: Noctowl (32), Vaporeon (32). Counter: KIMCHI (Sleep Powder) or Calcifer (Thunderpunch).
- Sage Koji: Noctowl (32), Jolteon (32). Counter: GNEISS (Earthquake).

## Capture Strategy (Suicune)
- Hypothesis: Lv40 static encounter in Tin Tower.
- Lead: XENON (Gastly) Lv21 (Hypnosis). Risk: Underleveled.
- Plan: Use Night Shade for fixed damage, Hypnosis for status.
- Items: 43 Great Balls, 1 Ultra Ball.

# Lessons Learned
- Suicune Sighting Sequence: Strictly sequential. Eusine battle in Cianwood is a mandatory flag.
- Tin Tower Sages: Dialogue "Tin Tower shook and a Pokemon must have returned to the top" (Turn 27084) confirms all sightings are done.
- Fly Map (Johto): A 2D grid, cursor movement depends on spatial relationship of cities. Tool navigate_fly_map_v2 is currently unreliable.
- Strategy Pivot: Sage dialogue overrides visual absence of Suicune if flags are set. Proceed to Wise Trio.