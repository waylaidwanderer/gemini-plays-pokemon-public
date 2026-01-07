# Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- TALL_GRASS: Traversable. Wild encounter trigger.
- LEDGE_HOP: One-way traversal.
- CAVE/WARP: Map transitions.
- WATER: Traversable (Surf).
- CUT_TREE: Obstacle (Cut).
- BOULDER: Obstacle (Strength).
- COUNTER: STAND ADJACENT to interact with NPC behind.
- PC: Stand below and face up to interact.

# Tile Mechanics: Route 45
- LEDGE_HOP_DOWN (⤵️): One-way movement (Top -> Bottom).
- LEDGE_HOP_LEFT (↩️): One-way movement (Right -> Left).
- LEDGE_HOP_RIGHT (↪️): One-way movement (Left -> Right).

# Strategy: Johto League Training
- Task: Train XENON (Haunter) and KIMCHI (Gloom) to Lv40.
- Method: Exp. Share on Kimchi. Lead with Xenon (Amulet Coin).
- Training Locations: Route 45 (high level Rock/Ground/Flying), Rematch Trainers (Dana, Arnie, Alan, Chad).
- Hazards: Magnitude/Earthquake. Use GNEISS (Graveler) as backup.

# Strategy: Rising Badge (Gym Leader Clair)
- Lead: Xenon (Lv40+). Use Night Shade for fixed damage.
- Support: Kimchi (Lv40+). Use Sleep Powder for CC.
- Backup: Calcifer (Typhlosion) and Gneiss.

# Significant Party Status
- XENON (Haunter): Lv30. HP 77/77. Night Shade: 11/15.
- ICARUS (Pidgey): Lv16. HP 43/43. Fly user.
- KIMCHI (Gloom): Lv29. HP 77/77. Holding EXP.SHARE.
- Ravioli (Krabby): Lv10. HP 27/27. Surf user.
- GNEISS (Graveler): Lv46. HP 129/129.
- Calcifer (Typhlosion): Lv48. HP 152/152.

# Pending Rematches / Gifts
- Arnie (Bug Catcher): Route 35. Rematch started (Turn #32266).
- Alan (Schoolboy): Route 36. Rematch potential.
- Chad (Schoolboy): Route 38. Rematch potential.

# Fly Destinations (List Order)
- New Bark Town, Cherrygrove City, Violet City, Azalea Town, Goldenrod City, Ecruteak City, Olivine City, Cianwood City, Mahogany Town, Blackthorn City.

# Party Menu Mapping
- Slot 1 (XENON): STATS, SWITCH, MOVE, ITEM, CANCEL
- Slot 2 (ICARUS): FLY, STATS, SWITCH, MOVE, ITEM, CANCEL
- Slot 3 (KIMCHI): FLASH, CUT, STATS, SWITCH, MOVE, ITEM, CANCEL
- Slot 4 (Ravioli): SURF, STATS, SWITCH, MOVE, ITEM, CANCEL
- Slot 5 (GNEISS): STRENGTH, STATS, SWITCH, MOVE, ITEM, CANCEL
- Slot 6 (Calcifer): STATS, SWITCH, MOVE, ITEM, CANCEL

# Reflection (Turn #32278)
1. Immediate Execution: I previously deferred Cut, but I've executed it now. No other deferred tasks.
2. Notepad Hygiene: Added reflection and updated trainer status. Tile mechanics are current.
3. Map Hygiene: Marked the Cut tree and Arnie's defeat. No redundant markers found.
4. Automation Strategy: Current tools (find_path_v2, press_menu_buttons) are working well. No new ones needed yet.
5. Goal Clarity: Goals are outcome-focused. Method is in the notepad.
6. Error Analysis: I initially mixed directional and action buttons, which failed. Lesson: Always use press_menu_buttons or individual presses for interaction sequences. Root hypothesis for Arnie was correct, and exploration is proceeding.