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
- Hypnosis (Gen 2): Misses are reported as "It didn't affect Enemy [Pokemon]!".
- Night Shade: Deals fixed damage equal to the user's level.
- Type Effectiveness: Dark super-effective against Ghost/Poison.

## PC Storage (Box 1)
- 1. SPINARAK (Lv13), 2. SCYTHER (Lv14), 3. SELKIE (Lv24), 4. DELTA (MANTINE) (Lv20), 5. RANGOON (KRABBY) (Lv22), 6. NOMURA (TENTACOOL) (Lv17), 7. Ravioli (KRABBY) (Lv10), 8. Ouroboros (DRATINI) (Lv15)

## Movesets (HM Users)
- KIMCHI (GLOOM): Lv41 | FLASH, MOONLIGHT, CUT, SLEEP POWDER
- GNEISS (GRAVELER): Lv53 | EARTHQUAKE, DEFENSE CURL, STRENGTH, ROLLOUT
- LAPIS (POLIWAG): Lv12 | WATERFALL, SURF, HYPNOSIS, WHIRLPOOL
- ICARUS (PIDGEOTTO): Lv19 | FLY, SAND-ATTACK, GUST, QUICK ATTACK

## TMs & HMs Obtained
- HM01-07, TM07, TM24, TM28, TM33, TM37, TM44, TM47

## Saffron Gym Challenge
- **Start Turn:** 39791
- **Goal:** Defeat Sabrina.
- **Warp Maze Logic:** Rooms are arranged in a grid. Corner warp panels lead to adjacent rooms. Taking the bottom-left panel in each room eventually leads to the center (Sabrina's room).
- **Shortest Warp Path:** (11, 15) [BC] -> (15, 15) [BR] -> (15, 5) [TR] -> (1, 5) [TL] -> (11, 9) [MC - Sabrina].
- **Time Tracking:** Saffron Gym Challenge Start: Turn 39791.

### Tile Mechanics (Saffron Gym)
- FLOOR: Traversable.
- WALL: Impassable.
- WARP_PANEL: Immediate teleportation. Linked in a maze-like fashion. Located in room corners.

### Saffron Gym Battle Strategy
- **Sabrina's Team:** Espeon (Lv46), Mr. Mime (Lv46), Alakazam (Lv48).
- **Current Status:** GNEISS (Lv53) active vs Alakazam (Lv48). Calcifer (Lv58) at 5 HP.
- **Tactics:** GNEISS uses Earthquake to exploit Alakazam's low Physical Defense.

## Lessons Learned
- **Menu Mechanic:** The overworld menu loops (e.g., pressing Up from POKEDEX goes to EXIT).
- **Battle Accuracy:** Accuracy drops (like Sand-Attack) are severe; switching out is usually better than staying in with a high-level lead.
- **Gym Navigation:** BFS or systematic corner-testing is the most reliable way to solve warp mazes.