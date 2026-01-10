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
- WARP_PANEL: Teleports player between rooms. Interaction is immediate upon stepping.

## Battle Mechanics (Verified)
- Hypnosis (Gen 2): Misses are reported as "It didn't affect Enemy [Pokemon]!".
- Night Shade: Deals fixed damage equal to the user's level.
- Type Effectiveness: Dark is super-effective against Ghost/Poison (Haunter).

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
- **Warp Sequence (Shortest):**
  1. Entrance (BC): Warp at (11, 15). Arrive at (19, 17) [BR].
  2. BR Room: Warp at (15, 15). Arrive at (19, 3) [TR].
  3. TR Room: Warp at (15, 5). Arrive at (1, 3) [TL].
  4. TL Room: Warp at (1, 5). Arrive at (11, 9) [MC - Sabrina].
- **Strategy:** Lead with Typhlosion (Calcifer) to sweep Psychic-types. Avoid using Haunter (Xenon) or Gloom (Kimchi).
- **Hypothesis:** Bottom-Left rule (taking the bottom-left panel in each room) works.
- **Test Result:** (1, 3) -> (1, 5) is the final leg to Sabrina.

## Lessons Learned
- **Menu Persistence:** Automated menu tools can fail if the cursor or menu state is not what's expected. Manual sequences with `press_menu_buttons_v2` are more reliable for complex tasks like swapping.
- **Warp Maze Logic:** BFS scripts on Map Events data are highly effective for solving warp puzzles.
- **Pathing:** Always verify traversability through observation.