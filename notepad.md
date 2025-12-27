# Suicune Quest Log (Crystal Version)
- Prerequisites: Clear Bell, All Sightings Completed.
- Start: Turn 24182, Saturday 12:45 AM.

## Story Progress
- Clear Bell: Obtained.
- Team Rocket: Disbanded at Radio Tower.
- Tin Tower: Shook after entering gatehouse with Clear Bell.
- Wise Trio Room: Emptied.

## Sighting Progress
1. Burned Tower: Beasts fled. [Verified]
2. Cianwood City (North): Seen at (10, 14). [Verified]
3. Route 42 (Central Island): Pending. (Swept island Turn 25515, no trigger).
4. Route 36 (Sudowoodo Junction): Pending.
5. Tin Tower 1F: Pending. (Checked Turn 25477, no encounter).

## Hypotheses & Strategy
- Hypothesis 1: Route 42 sighting is next.
- Hypothesis 2: Route 36 sighting is next. [Current Target - Started Turn 25535]
- Hypothesis 3: Eusine provides a trigger. (Confirmed: No at Ecruteak Pokecenter)
- Hypothesis 4: Suicune is already at Tin Tower 1F. (Confirmed: No)

## Strategy & Planning
- Route 36 sighting: Fly to Ecruteak, walk south to Route 36 junction via Route 37, and approach from the south (Route 35 entrance).
- Route 42 sighting: Use Surf to reach the island and Cut to remove the tree. Stand on every tile of the island platform.

## Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- DOOR: Map transition.
- COUNTER: Impassable; interact with NPC behind it.
- WARP_CARPET: Map transition.
- LADDER/STAIRS: Map transition.
- CUT_TREE: Impassable; remove with CUT.
- HEADBUTT_TREE: Impassable; can be Headbutted.
- WATER: Traversable with SURF.
- GRASS: Traversable; wild encounters.
- LEDGE_HOP: One-way traversal.

## Party Movesets
- KIMCHI (GLOOM): ABSORB, SWEET SCENT, CUT, SLEEP POWDER
- ICARUS (PIDGEY): FLY, SAND-ATTACK, GUST, QUICK ATTACK
- GNEISS (GRAVELER): EARTHQUAKE, DEFENSE CURL, STRENGTH, ROLLOUT
- Ravioli (KRABBY): BUBBLE, LEER, SURF
- Calcifer (TYPHLOSION): FLAME WHEEL, HEADBUTT, SMOKESCREEN, THUNDERPUNCH
- XENON (GASTLY): HYPNOSIS, LICK, NIGHT SHADE, MEAN LOOK

## NPC Registry
- Ecruteak Pokecenter: Nurse, Gym Guide, Pokefan M, Cooltrainer F [All Checked]
- Tin Tower Gatehouse: Sage (4, 6) [Pass], Sage (6, 9) [Info], Gramps (3, 11) [Info]
- Tin Tower 1F: Sages at (11, 11), (5, 9), (14, 6) [All Info]

## Tool Notes
- `find_path_v3`: Robust pathfinding. Fails between separate Ecruteak maps.
- `suicune_tracker_v2`: Expert on sightings.
- `open_fly_map_v4`: Robust Fly map opener (Turn 25536).