# persistent_knowledge
## Tile Mechanics (Global)
- FLOOR: Traversable. Standard collision.
- WALL: Impassable.
- WATER: Traversable with HM Surf.
- TALL_GRASS: Traversable, triggers wild encounters.
- DOOR/WARP: Step on to enter buildings/areas.
- LEDGE_HOP_DOWN: One-way traversal (North to South).
- COUNTER: Impassable Wall. Interact from adjacent tile.
- STAIRCASE: Warp tile that transitions between floors.
- WARP_PANEL: Teleports player between rooms. Interaction is immediate upon entry. In Saffron Gym, these tiles are placed in the corners of rooms and lead to other rooms in the maze.

## Battle Mechanics (Verified)
- Status Moves: Misses are reported as "The attack missed!". "It didn't affect..." indicates type immunity.
- Night Shade: Deals fixed damage equal to the user's level.
- Type Effectiveness (Psychic): Weak to Bug, Ghost, Dark.
- Type Effectiveness (Ghost): Weak to Ghost, Dark. Immune to Normal, Fighting.
- Type Effectiveness (Dark): Super-effective against Ghost, Psychic.
- Type Effectiveness (Poison): Weak to Ground, Psychic.

## PC Storage (Box 1)
- 1. SPINARAK (Lv13), 2. GLAIVE (SCYTHER) (Lv14), 3. SELKIE (SEEL) (Lv24), 4. DELTA (MANTINE) (Lv20), 5. RANGOON (KRABBY) (Lv22), 6. NOMURA (TENTACOOL) (Lv17), 7. Ravioli (KRABBY) (Lv10), 8. Ouroboros (DRATINI) (Lv15)

## Movesets (HM Users)
- KIMCHI (GLOOM): Lv41 | FLASH, MOONLIGHT, CUT, SLEEP POWDER
- GNEISS (GRAVELER): Lv53 | EARTHQUAKE, DEFENSE CURL, STRENGTH, ROLLOUT
- LAPIS (POLIWAG): Lv12 | WATERFALL, SURF, HYPNOSIS, WHIRLPOOL
- ICARUS (PIDGEOTTO): Lv19 | FLY, SAND-ATTACK, GUST, QUICK ATTACK

## TMs & HMs Obtained
- HM01-07, TM07, TM24, TM28, TM33, TM37, TM44, TM47

## Saffron Gym Challenge
- **Start Turn:** 39791
- **Status:** Marsh Badge obtained (Turn 39878).
- **Warp Maze Logic:** Rooms are arranged in a grid. Corner warp panels lead to adjacent rooms. Taking the bottom-left panel in each room eventually leads to the center (Sabrina's room).

## Lessons Learned
- **Menu Mechanic:** The overworld menu loops. The cursor remembers its last position. To reset, press B multiple times. Fixed sequences for menu navigation are unreliable without a reset.
- **Battle Accuracy:** Accuracy drops (like Sand-Attack) are severe; switching out is usually better than staying in with a high-level lead.
- **Gym Navigation:** BFS or systematic corner-testing is the most reliable way to solve warp mazes.
- **Warp Maze Pathfinding:** BFS on Map Events data is optimal for finding paths through warp tiles.