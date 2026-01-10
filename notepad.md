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

## Battle Mechanics (Verified)
- Hypnosis (Gen 2): Misses are reported as "It didn't affect Enemy [Pokemon]!". This does not imply type immunity.
- Night Shade: Deals fixed damage equal to the user's level.
- Type Effectiveness: Dark is super-effective against Ghost/Poison (Haunter).

## Kanto Strategy
- **Primary Goal: Complete Kanto Region Journey.**
- **Current Objective: Resolve Power Plant crisis.**
  - Plan: Retrieve Machine Part from Cerulean Gym water -> Return Part to Power Plant.

## PC Storage (Box 1)
1. GLAIVE (Lv14), 2. SELKIE (Lv24), 3. DELTA (MANTINE) Lv20, 4. RANGOON (KRABBY) Lv22, 5. NOMURA (TENTACOOL) Lv17, 6. Ravioli (Lv10), 7. Ouroboros (DRATINI) Lv15

## Movesets (HM Users)
- KIMCHI (GLOOM): Lv40 | CUT, FLASH
- GNEISS (GRAVELER): Lv53 | STRENGTH
- LAPIS (POLIWAG): Lv12 | SURF, WHIRLPOOL, WATERFALL
- ICARUS (PIDGEOTTO): Lv19 | FLY

## Power Plant Investigation
- **Start Turn:** 39084
- **Current Turn:** 39454
- **Clues:** Machine Part stolen. Rocket Grunt defeated on Route 24.
- **Location Revealed:** The Machine Part is hidden in the water in the center of the Cerulean Gym.
- **Next Step:** Use Itemfinder in the large pool at (1, 5)-(6, 6).

## Cerulean Gym Search Plan
- Target Area: Central pools.
- Method: Use ITEMFINDER. If it pings, move toward the sound. If not, reposition and try again.
- Known Pools: 
  - Pool A (North): (1, 5)-(6, 6).
  - Pool B (South): (3, 8)-(4, 9).
- Hidden Item Interaction: Stand on the tile or face it and press A.
- Interaction Log:
  - (4, 8): Itemfinder pinged "nearby" in Turn 39452.
  - (4, 6): Currently surfing. Use Itemfinder now.
  - (4, 8): Facing Up, A pressed -> No effect (facing FLOOR).
- Note: In Crystal, the Itemfinder pings if an item is on the map. It doesn't give a "hot/cold" direction. I must check tiles manually. Common spot: (4, 4) or (5, 4) in the water. Wait, mental map shows (4,4) is FLOOR?
  - Row 4: (1,4) WATER, (2,4)-(7,4) FLOOR, (8,4) WATER.
  - Row 5: (1,5)-(6,5) WATER.
  - Center of Gym pool is likely around (3,5) or (4,5).
  - (4, 6) is where I am now. I will use Itemfinder here.