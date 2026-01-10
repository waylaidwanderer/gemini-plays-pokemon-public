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

## Kanto Strategy
- **Primary Goal: Complete Kanto Region Journey.**
- **Current Objective: Resolve Power Plant crisis.**
  - Plan: Retrieve Machine Part from Cerulean Gym water -> Return Part to Power Plant.
- **Quest Start:** Turn 39084 (Saturday, Jan 10, 2026).

## PC Storage (Box 1)
1. GLAIVE (Lv14), 2. SELKIE (Lv24), 3. DELTA (MANTINE) Lv20, 4. RANGOON (KRABBY) Lv22, 5. NOMURA (TENTACOOL) Lv17, 6. Ravioli (Lv10), 7. Ouroboros (DRATINI) Lv15

## Movesets (HM Users)
- KIMCHI (GLOOM): Lv40 | CUT, FLASH
- GNEISS (GRAVELER): Lv53 | STRENGTH
- LAPIS (POLIWAG): Lv12 | SURF, WHIRLPOOL, WATERFALL
- ICARUS (PIDGEOTTO): Lv19 | FLY

## Power Plant Investigation
- **Start Turn:** 39084
- **Current Turn:** 39504
- **Clues:** Machine Part stolen. Rocket Grunt revealed it is hidden in the Cerulean Gym water.
- **Goal:** Search the center of the gym pool.
- **Hypothesis:** Itemfinder "Nope!" at (3, 3). Testing (4, 7) next.

## Cerulean Gym Search Plan
- Target Area: Center of the pool area.
- Interaction Log:
  - (3, 3) facing Up (searching 3, 2): No result with direct A press.
  - (3, 3): Itemfinder "Nope!".
- Next: Use Itemfinder at (4, 7).
- Lesson: Manual menu navigation is more reliable than custom tools when menu state is complex.

## Error Analysis & Lessons
- Turn 39485: `use_itemfinder_robust` failed (unexpected menu state).
- Turn 39494: Itemfinder confirmed no item at (3, 3).
- Turn 39500-39503: Menu fumbles (Pokedex, Options). Recovered to overworld at (4, 7). Attempting Itemfinder again.