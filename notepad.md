# Tile Mechanics: Route 45
- TALL_GRASS: Traversable. Triggers wild encounters. Verified at (12, 10), (13, 10).
- LEDGE_HOP_DOWN: One-way traversal (Down). Verified at (13, 9), (12, 13), (4, 41), (2, 55), (2, 63), (4, 77).
- WALL: Impassable. Verified at (13, 12).
- FLOOR: Traversable. Verified at (12, 6).
- CAVE: Map transition warp. Verified at (2, 5).
- SIGN: Background object. Verified at (10, 4).

# Strategy: Rising Badge (Gym Leader Clair)
- Objective: Defeat Clair in Blackthorn Gym.
- Team Composition:
    - XENON (Haunter): Main attacker. Goal Lv40+. Use Night Shade for fixed damage.
    - KIMCHI (Gloom): Support. Goal Lv40+. Use Sleep Powder.
    - CALCIFER (Typhlosion): Heavy hitter backup.
    - GNEISS (Graveler): Tank backup.
- Detailed Plan:
    1. Use Hypnosis/Sleep Powder to manage threats.
    2. Night Shade bypasses high special defense of Clair's Dragon-types.
    3. **CRITICAL:** Use `battle_advisor` agent for all trainer and significant wild battles to optimize EXP and safety.

# Training Progress (Route 45)
- Goal: Lv40 for Xenon and Kimchi.
- Strategy: Lead with Xenon (Amulet Coin). Exp. Share on Kimchi. 
- Healing Log: Turn #32731 (Start). Night Shade PP was 1. Status: Healing in progress.

# Unexplored Tiles (Route 45)
- Check (11, 20-36) area; likely behind ledges/walls.
- Check (17, 82-89) area; south end near Route 46.

# Pending Rematches / Gifts
- Arnie (Bug Catcher): Route 35.
- Alan (Schoolboy): Route 36.
- Chad (Schoolboy): Route 38.

# Lessons Learned
- Haunter Mechanics: Grounded in Gen 2; weak to Magnitude.
- Battle Strategy: Switch to GNEISS if Ground moves expected. Use battle_advisor for optimal moves.
- Fly Map: Cursor snaps to locations. Movement is not strictly 1:1. The "Right" button does not always move the cursor east; it cycles through the list of available Fly destinations. Verified sequence: Azalea -> Ecruteak -> Olivine -> Cianwood -> Mahogany -> Blackthorn.
- Menu Navigation: Use press_menu_buttons to avoid mixing inputs.
- Counter Interaction: To talk to NPCs behind counters (Nurses/Clerks), face the counter tile and press A. You do not need to be on the counter tile.