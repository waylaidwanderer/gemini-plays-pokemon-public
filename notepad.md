# Strategy: Suicune Hunt (Crystal)
- Start Turn: 20637 (Thursday)
- Sequence: 1. Burned Tower (Done) -> 2. Cianwood (Done) -> 3. Route 42 (Done) -> 4. Route 38 (Ledge trigger) -> 5. Route 14 -> 6. Tin Tower (Stationary battle).
- Route 38 Trigger: Proximity to the northern ledge (Rows 8-12, X=0-15).
- Route 38 Topology:
  - Western Ledge (X=0-7): Isolated from East. Reachable from Route 39 (West) or Row 14 (South) or Row 5 (North).
  - Central Trough (X=8-10): Reachable from East via ledge jump at (10, 12) or (10, 9). Exit South at (9, 13) to Row 14.
  - Eastern Ledge (X=11-35): Reachable from Ecruteak Gatehouse.
- Plan: Scour the Western Ledge (X=0-7, Rows 10-12).

# Side Quests & Resources
- Arthur (Hard Stone): Route 36. Thursday only. Arthur is in the NE corner of Route 36, near the National Park entrance.
- Clear Bell: In Key Items (Verified Turn 20623).

# Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- TALL_GRASS: Traversable; triggers wild encounters.
- LEDGE_HOP_DOWN: One-way jump South.
- LEDGE_HOP_LEFT: One-way jump West.
- LEDGE_HOP_RIGHT: One-way jump East.
- HEADBUTT_TREE: Impassable.
- WATER: Traversable with Surf.
- BERRY_TREE: Impassable.

# Lessons Learned
- Menu Automation: Manual `press_buttons` is more reliable for simple tasks.
- Ledge Navigation: Check tile types before pathing. (8, 12) is isolated from (7, 12) by collision.

# Plan: Fly to Olivine City to reach Route 38 Western Ledge
- Start Turn: 20771
- Step 1: Open PKMN menu and select Icarus (PIDGEY).
- Step 2: Use FLY. (Failed once, landed in Cherrygrove Turn 20776)
- Step 3: Select Olivine City on the map.
- Step 4: Walk North through Route 39 to Route 38 (X=0-7).
- Step 5: Approach (3, 10) on Route 38 to trigger Suicune.