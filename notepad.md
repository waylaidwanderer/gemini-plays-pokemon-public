# Tile Mechanics
- FLOOR: Traversable. Standard ground.
- WALL: Impassable.
- TALL/LONG GRASS: Traversable. Wild encounter trigger.
- LEDGE_HOP_DOWN/LEFT/RIGHT: One-way jump in indicated direction.
- CAVE/DOOR/STAIRS/LADDER: Map transitions.
- WATER: Traversable with HM03 SURF.
- CUT_TREE: Impassable; removable with HM01 CUT.
- HEADBUTT_TREE: Impassable; interactive.
- BOULDER: Impassable; pushable with HM04 STRENGTH.
- COUNTER/PC: Stand adjacent/below to interact.
- BUOY: Impassable; water boundary.

# Strategy: Johto League Training
- Started: Turn #32266.
- Goal: Train XENON (Haunter) and KIMCHI (Gloom) to Lv40.
- Method: Exp. Share on Kimchi. Lead with Xenon (Amulet Coin).
- Training Location: Route 45 (high level Rock/Ground/Flying).
- Hazards: Magnitude/Earthquake (use GNEISS as backup).

# Strategy: Rising Badge (Gym Leader Clair)
- Lead: Xenon (Lv40+). Night Shade for fixed damage.
- Support: Kimchi (Lv40+). Sleep Powder for CC.

# Significant Party Status
- XENON (Haunter): Lv30. HP 76/77. Night Shade: 7/15.
- ICARUS (Pidgey): Lv16. HP 43/43. Fly user.
- KIMCHI (Gloom): Lv29. HP 77/77. Holding EXP.SHARE.
- GNEISS (Graveler): Lv46. HP 129/129.
- Calcifer (Typhlosion): Lv48. HP 152/152.

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