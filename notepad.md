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
- WARP_PANEL: Teleports player between rooms. Interaction is immediate upon entry.

## Battle Mechanics (Verified)
- Hypnosis (Gen 2): Misses are reported as "It didn't affect Enemy [Pokemon]!".
- Night Shade: Deals fixed damage equal to the user's level.
- Type Effectiveness: Dark super-effective against Ghost/Poison.

## PC Storage (Box 1)
1. SPINARAK (Lv13), 2. SCYTHER (Lv14), 3. SEEL (Lv24), 4. MANTINE (Lv20), 5. KRABBY (Lv22), 6. TENTACOOL (Lv17), 7. KRABBY (Lv10), 8. DRATINI (Lv15)

## Movesets (HM Users)
- KIMCHI (GLOOM): Lv40 | CUT, FLASH
- GNEISS (GRAVELER): Lv53 | STRENGTH
- LAPIS (POLIWAG): Lv12 | SURF, WHIRLPOOL, WATERFALL
- ICARUS (PIDGEOTTO): Lv19 | FLY

## TMs & HMs Obtained
- HM01-07, TM07, TM24, TM28, TM33, TM37, TM44, TM47

## Magnet Train (Restored Turn 39771)
- PASS obtained from Copycat. Power restored to Kanto. Service active between Saffron and Goldenrod.

## Saffron Gym Challenge (Started Turn 39791)
- **Goal:** Defeat Sabrina.
- **Shortest Warp Path:** (11, 15) [BC] -> (15, 15) [BR] -> (15, 5) [TR] -> (1, 5) [TL] -> (11, 9) [MC - Sabrina].
- **Strategy:** Sweep Sabrina with Typhlosion (Calcifer) Lv58.
- **Hypothesis:** Taking the bottom-left panel in each room leads to the center.
- **Test Result:** Path verified via BFS and manual testing.
- **Attempt History:** 10 failed menu swaps. Swapping lead to Calcifer (Lv58) via custom tool.
- **Warp Panel Mechanic:** Verified that stepping on a WARP_PANEL tile (like 1, 5) teleports the player immediately to the linked destination.

## Saffron Gym Warp Solution (Full Table)
- BC (Entrance) (11, 15) <-> BR (19, 17)
- BR (15, 15) <-> TR (19, 3)
- BR (15, 17) <-> BL (5, 15)
- TR (15, 3) <-> MR (15, 9)
- TR (15, 5) <-> TL (1, 3)
- TR (19, 5) <-> BL (1, 15)
- TL (1, 5) <-> MC (11, 9)
- ML (1, 11) <-> BL (1, 17)
- ML (5, 11) <-> BL (5, 17)
- ML (1, 9) <-> MR (1, 9)
- ML (5, 9) <-> TC (5, 9)

## Lessons Learned
- **Menu Sequence:** Use "Start, Up (x6), Down" to reliably reach POKEMON from overworld.
- **Warp Maze:** BFS on Map Events data is optimal for finding paths through warp tiles.