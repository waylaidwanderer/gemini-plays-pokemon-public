# Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- TALL_GRASS: Traversable. Wild encounter trigger.
- LEDGE_HOP: One-way traversal (South/West/East).
- CAVE: Warp to cave/indoor areas.
- WATER: Traversable (Surf).
- CUT_TREE: Obstacle (Cut).
- BOULDER: Obstacle (Strength).
- COUNTER: Interaction point. Stand adjacent.
- WARP_CARPET: Map transition at exits.
- PC: Pokémon/Item storage. Face up from below.
- WARP: Tile triggering map transition.
- BUOY: Impassable water boundary.
- LADDER: Warp tile for floor transitions.

# Menu Mechanics (Crystal)
- Start Menu (8 options): POKEDEX, POKEMON, PACK, GEAR, GEM, SAVE, OPTION, EXIT. WRAPS.
- Party Menu (6 slots): WRAPS.
- Bag Pockets: Items, Balls, Key Items, TM/HM.
- Menu Lag: Severe. Use 500ms-1000ms sleep.

# Fly Map Navigation
- New Bark -> Cherrygrove -> Violet -> Azalea -> Goldenrod -> Ecruteak -> Olivine -> Cianwood -> Mahogany -> Blackthorn.

# Strategy: Johto League Training
- Method: Exp. Share on Kimchi, lead with Xenon (holding Amulet Coin).
- Spot: Route 45 grass (4, 12).
- Resource Management: Fly to Blackthorn PC to heal.
- Hazards: Watch for Ground moves on Route 45.

# Strategy: Rising Badge (Gym Leader Clair)
- Level Target: Xenon and Kimchi to Lv40.
- Tactical Plan: Lead with Xenon. Night Shade for fixed damage.
- Preparation: Stock up on Full Heals.
- Kingdra Tactics: Sleep Powder/Stun Spore. Destiny Bond (Lv45) as fallback.

# Ground-Type Safety Protocol
- Problem: Xenon is weak to Ground.
- Solution: NEVER switch Xenon into suspected Ground-type users.

# Party Item Audit (Turn #32072)
- Audit: COMPLETE. XENON cleared of ICE HEAL.
- Goal: Give AMULET COIN to XENON (Slot 1).
- Status: XENON leading, HP 64/74. KIMCHI holding EXP.SHARE. (Turn #32075)

# Progress Tracker
- Xenon (Haunter): Lv29 (20635 EXP).
- Kimchi (Gloom): Lv28 (17941 EXP).
- Gneiss (Graveler): Lv46 (93886 EXP).
- Calcifer (Typhlosion): Lv48 (109364 EXP).

# Party Menu Mapping
- Slot 1 (XENON): STATS, SWITCH, MOVE, ITEM, CANCEL
- Slot 2 (ICARUS): FLY, STATS, SWITCH, MOVE, ITEM, CANCEL
- Slot 3 (KIMCHI): FLASH, CUT, STATS, SWITCH, MOVE, ITEM, CANCEL
- Slot 4 (Ravioli): SURF, STATS, SWITCH, MOVE, ITEM, CANCEL
- Slot 5 (GNEISS): STRENGTH, STATS, SWITCH, MOVE, ITEM, CANCEL
- Slot 6 (Calcifer): STATS, SWITCH, MOVE, ITEM, CANCEL

# Meta
- Training Task Start: Turn #31883.
- Menu Navigator Agent: Defined Turn #32011.
- Pathfinding Tool (find_path_v2): Defined/Updated Turn #32021.