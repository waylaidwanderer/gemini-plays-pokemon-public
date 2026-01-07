# Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- TALL_GRASS: Traversable. Triggers wild encounters.
- LEDGE_HOP: One-way traversal (South/West/East).
- CAVE: Warp to indoor areas.
- WATER: Traversable with HM03 SURF.
- CUT_TREE: Removed with HM01 CUT.
- BOULDER: Pushed with HM04 STRENGTH.
- COUNTER: Interaction point for NPCs behind desks.
- WARP_CARPET: Map transition tile at exits.
- PC: Interaction point for Pokémon storage. Stand below and face up.
- WARP: Tile that triggers map transition.

# Strategy: Rising Badge (Gym Leader Clair)
- Level Target: Xenon and Kimchi to Lv40.
- Tactical Plan: Lead with Xenon (Ghost; immune to Selfdestruct). Night Shade for fixed damage. Gneiss/Calcifer as finishers.
- Preparation: Stock up on Full Heals. Prepare status/counters for Kingdra.

# Strategy: Johto League Training
- Method: Exp. Share on Kimchi, lead with Xenon.
- Spot: Route 45 grass (4, 12).
- Resource Management: Fly to Blackthorn PC to heal.

# Ground-Type Safety Protocol
- Problem: Xenon is weak to Ground (Magnitude/Earthquake).
- Solution: NEVER switch Xenon into suspected Ground-type users. Use Icarus/Gneiss instead.

# Progress Tracker
- Kimchi (Gloom): Lv28 (17615 EXP).
- Xenon (Haunter): Lv29 (20309 EXP).

# Key Locations & Completed Tasks
- Mr. Pokemon: Route 30 (17, 5). Trade completed. Exp. Share obtained.
- Dana (Lass): Route 38. Has a gift.
- Chad (Schoolboy): Route 38. Wants to battle.
- Dark Cave Entrance: Route 45 (2, 5).

# Turn Synchronization
- Turn #31895. Executing manual Fly to Blackthorn City from Option menu state.
- Cursor: OPTION (Start Menu).
- Goal: Reach Blackthorn City and heal.
- Training Plan: Xenon/Kimchi to Lv40.

# Failed Hypotheses Log (Training Prep)
1. Give Exp. Share via menu (Turn #31883): Failed, took Amulet Coin.
2. Swap Xenon to lead (Turn #31886): Failed, entered Save menu.
3. Give Exp. Share via tool (Turn #31890): Failed, menu lag.
4. press_menu_buttons sequence (Turn #31892): Failed, entered Option menu.
5. fly_to_city_v4 tool call (Turn #31891): Failed, JSON error.
- Total Failures: 5.

# Decisive Action Phase
- I am manually navigating the fly menu using press_menu_buttons. I've also refined the fly_to_city_v4 tool to be more robust for future use. No more multi-step sequences until we are out of this laggy area!