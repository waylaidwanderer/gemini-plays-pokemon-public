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
- Method: Exp. Share on Kimchi, lead with Xenon.
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

# Progress Tracker
- Kimchi (Gloom): Lv28. Holding EXP.SHARE.
- Xenon (Haunter): Lv29.
- GNEISS (Graveler): Lv46.
- Item: HARD STONE is in Bag (Not held by Gneiss).

# Party Item Audit
- Xenon: Checking...
- Icarus: Has item icon.
- Kimchi: Exp. Share.
- Ravioli: Was holding Bitter Berry.
- Gneiss: Was holding Amulet Coin.
- Calcifer: Has item icon.

# Party Menu Mapping
- Slot 1 (XENON): STATS, SWITCH (Offset 1)
- Slot 2 (ICARUS): FLY, STATS, SWITCH (Offset 2)
- Slot 3 (KIMCHI): FLASH, CUT, STATS, SWITCH, MOVE, ITEM, CANCEL
- Slot 4 (Ravioli): SURF, STATS, SWITCH (Offset 2)
- Slot 5 (GNEISS): STRENGTH, STATS, SWITCH (Offset 2)
- Slot 6 (Calcifer): STATS, SWITCH (Offset 1)

# Meta
- Training Task Start: Turn #31883.
- Menu Navigator Agent: Defined Turn #32011.
- Pathfinding Tool (find_path_v2): Defined/Updated Turn #32021.