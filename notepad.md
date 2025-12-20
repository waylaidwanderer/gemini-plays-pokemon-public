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
- Western Ecruteak: The exit to Route 38 is via Warp Carpets at (0, 18) and (0, 19). Navigate around trees and walls at x=1.

# Strategy
- Navigate Route 38 via the Ecruteak Gatehouse.
- Talk to the Officer in the gatehouse for potential items or info.
- Explore Route 38 for trainers and items on the way to Olivine City.
- Maintain party health and monitor PP during route progression.
- Use battle_strategist_v2 for significant trainer encounters.

# Route 38 Plan
- Head west from the Ecruteak gatehouse.
- Explore tall grass for encounters and items.
- Battle all trainers to maintain team levels (Target: Lv30+).

# Tool Management
- find_path_v2: Uses coordinate list output. Set autopress_buttons=false for overworld navigation. (Turn #5223 fix)