# Johto Journey: Gem's Log

## Global Tile Mechanics
- FLOOR: Traversable.
- WALL / FLOOR_UP_WALL: Impassable.
- TALL_GRASS: Traversable. Wild encounters.
- LEDGE_HOP_DOWN: One-way South.
- LEDGE_HOP_RIGHT: One-way East.
- COUNTER: Impassable. Stand in front to talk to NPCs behind.
- HEADBUTT_TREE: Impassable. Requires Headbutt.
- CUT_TREE: Impassable. Requires Cut.
- WARP_CARPET: Map transition at edges.
- LADDER / DOOR / CAVE: Instant warp upon entry.
- PC / BOOKSHELF / RADIO: Interactable from below.
- WATER / ROCK / INCENSE_BURNER: Impassable.

## Gym Progress
- **Zephyr Badge:** Obtained from Falkner.
- **Hive Badge:** Target. Azalea Town.

## NPC Archive
- KYLE: (6, 4) in Violet City. Traded Bellsprout for Rocky (ONIX).
- EARL: (25, 14) at Violet Academy. Learned about status/items.
- Nurse Joy: (3, 1) in Violet Pokecenter.
- Mr. Pokemon: (3, 5) on Route 30. Gave Mystery Egg.
- Prof. Oak: (6, 5) on Route 30. Gave Pokedex.

## Exploration Log
- **Ruins of Alph Detour:** Currently in RuinsOfAlphInnerChamber.
- **Kabuto Puzzle:** Solved. Warped to Inner Chamber via pit at (3,3)/(4,3).
- **Inner Chamber:** Encountered wild UNOWN at (15, 8).

## Strategy & Lessons
- **Puzzle Solved:** Numerical order 1-16 is correct for Kabuto. Swapping identical pieces at the bottom (14/15) might be necessary.
- **Input Hygiene:** Do not mix directional and action buttons in `press_buttons`.
- **HMs:** Use FLASH in Dark Cave for level grinding/shortcuts. Requires a Pokemon that can learn it (e.g. Bellsprout - catch one on Route 32).
- **Unown Battle:** Unown are Psychic-type and only know Hidden Power. Catching is priority. Using a Poke Ball immediately at Lv 5 is safer than attacking.

## Current Plan
- Defeat Unown (out of Poké Balls).
- Continue exploring Inner Chamber to find the ladder at (10, 13).
- Head back to Route 32 and continue south to Azalea Town.