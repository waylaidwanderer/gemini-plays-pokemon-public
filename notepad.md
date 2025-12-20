# Key Items & Progress
- HM01 Cut (Hive Badge)
- HM03 Surf (Dance Theater)
- HM05 Flash (Zephyr Badge)
- Badges: Zephyr, Hive, Plain.

# Gym Prep: Morty (Ghost)
- Team: Gastly, Haunter, Gengar (Ghost/Poison).
- Weaknesses: Ground, Psychic, Ghost, Dark.
- Strategy: Use GNEISS (Graveler) with Magnitude.

# Party
- GNEISS (GRAVELER) Lv28: STAB Magnitude.
- Calcifer (QUILAVA) Lv27
- FRITTATA (TOGEPI) Lv5
- KIMCHI (ODDISH) Lv10
- EGG (CLEFFA) Lv5

# Tile Mechanics
- PIT: Warp tile that resets position to the Gym entrance.
- STATUE: Impassable background object.
- COUNTER: Impassable, interact over it.
- LEDGE_HOP: One-way traversable.
- FLOOR: Traversable. WALL: Impassable.

# Trainer Rosters
- Sage Ping: Gastly Lv16 x3.
- Medium Grace: Haunter Lv20, Haunter (upcoming).

# Locations
- Ecruteak Gym (4_7): Entrance/Exit (4, 17), (5, 17). Morty is the Leader.
- Invisible Path Strategy: Avoid tiles with `is-warp='true'` in Mental Map. Use find_path.

# Defeated Trainers
- Malice (Burned Tower 1F): Haunter Lv20, Croconaw Lv22, Zubat Lv20, Magnemite Lv18.
- Sage Ping (Ecruteak Gym): Gastly Lv16 x3.

# Strategy
- Avoid all tiles with `is-warp='true'` or Pit markers.
- Use `find_path` to navigate between safe tiles.
- Use battle_strategist_v2 for Gym trainers and Morty.