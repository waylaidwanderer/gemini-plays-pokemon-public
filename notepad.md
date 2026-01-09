# Johto Journey - Final Phase

## Strategy: Navigate Tohjo Falls
- Start Turn: 35972
- Objective: Traverse Tohjo Falls to reach the eastern exit leading to the rest of Route 27.
- Requirements: SURF and WATERFALL (Rising Badge allows use).
- Status: Searching for HM07 Waterfall. [Turn 35972 - Present]
- Steps:
  1. Use Surf to cross the water. [Done]
  2. Search for HM07 Waterfall on land patches. [Current]
     - Explore central island (Row 8).
     - Explore eastern water/land (Column 18+).
     - Explore western strip (Column 0).
  3. Use Waterfall to climb the falls.
  4. Locate the eastern exit.

## Strategy: Search for HM07 Waterfall
- Verified Location: Ice Path 1F, northeast corner of main floor. [Confirmed by location_analyst Turn 36062]
- Tohjo Falls Search: Conducted from Turn 35972 to 36062. Result: Moon Stone found, HM07 NOT present.
- New Plan:
  1. Exit Tohjo Falls to Route 27.
  2. Fly to Mahogany Town.
  3. Travel east to Route 44 and enter Ice Path.
  4. Locate and pick up HM07 Waterfall.
  5. Return to Tohjo Falls and climb the waterfall.

## Tile Mechanics (Tohjo Falls specific)
- Ledge (FLOOR_UP_WALL): Impassable from North at (9, 16) through (12, 16). [7 failed attempts total]
- Waterfall: Requires HM07 Waterfall to climb. Rising Badge is already obtained.

## Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Traversable (requires SURF).
- WATERFALL: Impassable (requires WATERFALL).
- LEDGE (FLOOR_UP_WALL): One-way jump.

## Lessons Learned
- Rising Badge: Allows use of HM07 Waterfall outside battle.
- Tohjo Falls Ledges: Row 16 ledges are impassable from North.
- Navigation: If a movement fails twice, the tile is impassable from that direction.
- Item Discovery: Moon Stone found in Tohjo Falls at (2, 6).