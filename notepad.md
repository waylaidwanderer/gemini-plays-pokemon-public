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

## Magnet Train
- Service: Saffron City <-> Goldenrod City.
- Status: Active (Power restored Turn 39771).
- Requirement: PASS (Obtained from Copycat).

## Saffron Gym Challenge (Completed)
- **Status:** Marsh Badge obtained (Turn 39878).
- **Sabrina Dialogue:** Confirmed she does not give a TM in this version after multiple interactions.
- **Shortest Path (Out):** MC (11, 9) -> TL (1, 3) -> TR (19, 3) -> BR (19, 17) -> BC (Entrance).

## Machine Part Quest
- **Location:** Suspected to be in the water at Cerulean Gym (based on Rocket Grunt dialogue and Itemfinder pings at 3,7 and 4,7).
- **Status:** Not yet retrieved. Power Plant remains inactive.

## Lessons Learned
- **Menu Mechanic:** The overworld menu loops. The cursor remembers its last position. To reset, press B multiple times.
- **Battle Accuracy:** Accuracy drops (like Sand-Attack) are severe; switching out is usually better than staying in with a high-level lead.
- **Gym Navigation:** BFS or systematic corner-testing is the most reliable way to solve warp mazes.
- **Warp Maze Pathfinding:** BFS on Map Events data is optimal for finding paths through warp tiles.