# Suicune Quest Log (Crystal Version)
- Prerequisites: Clear Bell, All Sightings Completed.
- Start: Turn 24182, Saturday 12:45 AM.

## Story Progress
- Clear Bell: Obtained.
- Team Rocket: Disbanded at Radio Tower.
- Tin Tower: Shook after obtaining Clear Bell.
- Wise Trio Room: Emptied.

## Sighting Progress
1. Burned Tower: Beasts fled. [Verified]
2. Cianwood City (North): Seen at (10, 14). [Verified]
3. Route 42 (Central Island): First attempt failed (likely missed trigger tile).
4. Route 36 (Sudowoodo Junction): Pending.
5. Tin Tower 1F: Checked. Suicune not present.

## Hypotheses
- Hypothesis 1: Route 42 sighting is next. (Likely missed tile)
- Hypothesis 2: Route 36 sighting is next.
- Hypothesis 3: Eusine at Ecruteak Pokecenter provides a trigger. (Confirmed: No)
- Hypothesis 4: Suicune is already at Tin Tower 1F. (Confirmed: No)

## Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- DOOR: Map transition (Building entrance).
- COUNTER: Impassable; interact with NPC behind it.
- WARP_CARPET_DOWN/LEFT/RIGHT: Map transition.
- LADDER/STAIRS: Map transition.
- PC: Impassable; interact for storage.
- CUT_TREE: Impassable; remove with HM01 CUT.
- HEADBUTT_TREE: Impassable; can be Headbutted.
- WATER: Traversable with HM03 SURF.
- GRASS: Traversable; wild encounters possible.
- LEDGE_HOP_DOWN/RIGHT: One-way traversal (down/right only).

## Type Effectiveness (Verified in Crystal)
- Ghost vs Normal: Immune (XENON Lick vs Raticate)
- Fire vs Grass: Super Effective (Calcifer Flame Wheel vs Oddish)
- Water vs Rock/Ground: Super Effective (Ravioli Bubble vs Geodude)
- Psychic vs Poison: Super Effective (Lucid Confusion vs Koffing)

## Party Movesets
- KIMCHI (GLOOM): ABSORB, SWEET SCENT, CUT, SLEEP POWDER
- ICARUS (PIDGEY): FLY, SAND-ATTACK, GUST, QUICK ATTACK
- GNEISS (GRAVELER): EARTHQUAKE, DEFENSE CURL, STRENGTH, ROLLOUT
- Ravioli (KRABBY): BUBBLE, LEER, SURF
- Calcifer (TYPHLOSION): FLAME WHEEL, HEADBUTT, SMOKESCREEN, THUNDERPUNCH
- XENON (GASTLY): HYPNOSIS, LICK, NIGHT SHADE, MEAN LOOK

## NPC Registry
- Ecruteak Pokecenter:
  - Nurse (3, 1) [Checked]
  - Gym Guide (7, 1) [Checked]
  - Pokefan M (7, 6) [Checked]
  - Cooltrainer F (1, 4) [Checked]
- Tin Tower Gatehouse:
  - Sage (4, 6) [Allowed passage]
  - Sage (6, 9) [Tin Tower shook info]
  - Gramps (3, 11) [Tower history info]
- Tin Tower 1F:
  - Sage (11, 11) [Beast legend info]
  - Sage (5, 9) [Rainbow Pokemon legend info]
  - Sage (14, 6) [Tower history info]

## Tool Notes
- `find_path_v3`: Fails if target is in Ecruteak Restricted Area while player is in Main Ecruteak (and vice versa) because there is no walking path on map 4_9. Must use bridge (Wise Trio Room/Gatehouse) or Fly.
- `suicune_tracker_v2`: Expert on sightings. Confirms Route 42 sighting is required.