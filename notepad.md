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
- Current Status: Xenon Lv30, Kimchi Lv30. Turn #32510.
- Method: Exp. Share on Kimchi. Lead with Xenon (Amulet Coin).
- Training Location: Route 45 (high level Rock/Ground/Flying).

# Incident Log
- Turn #32469: XENON fainted to a critical hit Magnitude 6 from wild Graveler (Lv23).
- Turn #32496: Encountered wild Gligar (Lv24). Training spot (12, 10) marked on Route 45.
- Turn #32505: Defeated wild Gligar (Lv24). Arnie called.

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