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

# Progress Tracking
- Cianwood Consolidation: Started Turn #31883.
- Failures Log: 16 failed attempts at party management (Turns 31883-31919). Cause: Menu lag, wrapping, and field move sub-menu offsets in Crystal.
- Turn #31927: Party swap successful! Xenon is now in the lead.
- Turn #31931: Using give_item_v2 to give Exp. Share (slot 3) to Kimchi (slot 3).

# Strategy: Cianwood Consolidation
- Step 1: Swap Xenon to lead (Complete).
- Step 2: Give Kimchi Exp. Share (Current).
- Step 3: Fly to Blackthorn City.

# Menu Mapping (Cianwood PC)
- Slot 1 (Kimchi): FLASH, CUT, STATS, SWITCH (3 downs)
- Slot 2 (Icarus): FLY, STATS, SWITCH (2 downs)
- Slot 3 (Xenon): STATS, SWITCH (1 down)
- Slot 4 (Ravioli): SURF, STATS, SWITCH (2 downs)
- Slot 5 (GNEISS): STRENGTH, STATS, SWITCH (2 downs)
- Slot 6 (Calcifer): STATS, SWITCH (1 down)

# Lessons Learned (Menu Management)
- Turn #31916: Menu lag in Crystal can be severe. Raw `press_buttons` sequences for deep menus are prone to desync. 
- Strategy: Use specialized tools (`swap_pokemon_v2`, `use_item_on_pokemon_v2`) from a clean overworld state whenever possible.
- If tools fail, use `press_menu_buttons` with at least 1000ms `sleep` after any menu-opening action.