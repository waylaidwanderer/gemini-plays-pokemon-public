# Suicune Capture Strategy (Crystal Version)
## Primary Goal: Capture Suicune
- Step 1: Obtain Clear Bell. (COMPLETE)
- Step 2: Access Tin Tower. Defeat the Wise Trio. (COMPLETE)
- Step 3: Encounter Suicune at Tin Tower. (COMPLETE - It fled).
- Step 4: Track Suicune. Use Pokédex. (Started Turn 14853).
- Step 5: Prepare Catcher. Obtain Parasect (Spore + False Swipe).
- Step 6: Execute Capture. Corner -> Mean Look -> False Swipe -> Sleep -> Ultra Balls.

## Route 42 Strategy
- Goal: Locate Suicune and find Fisher Tully.
- Requirements: Surf (Ravioli knows it), Cut (KIMCHI knows it).

## Suicune Tracking Notes (Started Turn 14853)
- Suicune roams Johto after Tin Tower encounter.
- Pokédex "SUICUNE'S NEST" shows multiple red dots: Routes 30, 32, 34, 36, 37, 38/39, 42, 44, and 27.

## Tile Mechanics
- FLOOR: Standard traversal.
- WALL / FENCE: Impassable.
- TALL_GRASS / LONG_GRASS: Encounters.
- WATER: Requires SURF.
- LEDGE: One-way jump.
- WARP: Map transition.
- HEADBUTT_TREE: Impassable / Interact.
- FLOOR_UP_WALL: One-way North only.
- COUNTER: Impassable; interact from front.
- WARP_CARPET_DOWN / WARP_CARPET_RIGHT / WARP_CARPET_LEFT: Map transitions.
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
- **Tool Hygiene:** Use `navigate` with `path_plan` for overworld movement. Always include a `commit_message` when updating custom tools. NEVER use `autopress_buttons` in custom tools for overworld navigation.
- **Navigation:** National Park is a valid path to Route 36 via the east exit at (33, 18).
- **Battle Mechanics:** Ghost-types are immune to Normal/Fighting moves. Hypnosis is unreliable.

## National Park & Bug-Catching Contest
- Contest Days: Tuesday, Thursday, Saturday.
- Location: Route 35 National Park Gate (10_15).
- Rules: Use lead Pokémon to catch a bug Pokémon; judged on health, level, and stats.

## Reflection (Turn 14905)
- Strategy: Efficient pathing via custom tool and `navigate`.
- Verification: Root hypothesis (Park is best route) confirmed by standard map layouts.