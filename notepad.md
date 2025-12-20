# Tile Mechanics
- FLOOR: Traversable. No effects. (Verified: Turn #4526)
- LONG_GRASS: Traversable. Wild Pokémon encounters. (Verified: Turn #4526)
- TALL_GRASS: Traversable. Wild Pokémon encounters. (Verified: Turn #4526)
- WALL: Impassable. Includes fences, benches, trees, signs, and NPCs. (Verified: Turn #4526)
- WATER: Impassable. Requires Surf.
- HEADBUTT_TREE: Impassable. Shaken with Headbutt.
- CUT_TREE: Impassable. Cleared with Cut.
- DOOR/WARP_CARPET: Traversable. Map transition.
- LEDGE_HOP_DOWN: One-way traversal (jump down). Blocks movement from below. (Verified: Turn #4694)
- COUNTER: Impassable. Interaction point for NPCs behind it.
- PC: Impassable. Interacted from below.

# Battle Strategy & Type Effectiveness (Verified)
- Super Effective: Ground -> Electric, Fire, Poison, Rock, Steel; Rock -> Bug, Fire, Flying, Ice; Flying -> Bug, Fighting, Grass; Fire -> Bug, Grass, Ice, Steel.
- Not Very Effective: Normal -> Rock, Steel; Rock -> Rock, Ground; Grass -> Fire.
- Immune: Ground -> Flying.
- Strategy: Use battle_strategist for trainer fights.

# PC Storage
## Box 1 (Current)
- Blarney (SUDOWOODO) Lv20
- ROCKY (ONIX) Lv6
- ICARUS (PIDGEY) Lv11

# Pokemon Locations
- Route 29: Pidgey, Rattata, Sentret.
- Route 30: Pidgey, Rattata, Caterpie, Metapod, Hoothoot (Night).
- Route 31: Pidgey, Rattata, Caterpie, Metapod, Bellsprout, Hoothoot (Night).
- Sprout Tower: Rattata, Gastly (Night).
- Route 32: Rattata, Ekans, Zubat, Bellsprout, Mareep, Wooper.
- Union Cave: Rattata, Sandshrew, Zubat, Geodude, Onix.
- Route 33: Rattata, Spearow, Ekans, Hopip.
- Slowpoke Well: Zubat, Slowpoke.
- Ilex Forest: Caterpie, Metapod, Weedle, Kakuna, Paras, Oddish, Venonat, Psyduck.
- Route 34: Rattata, Spearow, Jigglypuff, Abra, Ditto.
- Route 35: Pidgey, Nidoran M/F, Jigglypuff, Abra, Yanma (Swarm), Ditto.
- National Park: Pidgey, Caterpie, Metapod, Weedle, Kakuna, Sunkern.
- Route 36: Pidgey, Growlithe, Hoothoot, Ledyba, Spinarak.

# Strategy & Notes
- Sudowoodo: Caught (Turn #4593).
- Badges: Zephyr (Violet), Hive (Azalea), Plain (Goldenrod).
- Key Items: Squirtbottle (used on Sudowoodo), Coin Case (Goldenrod Underground), Old Rod.
- HMs: HM01 Cut (learned by KIMCHI), HM05 Flash.
- TMs: TM28 Dig (National Park), TM08 Rock Smash (Route 36), TM12 Sweet Scent, TM45 Attract, TM49 Fury Cutter, TM50 Nightmare.
- Route 35 Crossing: (West) <-> (6, 19) <-> (Middle) <-> (12, 17) <-> (East).
- Shortcut: Use Cut on the tree at (17, 6) to reach Route 36 directly.
- Arnie (Bug Catcher): Swarm notification for Yanma on Route 35.
- Violet City Navigation: To reach the north/west exit from the south, move to (27, 23) to bypass the ledges at y=23. Note: The pathfinding tool might attempt to walk up ledges, which is impossible.

# Exploration Progress
## Route 31
- Delivered KENYA to Fisher at (17, 7). (Turn #4645)
- Collected POKé BALL at (19, 15). (Turn #4648)
- Collected BITTER BERRY from tree at (16, 7). (Turn #4661)

# Item/TM Locations
- Route 36: TM08 (Rock Smash) from Fisher at (44, 9). (Turn #4607)
- Route 31: TM50 (Nightmare) from Fisher at (17, 7). (Turn #4645)
- Route 31: POKé BALL at (19, 15). (Turn #4648)

# Lessons Learned
- Menu Navigation: Do not mix directional and action buttons in a standard `press_buttons` call unless using `press_sequence`. Standard sequences will be truncated.
- Interaction Rule: You must be directly facing an NPC or object to interact. Stand adjacent and face the target tile. For counters, face the counter tile. (Lesson from Turn #4634)
- Pathfinding Rule: Paths in 2D top-down games are often wider than a single tile. Analyze adjacent tiles (up, down, left, right) to find ways around obstacles. (Lesson from Turn #4603)