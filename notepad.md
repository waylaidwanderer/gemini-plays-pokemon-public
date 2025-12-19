# Tile Mechanics
- FLOOR: Traversable. No effects. (Verified: Turn #4526)
- LONG_GRASS: Traversable. Wild Pokémon encounters. (Verified: Turn #4526)
- TALL_GRASS: Traversable. Wild Pokémon encounters. (Verified: Turn #4526)
- WALL: Impassable. Includes fences, benches, trees, signs, and NPCs. (Verified: Turn #4526)
- WATER: Impassable. Requires Surf.
- HEADBUTT_TREE: Impassable. Shaken with Headbutt.
- CUT_TREE: Impassable. Cleared with Cut.
- DOOR/WARP_CARPET: Traversable. Map transition.
- LEDGE_HOP: One-way traversal.
- COUNTER: Impassable. Interaction point for NPCs behind it.
- PC: Impassable. Interacted from below.

# Battle Strategy & Type Effectiveness (Verified)
- Super Effective: Ground -> Electric, Fire, Poison, Rock, Steel; Rock -> Bug, Fire, Flying, Ice; Flying -> Bug, Fighting, Grass; Fire -> Bug, Grass, Ice, Steel.
- Not Very Effective: Normal -> Rock/Ground; Rock -> Rock/Ground; Grass -> Fire.
- Immune: Ground -> Flying.
- Policy: Use battle_strategist for trainer fights.

# Strategy & Notes
- Sudowoodo: Caught (Turn #4593).
- Zephyr Badge: Obtained from Falkner (Turn #1636).
- Hive Badge: Obtained from Bugsy (Turn #3354).
- Plain Badge: Obtained from Whitney (Turn #4330).
- TM28 (Dig): Found in National Park (1, 43) (Turn #4545).
- TM04 (Rollout): Found on Route 35 (Turn #3895).
- Coin Case: Found in Goldenrod Underground (Turn #4010).
- Route 35 Crossing: (West) <-> (6, 19) <-> (Middle) <-> (12, 17) <-> (East).
- Shortcut: Use Cut on the tree at (17, 6) to reach Route 36 directly.
- Pokefan William (National Park): Raichu (Lv14). Gneiss is immune to its Electric moves.
- Arnie (Bug Catcher): Swarm notification for Yanma (verified Turn #4592) on Route 35; wants a Snubbull (Turn #4540).

# General Lessons
- Menu Navigation: Do not mix directional and action buttons in a standard `press_buttons` call unless using `press_sequence`. Standard sequences will be truncated.
- Narrative Rule: In `thoughts`, state only the next single action and its purpose. Do not narrate future outcomes.

# Exploration Progress: Route 36
- Sudowoodo cleared at (35, 9).
- Path to the north (Ecruteak) and east (Violet City) is now open.

# Item/TM Locations
- Route 36: TM08 (Rock Smash) from Fisher at (44, 9). (Turn #4607)
- Route 31: TM50 (Nightmare) from Fisher at (17, 7) for KENYA delivery. (Turn #4645)
- Route 31: POKé BALL at (19, 15). (Turn #4648)