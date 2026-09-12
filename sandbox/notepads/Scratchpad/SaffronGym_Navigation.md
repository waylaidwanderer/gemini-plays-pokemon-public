# Saffron Gym & Fighting Dojo - Strategy & Navigation

## Overview
Located in the Northeast District of Saffron City (rows 4..6, cols 24..37).
- Facility 1: Fighting Dojo (cols 26..29). Houses Blackbelt trainers and Karate Master. Reward: Hitmonlee or Hitmonchan.
- Facility 2: Saffron Gym (cols 30..35). Gym Leader Sabrina (Psychic specialist). Marshbadge (allows Pokémon up to Lv 70 to obey, enables HM field move outside battle if applicable).

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
