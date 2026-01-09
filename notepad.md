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
- Hypothesis: HM07 is located on one of the land patches in Tohjo Falls.
- Current Plan:
  1. Explore the eastern water and land patches. [Current]
  2. If blocked, check if (15, 14) or (16, 14) allow jumping east/south.
  3. Investigate the warp at (13, 15).
- Observation: Moon Stone found at (2, 6). [Turn 35981]
- Warning: If HM07 is not found here, it may be in Ice Path (missed earlier).

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