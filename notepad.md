# Pokémon Crystal Playthrough
- Started: Friday, January 16, 2026 at 5:08 PM PST

### Current Objectives & Strategy
- **Main Quest**: Navigate Ilex Forest to Goldenrod City.
- **Location**: Northern Ilex Forest (Gatehouse Front - Row 4).
- **Goal**: Enter the Gatehouse via the Left Door at (22, 3).
- **Map Data**: Warps located at (22, 3) and (24, 3).
- **Status**: Resetting position to (22, 4) to attempt a clean entry from the South.
- **Note**: Previous attempts were confusing due to potential map glitches or misinterpretation of visual depth.
- **Consolidated Findings**:
    - (23, 3) is a GAP (Floor), not a warp.
    - Path North of Row 0 loops; no exit there.
    - (22, 3) and (24, 3) are Warps in XML; need to verify entry vector (South?).

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