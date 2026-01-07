# Key Locations & Mechanics
- New Bark Town (Mom's House 24_6): Talking to Mom at (2, 2) allows changing Daylight Saving Time and managing money.
- New Bark Town (Elm's Lab 24_5): Healing Machine at (2, 2) heals the entire party. Verified Turn 32811.
- Blackthorn City (Pokemon Center 25_3): Standard healing. Warp at (21, 30).
- Route 45: High-level training area. Lead with Xenon (Amulet Coin), Exp. Share on Kimchi.

# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- TALL_GRASS: Traversable. Triggers wild encounters.
- LEDGE_HOP_DOWN: One-way traversal (Down).
- LEDGE_HOP_LEFT: One-way traversal (Left).
- LEDGE_HOP_RIGHT: One-way traversal (Right).
- CAVE: Map transition warp.
- SIGN: Background object.

# Fly Navigation (Johto Cycle)
- Sequence (using Up): New Bark -> Cherrygrove -> Violet -> Azalea -> Goldenrod -> Ecruteak -> Olivine -> Cianwood -> Mahogany -> Lake of Rage -> Blackthorn.
- Strategy: Use fly_navigator_v2. Verify town name on screen.

# Training Progress (Route 45)
- Session Start: Turn 32625.
- Status (Turn 32966): Xenon (Lv32, 82/82 HP, Night Shade 15 PP), Kimchi (Lv31, 82/82 HP).
- Goal: Lv40 for both.

# Strategy: Rising Badge (Gym Leader Clair)
- Team: Xenon (Haunter), Kimchi (Gloom), Calcifer (Typhlosion), Gneiss (Graveler).
- Plan: Use Night Shade (Xenon) for fixed damage. Use Sleep Powder/Hypnosis for control.
- Training Start: Turn 32625 (Wed Jan 7 9:15 AM).

# World Events & Rematches
- Yanma Swarm: Route 35 (Arnie).
- Arnie (Bug Catcher): Route 35.
- Alan (Schoolboy): Route 36.
- Chad (Schoolboy): Route 38.

# Lessons Learned
- Menu Navigation: Limit manual sequences to 1-3 buttons. Verify screen state after each call.
- Fly Map: In Crystal, the Up button cycles through visited towns.
- Battle Mechanics: HP bar animations can occur while move text is displayed, which may look like multi-hit moves. Always verify actual move properties.
- Input Restrictions: Do NOT mix directional (Up, Down, Left, Right) and action (A, B, Start, Select) buttons in a single manual `press_buttons` call. Use specialized tools like `press_menu_buttons` or `find_path_v2` instead. Verified Turn 32936.