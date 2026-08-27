# Saffron Gym - Layout, Warp Network & Progression

## Overview
- Saffron Gym (Psychic specialty).
- Gym Leader: Sabrina (Reward: Marsh Badge & TM46 Psywave).
- Mechanics: 9 square rooms connected by red warp pads.

## Room Layouts & Warp Permutations

### Entrance Room (South-Central / Room 1)
- Boundaries: cols 7-12, rows 13-17 [Entrance at (8..9, 17)]
- Gym Guide: (10, 15), Statues: (9, 14..15)
- Warp Pad: (11, 15) -> Southeast Room (19, 17)

### Southeast Room (SE / Room 9)
- Boundaries: cols 14-19, rows 13-17
- Trainer: Psychic at (17, 15): Slowpoke Lv 33, Slowbro Lv 33 [Defeated]
- Warp Pads:
  - Top-Left: (15, 15) -> Northeast Room (19, 3)
  - Top-Right: (19, 15)
  - Bottom-Left: (15, 17)
  - Bottom-Right: (19, 17) [Arrival from Entrance (11, 15)]

### Northeast Room (NE / Room 3)
- Boundaries: cols 14-19, rows 1-5
- Trainer: Psychic at (17, 1): Kadabra Lv 31, Slowpoke Lv 31, Mr. Mime Lv 31 [Defeated]
- Warp Pads:
  - Top-Left: (15, 3)
  - Top-Right: (19, 3) [Arrival from Southeast (15, 15)]
  - Bottom-Left: (15, 5) -> Northwest Room (1, 3)
  - Bottom-Right: (19, 5)

### Northwest Room (NW / Room 1)
- Boundaries: cols 0-5, rows 1-5
- Trainer: Psychic at (3, 1): Slowbro Lv 38 [Defeated]
- Warp Pads:
  - Top-Left: (1, 3) [Arrival from Northeast (15, 5)]
  - Top-Right: (5, 3) [Arrival from North-Center (11, 3)]
  - Bottom-Left: (1, 5) -> Center Room (11, 11)
  - Bottom-Right: (5, 5) -> West Room (1, 11)

### West Room (W / Room 4)
- Boundaries: cols 0-5, rows 7-11
- Trainer: Channeler at (3, 7): Haunter Lv 38 [Defeated]
- Warp Pads:
  - Top-Left: (1, 9)
  - Top-Right: (5, 9) -> North-Center Room (9, 5)
  - Bottom-Left: (1, 11) [Arrival from Northwest (5, 5)]
  - Bottom-Right: (5, 11)

### North-Center Room (N / Room 2)
- Boundaries: cols 7-12, rows 1-5
- Trainer: Channeler at (10, 1) [Defeated]
- Warp Pads:
  - Top-Left: (9, 3) [Arrival from Southwest (5, 15)]
  - Top-Right: (11, 3) -> Northwest Room (5, 3)
  - Bottom-Left: (9, 5) [Arrival from West (5, 9)]
  - Bottom-Right: (11, 5) -> Southwest Room (1, 17)

### Southwest Room (SW / Room 7)
- Boundaries: cols 0-5, rows 13-17
- Trainer: Channeler at (3, 13..15): Gastly Lv 34, Haunter Lv 34 [Engaged Turn 18361]
- Warp Pads:
  - Top-Left: (1, 15)
  - Top-Right: (5, 15) -> North-Center Room (9, 3)
  - Bottom-Left: (1, 17) [Arrival from North-Center (11, 5)]
  - Bottom-Right: (5, 17)

### Center Room (Sabrina's Chamber / Room 5)
- Boundaries: cols 7-12, rows 7-11
- Gym Leader Sabrina: (9, 8) [Kadabra Lv 38, Mr. Mime Lv 37, Venomoth Lv 38, Alakazam Lv 43]
- Warp Pad: (11, 11) [Arrival from Northwest (1, 5)]

## Saffron Gym Complete Warp Permutation Matrix
| Source Room | Warp Coordinate | Destination Room | Destination Coord |
|---|---|---|---|
| Entrance (S) | (11, 15) | Southeast (SE) | (19, 17) |
| Southeast (SE) | (15, 15) | Northeast (NE) | (19, 3) |
| Northeast (NE) | (15, 5) | Northwest (NW) | (1, 3) |
| Northwest (NW) | (5, 5) | West (W) | (1, 11) |
| West (W) | (5, 9) | North-Center (N) | (9, 5) |
| North-Center (N) | (11, 5) | Southwest (SW) | (1, 17) |
| Southwest (SW) | (5, 15) | North-Center (N) | (9, 3) |
| North-Center (N) | (11, 3) | Northwest (NW) | (5, 3) |
| Northwest (NW) | (1, 5) | Center (Sabrina) | (11, 11) |

## Full Verified Sabrina Optimal Path (9 Warps)
Entrance (11, 15) -> SE (15, 15) -> NE (15, 5) -> NW (5, 5) -> W (5, 9) -> N (11, 5) -> SW (5, 15) -> N (11, 3) -> NW (1, 5) -> Center Room (11, 11) -> Sabrina at (9, 8).
