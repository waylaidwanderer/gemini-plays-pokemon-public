# Key Locations & Mechanics
- New Bark Town (Mom's House): Mom at (2, 2) manages money and Daylight Saving Time.
- New Bark Town (Elm's Lab): Healing Machine at (2, 2).
- Blackthorn City (Pokemon Center): Warp at (21, 30).
- Route 45: High-level training area.

# Tile Mechanics
- FLOOR: Standard walkable surface.
- WALL: Solid obstacle.
- TALL_GRASS: Walkable. Triggers wild encounters.
- LEDGE_HOP_DOWN: One-way vertical jump (Down).
- LEDGE_HOP_LEFT: One-way horizontal jump (Left).
- LEDGE_HOP_RIGHT: One-way horizontal jump (Right).
- CAVE: Warp tile.
- SIGN: Background object. Read text from adjacent tile.

# Fly Navigation (Johto Cycle)
- Sequence (using Up): New Bark -> Cherrygrove -> Violet -> Azalea -> Goldenrod -> Ecruteak -> Olivine -> Cianwood -> Mahogany -> Lake of Rage -> Blackthorn.
- Strategy: Use fly_navigator_v2. Verify town name on screen.

# Strategy: Rising Badge (Gym Leader Clair)
- Team: Xenon (Haunter), Kimchi (Gloom), Calcifer (Typhlosion), Gneiss (Graveler).
- Plan: Use Night Shade (Xenon) for fixed damage. Use Sleep Powder/Hypnosis for control.
- Kingdra Strategy: Use Sleep Powder (Kimchi) and Night Shade (Xenon) to bypass defenses.
- Speed Control: Teach TM16 Icy Wind to Naga or Blitz to slow down Dragonairs.
- Survival: Level supports to Lv40+ to survive hits.
- Party Management: Swap low-level members (Icarus, Ravioli) for stronger PC options (Naga Lv42, Blitz Lv40) before challenging.

# World Events & Rematches
- Yanma Swarm: Route 35 (Arnie).
- Tully (Fisher): Route 42. Verified Turn 32394.
- Arnie (Bug Catcher): Route 35.
- Alan (Schoolboy): Route 36.
- Chad (Schoolboy): Route 38.

# Lessons Learned
- Menu Navigation: Verify screen state after each step. Avoid long blind sequences.
- Fly Map: In Crystal, the Up button cycles through visited towns.
- Battle Mechanics: HP bar animations occur during move text.
- Input Restrictions: Do NOT mix directional and action buttons in manual `press_buttons`.

# Current Plan
1. Fly to Blackthorn City landing point.
2. Heal at Pokemon Center.
3. Check PC for TM16 (Icy Wind).
4. Swap Exp. Share to Xenon, Amulet Coin to Kimchi.
5. Lead with Gneiss (Lv46) for safe/fast grinding.
6. Fly to Goldenrod, then Route 35 for Yanma swarm.