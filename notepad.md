# Warehouse Strategy
- Objective: Find the Director in Underground Warehouse.
- Constraint: Team Rocket barriers block South Goldenrod. Must access South Underground Entrance via West Route 34.

# Route 34 Exploration
- Terrain Analysis:
  - TYPE_4e8c = Water (Surfable).
  - TYPE_1f49 = Whirlpool (Barrier).
  - TYPE_2889 = Trees (Blocked).
  - TYPE_3fe2 = Ground (Walkable).
- Current Status: Surfing North to Row 3 to find Whirlpool Gap.
- Navigation Plan: Walk North to (6, 43) to re-enter Water (TYPE_4e8c).
- Whirlpool Analysis:
  - Trees block North progress at Row 7 in East Channel.
  - Trees block access to West Channel from the South (Row 44-53).
  - CONCLUSION: I MUST break the Whirlpool at (3, 8) to proceed. No other path exists.
- Current Action: Clear menus (stuck in "Can't use that here"), Face Left, and interact directly with 'A'.

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
- Menu Correction: Tool 'select_party_pokemon' caused desync. Manually navigating: Main Menu -> Pokemon -> Headache -> Surf.
Reflection Turn 40917:
- Realized trees (TYPE_2889) block Westward Surf attempts from Row 44 to 54. 
- Must travel North to Row 43 (Col 6) to find open water.
- Created tool 'find_surf_start_point' to prevent future "bonking" against non-water tiles.