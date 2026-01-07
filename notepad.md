# Tile Mechanics
- FLOOR: Traversable. Standard collision-free tile.
- WALL: Impassable.
- TALL_GRASS: Traversable. Triggers wild Pokemon encounters.
- LONG_GRASS: Traversable. Triggers wild Pokemon encounters.
- LEDGE_HOP_DOWN: One-way traversal (Down only).
- LEDGE_HOP_LEFT: One-way traversal (Left only).
- LEDGE_HOP_RIGHT: One-way traversal (Right only).
- CAVE/DOOR/STAIRS: Map transition warp.
- FLOOR_UP_WALL: Traversable (functions as FLOOR).
- WATER: Traversable with HM03 SURF.
- CUT_TREE: Impassable; removable with HM01 CUT.
- HEADBUTT_TREE: Impassable; interactive.
- BOULDER: Impassable; pushable with HM04 STRENGTH.
- COUNTER/PC: Stand adjacent/below to interact.
- BUOY: Impassable; water boundary.

# Strategy: Johto League Training
- Task: Train XENON (Haunter) and KIMCHI (Gloom) to Lv40.
- Started: Turn #32266, 2026-01-07 04:30 AM.
- Method: Exp. Share on Kimchi. Lead with Xenon (Amulet Coin).
- Training Location: Route 45 (high level Rock/Ground/Flying).

# Strategy: Rising Badge (Gym Leader Clair)
- Objective: Defeat Clair in Blackthorn Gym.
- Team Composition:
    - XENON (Haunter): Main attacker. Goal Lv40+. Use Night Shade for fixed damage.
    - KIMCHI (Gloom): Support. Goal Lv40+. Use Sleep Powder.
    - CALCIFER (Typhlosion): Heavy hitter backup.
    - GNEISS (Graveler): Tank backup.
- Detailed Plan:
    1. Grind Xenon and Kimchi to Lv40 on Route 45.
    2. Ensure Xenon has full PP for Night Shade.
    3. Use Hypnosis/Sleep Powder to manage threats.
    4. Night Shade bypasses the high special defense of Clair's Dragon-types.
- Preparation: Heal at Pokemon Center and restore PP before each major training session or gym attempt.

# Pending Rematches / Gifts
- Arnie (Bug Catcher): Route 35. Rematch potential (Turn #32311).
- Alan (Schoolboy): Route 36. Rematch potential.
- Chad (Schoolboy): Route 38. Rematch potential.

# Lessons Learned
- Fly Map: It's a 2D snapping grid. Cursor starts on current city.
- Button Inputs: Never mix directional and action buttons in a single press_buttons sequence.
- Battle (Route 45): Wild Ground types (Graveler, Donphan) use Magnitude. Haunter is extremely vulnerable. Switch to GNEISS if Magnitude is expected.
- Critical Hits: A crit Magnitude 6 can OHKO Haunter even at a level advantage.
- Haunter Utility: Confuse Ray (Lv31) is a strong addition for disruption.

# Tile Mechanics: Route 45
- TALL_GRASS: Traversable. Triggers wild encounters. Verified at (12, 10), (13, 10).
- LEDGE_HOP_DOWN: One-way traversal (Down). Verified at (13, 9), (12, 13).
- WALL: Impassable. Verified at (13, 12).
- FLOOR: Traversable. Verified at (12, 6).

# Training Session Log
- Turn #32530: Started grinding Xenon and Kimchi on Route 45.
- Status: Xenon reached Lv31. Night Shade PP is low (3/15).
- Post-Battle Plan: Head to Blackthorn City Pokemon Center to heal and restore PP.