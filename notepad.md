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
- **Clues:** Machine Part hidden in Cerulean Gym water.
- **Status:** Machine Part retrieved from (3, 8) on Turn 39544.
- **Goal:** Return the Machine Part to the Power Plant Manager.

## Cerulean Gym Search Plan
- Strategy: Systematic search completed.
- Result: Found at (3, 8) by searching while standing at (3, 7) facing down.
- Progress:
  - (3, 3): 🚫 Itemfinder: Nope!
  - (4, 7): ✨ Itemfinder: Yes!
  - (3, 7): ✨ Itemfinder: Yes!
  - (3, 8): ✅ Found Machine Part!

## Error Analysis & Lessons
- Menu fumbles occur due to assuming menu resets. 
- Solution: Observe menu state or press B multiple times to reset before long sequences.
- Itemfinder range is limited; triangulation is effective for finding hidden items.
- Hidden items in water can be found by facing the tile and pressing A from an adjacent walkway.