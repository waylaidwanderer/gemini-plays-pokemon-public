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
- PIT: Warp tile that resets position to the Gym entrance. Identified by `is-warp='true'` or `type='PIT'`. These tiles are impassable.
- STATUE: Impassable background object.
- COUNTER: Impassable, interact over it.
- LEDGE_HOP: One-way traversable.
- FLOOR: Traversable (unless `is-warp='true'`). 
- WALL: Impassable.

# Defeated Trainers
- Malice (Burned Tower 1F): Haunter Lv20, Croconaw Lv22, Zubat Lv20, Magnemite Lv18.
- Sage Ping, Medium Grace, Sage Jeffrey, Medium Martha, Leader Morty: Defeated. (Ecruteak Gym)

# Lessons Learned
- Pit Warps: XML `is-warp='true'` or `type='PIT'` are hazards in Ecruteak Gym.
- Switching: 'Will you switch?' prompt is YES/NO.
- Trust the XML: Structural data is the primary truth for navigation.
- Party Menu: Use 'Up' to reset cursor for reliability when using items.
- Ecruteak Gym Path: Safe path follows trainer sightlines; (6, 7) is a verified safe connection.

# Strategy
- Navigate to Route 38 via the western exit of Ecruteak City.
- Prepare for Route 38 by exploring for trainers and items.
- Monitor Pokémon health and PP during route traversal.
- Use battle_strategist_v2 for significant trainer battles.