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
- FLOOR_UP_WALL: Collision type for walls that look like floor? Needs verification. (Present on Route 42).

# Suicune Quest Strategy (Crystal)
- Quest Phase Start: Turn 27180
- Current Status: Eusine's defeat in Cianwood verified at Turn 27735. Flying to Mahogany Town to thoroughly explore Route 42 middle island for Suicune sighting.
- Key Items: Clear Bell (Acquired)
- Prerequisite Strategy: Eusine must be defeated at Cianwood City north shore. (Status: Verified).
- Route 42 Trigger: (26, 15) - Small clearing with 3 Apricorn trees.
- Route 36 Trigger: (35, 9) - Near the junction where Sudowoodo was.
- Final Encounter: Tin Tower (static battle) after all wild sightings and Wise Trio battle.

## Time Tracking
- Suicune Quest Sequence: Started Turn 27180.
- Route 42 Attempt 1: Turn 27718 (Reached 26, 15 - No trigger).

## Battle Strategy (Wise Trio)
- Sage Gaku: Noctowl (32), Flareon (32). Counter: GNEISS (Rollout/Earthquake).
- Sage Masa: Noctowl (32), Vaporeon (32). Counter: KIMCHI (Sleep Powder) or Calcifer (Thunderpunch).
- Sage Koji: Noctowl (32), Jolteon (32). Counter: GNEISS (Earthquake).

## Capture Strategy (Suicune)
- Hypothesis: Suicune is a static encounter in Tin Tower (Crystal) at Lv40.
- Lead: XENON (Gastly) Lv21 (Hypnosis, Night Shade).
- **CRITICAL RISK:** Xenon is severely underleveled. Suicune will likely outspeed and KO Xenon. Consider training or using items.
- Items: 43 Great Balls, 1 Ultra Ball.

## Lessons Learned
- Suicune Quest (Crystal): Sages in Tin Tower 1F telling lore indicates progress. If they don't battle, a sighting is missing.
- Gatehouse Sages: The Sage at (4, 6) only checks for the Clear Bell. The Sage at (7, 10) tracks Suicune sighting progress.
- Flight Check: Always verify destination city before confirming Fly.
- Wise Trio: Battle sequence is the final gate to Suicune in the Tin Tower.
- Lesson: Suicune sightings are strictly sequential (Burned Tower -> Cianwood -> Route 42 -> Route 36 -> Tin Tower). If sages don't battle at Tin Tower, verify previous sightings using the tracker. Trigger points must be stepped on directly.
- Suicune Quest Detail: Sage at Gatehouse (Turn 27216) said "Tin Tower shook and a Pokemon must have returned to the top." This suggests the Clear Bell is active.
- Attempt: Route 42 (26, 15) reached at Turn 27718, but no sighting triggered.
- Hypothesis: Missing Eusine battle flag in Cianwood or sighting sequence is out of order.
- Plan: Fly to Cianwood to verify Eusine's presence.
- Verification: Eusine is NOT at (11, 17) in Cianwood City at Turn 27735. This confirms he was previously defeated.
- Strategy: Returning to Route 42 to explore the entire central island (24, 13 area) to trigger the sighting. If that fails, I'll check Route 36.
- Observation: Sages in Tin Tower Gatehouse (7, 10) say the tower shook, confirming Clear Bell is active. Sages in Tin Tower 1F are present but not battling, confirming sightings are incomplete.