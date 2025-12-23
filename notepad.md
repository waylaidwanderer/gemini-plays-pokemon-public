# Suicune Capture Strategy (Crystal Version)
## Primary Goal: Capture Suicune
- Step 1: Obtain Clear Bell. (COMPLETE)
- Step 2: Access Tin Tower. Defeat the Wise Trio. (COMPLETE)
- Step 3: Encounter Suicune at Tin Tower. (COMPLETE - It fled).
- Step 4: Track Suicune. Use Pokédex. (Started Turn 14853).
- Step 5: Prepare Catcher. Obtain Parasect (Spore + False Swipe).
- Step 6: Execute Capture. Corner -> Mean Look -> False Swipe -> Sleep -> Ultra Balls.

## Route 42 Strategy
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
- Fisher Tully: (40, 10) Route 42. Fishing info.
- Arnie (Bug Catcher): Route 35. Reports Yanma swarms.

## Lessons Learned
- **Tool Hygiene:** Use `navigate` with `path_plan` for overworld movement. Always include a `commit_message` when updating custom tools. NEVER use `autopress_buttons` in custom tools for overworld navigation.
- **Battle Mechanics:** Ghost-types are immune to Normal/Fighting moves. Hypnosis is unreliable.

## National Park & Bug-Catching Contest
- Contest Days: Tuesday, Thursday, Saturday.
- Location: Route 35 National Park Gate (10_15).
- Rules: Use lead Pokémon to catch a bug Pokémon; judged on health, level, and stats.
- Suicune confirmed on Route 42 (Turn 14980). Currently in the tall grass at (46, 12). strategy: walk back and forth to trigger encounter.
- Note: Roaming Pokemon change locations when player changes maps. Stay on Route 42 to keep Suicune here.