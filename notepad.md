# persistent_knowledge
## Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Traversable with HM Surf.
- TALL_GRASS: Traversable, triggers wild encounters.
- DOOR/WARP: Step on to enter buildings/areas.
- LEDGE_HOP_DOWN: One-way traversal (North to South).
- FLOOR_UP_WALL: Acts as a WALL from the North (cannot be jumped).
- COUNTER: Impassable Wall. Interact from adjacent tile.
- GYM_PLATFORM: Raised floor area. Accessible via stairs (LADDER tile type) or by Surfing onto it from water.

## Battle Mechanics (Verified)
- Hypnosis (Gen 2): Misses are reported as "It didn't affect Enemy [Pokemon]!". This does not imply type immunity.
- Night Shade: Deals fixed damage equal to the user's level.
- Type Effectiveness: Dark is super-effective against Ghost/Poison (Haunter).

## PC Storage (Box 1)
1. GLAIVE (Lv14), 2. SELKIE (Lv24), 3. DELTA (MANTINE) Lv20, 4. RANGOON (KRABBY) Lv22, 5. NOMURA (TENTACOOL) Lv17, 6. Ravioli (Lv10), 7. Ouroboros (DRATINI) Lv15

## Movesets (HM Users)
- KIMCHI (GLOOM): Lv40 | CUT, FLASH
- GNEISS (GRAVELER): Lv53 | STRENGTH
- LAPIS (POLIWAG): Lv12 | SURF, WHIRLPOOL, WATERFALL
- ICARUS (PIDGEOTTO): Lv19 | FLY

## Power Plant Investigation
- **Status:** Machine Part retrieved from Cerulean Gym.
- **Goal:** Return the Machine Part to the Power Plant Manager at Route 10.
- **Plan:**
  1. Navigate Route 9: (14, 10) -> (14, 11) -> East to (20, 11) -> South to (20, 12) -> East to (28, 12) -> North to (28, 3) -> East to (36, 3) -> South to (36, 8) -> East to (46, 8) -> South to (46, 11) -> East to (50, 11) -> South to (50, 15) -> East to (54, 15) -> South to Route 10 exit at (54, 17).
  2. Enter Power Plant and talk to the Manager at (14, 10).

## Lessons Learned
- **Hidden Items in Water:** Can be found by facing the water tile and pressing A from an adjacent walkway. 
- **Itemfinder:** Range is limited (~4-5 tiles). Triangulation by checking multiple spots is effective.
- **Menu Navigation:** Always check the screen state before executing long button sequences to avoid fumbles. Assume the menu DOES NOT reset to the first option.
- **Pathing:** 2D top-down paths are often wider than they look. Analyze all adjacent tiles when blocked.
- **Stagnation:** Spent ~460 turns in Cerulean Gym (39084-39544) due to search logic and menu fumbles. Moving forward immediately.