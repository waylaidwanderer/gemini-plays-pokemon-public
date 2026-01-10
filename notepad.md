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
- **Strategy:** Sweep Sabrina with Typhlosion (Calcifer) Lv58. Avoid using Haunter or Gloom.
- **Hypothesis:** Bottom-Left rule (taking the bottom-left panel in each room) works.
- **Test Result:** Verified shortest path via BFS and manual traversal.

## Lessons Learned
- **Menu Persistence:** Automated menu tools can fail if the cursor or menu state is not what's expected. Manual sequences with `press_menu_buttons_v2` are more reliable for complex tasks like swapping.
- **Warp Maze Logic:** BFS scripts on Map Events data are highly effective for solving warp puzzles.
- **Pathing:** Always verify traversability through observation.

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

## Unverified NPCs
- NPC at (3, 4) [TL Room]: Suspected Medium Doris.
- NPC at (17, 4) [TR Room]: Suspected Psychic Jared.