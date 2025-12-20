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
- GRASS: Standard wild encounter tile. Traversable.
- LEDGE_HOP_DOWN: One-way jump down. Traversable from above.
- LEDGE_HOP_LEFT: One-way jump left. Traversable from right.
- LEDGE_HOP_RIGHT: Jump from left to right (West to East). Impassable from the right.
- HEADBUTT_TREE: Impassable. Can be interacted with using Headbutt.

# Trainer Teams & Progress
- Malice (Burned Tower 1F): Haunter Lv20, Croconaw Lv22, Zubat Lv20, Magnemite Lv18.
- Sage Ping, Medium Grace, Sage Jeffrey, Medium Martha, Leader Morty: Defeated. (Ecruteak Gym)
- Beauty Valerie (Route 38): Hoppip, Skiploom. Defeated.
- Bird Keeper Toby (Route 38): Doduo Lv15, Doduo Lv16, Doduo Lv17. Defeated.
- Sailor Harry (Route 38): Wooper Lv19 (Active).

# Lessons Learned
- Keyboard Layout (Naming Screen): 9 Columns wide. Row 0: A-I, Row 1: J-R, Row 2: S-Z, Row 3: symbols, Row 4: [lower], [DEL], [END]. Wide buttons on Row 4.
- Nicknaming Error: Failed 'Ducat' naming resulted in 'XFDW' due to keyboard layout hallucination.
- Ecruteak Gym Path: Safe path follows trainer sightlines; (6, 7) is a verified safe connection.
- Route 38 Navigation: Map divided by wall at row 8. Westward path to Olivine is north of the wall. Access via column 30.

# Strategy & Exploration
- Goal: Reach Olivine City (West) via Route 38/39.
- Current Task: Exploration of Route 38. Started Turn #5240 (Friday, Dec 19, 9:00 PM).
- Catch Checklist: Magnemite, Miltank, Tauros.

# Type Effectiveness (Verified)
- Rock vs Flying: Super Effective (Gneiss's Rock Throw vs Doduo).
- Normal vs Rock: Not Very Effective (Doduo's Scratch vs Gneiss).

# Tool Management
- find_path_v2: Reliable for navigation. Use (6,7) override for Ecruteak Gym.
- battle_strategist_v2: Use for tactical advice in major battles.