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

## Gym Trainers (Empirically Verified)
1. Juggler 1 at (8, 13): [DEFEATED Turn 17363] Hypno Lv 38; �1330 prize.
2. Juggler 2 at (7, 8) / (8, 8): [DEFEATED Turn 17378] Drowzee Lv 31, Drowzee Lv 31, Kadabra Lv 31, Drowzee Lv 31; �1085 prize.

## Verified Collision & Traversal Matrix (Turn 17371)
- **Open Passable Tiles**:
  - Entrance Corridor: (4..5, 14..17)
  - Eastern Outer Corridor: (9, 5..14) and (8, 9..14)
  - Central Corridors: (4..7, 13)
- **Verified Invisible Wall Collisions**:
  - Row 12 Horizontal Barrier: (3..7, 12) solid invisible wall
  - Row 11: (7, 11) solid invisible wall
  - Row 10: (7, 10) solid invisible wall
  - Row 9: (6, 9) solid invisible wall
  - Row 8: (5..6, 8) solid invisible wall
  - Row 7: (6..7, 7) solid invisible wall
  - Row 6: (6, 6) solid invisible wall
  - Row 5: (7, 5) solid invisible wall
  - Ledge / Wall on Row 31 (exterior): (2..6, 31)

## Koga Battle Preparation (Hypothesis to be Verified in Battle)
- Expected Type: Poison-type specialists (Koffing/Muk/Weezing lines).
- Active Counter: Blastoise (Surf / Ice Beam / Double-Edge).
