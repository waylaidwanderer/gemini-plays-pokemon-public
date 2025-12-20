# Key Items & Progress
- HM01 Cut (Hive Badge)
- HM03 Surf (Dance Theater)
- HM05 Flash (Zephyr Badge)
- Badges: Zephyr, Hive, Plain, Fog.
- Items: TM30 Shadow Ball.

# Party
- GNEISS (GRAVELER) Lv30: STAB Magnitude.
- Calcifer (QUILAVA) Lv28: QUICK ATTACK, HEADBUTT, SMOKESCREEN, EMBER.
- FRITTATA (TOGEPI) Lv5
- KIMCHI (ODDISH) Lv10
- EGG (CLEFFA) Lv5

# Tile Mechanics
- PIT: Warp tile that resets position to the Gym entrance. Identified by `is-warp='true'` or `type='PIT'`. These tiles are impassable. (Turn #5131)
- STATUE: Impassable background object.
- COUNTER: Impassable, interact over it.
- LEDGE_HOP: One-way traversable.
- FLOOR: Traversable (unless `is-warp='true'`). 
- WALL: Impassable.

# Trainer Rosters
- Leader Morty: Gastly Lv21 (D), Gengar Lv25 (D), Haunter Lv21 (D), Haunter Lv23 (D). (Turn #5196)

# Gym Strategy: Morty (Ghost/Poison)
- Weaknesses: Ground, Psychic, Ghost, Dark.
- Strategy: Use GNEISS with Magnitude. Rock typing resists Shadow Ball (Physical in Gen 2).
- Invisible Path: Avoid all tiles with `is-warp='true'` or `type='PIT'`. Use find_path_v2 tool.

# Defeated Trainers
- Malice (Burned Tower 1F): Haunter Lv20, Croconaw Lv22, Zubat Lv20, Magnemite Lv18.
- Sage Ping, Medium Grace, Sage Jeffrey, Medium Martha, Leader Morty: Defeated. (Ecruteak Gym)

# Lessons Learned
- Pit Warps: Tiles with `is-warp='true'` or `type='PIT'` in the Ecruteak Gym are pits that return you to the start. They are NOT safe to walk on. (Turn #5131)
- Switching in Battle: In Gen 2, the 'Will you switch?' prompt after an opponent's Pokémon faints is a YES/NO choice. Selecting 'YES' leads to the party menu. If you change your mind, press 'B' to return to the battle menu. (Turn #5140)
- Trust the XML: The Mental Map's structural data (`is-warp`, `type`) is the primary source of truth for navigation. (Turn #5144)
- Party Menu Persistence: The cursor in the party menu when using items often stays on the last selected Pokémon or moves to the next one. Use multiple 'Up' presses to reset to the top for reliable selection. (Turn #5172)

# Strategy
- Use `find_path_v2` for overworld navigation.
- Use battle_strategist_v2 for Gym leaders. (Turn #5199)