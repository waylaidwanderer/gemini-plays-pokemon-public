# Tile Mechanics
- FLOOR: Standard traversable ground.
- WALL: Impassable structural obstacle.
- MART_SHELF: Impassable shop display in Poké Marts.
- FLOOR_UP_WALL: Impassable vertical ledge face (cannot be jumped up).
- LEDGE_HOP_DOWN: One-way jumpable ledge (jump down to bypass obstacles).
- LEDGE_HOP_LEFT: One-way jumpable ledge (jump left to bypass obstacles).
- PIT: Impassable; warps the player to the floor below.
- LADDER: Warp between different floors of a building or cave.
- BOULDER: Movable object requiring Strength (HM04) to push.
- LAVA: Impassable hazard with WALL collision.
- WATER: Traversable surface requiring Surf (HM03) to cross.
- CAVE: Warp entrance leading to an interior map.
- TALL_GRASS: Reachable area where wild Pokémon encounters are triggered.

# Strategy: Final Badge
- Primary Goal: Acquire the Rising Badge from Gym Leader Clair in Blackthorn City.
- Training Plan: Grind Xenon (Haunter) and Kimchi (Gloom) to Lv30+ on Route 45.
- Method: Switch-training. Lead with trainee, then switch to Calcifer (Lv48) or Gneiss (Lv45).
- CRITICAL: In trainer battles, switch trainee back in for EVERY new Pokémon sent out to maximize EXP sharing.
- Logistics: Battle all trainers on Route 45 to earn money for supplies. Sell NUGGET (¥5000) at next opportunity.

# Kingdra Analysis (Gym Leader Clair)
- Type: Water/Dragon.
- Defensive Matchups: Neutral to Electric, Grass, Ground, Rock, Normal. Resists Fire/Water (1/4x), Ice (1/2x). Weak to Dragon.
- Observed Moves: Smokescreen, Dragonbreath, Surf.

# Training Progress Tracker
- Xenon (Lv26): 14157 / 21760 EXP (Target: Lv30)
- Kimchi (Lv21): 7006 / 21760 EXP (Target: Lv30)
- Milestones: Xenon reached Lv25 (Turn 30625), Lv26 (Turn 30724).

# Exploration Progress
- Ledge Verification: Confirmed one-way Down at (4, 41), (2, 55), (2, 63), (4, 77).
- Route 45 Vertical Lanes: Navigation is limited to southward movement within vertical "lanes" separated by ledges.
- Turn 30779: Healing Calcifer (76/152 HP) with Hyper Potion. Xenon and Gneiss are healthy. Next: Fix Xenon's held item, then continue south on Route 45.
- Task: Verify if trainer at (10, 16) is defeated. Requires flying back to Blackthorn and re-entering Route 45 lanes.
- Turn 30774: [2026-01-06 12:53 PM] Performed 50-turn reflection. Defined find_path_v2 and get_type_effectiveness tools. Navigating to PACK to heal Calcifer and fix Xenon's held item.