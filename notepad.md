# Tile Mechanics
- FLOOR: Traversable. Standard collision-free tile.
- WALL: Impassable. Provides collision from all directions.
- TALL_GRASS: Traversable. Triggers wild Pokemon encounters.
- LONG_GRASS: Traversable. Triggers wild Pokemon encounters.
- LEDGE_HOP_DOWN: One-way traversal. Can only be entered from the top to jump down. Impassable from other sides.
- LEDGE_HOP_LEFT: One-way traversal. Can only be entered from the right to jump left. Impassable from other sides.
- LEDGE_HOP_RIGHT: One-way traversal. Can only be entered from the left to jump right. Impassable from other sides.
- CAVE: Map transition warp. Stand on or walk into to trigger.
- FLOOR_UP_WALL: Traversable. Functions as standard FLOOR collision.
- WATER: Traversable with HM03 SURF.
- CUT_TREE: Impassable; removable with HM01 CUT.
- HEADBUTT_TREE: Impassable; interactive.
- BOULDER: Impassable; pushable with HM04 STRENGTH.
- COUNTER/PC: Stand adjacent/below to interact.
- BUOY: Impassable; water boundary.

# Strategy: Johto League Training
- Task: Train XENON (Haunter) and KIMCHI (Gloom) to Lv40.
- Started: Turn #32266, 2026-01-07 04:30 AM.
- Current Status: Xenon Lv30, Kimchi Lv29. Turn #32440.
- Method: Exp. Share on Kimchi. Lead with Xenon (Amulet Coin).
- Training Location: Route 45 (high level Rock/Ground/Flying).
- Hazards: Magnitude/Earthquake (use GNEISS as backup).

# Strategy: Rising Badge (Gym Leader Clair)
- Objective: Defeat Clair in Blackthorn Gym.
- Team Composition:
    - XENON (Haunter): Main attacker. Goal Lv40+. Use Night Shade for fixed damage against high-defense Dragons.
    - KIMCHI (Gloom): Support. Goal Lv40+. Use Sleep Powder for crowd control.
    - CALCIFER (Typhlosion): Heavy hitter backup.
    - GNEISS (Graveler): Tank backup.
- Detailed Plan:
    1. Grind Xenon and Kimchi to Lv40 on Route 45.
    2. Ensure Xenon has full PP for Night Shade.
    3. Use Hypnosis/Sleep Powder to manage threats.
    4. Night Shade bypasses the high special defense of Clair's Dragon-types.
- Preparation: Heal at Pokemon Center and restore PP before each major training session or gym attempt.

# Pending Rematches / Gifts
- Arnie (Bug Catcher): Route 35. Rematch #1 defeated. Rematch #2 available (Turn #32311).
- Alan (Schoolboy): Route 36. Rematch potential (Turn #32289: No battle).
- Chad (Schoolboy): Route 38. Rematch potential.

# Current Plan: Route 45 Training
1. Grinding in tall grass.
2. Battle wild Pokemon to level Xenon and Kimchi to Lv40.
3. Monitor HP/PP; Fly to Blackthorn to heal if needed.

# Lessons Learned
- Fly Map: It's a 2D snapping grid, not a list. Cursor starts on current city.
- Button Inputs: Never mix directional and action buttons in a single press_buttons sequence. Use press_menu_buttons for menu navigation.
- Interaction: Always ensure you are facing the target tile before pressing A.

# Reflection (Turn #32382)
1. Immediate Execution: No deferred tasks.
2. Notepad Hygiene: Reorganized and added Lessons Learned.
3. Map Hygiene: Training spot marked.
4. Automation Strategy: find_path_v2 refined for ledges.
5. Goal Clarity: Goals are outcome-focused.
6. Error Analysis: Fly menu and button mixing mistakes addressed. Hypothesis updated.