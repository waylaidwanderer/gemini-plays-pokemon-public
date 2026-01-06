# Tile Mechanics
- FLOOR: Standard ground.
- WALL: Impassable.
- TALL_GRASS: Reachable encounters.
- LEDGE_HOP_DOWN: One-way south. Impassable from south/east.
- LEDGE_HOP_LEFT: One-way west. Impassable from west.
- LEDGE_HOP_RIGHT: One-way east. Impassable from east.
- FLOOR_UP_WALL: Impassable ledge bottom.
- WATER: Requires SURF to cross.
- WHIRLPOOL: Requires WHIRLPOOL to clear.

# Strategy: Johto League Training
- Efficiency: Lead with trainee (Xenon/Kimchi), switch to Calcifer (Lv48) or Gneiss (Lv45) if outmatched.
- Target: Get Xenon and Kimchi to Lv30+ before challenging Clair.
- Pacing: Walk back and forth in TALL_GRASS on Route 45.

# Progress Tracker
- Xenon (Lv27): 16986 EXP. Target Lv28: 17242 EXP (~256 remaining).
- Kimchi (Lv21): 7006 EXP. Target Lv22: 7577 EXP (~571 remaining).
- Grinding Start: Turn #31060 (Tuesday, Jan 6, 2026).

# Lessons Learned
- Route 45 Navigation: Paths are primarily one-way SOUTH due to ledges. To return to Blackthorn, use FLY.
- Strength Mechanic: Strength must be used on each individual boulder; it is not a persistent status.
- Tool Hygiene: use_item_from_bag_v2 requires the bag to be open. Always use press_menu_buttons to navigate to the Pack first.
- Fly Map Logic: Destination names MUST be verified in Screen Text after every button press.
- Input Precision: Rushing menus leads to errors. Verify every screen change before the next input. Always use select_battle_option for main menu navigation.