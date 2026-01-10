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
- **Clues:** Machine Part hidden in Cerulean Gym water. Rocket Grunt said "center of the gym's pool".
- **Status:** Itemfinder "Yes!" at (4, 7) and (3, 7). "Nope!" at (3, 3).
- **Goal:** Retrieve the Machine Part.

## Cerulean Gym Search Plan
- Strategy: Systematic search of water tiles adjacent to central walkway (y=7).
- Method: Face the target water tile from the walkway or an adjacent tile and press A.
- Triangulation: Item is near (3, 7) and (4, 7).
- Target Tiles: (3, 6), (3, 8), (4, 6), (4, 8), (5, 6), (5, 8).

## Error Analysis & Lessons
- Menu fumbles occur due to assuming menu resets. 
- Solution: Observe menu state or press B multiple times to reset before long sequences.
- Triangulation confirms item is in the central region (Y=6 to Y=9).