# Tile Mechanics
- FLOOR: Standard ground.
- WALL: Impassable.
- TALL_GRASS: Reachable encounters.
- LEDGE_HOP_DOWN: One-way south. Impassable from south/east/west.
- FLOOR_UP_WALL: Impassable ledge bottom.

## Strategy: Johto League
- Training: Grind Xenon (Lv26) and Kimchi (Lv21) to Lv30+.
- Efficiency: Lead with trainee, switch to Calcifer (Lv48) or Gneiss (Lv45). Use battle_analyst_v2 move/switch recommendations STRICTLY. Do not ignore agent output.
- Logistics: Sell NUGGET (¥5000) at next Mart.

# Progress Tracker
- Xenon (Lv26) -> Target: Lv30.
- Kimchi (Lv21) -> Target: Lv30.
- Start Turn (Training): 30811

# Tasks
- Pick up item from Alan on Route 36.
- Grab Poke Ball at (30, 28) in Dark Cave.
- Locate the Move Deleter (Blackthorn City) if needed.

# Lessons Learned
- Tile Verification: FLOOR_UP_WALL is a wall/ledge bottom. (5, 2) on Route 46 is a dead end.
- Ledge Awareness: Route 45/46 require careful pathfinding due to one-way ledges.
- Warp Safety: find_path_v2 avoid_warps=True prevents accidental transitions.
- Strength Mechanic: Strength must be used on each individual boulder; it is not a persistent status.
- Tool Hygiene: use_item_from_bag_v2 requires the bag to be open. Always use press_menu_buttons to navigate to the Pack first.