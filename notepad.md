# Suicune Capture Strategy (Crystal Version)
## Primary Goal: Capture Suicune
- Step 1: Obtain Clear Bell. (COMPLETE)
- Step 2: Access Tin Tower. Defeat the Wise Trio. (COMPLETE)
- Step 3: Encounter Suicune at Tin Tower. (COMPLETE - It fled).
- Step 4: Track Suicune. Use Pokédex. (Started Turn 14853).
- Step 5: Prepare Catcher. Obtain Parasect (Spore + False Swipe).
- Step 6: Execute Capture. Corner -> Mean Look -> False Swipe -> Sleep -> Ultra Balls.

## Capture Contingency & Roamer Mechanics
- Roamers (Suicune, Raikou, Entei) move between adjacent maps whenever the player crosses a map boundary.
- Interception Strategy: Stay on the same map as the roamer and pace in grass/water. Do not cross map boundaries while hunting.
- Battle Contingency: If Gastly (XENON) faints, use ICARUS or Calcifer. Mean Look is required to prevent immediate fleeing. If Suicune flees, check Pokedex immediately.

## Tile Mechanics (Global)
- FLOOR: Standard traversal.
- WALL / FENCE / MOUNTAIN: Impassable.
- TALL_GRASS: Traversable, triggers wild encounters.
- WATER: Requires Surf HM to traverse.
- LEDGE: One-way jump (usually South).
- WARP: Map transition (Doors, Stairs, Cave Entrances).
- HEADBUTT_TREE: Impassable; can be Headbutted if known.
- CUT_TREE: Impassable; requires Cut HM to clear.
- FLOOR_UP_WALL: One-way movement North only.
- COUNTER: Impassable; interact with NPCs behind them from the front.
- WARP_CARPET: Map transition at edges.

## Route 42 Notes
- Requirements: Surf (Ravioli knows it), Cut (KIMCHI knows it).
- Suicune Roaming Area: Route 42 (Verified Turn 14980). Intercept point: (46, 12).

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
## Roamer Hunt Log
- Suicune hunt started Turn 14980. Location: Route 42.
- Interception Point: (46, 12).
- Repel Strategy: Lead with a Pokémon leveled higher than local wild Pokémon (Lv13-16) but lower than Suicune (Lv40), such as KIMCHI (Lv21), and use a Super Repel to isolate the Suicune encounter.
- Current Status: Training XENON to Lv 17 on Route 42 (Turn 15027). This will allow the Repel strategy to isolate Suicune encounters.