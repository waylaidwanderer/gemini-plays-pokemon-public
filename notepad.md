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

# Tile Mechanics (CianwoodPokecenter1F)
- FLOOR: Traversable.
- WALL: Impassable.
- COUNTER: Impassable. Interaction point for Nurse.
- PC: Impassable. Interaction point for PC.
- LADDER: Warp.
- WARP_CARPET_DOWN: Warp.

# Strategy: Rising Badge (Gym Leader Clair)
- Level Target: Xenon and Kimchi to Lv40.
- Tactical Plan: Lead with Xenon (Ghost; immune to Selfdestruct). Night Shade for fixed damage. Gneiss/Calcifer as finishers.
- Preparation: Stock up on Full Heals. Prepare status/counters for Kingdra.
- Kingdra Tactics: Use Kimchi's Sleep Powder/Stun Spore. Train Xenon for Destiny Bond (Lv45) as a fallback.

# Strategy: Johto League Training
- Method: Exp. Share on Kimchi, lead with Xenon.
- Spot: Route 45 grass (4, 12).
- Resource Management: Fly to Blackthorn PC to heal.
- Hazards: Watch for Ground moves (Magnitude/Earthquake) on Route 45; they hit Xenon hard. Use Icarus/Gneiss for safety.

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

# Strategy: Cianwood Consolidation
- Step 1: Swap Xenon to lead (Complete).
- Step 2: Give Kimchi Exp. Share (Manual confirmation Turn #31962).
- Step 3: Fly to Blackthorn City.

# Progress Tracking
- Cianwood Consolidation: Started Turn #31883.
- Turn #31960: Xenon successfully swapped to lead.
- Turn #31961: Located Exp. Share on Icarus; switching it to Kimchi.

# Start Menu (8 options) - WRAPS
1. POKEDEX
2. POKEMON
3. PACK
4. POKEGEAR
5. GEM (Trainer Card)
6. SAVE
7. OPTION
8. EXIT

# Party Menu Mapping
- Slot 1 (ICARUS): FLY, STATS, SWITCH (Offset 2)
- Slot 2 (XENON): STATS, SWITCH (Offset 1)
- Slot 3 (KIMCHI): FLASH, CUT, STATS, SWITCH (Offset 3)
- Slot 4 (Ravioli): SURF, STATS, SWITCH (Offset 2)
- Slot 5 (GNEISS): STRENGTH, STATS, SWITCH (Offset 2)
- Slot 6 (Calcifer): STATS, SWITCH (Offset 1)

# Lessons Learned (Menu Management)
- Turn #31916: Menu lag in Crystal can be severe. Raw `press_buttons` sequences for deep menus are prone to desync. 
- Strategy: Use specialized tools (`swap_pokemon_v2`, `use_item_on_pokemon_v2`) from a clean overworld state whenever possible.
- Crystal's Start and Party menus WRAP. Up-resetting is unreliable without knowing the exact menu size.
- Tool fly_to_city_v4 and give_item_v3_ultimate are currently brittle due to wrapping. Redefinition required.