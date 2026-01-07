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
    1. Grind Xenon and Kimchi to Lv40 on Route 45.
    2. Ensure Xenon has full PP for Night Shade.
    3. Use Hypnosis/Sleep Powder to manage threats.
    4. Night Shade bypasses high special defense of Clair's Dragon-types.
    5. **CRITICAL:** Use `battle_advisor` agent for all trainer and significant wild battles to optimize EXP and safety.

# Training Progress (Route 45)
- Goal: Lv40 for Xenon and Kimchi.
- Strategy: Lead with Xenon (Amulet Coin). Exp. Share on Kimchi. Night Shade PP management: Fly to Blackthorn to heal.

# Fly Map Navigation (Experimental)
- Sequence found via Up/Right presses: Azalea -> Ecruteak -> Olivine -> Cianwood -> Mahogany.
- Mahogany -> Up -> Lake of Rage.
- Goal: Blackthorn City (Northeast of Mahogany).
- Strategy: Try Up/Right combinations from Mahogany/Lake of Rage.

# Pending Rematches / Gifts
- Arnie (Bug Catcher): Route 35. Rematch potential.
- Alan (Schoolboy): Route 36. Rematch potential.
- Chad (Schoolboy): Route 38. Rematch potential.

# Lessons Learned
- Haunter Mechanics: Grounded in Gen 2; weak to Magnitude.
- Battle Strategy: Switch to GNEISS if Ground moves expected. Use battle_advisor for optimal moves.
- Fly Map: Cursor snaps to locations. Movement is not strictly 1:1. Check text after every press.
- Menu Navigation: Use press_menu_buttons to avoid mixing inputs.