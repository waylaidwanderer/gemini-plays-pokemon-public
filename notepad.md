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
- Western Ecruteak: The exit to Route 38 is via Warp Carpets at (0, 18) and (0, 19) in Ecruteak City, leading to (9, 4) and (9, 5) in the gatehouse.

# Strategy
- Traverse Route 38 and 39 west towards Olivine City.
- Catch new species for Pokedex (Magnemite, Miltank, Tauros, Meowth).
- Battle all trainers to maintain level parity (Target: Lv30+).
- Locate Moomoo Farm on Route 39.

# Tool Management
- find_path_v2: Uses coordinate list output. Set autopress_buttons=false for overworld navigation. Includes safe_overrides for incorrectly labeled warps.