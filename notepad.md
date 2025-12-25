# Strategy: Suicune Hunt (Crystal)
- Sequence: 1. Burned Tower (Done) -> 2. Cianwood (Done) -> 3. Route 42 (Done) -> 4. Route 38 (Ledge trigger) -> 5. Route 14 -> 6. Tin Tower (Stationary battle).
- Route 38 Trigger: Approach Western Ledge at (3, 10). Reachable via Olivine -> Route 39 -> Route 38.
- Battle Strategy (Tin Tower):
  - Lead: XENON (GASTLY).
  - Use MEAN LOOK to prevent fleeing (if applicable).
  - Use HYPNOSIS to induce sleep.
  - Use NIGHT SHADE for fixed 21 HP damage until low.
  - Catch with GREAT BALLs/ULTRA BALL.

# Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL/HEADBUTT_TREE/BERRY_TREE/BUOY: Impassable.
- TALL_GRASS: Traversable; triggers wild encounters.
- LEDGE_HOP (DOWN/LEFT/RIGHT): One-way traversal in specified direction.
- WATER: Traversable with Surf.
- DOOR/WARP: Triggers map transition.

# Route 38 Ledge Mechanics
- (7, 12) -> (8, 12): LEDGE_HOP_RIGHT (Jump East).
- (7, 14) -> (8, 14): LEDGE_HOP_RIGHT (Jump East).
- (10, 9) -> (11, 9): LEDGE_HOP_RIGHT (Jump East).
- (10, 12) -> (11, 12): LEDGE_HOP_RIGHT (Jump East).
- Result: Central trough (X=8-10) is a pit that can only be exited South at (9, 13). Western ledge (X=0-7) is isolated from the trough.

# Side Quests
- Clear Bell: In Key Items (Verified).
- Arthur (Hard Stone): Route 36 (NE corner). Thursday only. (Pivoted Turn 20816: Stuck in dialogue loop).

# Plan: Reach Route 38 Western Ledge (Started Turn 20771)
1. Fly to Olivine City. (Manual Step-by-Step)
   - [Done] Up from New Bark -> Cherrygrove (Turn 20885)
   - [Next] Up from Cherrygrove -> Violet
   - Up from Violet -> Ecruteak
   - Left from Ecruteak -> Olivine
   - Press A to land.
2. Walk North through Route 39 to Route 38.
3. Approach (3, 10) on Route 38 to trigger Suicune.

# Navigation: Fly Map (Johto)
- Grid: Cianwood(0,0), Olivine(1,0), Ecruteak(2,0), Mahogany(3,0), Blackthorn(4,0); Goldenrod(1,1), Violet(3,1); Azalea(1,2), Cherrygrove(3,2), New Bark(4,2).
- Route from Violet/New Bark to Olivine: Use navigate_fly_map_v2.

# Lessons Learned
- Arthur Loop: Arthur (Thursday) on Route 36 may repeat his introduction without giving the Hard Stone. If this happens for 3+ turns, pivot immediately.
- Inventory Check: Always check Game State Information inventory list before pursuing items to ensure they haven't been collected in summarized turns.
- Fly Map Snapping: Vertical movement causes the cursor to snap to the closest city in the new row. Use step-by-step snapping simulation for reliability.
- Input Latency (Fly): When using Fly, wait for the "Where?" bubble to appear before sending map navigation inputs to avoid moving the character in the overworld.