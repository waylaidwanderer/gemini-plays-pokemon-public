# persistent_knowledge
## Tile Mechanics (Global)
- FLOOR: Traversable. Standard collision.
- WALL: Impassable.
- WATER: Traversable with HM Surf.
- TALL_GRASS: Traversable, triggers wild encounters.
- DOOR/WARP: Step on to enter buildings/areas.
- LEDGE_HOP_DOWN: One-way traversal (North to South).
- FLOOR_UP_WALL: Impassable Wall from the North.
- COUNTER: Impassable Wall. Interact from adjacent tile.
- GYM_PLATFORM: Raised floor area. Accessible via stairs (LADDER tile type) or by Surfing onto it from water.
- STAIRCASE: Warp tile that transitions between floors.
- BOOKSHELF: Impassable Wall.
- WINDOW: Impassable Wall.
- TV: Impassable Wall.

## Battle Mechanics (Verified)
- Hypnosis (Gen 2): Misses are reported as "It didn't affect Enemy [Pokemon]!". This does not imply type immunity.
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

## Magnet Train Restoration (Turn 39771)
- **Status:** Obtained the PASS. Power is restored. Boarded the Magnet Train in Saffron.
- **Goal:** Arrive in Goldenrod City.
- **Current Status:** On board the Magnet Train.
- **Next Step:** Wait for the train to arrive in Goldenrod City.

## Power Plant Investigation (Resolved)
- Machine Part returned to Manager. Power restored to Kanto.
- Obtained EXPN Card from Lavender Radio Tower.

## Lessons Learned
- **FLY Map Navigation:** Use `press_menu_buttons_v2`. Verify destination text "SAFFRON CITY" before pressing A. Avoid long sequences.
- **Takeoff:** Move to a neutral tile (not a door mat) before using FLY.
- **Interactions:** Always ensure facing the target tile.
- **Building Search:** Look for specific Pokémon-related landmarks when searching for lost items.
- **Navigation:** If blocked by water or obstacles, use the `navigate` tool to find a clear path around them.
- **Pathing Around Obstacles:** Paths in 2D top-down games are often multiple tiles wide. Check adjacent tiles if blocked.
- **Route 6 Navigation:** Circling East around the pond is required to reach Saffron City from Vermilion.