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
    - Bottom-Left (15, 17): [Untested].
    - Top-Left (15, 15): [Untested].

- **Room 3 (East-Central Room)**:
  - Interior Bounds: cols 14..19, rows 7..11.
  - Trainer: Psychic Cameron at (17, 7) facing South. Team: Mr. Mime Lv 34, Kadabra Lv 34 (in progress).
  - Warp Tiles:
    - Top-Right (19, 9): <---> Room 2 (Southeast) (19, 15) [Verified Turn 13118].
    - Bottom-Right (19, 11): [Untested].
    - Top-Left (15, 9): [Untested].
    - Bottom-Left (15, 11): [Untested].