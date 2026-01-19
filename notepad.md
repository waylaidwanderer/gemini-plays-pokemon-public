# Pokémon Crystal Playthrough
- Started: Friday, January 16, 2026 at 5:08 PM PST

### Current Objectives & Strategy
- **Main Quest**: Navigate Ilex Forest to Goldenrod City.
- **Location**: Northern Ilex Forest (Gatehouse Front).
- **Goal**: Enter the Gatehouse via the Left Door at (22, 3).
- **Status**: At (22, 4). Left Door (22, 3) and Right Door (24, 3) are both SOLID (blocked movement).
- **Anomaly**: Mental Map lists the "Pillar" tile at (23, 3) as `TYPE_3fe2` (Walkable), while the doors are `TYPE_a336` (Solid?).
- **Plan**: Move Right to (23, 4) and try walking UP through the "Pillar" at (23, 3).
- **Fact**: Doors blocked movement. Testing the space between them.

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