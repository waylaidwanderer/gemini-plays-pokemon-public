# Key Items & Progress
- HM01 Cut (Hive Badge)
- HM03 Surf (Gentleman in Dance Theater)
- HM05 Flash (Zephyr Badge)
- Badges: Zephyr, Hive, Plain.

# Gym Prep: Morty (Ghost)
- Team: Gastly, Haunter, Gengar (Ghost/Poison).
- Weaknesses: Ground, Psychic, Ghost, Dark.
- Strategy: Use GNEISS (Graveler) with Magnitude.

# PC Storage
## Box 1 (Current)
- Blarney (SUDOWOODO) Lv20
- ROCKY (ONIX) Lv6
- ICARUS (PIDGEY) Lv11

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

# Type Effectiveness (Verified)
- Ground vs Ghost/Poison: Super Effective.
- Rock vs Flying/Poison: Super Effective (4x).

# Trainer Rosters
## Dance Theater
- Miki: Jolteon, Kuni: Vaporeon, Zuki: Umbreon, Sayo: Espeon, Naoko: Flareon.
## Ecruteak Gym
- Sage Ping: Gastly Lv16, Gastly Lv16, Gastly Lv16.

# Locations
## Ecruteak City (4_9)
- Pokemon Center: (23, 27), Gym: (6, 27), Dance Theater: (23, 21).

## Burned Tower 1F (3_13)
- Entrance: (9, 15), Holes to B1F: (5, 14), (14, 14), (10, 9), etc.

## Burned Tower B1F (3_14)
- Exit Ladder: (7, 15). Legendary Beasts released (Turn #4995).

## Ecruteak Pokecenter 1F (4_3)
- Nurse: (3, 1) area (behind counter).
- PC: (9, 1) area.
- Gym Guide: (7, 1) area.

## Ecruteak Gym (4_7)
- Entrance/Exit: (4, 17) and (5, 17).
- Sage Ping: (3, 13).
- Gym Guide Advice: Trainers have secret motives; winning reveals secrets about Ecruteak.
- Invisible Path Puzzle: The floor has pits that warp the player back to the start. Avoid tiles with `is-warp='true'` in Mental Map or Pit markers.

# Defeated Trainers
- Malice (Burned Tower 1F): Haunter Lv20, Croconaw Lv22, Zubat Lv20, Magnemite Lv18. (Turn #4982)
- Sage Ping (Ecruteak Gym): Gastly Lv16 x3. (Turn #5072)

# Strategy
- Avoid all tiles with `is-warp='true'` or Pit markers.
- Use `find_path` to navigate between safe tiles.
- Use battle_strategist_v2 for Gym trainers and Morty.