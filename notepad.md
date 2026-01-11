# Gem's Pokémon Crystal Knowledge Base

## Core Principles & Strategy
- **Scientific Method:** Observe -> Hypothesize -> Test -> Conclude.
- **Efficiency:** Running from wild battles is preferred. Use Fly for distance.
- **Menu Verification:** Use short sequences (1-5 buttons). Verify focus indicators.

## Global Tile Mechanics (Verified)
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Traversable with SURF (requires Move + Badge).
- TALL_GRASS / LONG_GRASS: Traversable.
- DOOR / WARP / CAVE: Entry points.
- LADDER / PIER: Traversable. Pier stops surfing.
- COUNTER: Impassable. Interact from front tile.
- WARP_CARPET: Warp at map edges.
- WARP_CARPET_DOWN: Exit tile.
- LEDGE / LEDGE_HOP_DOWN: One-way jump down (from Above).
- FLOOR_UP_WALL: Collision type for ledges.
- OBJECTS (NPCs/Items): Impassable.

## Party Management
- **Current Lead:** GNEISS (GRAVELER Lv53). (Healed Turn 40790).
- **HM Users:** ICARUS (FLY), LAPIS (SURF/WATERFALL/WHIRLPOOL), KIMCHI (CUT/FLASH), GNEISS (STRENGTH/ROCK SMASH).

## Battle Strategies
- **Brock (Pewter Gym):** DEFEATED. (Turn 40782).
- **Misty (Cerulean Gym):** Target. Use Grass (Kimchi) or Electric moves.

## Quest Log & Battle History
- **Kanto Gyms:**
  - Vermilion (Lt. Surge): DEFEATED.
  - Saffron (Sabrina): DEFEATED.
  - Pewter (Brock): DEFEATED.
  - Cerulean (Misty): Target. End of Route 25.
- **Recent Battles:**
  - Youngster Warren (Route 3): DEFEATED. (Turn 40814).
  - Youngster Jimmy (Route 3): DEFEATED. (Turn 40826).
  - Firebreather Otis (Route 3): Defeating. (Turn 40841).

## General Lessons & Error Log
- **Radio UI:** Press 'Down' to move focus from tabs to the dial.
- **Snorlax:** Occupies (34,8)-(35,9). Interact from (34,10) Up or (36,8) Left.
- **Diglett's Cave:** (3, 3) <-> (17, 3) is an internal loop. Northern exit is (15, 5) warp carpet.

## Strategy: Finding Misty
- **Start Turn:** 40635
- **Objective:** Find Misty on Route 25 (Cerulean Cape).
- **Path:** Pewter City -> Route 3 -> Mt. Moon -> Cerulean City -> Route 24 -> Route 25.
- **Current Status:** Heading East on Route 3.
- **Pewter City (33, 19):** Sign says "MT.MOON GIFT SHOP NOW OPEN!".
- **Route 3:** Vertical walls block at X=13 (Y=4-9), X=19 (Y=4-7), and X=24 (Y=1-7). Row 0 is clear at these X-coordinates.

## Custom Tools
- find_path_v5: A* pathfinding for current map.
- press_menu_buttons_v3: Menu navigation.