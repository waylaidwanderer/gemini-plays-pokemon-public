# Key Items & Progress
- HM01 Cut (Hive Badge)
- HM03 Surf (Dance Theater)
- HM05 Flash (Zephyr Badge)
- Badges: Zephyr, Hive, Plain, Fog.
- Items: TM30 Shadow Ball.

# Party
- GNEISS (GRAVELER) Lv30: MAGNITUDE, DEFENSE CURL, ROCK THROW, ROLLOUT.
- Calcifer (QUILAVA) Lv28: QUICK ATTACK, HEADBUTT, SMOKESCREEN, EMBER.
- FRITTATA (TOGEPI) Lv5: GROWL, CHARM, MUD-SLAP.
- KIMCHI (ODDISH) Lv10: ABSORB, SWEET SCENT, CUT.
- EGG (CLEFFA) Lv5: POUND, CHARM, DIZZY PUNCH.
- XFDW (MEOWTH) Lv16: SCRATCH, GROWL, BITE.

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
- Sailor Harry (Route 38): Wooper Lv19. Defeated.
- Lass Dana (Route 38): Flaaffy Lv18 (D), Psyduck (Active).

# Lessons Learned
- Keyboard Layout (Naming Screen): Hypothetical 9-column layout based on failed 'XFDW' entry. Needs verification.
- Nicknaming Error: Failed 'Ducat' naming resulted in 'XFDW'.
- Ecruteak Gym Path: Safe path follows trainer sightlines; (6, 7) is a verified safe connection.
- Route 38 Navigation: Map divided by wall at row 8. Westward path to Olivine is north of the wall. Access via column 30.

# Strategy & Exploration
- Goal: Reach Olivine City (West) via Route 38/39.
- Catch Checklist: Magnemite, Miltank, Tauros.

# Tool Management
- find_path_v2: Reliable for navigation. Use (6,7) override for Ecruteak Gym.
- battle_strategist_v2: Use for tactical advice in major battles.
- get_reachable_unseen_tiles_v1: Use to verify exploration progress.