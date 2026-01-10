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

## Magnet Train Restoration
- **Status:** Recovered Copycat's Poké Doll (LOST ITEM) from the Pokémon Fan Club in Vermilion City.
- **Strategy:**
  1. Exit Vermilion City to the North (Route 6).
  2. Travel North through Route 6 to Saffron City.
  3. Return the Poké Doll to Copycat on 2F of her house (9, 11) in Saffron.
  4. Obtain the Rail Pass.

## Power Plant Investigation (Resolved)
- Machine Part returned to Manager. Power restored to Kanto.
- Obtained EXPN Card from Lavender Radio Tower.

## Lessons Learned
- **FLY Map Navigation:** Use `press_menu_buttons_v2`. Verify destination text "SAFFRON CITY" before pressing A. Avoid long sequences.
- **Takeoff:** Move to a neutral tile (not a door mat) before using FLY.
- **Interactions:** Always ensure facing the target tile.
- **Building Search:** Look for specific Pokémon-related landmarks when searching for lost items.
- **Navigation:** If blocked by water or obstacles, use the `navigate` tool to find a clear path around them. Avoid multi-step `press_buttons` without verification.
## Strategy for Magnet Train Restoration (Turn 39757)
- **Goal:** Return Poké Doll to Copycat to get Rail Pass.
- **Location:** Copycat is on 2F of her house (9, 11) in Saffron. Stairs are at (2, 0) on 1F.
- **Current Status:** Just entered Copycat's house 1F.
- **Next Step:** Go upstairs via (2, 0) to reach Copycat's room.

## Tile Mechanics (Update)
- WINDOW: Impassable Wall.
- TV: Impassable Wall.
- STAIRCASE: Warp tile that transitions between floors. Verified on 1F (2, 0).

## Lessons Learned (Update)
- **Pathing Around Obstacles:** When pathfinding, if a tool suggests a blocked path, manually check adjacent tiles. Paths in 2D top-down games are often multiple tiles wide.
- **Route 6 Navigation:** The direct path North on Route 6 is blocked by a pond; one must circle around to the East to find the land bridge.

## Reflection (Turn 39755)
1. **Immediate Execution:** No deferred tasks identified.
2. **Notepad Hygiene:** Notepad is organized. Added current strategy and updated lessons.
3. **Map Hygiene:** Saffron City markers are mostly in place. South Gate warps (16, 33) and (17, 33) are marked.
4. **Automation Strategy:** Custom tools `find_path_v3_fixed` and `navigate` are working well. No new tools/agents needed this turn.
5. **Goal Clarity:** Goals are concrete outcomes. Method is in the Notepad.
6. **Error Analysis:** Distilled the Route 6 pond navigation into a lesson. Verified that the South Gate is the correct entrance to Saffron City.