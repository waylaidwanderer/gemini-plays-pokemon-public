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
- WARP_CARPET / WARP_CARPET_DOWN: Entry/Exit points.
- LEDGE / LEDGE_HOP_DOWN: One-way jump down (from Above).
- FLOOR_UP_WALL: Collision type for ledges. Blocks movement from North.
- OBJECTS (NPCs/Items): Impassable.
- MART_SHELF / BOOKSHELF / RADIO / INCENSE_BURNER: Impassable.
- grass: Traversable. (Turn 40984).

## Party Management
- **Current Lead:** Calcifer (TYPHLOSION Lv58). (Turn 40991).
- **HM Users:** ICARUS (FLY), LAPIS (SURF/WATERFALL/WHIRLPOOL), KIMCHI (CUT/FLASH), GNEISS (STRENGTH/ROCK SMASH).

## Battle Strategies
- **Brock (Pewter Gym):** DEFEATED.
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
  - Firebreather Burt (Route 3): DEFEATED. (Turn 40906).
  - Firebreather Otis (Route 3): DEFEATED. (Turn 40845).

## Strategy: Mt. Moon
- **Start Turn:** 40843
- **Preparation:** Ensure GNEISS (Graveler) has PP for Earthquake/Rollout. Check for items like Moon Stone.
- **Navigation:** Mt. Moon often has multiple floors. Use ladders and mark them.
- **Exploration:** Check "Potentially Reachable Unseen Tiles" near walls for hidden paths or items.

## General Lessons & Error Log
- **Radio UI:** Press 'Down' to move focus from tabs to the dial.
- **Snorlax:** Occupies (34,8)-(35,9). Interact from (34,10) Up or (36,8) Left.
- **Diglett's Cave:** (3, 3) <-> (17, 3) is an internal loop. Northern exit is (15, 5) warp carpet.

## Strategy: Finding Misty
- **Start Turn:** 40635
- **Path:** Pewter City -> Route 3 -> Mt. Moon -> Cerulean City -> Route 24 -> Route 25.
- **Pewter City (33, 19):** Sign says "MT.MOON GIFT SHOP NOW OPEN!".
- **Route 3 Navigation:** Vertical walls block at X=13, 19, 24, 32, 35, 40, and 54. Rows 0, 3, 4 are clear for early walls. Row 6/7 seems to be the bypass for the X=50 and X=54 walls. (Turn 40897).
- **Repel Status:** Super Repel active (200 steps from Turn 40885).
## Strategy: Rival Silver (Mt. Moon)
- Location: Mt. Moon (3_85) at (4, 3).
- Silver's Team: DEFEATED (Turn 40946).
- Team Summary: Sneasel, Feraligatr, Golbat, Gengar, Alakazam, Magneton.
- Victory: Calcifer (Typhlosion) finished with Flame Wheel.
- **Mt. Moon Square:** Sign at (17, 7) says "MT. MOON SQUARE - DON'T LITTER". Gift Shop is at (13, 7). (Turn 40956).
- **Mt. Moon Gift Shop (15_11):** Gramps (4, 3) sells: Poke Doll (1000), Fresh Water (200), Soda Pop (300), Lemonade (350), Repel (350), Portraitmail (50). (Turn 40969).
- **Tile Mechanics Update:** 
    - MART_SHELF, COUNTER, BOOKSHELF, RADIO, INCENSE_BURNER: Impassable.
    - grass (in Mt. Moon Square): Traversable, potential wild encounters. (Turn 40981).
- **Healing Task:** Started Turn 40974. Using Lemonade on GNEISS. (Turn 40981).
## Strategy: Mt. Moon Square Exploration
- **Goal:** Reach the western edge (1, 8).
- **Obstacles:** Walls at X=3, 4, 11, 15, 19, 20, 23, 25. Ledges at Y=11, 14.
- **Hypothesis:** The map has isolated tiers. The central Box (Rows 6-10) and Lower Area (Rows 12-13) are trapped by walls and ledges. Access to the Western Edge (X=1-2) likely requires a different entry from Mt. Moon.
- **Plan:**
  1. Jump Down the ledge at (13, 11) to explore the Lower Area.
  2. Use the Cave at (22, 11) to return to Mt. Moon (3_85).
  3. Look for other ladders or exits in Mt. Moon that lead to the western Square.
- **Status:** At (13, 10). Repel expired. Calcifer leading. (Turn 41007).