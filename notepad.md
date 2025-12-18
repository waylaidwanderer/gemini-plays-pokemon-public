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
- Hive Badge: Target. Azalea Town.

## NPC Archive
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
- Ruins of Alph Detour:
  - Solved Kabuto Puzzle.
  - Explored Inner Chamber.
  - Encountered wild UNOWN (Psychic, Hidden Power).
  - Found ladder at (10, 13) leading back to RuinsOfAlphOutside.
  - Discovered cave entrance at (6, 19).
  - Entered Route36RuinsOfAlphGate.
  - Gramps confirmed "strange tree" blocking Route 36.
- Route 36: Investigating the "odd tree" reported by NPCs. Sign at (55, 7) confirms location. Lass confirms it blocks the way to Goldenrod City. Arthur found at (45, 5).

## Strategy & Lessons
- Puzzle Solved: Numerical order 1-16 is correct for Kabuto.
- Input Hygiene: Do not mix directional and action buttons in press_buttons. Use press_sequence for multi-step interactions.
- HMs: Use FLASH in Dark Cave (requires Bellsprout).
- Unown Battle: Psychic-type. Only know Hidden Power. Catching is priority.
- Path to Azalea: Exit Violet City south to Route 32. Follow road south to Union Cave. Pass through cave to reach Azalea Town.
- Resource Management: Need to restock Poké Balls at the next Mart.

## Strategy for Reaching Azalea Town
1. **Route 32:** From Violet City, head south through the gatehouse to Route 32.
2. **Union Cave:** Navigate south along Route 32 to the entrance of Union Cave.
3. **Azalea Town:** Traverse Union Cave to exit on the southern side, leading directly to Azalea Town.
4. **Training:** Use Geodude (Gneiss) for training against trainers on Route 32 to prepare for the next Gym.

## Tile Mechanics - Route 32
- FLOOR: Traversable. Verified.
- TALL_GRASS: Traversable. Verified. Wild encounters possible.
- LEDGE_HOP_RIGHT: One-way East. Verified at (17, 12), (17, 13), (17, 14).
- LEDGE_HOP_DOWN: One-way South. Verified at (16, 15).
- WALL / FLOOR_UP_WALL: Impassable. Verified.
- WATER: Impassable without Surf. Verified.
- WARP_CARPET_LEFT: Map transition at (4, 2) and (4, 3). Verified.

## Strategy for Training
- **Rocky (Onix):** Switch-train against trainers on Route 32 to catch up in levels.
- **Egg (Togepi):** Switch-train to gain happiness and levels.
- **Gneiss (Geodude):** Primary for bird trainers, but needs healing. Current priority: Heal with Potion.
- **Calcifer (Quilava):** Lead for safety and efficiency against grass types.

## NPC Archive - Route 32
- Fisher (15, 13): Discovered.
- Cooltrainer M (19, 8): Blocking path (Badge Req).
- Fisher (19, 14): Discovered.

## Lessons Learned
- **Tile Mechanics:** `FLOOR_UP_WALL` and `MART_SHELF` are impassable obstacles that must be accounted for in pathfinding.
- **Menu Navigation:** When purchasing items, "Up" increases quantity and "Down" decreases it. Rolling over from 1 using "Down" can reach the maximum affordable quantity.
- **Tool Maintenance:** Always ensure pathfinding tools account for both tile collision types and map markers (for off-screen obstacles).

## Task Tracking
- **Route 32 Exploration:** Started Turn 2038. Goal: Reach Union Cave.