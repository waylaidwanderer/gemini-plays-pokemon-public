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
- Type Effectiveness: Bite (Dark) is super-effective against XENON (Ghost/Poison).

## Kanto Strategy
- **Primary Goal: Complete Kanto Region Journey.**
- **Current Objective: Resolve Power Plant crisis.**
  - Strategy: Retrieve the stolen Machine Part to restore power.
  - Plan: Search Route 24 (North) for the Rocket Grunt -> Defeat Grunt -> Search Cerulean Gym water for Machine Part -> Return Part to Power Plant.

## PC Storage (Box 1)
1. GLAIVE (Lv14), 2. SELKIE (Lv24), 3. DELTA (MANTINE) Lv20, 4. RANGOON (KRABBY) Lv22, 5. NOMURA (TENTACOOL) Lv17, 6. Ravioli (Lv10), 7. Ouroboros (DRATINI) Lv15

## Movesets (HM Users)
- KIMCHI (GLOOM): Lv40 | CUT, FLASH
- GNEISS (GRAVELER): Lv53 | STRENGTH
- LAPIS (POLIWAG): Lv12 | SURF, WHIRLPOOL, WATERFALL
- ICARUS (PIDGEOTTO): Lv19 | FLY

## Power Plant Investigation
- **Start Turn:** 39084
- **Clues:** Machine Part stolen. Shady character (Rocket Grunt) fled Cerulean Gym to Route 24.
- **Investigator Analysis:** Grunt is likely hiding on the bridge. Defeating him reveals the part's location.

## Battle Strategy: Rocket Grunt
- Opponent: Golbat (Lv30).
- Current Plan: Use Night Shade (43 fixed damage). 2HKO expected.
- Backup: Calcifer (Lv58 Typhlosion) with Thunderpunch.

## Route 9 Exploration (Completed)
- Summary: Fully explored. Cut tree at (5, 8) cleared.

## Lessons Learned
- NPCs act as walls and must be navigated around.
- "find_path_v3_fixed" is more reliable than manual directional inputs for navigating around obstacles.
- Sand-Attack lowers accuracy; fixed-damage moves like Night Shade are good for consistency.
- Always check for gaps in ledges for passage.
- Don't confuse miss messages with type immunities in Gen 2.