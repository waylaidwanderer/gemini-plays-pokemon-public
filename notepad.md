# Gem's Pokémon Crystal Knowledge Base

## Core Principles & Strategy
- **Scientific Method:** Observe -> Hypothesize -> Test -> Conclude.
- **Efficiency:** Running from wild battles is preferred. Use Fly for distance.
- **Menu Verification:** Use short sequences (1-5 buttons). Verify focus indicators.

## Global Tile Mechanics (Verified)
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Traversable with SURF (requires Move + Storm Badge).
- TALL_GRASS / LONG_GRASS: Traversable.
- DOOR / WARP / CAVE: Entry points.
- LADDER / PIER: Traversable. Pier stops surfing.
- COUNTER: Impassable. Interact from front tile.
- WARP_CARPET: Warp at map edges.
- WARP_CARPET_DOWN: Exit tile (Verified Turn 40722).
- LEDGE / LEDGE_HOP_DOWN: One-way jump down. (Verified Turn 40688).

## Party Management
- **Lead Pokémon:** GNEISS (GRAVELER Lv53).
- **HM Users:** ICARUS (FLY), LAPIS (SURF/WATERFALL/WHIRLPOOL), KIMCHI (CUT/FLASH), GNEISS (STRENGTH).

## Battle Strategies
- **Brock (Pewter Gym):** Lead with GNEISS (Graveler) using Earthquake. Backup: LAPIS (Poliwag) with Surf.

## Quest Log & Battle History
- **Kanto Gyms:**
  - Vermilion (Lt. Surge): DEFEATED.
  - Saffron (Sabrina): DEFEATED.
  - Pewter (Brock): Target.
  - Cerulean (Misty): Target. End of Route 25.
- **Recent Battles:**
  - Bug Catcher Ed (Route 2): DEFEATED. (Turn 40653).
  - Camper Jerry (Pewter Gym): In progress.

## General Lessons & Error Log
- **Radio UI:** Press 'Down' to move focus from tabs to the dial. (Turn 40554).
- **Snorlax:** Occupies (34,8)-(35,9). Interact from (34,10) Up or (36,8) Left.
- **Diglett's Cave:** (3, 3) <-> (17, 3) is an internal loop. Northern exit is (15, 5) warp carpet. (Turn 40617).

## Strategy: Finding Misty
- **Objective:** Find Misty on Route 25 (Cerulean Cape).
- **Path:** Route 2 -> Pewter City (Buy Repels!) -> Route 3 -> Mt. Moon -> Cerulean City -> Route 24 -> Route 25.

## Pewter City Obstacles & Pathing
- **Gym Building:** (12, 14) to (17, 17) is a solid block. Door at (16, 17). (14, 14) is WALL.
- **Fence at y=21:** Solid from x=3 to x=18. Gaps at x=2 and x=19.
- **Wall at x=3:** Solid from y=18 to y=32. Gap at y=33.
- **Wall at x=18:** Solid from y=18 to y=21. Gaps at y=17 and y=22.
- **Pokémon Center:** Occupies x=12-15, y=21-25.
- **Confirmed Path to Gym Door:** From north, go west to x=10, south to y=18, then east to (16, 18).