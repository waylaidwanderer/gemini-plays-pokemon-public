# Suicune Capture Strategy (Crystal Version)
## Primary Goal: Capture Suicune
- Step 1: Obtain Clear Bell. (COMPLETE)
- Step 2: Access Tin Tower. Defeat the Wise Trio. (COMPLETE)
- Step 3: Encounter Suicune at Tin Tower. (COMPLETE - It fled).
- Step 4: Track Suicune. Use Pokédex.
- Step 5: Prepare Catcher. Obtain Parasect (Spore + False Swipe).
- Step 6: Execute Capture. Corner -> Mean Look -> False Swipe -> Sleep -> Ultra Balls.

## Route 42 Strategy
- Goal: Locate Suicune and find Fisher Tully.
- Path: Goldenrod -> Route 35 -> Route 36 -> Route 37 -> Ecruteak -> Route 42.
- Requirements: Surf (Ravioli knows it), Cut (KIMCHI knows it).

## Completed Tasks
- **Yanma Swarm (Route 35):** Caught Level 12 Female Yanma (INTERCEPT) using KIMCHI (Gloom) with Sleep Powder + Absorb. (Turn 14795).
- **Heal Party:** Restored HP/PP at Goldenrod Pokecenter. (Turn 14847).

## Tile Mechanics
- FLOOR: Standard traversal.
- WALL / FENCE: Impassable.
- TALL_GRASS: Encounters.
- WATER: Requires SURF.
- LEDGE: One-way jump.
- WARP: Map transition.
- HEADBUTT_TREE: Impassable / Interact.
- FLOOR_UP_WALL: One-way North only.
- COUNTER: Impassable; interact from front.
- WARP_CARPET_DOWN: Exit map south.
- LADDER: Map transition.
- PC: Background object for storage.

## Type Effectiveness Chart (Observed)
- Ghost: Immune to Normal/Fighting.
- Normal: Immune to Ghost.
- Grass vs. Bug/Flying: 0.25x (Observed: Gloom's Absorb vs. Yanma).
- Normal vs. Poison/Grass: 1.0x (Observed: Yanma's Tackle vs. Gloom).

## NPCs & Locations
- Fisher Tully: (15, 13) Route 32. Fishing info (Route 42).
- Arnie (Bug Catcher): Route 35. Reports Yanma swarms.

## Wild Encounters (Route 35)
- DITTO (Lv 10), PIDGEY (Lv 12, 14), NIDORAN♀/♂ (Lv 12), YANMA (Lv 12 - Swarm).
- Observed Moves (Yanma): Tackle, Quick Attack, Foresight.

## Immediate To-Do
- Track Suicune using the Pokédex.
- Head to Route 42 to find Fisher Tully and check for Suicune.
## Lessons Learned
- **Tool Hygiene:** Always include a `commit_message` when updating custom tools with `define_tool`. Deferring tool fixes leads to data loss after context summarization.
- **Navigation:** ROute 42 is accessible from Ecruteak City's east gate once Sudowoodo is cleared.
- **Battle Mechanics:** Ghost-types are immune to Normal/Fighting moves (e.g. Tackle from Yanma). Hypnosis is unreliable against certain types or just misses frequently.