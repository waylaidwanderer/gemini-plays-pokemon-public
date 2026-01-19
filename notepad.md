# Pokémon Crystal Playthrough
- Started: Friday, January 16, 2026 at 5:08 PM PST

### Current Objectives & Strategy
- **Main Quest**: Explore Goldenrod City.
- **Location**: Goldenrod City (Map 11_2).
- **Goal**: Find the Pokemon Center and HEAL.
- **Sub-Goals**: Visit Daycare (Route 34), Get Radio Card, Bike Shop.
- **Team**: Garnet is Hurt (17/69 HP). Priority is Healing.
- **Next**: Finish call, then heal (Still on phone).

### Team Status
- **Party**: Garnet (Lv23), Amethyst (Lv8), T (Lv3), Jasper (Lv2), Basil (Lv6), Pearl (Togepi, Lv5).
- **PC**: Jade (Oddish).

### Key Items & Progress
- **Badges**: Zephyr Badge, Hive Badge.
- **HMs**: Cut (HM01), Flash (HM05).
- **TMs**: Mud-Slap (TM31), Fury Cutter (TM49).
- **Items**: Old Rod, Miracle Seed.

### Completed Quests
- Sprout Tower (Flash obtained).
- Falkner Defeated.
- Union Cave Crossed.
- Slowpoke Well Cleared.
- Bugsy Defeated.
- Farfetch'd Returned & HM01 Obtained.
- Rival Defeated in Azalea.
### Tile Mechanics (Ilex Forest)
- **TYPE_3fe2**: Walkable floor.
- **TYPE_80fc**: Small trees/bushes. Validated as NON-CUTTABLE WALLS in this area (e.g., at 2,14 and 10,13). Treat as obstacles.
- **TYPE_2889**: Large trees (Walls).
- **TYPE_a339**: Ledge (Jumpable downwards?).
- **TYPE_4e8c**: Water/Pond (Obstacle).
- **TYPE_a336**: Gatehouse Door/Warp.
- **Anomaly**: Heatmap shows 14 visits to (23, 0) and 33 visits to (23, 3). This suggests I have traversed this gatehouse multiple times without exiting.
- **Hypothesis**: The Gatehouse might not be the exit, or requires a specific trigger. Or the exit is blocked by a cuttable bush in the North West.
- **Plan**: Move to (23, 0). If no warp, move Left to investigate the path to Wayne and the North West bushes.
- **Discovery**: The "Gatehouse" facade has a gap at (23, 3) leading to a path behind it at Row 0.
- **Plan**: Follow the path at Row 0 to the West. It appears to be a narrow corridor behind the trees.
- **Observation**: Following the hidden path at Row 0 to the West. I haven't been to (14, 0) yet.
- **Possibility**: This path might lead to the other side of the forest or a cuttable tree shortcut.
### Game Mechanics
- **Battle Menu**: Vertical List (1. Quick Attack, 2. Leer, 3. Smokescreen, 4. Ember).
- **Cursor Behavior**: Resets to Top (Move 1) at start of battle. Remembers last position within battle.
- **Navigation**: Inputs can drop if too fast. Use single-step or the `battle_select_move` tool with delays.
- **Daycare Location**: Confirmed at (13, 15). I can see the door! Prioritizing healing first.
- **NPC Obstacle**: Officer at (9, 11). Bypassed on the Left.
- **Pathing**: Heading North along Column 8 to reach Goldenrod City.