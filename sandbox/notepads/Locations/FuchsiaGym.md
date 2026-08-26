# Fuchsia Gym - Layout, Invisible Wall Maze & Battle Strategy

## Overview
- Gym Leader: **Koga** (Poison specialist)
- Reward: **Soul Badge** (Badge 5/8, allows field use of HM03 Surf, boosts Defense) + **TM06 (Toxic)**
- Mechanics: Invisible walls dividing the arena into a maze; Jugglers and Tamers positioned along the paths.

## Layout & Landmarks (Empirically Verified)
- Entrance / Exit Mat: (4..5, 17) [South exit to Fuchsia City]
- Left Statue: (3, 14..15)
- Right Statue: (6, 14..15)
- Gym Guide: (7, 15)
- Center Platform: Koga positioned at (4..5, 10..11)

## Gym Trainers
1. Juggler 1 at (8, 13): [DEFEATED Turn 17363] Hypno Lv 38; �1330 prize.
2. Juggler 2 at (7, 8) / (8, 8): [DEFEATED Turn 17378] Drowzee Lv 31, Drowzee Lv 31, Kadabra Lv 31, Drowzee Lv 31; �1085 prize.
3. Tamer 1 at (8, 2): [DEFEATED Turn 17386] Arbok Lv 33, Sandslash Lv 33, Arbok Lv 33; �1320 prize.
4. Tamer 2 at (3, 5): [DEFEATED Turn 17399] Sandslash Lv 34, Arbok Lv 34; �1360 prize.
5. Juggler 3 at (2, 7): [DEFEATED Turn 17407] Drowzee Lv 34, Hypno Lv 34; �1190 prize.
6. Trainer at (1, 12): Engaging from (1, 13) [Turn 17410].

## Maze Topology & Traversal Protocol
- **Empirically Verified Invisible Wall Collisions**:
  - (2, 6) confirmed solid invisible wall [Turn 17403]
  - (1, 11) confirmed solid invisible wall [Turn 17410]
- **Empirically Verified Walkable Corridors**:
  - Entrance Area: (4..5, 14..17)
  - Eastern Perimeter: (9, 1..14) and (8, 9..14)
  - Northern Perimeter: (1..9, 1)
  - Northwest Approach: (1, 1..3) -> (2..3, 3) -> (3, 4)
  - West Corridor: (2, 3..6)
- **Visually Identified Dashed Invisible Wall Tiles (To be confirmed by path avoidance)**:
  - Row 2: (2, 2), (3, 2), (7, 2)
  - Row 3: (4, 3), (5, 3), (7, 3)
  - Row 4: (0, 4), (1, 4), (4, 4), (7, 4)
  - Row 5: (4, 5), (7, 5)
  - Row 6: (0, 6), (3, 6), (6, 6)
  - Row 7: (0, 7), (6, 7), (8, 7)

## Gym Leader Koga Battle (Empirically Verified Turn 17419)
- Leader: Koga (Poison specialist)
- Team: Koffing Lv 37, Muk Lv 39, Koffing Lv 37, Weezing Lv 43
- Result: Defeated! Soul Badge & TM06 (Toxic) obtained; �4257 prize money.
- Unlocked Field HM: HM03 Surf usable outside of battle.
