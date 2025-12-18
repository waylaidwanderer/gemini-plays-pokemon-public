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

## NPC Archive
- KYLE: (6, 4) in Violet City. Traded Bellsprout for Rocky (ONIX).
- EARL: (25, 14) at Violet Academy. Learned about status/items.
- Nurse Joy: (3, 1) in Violet Pokecenter.
- Mr. Pokemon: (3, 5) on Route 30. Gave Mystery Egg.
- Prof. Oak: (6, 5) on Route 30. Gave Pokedex.

## Exploration Log
- **Ruins of Alph Detour:** Started Turn 1888. Currently in RuinsOfAlphInnerChamber.
- **Kabuto Puzzle:** Solved Turn 1941. Warped to Inner Chamber via pit at (3,3)/(4,3).
- **Inner Chamber:** "There is a strange presence here..." Triggered Turn 1941.

## Strategy & Lessons
- **Puzzle Solved:** Numerical order 1-16 is correct for Kabuto. Swapping identical pieces at the bottom (14/15) might be necessary if it doesn't trigger immediately. Verified Turn 1941.
- **Input Hygiene:** Do not mix directional and action buttons in `press_buttons`. Use `press_sequence` or separate calls. Verified Turn 1922.
- **HMs:** Use FLASH in Dark Cave for level grinding/shortcuts. Requires a Pokemon that can learn it (e.g. Bellsprout - catch one on Route 32).

## Reflection Turn 1943
- **Immediate Execution:** Continuing exploration of Inner Chamber.
- **Goal Clarity:** Identify the 'strange presence' (likely Unown).
- **Map Progress:** 32.1% explored. Focus on southern unseen tiles.