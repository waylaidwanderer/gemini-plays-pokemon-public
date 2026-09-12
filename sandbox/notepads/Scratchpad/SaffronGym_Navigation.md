# Saffron Gym & Fighting Dojo - Strategy & Navigation

## Overview
Located in the Northeast District of Saffron City (rows 4..6, cols 24..37).
- Facility 1: Fighting Dojo (cols 26..29). Houses Blackbelt trainers and Karate Master. Reward: Hitmonlee or Hitmonchan.
- Facility 2: Saffron Gym (cols 30..35). Gym Leader Sabrina (Psychic specialist). Marshbadge (allows Pok�mon up to Lv 70 to obey, enables HM field move outside battle if applicable).

## Saffron Gym Teleporter Maze Mechanics
- Structure: Matrix of interconnected square rooms linked by floor warp tiles.
- Teleportation: Stepping onto a warp tile instantly teleports player to a specific destination room.
- Strategy: Empirically map warp pairings (Room/Coord -> Room/Coord) systematically to find the path to Sabrina.

## Combat Strategy vs Sabrina & Psychic Trainers
- Opponent Typing: Psychic (Kadabra, Mr. Mime, Venomoth, Alakazam).
- Weaknesses in Gen 1: Bug (twineedle/pin missile/leech life), Ghost (Lick is physical; note: Gen 1 engine has Psychic immune to Ghost due to coding quirk).
- Vulnerability: Gen 1 Psychic types generally have lower Physical Defense compared to their high Special stat.
- Active Team Matchup:
  - Blastoise (SHELDON) Lv 57:
    - Moves: Double-Edge (Normal, Power 100 physical, PP 15/15), Body Slam (Normal, Power 85 physical, PP 15/15), Surf (Water, Power 95 special, PP 15/15), Ice Beam (Ice, Power 95 special, PP 10/10).
    - Physical moves (Double-Edge, Body Slam) exploit the low physical Defense of Alakazam / Kadabra for easy OHKOs.
    - High HP (179) and Defense (153) provides massive bulk against Psychic attacks.

## Room & Warp Mapping
- **Room 1 (Entrance Room / South-Central)**:
  - Interior Bounds: cols 7..12, rows 13..17.
  - Entrance/Exit Mat: (8..9, 17) -> Saffron City.
  - Statue: (9, 15).
  - Gym Guide: (10, 15).
  - Warp Tile: (11, 15) <---> Room 2 (Southeast) (19, 17) [Verified Turn 13099].

- **Room 2 (Southeast Room)**:
  - Interior Bounds: cols 14..19, rows 13..17.
  - Trainer: Psychic Tyron at (17, 13) facing South. Team: Slowpoke Lv 33, Slowpoke Lv 33, Slowbro Lv 33. Defeated Turn 13116. Prize: ¥330.
  - Warp Tiles:
    - Bottom-Right (19, 17): <---> Room 1 (Entrance) (11, 15) [Verified Turn 13099].
    - Top-Right (19, 15): <---> Room 3 (East-Central) (19, 9) [Verified Turn 13118].
    - Bottom-Left (15, 17): <---> Room 5 (Southwest) (5, 15) [Verified Turn 13131].
    - Top-Left (15, 15): <---> Room 4 (Northeast) (19, 3) [Verified Turn 13130].

- **Room 3 (East-Central Room)**:
  - Interior Bounds: cols 14..19, rows 7..11.
  - Trainer: Psychic Cameron at (17, 7) facing South. Team: Mr. Mime Lv 34, Kadabra Lv 34. Defeated Turn 13124. Prize: ¥340.
  - Warp Tiles:
    - Top-Right (19, 9): <---> Room 2 (Southeast) (19, 15) [Verified Turn 13118].
    - Bottom-Right (19, 11): [Untested].
    - Top-Left (15, 9): <---> Room 4 (Northeast) (15, 3) [Verified Turn 13126].
    - Bottom-Left (15, 11): <---> Room 7 (North-Central) (9, 3) [Verified Turn 13162].

- **Room 4 (Northeast Room)**:
  - Interior Bounds: cols 14..19, rows 1..5.
  - NPC: Gym Member at (17, 1) (friendly advice: "Psychic POKéMON fear only ghosts and bugs!").
  - Warp Tiles:
    - Top-Left (15, 3): <---> Room 3 (East-Central) (15, 9) [Verified Turn 13126].
    - Top-Right (19, 3): <---> Room 2 (Southeast) (15, 15) [Verified Turn 13130].
    - Bottom-Left (15, 5): <---> Room 6 (Northwest) (1, 3) [Verified Turn 13145].
    - Bottom-Right (19, 5): <---> Room 5 (Southwest) (1, 15) [Verified Turn 13144].

- **Room 5 (Southwest Room)**:
  - Interior Bounds: cols 1..5, rows 13..17.
  - Trainer: Channeler at (3, 13) facing South. Team: Gastly Lv 33, Gastly Lv 33, Haunter Lv 33. Defeated Turn 13142. Prize: ¥990.
  - Warp Tiles:
    - Top-Right (5, 15): <---> Room 2 (Southeast) (15, 17) [Verified Turn 13131].
    - Top-Left (1, 15): <---> Room 4 (Northeast) (19, 5) [Verified Turn 13144].
    - Bottom-Left (1, 17): [Untested].
    - Bottom-Right (5, 17): [Untested].

- **Room 6 (Northwest Room)**:
  - Interior Bounds: cols 0..5, rows 1..5.
  - Trainer: Psychic at (3, 1) facing South. Team: Slowbro Lv 38. Defeated Turn 13152. Prize: ¥380.
  - Warp Tiles:
    - Top-Left (1, 3): <---> Room 4 (Northeast) (15, 5) [Verified Turn 13145].
    - Top-Right (5, 3): <---> Room 7 (North-Central) (11, 3) [Verified Turn 13154].
    - Bottom-Left (1, 5): [Untested].
    - Bottom-Right (5, 5): [Untested].

- **Room 7 (North-Central Room)**:
  - Interior Bounds: cols 7..12, rows 1..5.
  - Trainer: Channeler at (10, 1) facing South. Team: Gastly Lv 34, Haunter Lv 34. Defeated Turn 13159. Prize: ¥1020.
  - Warp Tiles:
    - Top-Right (11, 3): <---> Room 6 (Northwest) (5, 3) [Verified Turn 13154].
    - Top-Left (9, 3): <---> Room 3 (East-Central) (15, 11) [Verified Turn 13162].
    - Bottom-Left (9, 5): [Untested].
    - Bottom-Right (11, 5): [Untested].