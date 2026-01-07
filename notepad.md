# Tile Mechanics (Global)
- FLOOR: Traversable. Standard ground.
- WALL: Impassable. Structural boundary.
- TALL_GRASS: Traversable. Wild encounter trigger.
- LEDGE_HOP: One-way traversal (South/West/East).
- CAVE: Warp to cave/indoor areas.
- WATER: Traversable with HM03 SURF.
- CUT_TREE: Obstacle. Removed with HM01 CUT.
- BOULDER: Obstacle. Pushed with HM04 STRENGTH.
- COUNTER: Interaction point for NPCs behind desks. Stand adjacent.
- WARP_CARPET: Map transition at exits. Walk off-grid.
- PC: Pokémon/Item storage. Stand below and face up.
- WARP: Tile triggering map transition (stairs, doors).
- BUOY: Impassable water boundary.
- LADDER: Warp tile for floor transitions.

# Menu Mechanics (Crystal)
- Start Menu (8 options): POKEDEX, POKEMON, PACK, GEAR, GEM, SAVE, OPTION, EXIT. WRAPS.
- Party Menu (6 slots): WRAPS.
- Bag Pockets: Items, Balls, Key Items, TM/HM. Confirming if these wrap.
- Menu Lag: Severe. Use 500ms-1000ms sleep after transitions.
- Menu Logic: Cursor memory is persistent. Reset by closing menu or specific sequences.

# Fly Map Navigation
- Sequence: New Bark Town -> Cherrygrove City -> Violet City -> Azalea Town -> Goldenrod City -> Ecruteak City -> Olivine City -> Cianwood City -> Mahogany Town -> Blackthorn City.

# Strategy: Johto League Training
- Method: Exp. Share on Kimchi, lead with Xenon.
- Spot: Route 45 grass (4, 12).
- Resource Management: Fly to Blackthorn PC to heal.
- Hazards: Watch for Ground moves (Magnitude/Earthquake) on Route 45. Use Icarus/Gneiss for safety.

# Strategy: Rising Badge (Gym Leader Clair)
- Level Target: Xenon and Kimchi to Lv40.
- Tactical Plan: Lead with Xenon (Ghost; immune to Selfdestruct). Night Shade for fixed damage. Gneiss/Calcifer as finishers.
- Preparation: Stock up on Full Heals.
- Kingdra Tactics: Use Kimchi's Sleep Powder/Stun Spore. Train Xenon for Destiny Bond (Lv45) as a fallback.

# Ground-Type Safety Protocol
- Problem: Xenon is weak to Ground.
- Solution: NEVER switch Xenon into suspected Ground-type users.

# Progress Tracker
- Kimchi (Gloom): Lv28 (17615 EXP). Holding EXP.SHARE.
- Xenon (Haunter): Lv29 (20309 EXP).
- GNEISS (Graveler): Lv46. Holding HARD STONE. (Verified Turn #32020)
- Task: Train Xenon and Kimchi to Lv40 on Route 45. (Started Turn #31883)

# Party Menu Mapping
- Slot 1 (XENON): STATS, SWITCH (Offset 1)
- Slot 2 (ICARUS): FLY, STATS, SWITCH (Offset 2)
- Slot 3 (KIMCHI): FLASH, CUT, STATS, SWITCH, MOVE, ITEM, CANCEL
- Slot 4 (Ravioli): SURF, STATS, SWITCH (Offset 2)
- Slot 5 (GNEISS): STRENGTH, STATS, SWITCH (Offset 2)
- Slot 6 (Calcifer): STATS, SWITCH (Offset 1)
- Training Task Start: Turn #31883. Current Turn #32030.
- Menu Navigator Agent: Defined Turn #32011.
- Pathfinding Tool (find_path_v2): Defined/Updated Turn #32021.