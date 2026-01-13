# Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- TALL_GRASS: Traversable.
- HEADBUTT_TREE: Impassable.
- LEDGE_HOP_DOWN: One-way south.
- LEDGE_HOP_RIGHT: One-way east.
- WATER: Traversable (HM03 Surf).
- DOOR/WARP/WARP_CARPET: Map transition.
- PIT: One-way warp down.
- LADDER: Warp.

# Quest: Legendary Hunt
- Target: Suicune (Tin Tower)
- Lore: Ho-Oh resurrected Suicune, Entei, and Raikou. 
- Requirements: Clear Bell (Owned), 16 Badges (Owned).
- Plan:
    1. Find Suicune Sightings - IN PROGRESS.
       - Cianwood City: Northern ledge past Pharmacy at (7, 4). (NOT DONE).
         Route: Go south to row 33, cross column 9 at (9, 33), go south to row 34, cross column 5 at (5, 34), then go north up the far west side (column 2) to row 4.
       - Route 42: Middle island with Apricorn trees (requires Surf).
       - Route 36: Near Sudowoodo's old spot (36, 9).
    2. Defeat Wise Trio (Ecruteak 4_1) - Triggered by completing sightings.
    3. Battle Suicune (Tin Tower 1F).

# Strategy: Suicune Capture (Tactical Update)
- Lead: XENON (Haunter, Lv 44). Land Hypnosis immediately.
- Chipping: Use Night Shade TWICE (88 fixed damage). A Level 40 Suicune (HP ~130-145) will be in yellow/red health. Check bar before using a third hit.
- Status: Maintain Sleep. If Sleep fails, use KIMCHI's Sleep Powder (75% accuracy).
- Capture: Ultra Balls while asleep.
- Items: Ultra Balls (32), Full Restore.

# Observations: Wise Trio & Suicune
- Building 4_1: Sage KOJI loops dialogue. NPC at (3, 10) confirmed as Gramps (ID 4), not Sage Masa.
- Prerequisite: All Johto Suicune sightings must be completed to trigger the final event.

# Pokemon Movesets
- XENON (Haunter): Hypnosis, Confuse Ray, Night Shade, Dream Eater.
- Calcifer (Typhlosion): Flamethrower, Return, Smokescreen, Thunderpunch.
- KIMCHI (Gloom): Flash, Petal Dance, Cut, Sleep Powder.
- GNEISS (Graveler): Earthquake, Defense Curl, Strength, Rollout.
- GORP (Snorlax): Surf, Rest, Body Slam, Rollout.
- ICARUS (Pidgeotto): Fly, Sand-Attack, Gust, Quick Attack.

# Navigation Log
- Turn 46375: `navigate` to (2, 34) failed to move player from (9, 16). Player is boxed in by ROCK (8, 16) and ROCK (9, 17) and WALL (9, 15). Only exit is Right to (10, 16).
- Turn 46377: Fixed `find_path_v7_robust` bug (case-sensitivity and BUOY collision). Initiating manual movement to escape corner.
- Turn 46379: Traced path to West Cianwood. X=9 wall gap at Y=33 is blocked from North by FLOOR_UP_WALL at Y=34. Gap at X=9 and X=5 wall is at Y=51. 
- Plan: (11, 16) -> (11, 51) -> (2, 51) -> (2, 34) -> (2, 4) -> (7, 4).
- Turn 46381: Traced land path around north-east water. Column 11 is blocked by water at Y=22. 
- Path: (11, 21) -> (9, 21) -> (9, 29) -> (12, 29) -> (12, 44) -> (4, 44) -> (4, 34) -> (2, 34) -> (2, 4) -> (7, 4).
- Initiating first leg: navigate to (9, 29).
- Turn 46389: Navigation south at X=17 blocked by building at Y=36. Row 50 ledge (X=12-19) blocks south entry. Gap found at X=20.
- Revised Path: (17, 35) -> (20, 35) -> (20, 51) -> (4, 51) -> (4, 34) -> (2, 34) -> (2, 4) -> (7, 4).
- Initiating leg to (4, 51).

# Reflection Turn 46390
1. Immediate Execution: No deferred tasks.
2. Notepad Hygiene: Organized. Added Navigation Log timestamps.
3. Map Hygiene: Marked NPC 1 (Standing Youngster). Need to mark Pharmacy/Gym/Photo Studio more precisely if I visit.
4. Automation Strategy: `find_path_v7_robust` refined recently.
5. Goal Clarity: Primary goal is capture, sightings are steps.
6. Error Analysis: Corrected pathing at (25, 39). Ledge at Y=40 blocks south. Must go Left to X=20.

- Turn 46390: Path at (25, 39) blocked by WALL at (25, 40). Gap is at (20, 39).
- Revised Plan: (25, 39) -> (20, 39) -> (20, 48) -> (27, 48) -> (27, 41) -> (28, 41) -> (28, 51) -> (4, 51) -> (2, 34) -> (7, 4).
- Leg 1: (25, 39) -> (20, 39).
- Leg 2: (20, 39) -> (20, 48).
- Leg 3: (20, 48) -> (27, 48) -> (27, 41) -> (28, 41) -> (28, 51).
- Leg 4: (28, 51) -> (4, 51).
- Leg 5: (4, 51) -> (2, 34).
- Leg 6: (2, 34) -> (7, 4).
- Currently: Moving to (20, 48).