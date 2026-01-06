# Tile Mechanics
- FLOOR: Standard ground.
- WALL: Impassable.
- TALL_GRASS: Reachable encounters.
- LEDGE_HOP_DOWN: One-way south. Impassable from south/east/west.
- FLOOR_UP_WALL: Impassable ledge bottom.

## Strategy: Johto League
- Training: Grind Xenon (Lv26) and Kimchi (Lv21) to Lv30+.
- Method: Switch-training. Lead with trainee, switch to Calcifer (Lv48) or Gneiss (Lv45). Use battle_analyst_v2 in all battles.

# Progress Tracker
- Xenon (Lv26): 14172 / 21760 EXP (Target: Lv30)
- Kimchi (Lv21): 7006 / 21760 EXP (Target: Lv30)
- Start Turn (Training): 30811

# Tasks
- Pick up item from Alan on Route 36.
- Grab Poke Ball at (30, 28) in Dark Cave.
- Sell NUGGET (¥5000) at next Mart.

# Lessons Learned
- Tile Verification: FLOOR_UP_WALL is a wall/ledge bottom. (5, 2) on Route 46 is a dead end.
- Ledge Awareness: Route 45/46 require careful pathfinding due to one-way ledges.
- Warp Safety: find_path_v2 avoid_warps=True prevents accidental transitions.
- Strength Mechanic: Strength must be used on each individual boulder; it is not a persistent status.