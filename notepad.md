# Tile Mechanics
- FLOOR: Standard ground.
- WALL: Impassable.
- TALL_GRASS: Reachable encounters.
- LEDGE_HOP_DOWN: One-way south. Impassable from south/east/west.
- FLOOR_UP_WALL: Impassable. Confirmed at (6, 87) on Route 45 and (34, 34) in Dark Cave.

# Strategy: Final Badge
- Goal: Acquire Rising Badge from Gym Leader Clair.
- Current Task: Explore Route 46 and Dark Cave. Train Xenon/Kimchi to Lv30+.
- Start Turn (Training): 30811
- Training Method: Switch-training. Lead with trainee, switch to Calcifer (Lv48) or Gneiss (Lv45).
- Efficiency: Use `battle_analyst_v2` to optimize moves and switches.

# Verified Bag Order (Items)
1. ICE BERRY, 2. ICE HEAL, 3. GRN APRICORN, 4. PNK APRICORN, 5. YLW APRICORN, 6. FULL HEAL, 7. HYPER POTION, 8. REVIVE, 9. NUGGET, 10. AMULET COIN, 11. CANCEL

# Progress Tracker
- Xenon (Lv26): 14157 / 21760 EXP (Target: Lv30)
- Kimchi (Lv21): 7006 / 21760 EXP (Target: Lv30)

# Tasks
- Explore Route 46 and Dark Cave (Current).
- Investigate Dark Cave entrance at (14, 5) on Route 46.
- Grab Poke Ball at (30, 28) in Dark Cave.
- Sell NUGGET (¥5000) at next Mart.

# Lessons Learned
- **Tile Verification:** Never assume a tile type (like FLOOR_UP_WALL) is traversable based on its name. Always test collision immediately.
- **Ledge Awareness:** On maps with many ledges (Route 45, Route 46), use `find_path_v2` with updated ledge logic to avoid getting stuck in pockets.
- **Training Efficiency:** Use `battle_analyst_v2` during wild encounters to minimize damage and maximize EXP gain for trainees.
- Pick up item from Alan on Route 36.