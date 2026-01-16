# Suicune Quest: Cianwood City
- **Quest Start:** Turn 49885
- **Status:** Executing the "Ocean Loop" to bypass island elevation traps.

## The Strategy: The Ocean Loop
The northern plateau (14, 10) is a high-altitude zone protected by south-facing elevation traps (FLOOR_UP_WALL). The only entry is via the western coastal highway (X=2). To reach X=2 without hitting traps, we loop through the eastern ocean.

### Execution Plan
1. Eastern Shore: Walk to (23, 33). (Done)
2. Ocean Entry: Face Right and use SURF (GORP). (Done)
3. Sea Transit: Surf South along X=24 to (24, 51). (In Progress)
4. Southern Landing: Land at (24, 51).
5. Southern Traverse: Walk West along Row 51 to (4, 51).
6. Coastal Ascent: Walk North along X=4 to (4, 21).
7. Mechanical Bypass: Move North through (4, 20) [UP_WALL] to reach the highway.
8. The Dash: Walk North along X=2 to Row 12.
9. Victory: Walk East to (14, 12) and North to Suicune at (14, 10).

## Verified Mechanics
- Row 51: Completely clear land bridge from X=2 to X=24.
- UP_WALL: Blocks DOWN movement. Moving UP is allowed. (e.g., (4, 20)).
- X=4 Corridor: Clear north-south path from Row 51 to Row 20.
- X=2 Highway: Clear north-south path from Row 20 to Row 10.

## Battle Plan: Eusine
- Roster: Drowzee (Lv23), Haunter (Lv23), Electrode (Lv25).
- Lead: Calcifer (Lv64 Typhlosion). Strategy: Flamethrower sweep.

## Map Markers (Obstacles)
- (5, 29), (10, 27), (4, 25), (4, 19): Smashable Rocks.
- (14, 10): Suicune trigger point.