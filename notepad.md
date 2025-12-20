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
- PIT: Warp tile that resets position to the Gym entrance. Identified by `is-warp='true'` or `type='PIT'`. These tiles are impassable and return the player to the start of the gym. (Turn #5131)
- STATUE: Impassable background object.
- COUNTER: Impassable, interact over it.
- LEDGE_HOP: One-way traversable.
- FLOOR: Traversable (unless `is-warp='true'`). 
- WALL: Impassable.

# Trainer Rosters
- Sage Ping: Gastly Lv16 x3.
- Medium Grace: Haunter Lv20 x2.
- Sage Jeffrey: Haunter Lv22.
- Medium Martha (ID 4): Gastly Lv18, Haunter Lv20, Gastly Lv20. (Turn #5128)
- Leader Morty: Gastly Lv21 (Defeated), Gengar Lv25 (Active).

# Gym Strategy: Morty (Ghost/Poison)
- Weaknesses: Ground, Psychic, Ghost, Dark.
- Strategy: Use GNEISS with Magnitude. Morty's Gengar is fast and uses status moves; GNEISS's Rock typing provides solid defense against Shadow Ball (Physical in Gen 2).
- Invisible Path: Avoid all tiles with `is-warp='true'` or `type='PIT'`. Use find_path_v2 tool.

# Defeated Trainers
- Malice (Burned Tower 1F): Haunter Lv20, Croconaw Lv22, Zubat Lv20, Magnemite Lv18.
- Sage Ping (Ecruteak Gym): Gastly Lv16 x3.
- Medium Grace (Ecruteak Gym): Haunter Lv20 x2.
- Sage Jeffrey (Ecruteak Gym): Haunter Lv22. (Turn #5095)
- Medium Martha (Ecruteak Gym): Gastly Lv18, Haunter Lv20, Gastly Lv20. (Turn #5143)

# Lessons Learned
- Pit Warps: Tiles with `is-warp='true'` or `type='PIT'` in the Ecruteak Gym are pits that return you to the start. They are NOT safe to walk on. (Turn #5131)
- Switching in Battle: In Gen 2, the 'Will you switch?' prompt after an opponent's Pokémon faints is a YES/NO choice. Selecting 'YES' leads to the party menu. If you change your mind, press 'B' to return to the battle menu. (Turn #5140)
- Trust the XML: The Mental Map's structural data (`is-warp`, `type`) is the primary source of truth for navigation, even if it contradicts the discovered warps list. (Turn #5144)
- Party Menu Persistence: The cursor in the party menu when using items often stays on the last selected Pokémon or moves to the next one. Use multiple 'Up' presses to reset to the top for reliable selection. (Turn #5172)

# Strategy
- Use `find_path_v2` for overworld navigation.
- Use battle_strategist_v2 for Morty.
- Current Goal: Defeat Leader Morty (Gengar active). (Turn #5181)
- Primary Goal: Defeat Gym Leader Morty. Active since Turn #5080 (approx. 7:15 PM PST). Current Turn: #5181.