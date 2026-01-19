# Pokémon Crystal Playthrough
- Started: Friday, January 16, 2026 at 5:08 PM PST

### Current Objectives & Strategy
- **Main Quest**: Navigate Ilex Forest to Goldenrod City.
- **Location**: Northern Ilex Forest (Gatehouse Debug).
- **Status**: At (24, 4). "Windows" at (22, 3) and (24, 3) are blocked from South. Middle door (23, 3) is open but fails to warp.
- **Anomaly**: (24, 3) is walkable from the West (side) but acts as a ledge jumping South?
- **Navigation**: Testing the rightmost "Warp" tile at (25, 3). Moving Right to (25, 4) then Up.
- **Hypothesis**: The door might be offset or I need to trigger a specific tile.

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