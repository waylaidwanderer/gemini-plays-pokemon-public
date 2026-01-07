# Key Locations & Mechanics
- New Bark Town (Mom's House 24_6): Talking to Mom at (2, 2) allows changing Daylight Saving Time and managing money.
- New Bark Town (Elm's Lab 24_5): Healing Machine at (2, 2) heals the entire party. Verified Turn 32811.
- Blackthorn City (Pokemon Center 25_3): Standard healing. Warp at (21, 30).
- Route 45: High-level training area. Lead with Xenon (Amulet Coin), Exp. Share on Kimchi.

# Tile Mechanics
- FLOOR: Standard walkable surface. No special effects.
- WALL: Solid obstacle. Prevents movement into the tile from all directions.
- TALL_GRASS: Walkable. Has a chance to trigger wild Pokemon encounters when stepped on.
- LONG_GRASS: Walkable. Similar to TALL_GRASS, can trigger wild encounters.
- LEDGE_HOP_DOWN: One-way vertical jump. Can be traversed from top to bottom, but acts as a wall from all other directions.
- LEDGE_HOP_LEFT: One-way horizontal jump. Can be traversed from right to left, but acts as a wall from all other directions.
- LEDGE_HOP_RIGHT: One-way horizontal jump. Can be traversed from left to right, but acts as a wall from all other directions.
- FLOOR_UP_WALL: Acts as a wall when moving from below. Verified Turn 32958.
- CAVE: Warp tile. Stepping on it transitions the player to a different map (e.g., inside a cave).
- SIGN: Background object. Can be interacted with from an adjacent tile to read text.

# Fly Navigation (Johto Cycle)
- Sequence (using Up): New Bark -> Cherrygrove -> Violet -> Azalea -> Goldenrod -> Ecruteak -> Olivine -> Cianwood -> Mahogany -> Lake of Rage -> Blackthorn.
- Strategy: Use fly_navigator_v2. Verify town name on screen.

# Training Progress (Route 45)
- Session Start: Turn 32625.
- Status (Turn 33010): Xenon (Lv32, 47/82 HP, Night Shade 4 PP), Kimchi (Lv32, 85/85 HP).
- Goal: Train Xenon and Kimchi to Lv40 for Gym Leader Clair.

# Strategy: Rising Badge (Gym Leader Clair)
- Team: Xenon (Haunter), Kimchi (Gloom), Calcifer (Typhlosion), Gneiss (Graveler).
- Plan: Use Night Shade (Xenon) for fixed damage. Use Sleep Powder/Hypnosis for control.
- Kingdra Strategy: Use Sleep Powder (Kimchi) and Night Shade (Xenon) to bypass defenses. Kingdra only weak to Dragon.
- Speed Control: Teach TM16 Icy Wind to Naga or Blitz to slow down Dragonairs. Check for TM location (Inventory/PC/Learned).
- Survival: Level supports to Lv40+ to survive hits from Clair's Lv37-40 team. Verified strategy Turn 32974.
- Party Management: Swap low-level members (Icarus, Ravioli) for stronger PC options (Naga Lv42, Blitz Lv40) before challenging.

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