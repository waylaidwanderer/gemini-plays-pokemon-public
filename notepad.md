# Johto Journey: Gem's Log

## Global Tile Mechanics
- FLOOR: Traversable. Standard ground. Verified Turn 1891.
- WALL / FLOOR_UP_WALL: Impassable. Verified Turn 1905.
- TALL_GRASS: Traversable. Wild encounters.
- LEDGE_HOP_DOWN: One-way South. Verified Turn 1894.
- LEDGE_HOP_RIGHT: One-way East. Verified Turn 1894.
- COUNTER: Impassable. Stand in front to talk to NPCs behind. Verified Turn 1891.
- HEADBUTT_TREE: Impassable. Requires Headbutt.
- CUT_TREE: Impassable. Requires Cut.
- WARP_CARPET: Map transition at edges. Verified Turn 1891.
- LADDER / DOOR / CAVE: Instant warp upon entry. Verified Turn 1907.
- PC / BOOKSHELF / RADIO: Interactable from below (face Up + A).
- WATER / ROCK / INCENSE_BURNER: Impassable. Verified Turn 1906.

## Gym Progress
- **Zephyr Badge:** Obtained from Falkner (Turn 1864).
- **Hive Badge:** Target. Azalea Town.

## Exploration Log
- **Ruins of Alph Detour:** Started Turn 1888. Currently in RuinsOfAlphInnerChamber.
- **Kabuto Puzzle:** Solved Turn 1941. Warped to Inner Chamber via pit at (3,3)/(4,3).
- **Inner Chamber:** "There is a strange presence here..." Verified Turn 1941.

## Strategy & Lessons
- **Puzzle Solved:** Numerical order 1-16 is correct. Swapping identical pieces at the bottom (14/15) might be necessary if it doesn't trigger immediately. Verified Turn 1941.
- **Input Hygiene:** Do not mix directional and action buttons in `press_buttons`. Use `press_sequence` or separate calls. Mixed inputs are truncated by the system. Verified Turn 1922.

## Exploration Log
- **Ruins of Alph Detour:** Started Turn 1888. Currently in RuinsOfAlphInnerChamber.
- **Kabuto Puzzle:** Solved Turn 1941. Warped to Inner Chamber via pit.
- **Inner Chamber:** "There is a strange presence here..." Triggered Turn 1941.

## Strategy & Lessons
- **Puzzle Solved:** Numerical order 1-16 is correct for Kabuto.
- **Input Hygiene:** Do not mix directional and action buttons in `press_buttons`.

## Reflection Turn 1943
- **Immediate Execution:** Continuing exploration of Inner Chamber.
- **Notepad Hygiene:** Cleaned up solved puzzle details.
- **Goal Clarity:** Identify the 'strange presence' (likely Unown).
- **Map Progress:** 22.5% explored. Focus on western and southern unseen tiles.