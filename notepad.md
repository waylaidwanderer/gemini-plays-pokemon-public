# Key Items & Progress
- HM01 Cut (Hive Badge)
- HM03 Surf (Dance Theater)
- HM05 Flash (Zephyr Badge)
- Badges: Zephyr, Hive, Plain.

# Party
- GNEISS (GRAVELER) Lv29: STAB Magnitude.
- Calcifer (QUILAVA) Lv27
- FRITTATA (TOGEPI) Lv5
- KIMCHI (ODDISH) Lv10
- EGG (CLEFFA) Lv5

# Tile Mechanics
- PIT: Warp tile that resets position to the Gym entrance. Identified by `is-warp='true'`.
- STATUE: Impassable background object.
- COUNTER: Impassable, interact over it.
- LEDGE_HOP: One-way traversable.
- FLOOR: Traversable (unless `is-warp='true'`). 
- WALL: Impassable.

# Trainer Rosters
- Sage Ping: Gastly Lv16 x3.
- Medium Grace: Haunter Lv20 x2.
- Sage Jeffrey: Haunter Lv22.
- Medium Martha (ID 4): Upcoming.

# Gym Strategy: Morty (Ghost/Poison)
- Weaknesses: Ground, Psychic, Ghost, Dark.
- Strategy: Use GNEISS with Magnitude.
- Invisible Path: Avoid all tiles with `is-warp='true'`. Use find_path tool.

# Defeated Trainers
- Malice (Burned Tower 1F): Haunter Lv20, Croconaw Lv22, Zubat Lv20, Magnemite Lv18.
- Sage Ping (Ecruteak Gym): Gastly Lv16 x3.
- Medium Grace (Ecruteak Gym): Haunter Lv20 x2.
- Sage Jeffrey (Ecruteak Gym): Haunter Lv22. (Turn #5095)

# Strategy
- Use `find_path` to navigate between safe tiles.
- Use battle_strategist_v2 for Gym trainers and Morty.
- Healing GNEISS with Berries (Turn #5105).

# Gym Puzzle Notes
- Sightline Theory: The invisible path follows the trainers' sightlines.
- Ping (3, 13) -> (6, 13).
- (6, 13) to (6, 9) is safe.
- Grace (7, 9) -> (3, 9).
- (3, 9) to (3, 7) is safe.
- Jeffrey (2, 7) -> (5, 7).
- Connection from Jeffrey to Martha: (5, 7) -> (6, 7) -> (6, 6) -> (6, 5). (Turn #5106)