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

# Defeated Trainers
- Malice (Burned Tower 1F): Haunter Lv20, Croconaw Lv22, Zubat Lv20, Magnemite Lv18.
- Sage Ping: Gastly Lv16 x3.
- Medium Grace: Haunter Lv20 x2.
- Sage Jeffrey: Haunter Lv22.
- Medium Martha: Gastly Lv18, Haunter Lv20, Gastly Lv20.
- Leader Morty: Gastly Lv21, Gengar Lv25, Haunter Lv21, Haunter Lv23. (Turn #5196)

# Lessons Learned
- Pit Warps: XML `is-warp='true'` or `type='PIT'` are hazards. (Turn #5131)
- Switching: 'Will you switch?' prompt is YES/NO. (Turn #5140)
- Trust the XML: Structural data is the primary truth. (Turn #5144)
- Party Menu: Use 'Up' to reset cursor for reliability. (Turn #5172)
- Ecruteak Gym Path: Safe path follows trainer sightlines. (Turn #5110)

# Strategy
- Use `find_path_v2` for navigation.
- Use battle_strategist_v2 for Gym leaders. (Turn #5199)
- Verified: (6, 7) is SAFE in Ecruteak Gym. (Turn #5200)