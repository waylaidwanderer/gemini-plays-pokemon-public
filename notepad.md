# Warehouse Strategy
- Objective: Find the Director in Underground Warehouse.
- Constraint: Team Rocket barriers block South Goldenrod. Must access South Underground Entrance via West Route 34.

# Route 34 Exploration
- Barrier: Fence/Trees separate East (Current) and West (Goal).
- Water Barrier: A continuous line of "Whirlpool" tiles (Col 3) separates the water into Left/Right channels.
  - Right Channel: Connected to East Route 34.
  - Left Channel: Connected to West Route 34 (Goal).
  - Status: "Whirlpool" tiles act as a barrier. I have the Glacier Badge and HM06, so I can remove them if I can surf up to them.
  - Current Strategy: Surf on the East side (Right Channel), then interact with Whirlpools to cross or loop around South.

# Known Locations (Warehouse)
- Stairs: (23, 3) Silver Room <-> (22, 27) Warehouse.
- Switch 1 (Silver Room): Toggles Traps (21,31)-(22,31) and Grunt (22,24).
- Obstacles: Locked Shutter (6, 20), Frozen Grunt (22, 24), Burglar (19, 6).
- Battle Strategy Update: Navigation errors causing loops. Switching to single-step confirmed inputs for battle menus (Enter Fight -> Check Cursor -> Move).
- Menu Mechanics: Battle Move Menu is a VERTICAL LIST of 4 items. Use UP/DOWN to navigate, not Left/Right.
  1. Top
  2. Upper-Mid
  3. Lower-Mid
  4. Bottom
- Navigation Issue: Pressing 'A' to Surf at (2, 49) facing Left failed. Attempting via Menu to bypass potential interaction bug.
- Surf Fail: Unable to surf West from (2, 49). Tile (1, 49) is a non-surfable map edge.
- Navigation Plan: Surfing South from (2, 49) towards (2, 50).