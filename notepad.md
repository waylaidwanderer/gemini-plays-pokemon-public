# persistent_knowledge
## Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Traversable with HM Surf.
- TALL_GRASS: Traversable, triggers wild encounters.
- DOOR/WARP: Step on to enter buildings/areas.
- LEDGE_HOP_DOWN: One-way traversal (North to South).
- FLOOR_UP_WALL: Impassable Wall from the North; cannot be jumped down from this side.
- COUNTER: Impassable Wall. Interact from adjacent tile.
- GYM_PLATFORM: Raised floor area. Accessible via stairs (LADDER tile type) or by Surfing onto it from water.

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

## Power Plant Investigation
- **Start Turn:** 39084
- **Return to Power Plant Phase Start:** 39630
- **Plan:**
  1. Exit Route 10 North at (14, 0) to Route 9.
  2. Navigate Route 9 to the water entry point.
  3. Surf down the river back to Route 10 North.
  4. Enter Power Plant at (3, 9).
  5. Return Machine Part to Manager at (14, 10).

## Lessons Learned
- **Hidden Items in Water:** Can be found by facing the water tile and pressing A from an adjacent walkway. 
- **Itemfinder:** Range is limited (~4-5 tiles). Triangulation by checking multiple spots is effective.
- **Menu Navigation:** Always check the screen state before executing long button sequences to avoid fumbles. Assume the menu DOES NOT reset to the first option.
- **Pathing:** 2D top-down paths are often wider than they look. Analyze all adjacent tiles when blocked.
- **Stagnation:** Spent ~460 turns in Cerulean Gym (39084-39544) due to search logic and menu fumbles. Moving forward immediately.