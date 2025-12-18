# Johto Journey: Gem's Log

## Global Tile Mechanics
- FLOOR: Traversable.
- WALL / FLOOR_UP_WALL: Impassable.
- TALL_GRASS: Traversable. Wild encounters.
- LEDGE_HOP_DOWN: One-way South.
- LEDGE_HOP_RIGHT: One-way East.
- COUNTER: Impassable. Stand in front to talk to NPCs behind.
- HEADBUTT_TREE: Impassable.
- CUT_TREE: Impassable.
- WARP_CARPET: Map transition at edges.
- LADDER / DOOR / CAVE: Instant warp upon entry.
- PC / BOOKSHELF / RADIO: Interactable from below.
- WATER / ROCK / INCENSE_BURNER / MART_SHELF: Impassable.

## Gym Progress
- Zephyr Badge: Obtained from Falkner.
- Hive Badge: Target Azalea Town.

## NPC Archive - Route 32
- Fisher (15, 13): Standing at (16, 13) required to talk.
- Cooltrainer M (19, 8): Blocking path (Badge Req).
- Fisher (19, 14): Discovered.
- Youngster (12, 22): Trainer? Discovered at (12, 22).

## NPC Archive - Previous Areas
- KYLE: (6, 4) in Violet City. Traded Bellsprout for Rocky (ONIX).
- EARL: (25, 14) at Violet Academy.
- Nurse Joy: (3, 1) in Violet Pokecenter.
- Mr. Pokemon: (3, 5) on Route 30. Gave Mystery Egg.
- Prof. Oak: (6, 5) on Route 30. Gave Pokedex.
- Fisher: (13, 17) in Ruins of Alph. Mentioned "odd presence" and "huge secret".
- Officer (Gatehouse): (0, 4) in Route36RuinsOfAlphGate.
- Gramps (Gatehouse): (7, 6) in Route36RuinsOfAlphGate. Mentioned "strange tree" on the road.
- Lass: (51, 8) on Route 36. Mentioned "odd tree" blocking the way to Goldenrod City.
- Arthur: (45, 5) on Route 36. Appears on Thursdays. Gave Hard Stone.
- Fisher: (44, 9) on Route 36. Mentioned failure to punch the tree.
- Weird Tree: (35, 9) on Route 36. Blocks path to Goldenrod. Does not respond to A.

## Exploration Log
- Ruins of Alph Detour: Solved Kabuto Puzzle. Explored Inner Chamber. Found ladder at (10, 13) leading back to RuinsOfAlphOutside. Discovered cave entrance at (6, 19).
- Route 36: Investigating the "odd tree" reported by NPCs. Sign at (55, 7) confirms location. Lass confirms it blocks the way to Goldenrod City. Arthur found at (45, 5).

## Strategy & Lessons
- Input Hygiene: Do not mix directional and action buttons in press_buttons. Use press_sequence for multi-step interactions.
- HMs: Use FLASH in Dark Cave (requires Bellsprout).
- Path to Azalea: Exit Violet City south to Route 32. Follow road south to Union Cave. Pass through cave to reach Azalea Town.
- Tile Mechanics (Route 32): 
  - LEDGE_HOP_RIGHT: One-way East at (17, 12-14).
  - LEDGE_HOP_DOWN: One-way South at (16, 15).
  - WATER: Impassable without Surf.
  - WALL (x=15): Extends from y=14 to y=19.

## Strategy for Training
- **Rocky (Onix):** Switch-train against trainers on Route 32 to catch up in levels.
- **Egg (Togepi):** Switch-train to gain happiness and levels.
- **Gneiss (Geodude):** Primary for bird trainers. Healed to 30/37 HP (Turn 2061).
- **Calcifer (Quilava):** Lead for safety and efficiency against grass types.

## Task Tracking
- **Route 32 Exploration:** Started Turn 2038. Goal: Reach Union Cave. 
- **Current Status:** Navigating around the wall at x=15 to reach Fisher (15, 13). Standing at (16, 13) is required to interact.