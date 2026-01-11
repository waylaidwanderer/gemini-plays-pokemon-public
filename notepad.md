# Gem's Pokémon Crystal Knowledge Base

## Tile Mechanics (Verified)
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Traversable with SURF (requires Move + Badge). Pier stops surfing.
- TALL_GRASS / LONG_GRASS: Traversable.
- grass: Traversable.
- DOOR / WARP / CAVE: Entry points.
- LADDER: Traversable.
- COUNTER: Impassable. Interact from front tile.
- LEDGE_HOP_DOWN: One-way jump down from North to South.
- FLOOR_UP_WALL: Collision type for ledges. Blocks movement from North.
- OBJECTS (NPCs/Items): Impassable.

## Progress Tracking
- **Find Misty Quest:** Started Turn 40635.

## Party Management
- **HM Users:** ICARUS (FLY), LAPIS (SURF/WATERFALL/WHIRLPOOL), KIMCHI (CUT/FLASH), GNEISS (STRENGTH/ROCK SMASH).

## Quest Log & Battle History
- **Kanto Gyms:**
  - Vermilion (Lt. Surge): DEFEATED.
  - Saffron (Sabrina): DEFEATED.
  - Pewter (Brock): DEFEATED.
  - Cerulean (Misty): Target. End of Route 25.
- **Recent Battles (Route 4):**
  - Picnicker Hope (9, 8): DEFEATED.
  - Bird Keeper Hank (17, 9): DEFEATED.

## General Lessons & Error Log
- **Radio UI:** Press 'Down' to move focus from tabs to the dial.
- **Snorlax:** Occupies (34,8)-(35,9). Interact from (34,10) Up or (36,8) Left.
- **Diglett's Cave:** (3, 3) <-> (17, 3) is an internal loop. Northern exit is (15, 5) warp carpet.

- **Button Mixing:** Never mix directional and action buttons in a single `press_buttons` call. It results in only the first button being pressed.

## Cerulean City & Surroundings
- **Cerulean City Ledge Navigation:** The path around the ledges to reach the northern area (33, 23) involves going south to (32, 30), then east and north.
- **NPC Info:** Fisher (31, 26) is a fan of Misty but has no location info.
- **Cerulean Cape Sign:** (23, 7) "CERULEAN CAPE AHEAD".
- **Route 24 Exit:** The ladder at (21, 0) leads to Route 24.
- **Rocket Grunt:** Previously encountered at (8, 7).
- **Route 25 Trainers:**
  - #1 Schoolboy Dudley (12, 10): DEFEATED.
  - #2 Lass Ellen (16, 11): DEFEATED.
  - #3 Schoolboy Joe (21, 8): DEFEATED.
  - #4 Lass Laura (24, 6): DEFEATED.
  - #5 Camper Lloyd (25, 5): DEFEATED.
  - #6 Lass Shannon (28, 11): DEFEATED.
  - #7 Super Nerd Pat (31, 7): DEFEATED (Not part of challenge).
  - Challenge: Beat 6 trainers - COMPLETED.
  - Prize Giver: Cooltrainer Kevin (37, 8). Received NUGGET.
  - Battle: Cooltrainer Kevin (ID 10): DEFEATED.
  - Misty: Likely beyond Cut Tree at (34, 6).
  - Item picked up: PROTEIN at (32, 4).