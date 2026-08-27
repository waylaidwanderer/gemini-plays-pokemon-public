# Saffron Gym - Layout, Warp Network & Progression

## Overview
- Saffron Gym (Psychic specialty).
- Gym Leader: Sabrina (Reward: Marsh Badge & TM46 Psywave).
- Mechanics: 9 square rooms connected by red warp pads.

## Entrance Room (South-Central / Room 1)
- Entrance Mat: (8..9, 17) [Map entrance from Saffron City (34, 3)]
- Statues / Plaques: (9, 15)
- Gym Guide: (10, 15)
- Warp Pads in Entrance Room:
  - Top-Right Warp: (11, 15) [Connects to Southeast Room (19, 17)]

## Southeast Room (SE / Room 9)
- Boundaries: cols 14-19, rows 13-17
- Trainer: Psychic at (17, 15): Slowpoke Lv 33, Slowbro Lv 33 [Defeated Turn 18146]
- Warp Pads:
  - Top-Left Warp: (15, 15)
  - Top-Right Warp: (19, 15)
  - Bottom-Left Warp: (15, 17)
  - Bottom-Right Warp: (19, 17) [Arrival from Entrance Room (11, 15)]

## Northeast Room (NE / Room 3)
- Boundaries: cols 14-19, rows 1-5
- Trainer: Psychic at (17, 1): Kadabra Lv 31, Slowpoke Lv 31, Mr. Mime Lv 31 [Defeated Turn 18157]
- Warp Pads:
  - Top-Left Warp: (15, 3)
  - Top-Right Warp: (19, 3) [Arrival from Southeast (15, 15)]
  - Bottom-Left Warp: (15, 5)
  - Bottom-Right Warp: (19, 5)

## Northwest Room (NW / Room 1)
- Boundaries: cols 0-5, rows 1-5
- Trainer: Psychic at (3, 1): Slowbro Lv 38 [Defeated Turn 18166]
- Warp Pads:
  - Top-Left Warp: (1, 3) [Arrival from Northeast (15, 5)]
  - Top-Right Warp: (5, 3)
  - Bottom-Left Warp: (1, 5)
  - Bottom-Right Warp: (5, 5)

## West Room (W / Room 4)
- Boundaries: cols 0-5, rows 7-11
- Trainer: Channeler at (3, 7): Haunter Lv 38 [Defeated Turn 18174]
- Warp Pads:
  - Top-Left Warp: (1, 9)
  - Top-Right Warp: (5, 9)
  - Bottom-Left Warp: (1, 11) [Arrival from Northwest (5, 5)]
  - Bottom-Right Warp: (5, 11)

## Saffron Gym Warp Network Permutation Matrix
| Source Room | Warp Coordinate | Destination Room | Destination Coord |
|---|---|---|---|
| Entrance (S) | (11, 15) | Southeast (SE) | (19, 17) |
| Southeast (SE) | (15, 15) | Northeast (NE) | (19, 3) |
| Northeast (NE) | (15, 5) | Northwest (NW) | (1, 3) |
| Northwest (NW) | (5, 5) | West (W) | (1, 11) |
| West (W) | (5, 9) | North-Center (N) | (9, 5) |

## Saffron Gym Trainers
- Psychic in SE Room (17, 15): Slowpoke Lv 33, Slowbro Lv 33 [Defeated]
- Psychic in NE Room (17, 1): Kadabra Lv 31, Slowpoke Lv 31, Mr. Mime Lv 31 [Defeated]
- Psychic in NW Room (3, 1): Slowbro Lv 38 [Defeated]
- Gym Leader Sabrina: Alakazam Lv 43, Kadabra Lv 38, Mr. Mime Lv 37, Venomoth Lv 38

## North-Center Room (N / Room 2)
- Boundaries: cols 7-12, rows 1-5
- Trainer at (10, 1)
- Warp Pads:
  - Top-Left Warp: (9, 3)
  - Top-Right Warp: (11, 3)
  - Bottom-Left Warp: (9, 5) [Arrival from West (5, 9)]
  - Bottom-Right Warp: (11, 5)
