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
- XFDW (MEOWTH) Lv16: SCRATCH, GROWL, BITE. Caught on Route 38.

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
- Beauty Valerie (Route 38): Hoppip, Skiploom. Defeated.

# Lessons Learned
- Pit Warps: XML `is-warp='true'` or `type='PIT'` are hazards in Ecruteak Gym.
- Switching: 'Will you switch?' prompt is YES/NO.
- Trust the XML: Structural data is the primary truth for navigation.
- Party Menu: Use 'Up' to reset cursor for reliability when using items.
- Ecruteak Gym Path: Safe path follows trainer sightlines; (6, 7) is a verified safe connection.
- Route 38 Exit: The exit from Ecruteak City is via Warp Carpets at (0, 18) and (0, 19).

# Strategy
- Traverse Route 38 and 39 west towards Olivine City.
- Catch new species (Magnemite, Miltank, Tauros, Meowth).
- Battle all trainers to maintain level parity (Target: Lv30+).
- Locate Moomoo Farm on Route 39.

# Tool Management
- find_path_v2: Fixed JSON error and added (6,7) override. (Turn #5248 fix)
- battle_strategist_v2: Use exact name for calls. (Turn #5245 fix)
- Beauty Valerie (Route 38): Hoppip, Skiploom. Defeated.

# Wild Pokemon (Route 38)
- Meowth (Lv16). Caught. Nickname: XFDW (intended Ducat, input error).

# Trainer Teams
- Bird Keeper Toby (Route 38): Doduo Lv15, Doduo Lv16, Doduo Lv17. Defeated.

# Type Effectiveness (Verified)
- Rock vs Flying: Super Effective (Gneiss's Rock Throw vs Doduo).
- Normal vs Rock: Not Very Effective (Doduo's Scratch/Normal moves vs Gneiss).

# Tile Mechanics
- GRASS: Standard wild encounter tile. Traversable.
- LEDGE_HOP_DOWN: One-way jump down. Traversable from above.
- LEDGE_HOP_LEFT: One-way jump left. Traversable from right.
- HEADBUTT_TREE: Impassable. Can be interacted with using Headbutt.

# Route 38 Navigation Notes
- The map is divided by a long wall at row 8 (columns 14-29).
- A north-south fence of LEDGE_HOP_RIGHT tiles at column 7 (rows 10-14) blocks westward movement in the middle of the map.
- The path to Olivine City (west) is located north of the row 8 wall.
- To reach the Fruit Tree at (12, 10) and the western exit, I must travel east to column 30, then north to row 5, then west.
- LEDGE_HOP_RIGHT: Jump from left to right (West to East). Impassable from the right.
- LEDGE_HOP_LEFT: Jump from right to left (East to West). Impassable from the left.