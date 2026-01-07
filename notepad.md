# Verified Tile Mechanics
- FLOOR: Standard ground. Can be traversed.
- WALL: Impassable. Interaction with objects on wall tiles (like signs) must be done from an adjacent tile.
- TALL_GRASS: Can be traversed. Triggers wild encounters.
- LEDGE_HOP_DOWN: One-way south.
- FLOOR_UP_WALL: Impassable ledge bottom.

# Hypothesized Tile Mechanics
- LEDGE_HOP_LEFT: One-way west.
- LEDGE_HOP_RIGHT: One-way east.
- WATER: Requires SURF to cross.
- WHIRLPOOL: Requires WHIRLPOOL to clear.

# Strategy: Johto League Training
- Efficiency: Lead with trainee (Kimchi Lv24), switch to Calcifer (Lv48) or Gneiss (Lv46) if outmatched. Xenon (Lv28) is backup.
- Target: Get Xenon and Kimchi to Lv30+ before challenging Clair.
- Pacing: Walk back and forth in TALL_GRASS on Route 45. Use Acid for STAB damage.
- Resource Limit: Return to Blackthorn City to heal when Gneiss is at 0 Earthquake PP.

# Progress Tracker
- Xenon (Lv28): 17426 EXP. Target Lv30: ~21760 EXP (~4334 remaining).
- Kimchi (Lv24): 10645 EXP. Target Lv30: ~21760 EXP (~11115 remaining).
- Gneiss (Lv46): 111/129 HP. Earthquake PP: 9/10.
- Calcifer (Lv48): 152/152 HP. Flame Wheel PP: 24/25.
- Grinding Start: Turn #31060.
- Encounter Log: Donphan (Lv25), Graveler (Lv23), Gligar (Lv24) observed at (4,12)-(5,12). Gligar is immune to Electric.

# Evolution Methods (Hypotheses)
- Gloom: Likely evolves with an evolution stone (Leaf or Sun Stone).
- Haunter: Traditionally evolves via trading (needs verification in this version).

# Lessons Learned
- Route 45 Navigation: Paths are primarily one-way SOUTH due to ledges. To return to Blackthorn, use FLY.
- Strength Mechanic: Strength must be used on each individual boulder; it is not a persistent status.
- Tool Hygiene: use_item_from_bag_v2 requires the bag to be open. Always use press_menu_buttons to navigate to the Pack first.
- Fly Map Logic: Destination names MUST be verified in Screen Text after every button press.
- Input Precision: Rushing menus leads to errors. Verify every screen change before the next input. Always use select_battle_option for main menu navigation.
- Custom Tools (5/5): find_path_v2, press_menu_buttons, switch_to_pokemon_v2, use_item_from_bag_v2, grind_encounters.