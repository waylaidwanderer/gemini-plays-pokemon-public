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

## Suicune Tracking Notes (Turn 14884)
- Suicune roams Johto after Tin Tower encounter.
- Pokédex "SUICUNE'S NEST" shows multiple red dots: Routes 30, 32, 34, 36, 37, 38/39, 42, 44, and 27.
- Current Plan: Head to Route 42 via Ecruteak City.

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

## Lessons Learned
- **Tool Hygiene:** Use `navigate` with `path_plan` for overworld movement. Always include a `commit_message` when updating custom tools.
- **Navigation:** Main exit to Route 36 is likely through the gatehouse at (3, 5) or a building around (9, 0). (17, 0) is a side path.
- **Battle Mechanics:** Ghost-types are immune to Normal/Fighting moves. Hypnosis is unreliable.
## National Park & Bug-Catching Contest
- Contest Days: Tuesday, Thursday, Saturday.
- Location: Route 35 National Park Gate (10_15).
- Rules: Use lead Pokémon to catch a bug Pokémon; judged on health, level, and stats.