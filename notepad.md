# Suicune Quest (Crystal) - FIXED SIGHTINGS
- Milestone 1: Burned Tower (Seen).
- Milestone 2: Cianwood City (Seen). Defeated Eusine.
- Milestone 3: Route 42 (In Progress). Pokedex confirms location.
- Milestone 4: Route 36 (Next).
- Milestone 5: Tin Tower (Final). Requirement: Clear Bell (OBTAINED) + all overworld sightings.

## Failed Hypotheses (Route 42)
- Island floor sweep (Rows 10-17) [Turns 17819-17863].
- Apricorn tree interactions (Pink, Green, Yellow) [Turns 17804-17818].
- Far Western mainland floor sweep (X=1-3, Y=8-11) [Turns 17836-17837].
- Eastern approach via northern channel [Turns 17760-17765].
- Navigation attempt to mainland (X=12, Y=8) via navigate_menu_v2 failed; cliff at (19, 10) blocks water entry from (20, 10). [Turn 17870-17871].
- Accidental warp into Mt. Mortar middle entrance at (28, 9) on Route 42. [Turn 17872].
- Exited Mt. Mortar middle entrance at (28, 9). [Turn 17875].
- Hypothesis 37: Suicune trigger is on the northern path near Mt. Mortar (X=21-33, Y=4-8).

## Current Hypothesis Testing (Route 42)
- Hypothesis 34: Trigger is on the western mainland path (X=4-12, Y=8-13). [In Progress]
- Hypothesis 35: Landing trigger on southern island bank (X=24-32, Y=15).
- Hypothesis 36: Trigger requires exiting Mt. Mortar middle entrance (28, 9) and walking south. [Failed - Turn 17876].
- Hypothesis 37: Suicune trigger is on the northern path near Mt. Mortar (X=21-33, Y=4-8). [In Progress]

# Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL / HEADBUTT_TREE / ROCK / VOID / FLOOR_UP_WALL / WATER_ROCKS: Impassable.
- CUT_TREE: Impassable until HM01 CUT.
- WATER: Traversable with HM03 SURF.
- TALL_GRASS / LONG_GRASS: Traversable; triggers encounters.
- LEDGE: One-way traversable (usually South).
- WARP / DOOR / WARP_CARPET / CAVE: Map transition.
- FRUIT_TREE: Impassable; interact for fruit/apricorn.

# Verified Sprite Observations (Route 42)
- Turn 17786: run_code confirmed no Suicune sprite on screen.
- Reachable Unseen Tiles (via Mt. Mortar): (21, 4), (25, 5), (26, 5), (27, 5), (30, 4).

# PC Storage (Box 1)
- VORTEX (Poliwag 22), INTERCEPT (Yanma 12), ROCKY (Onix 6), EGG (CleFFA 5), XFDW (Meowth 16), FRITTATA (Togepi 5), SHUCKIE (Shuckle 15), Blarney (Sudowoodo 20).

# Items & Contacts
- Fire Stone: Route 36 (Alan).
- Rock Smash (Info): Route 36 (Fisher at 44, 9).
- Fisher Tully: Route 42. Gives items.
- Bug Catcher Arnie: Route 35. Reports Yanma swarms.

# Task Timestamps
- Suicune Hunt (Route 42): Started Turn 17642.
- Plan: Enter Mt. Mortar at (28, 9), exit, and walk North to explore (28, 8) and beyond to test Hypothesis 37.
- MountMortarB1F (3_60): Entered via ladder at (19, 29). Found item ball at (21, 26). Exploring for exit to Route 42 northern path.
- Observed strange movement redirection in MountMortarB1F:
  - Action 'Up' at (20, 28) moved player 'Right' to (21, 28).
  - Action 'Right' at (21, 27) moved player 'Down' to (21, 28).
  - Action 'Up' at (21, 28) successfully moved player 'Up' to (21, 27).
  - Hypothesis: FLOOR_UP_WALL tiles or specific boundaries in this area may redirect movement. Testing 'Up' at (21, 28) to reach item at (21, 26).