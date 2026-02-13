# Warehouse Strategy
- Objective: Find the Director in Underground Warehouse.
- Constraint: Team Rocket barriers block South Goldenrod. Must access South Underground Entrance via West Route 34.

# Route 34 Exploration
- Terrain Analysis:
  - TYPE_4e8c = Water (Surfable).
  - TYPE_1f49 = Whirlpool (Barrier).
  - TYPE_2889 = Trees (Blocked).
  - TYPE_3fe2 = Ground (Walkable).
- Current Status: Arrived in Goldenrod City (Game Corner). Healing at Pokémon Center, then exploring North/Harbor to access West Route 34.
- Revised Plan: Fly to Goldenrod City -> Surf South from Harbor -> Access West Route 34.

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
- Surf Fail (Route 34): Unable to surf West from (2, 49). Tile (1, 49) is a non-surfable map edge.
- Navigation Plan: Surfing South from (2, 49) towards (2, 50).
- Menu Correction: Tool 'select_party_pokemon' caused desync. Manually navigating: Main Menu -> Pokemon -> Headache -> Surf.
Reflection Turn 41022:
- Progress: Abandoned South Route 34 approach due to barriers. Relocated to Goldenrod City to attempt North approach.
- Current Goal: Heal at Pokémon Center (red roof), then find water access in Goldenrod Harbor to reach West Route 34.
- Lessons: "Can't use that here" on a valid tile = Wall. Visual maps can be deceiving; check tile types.
- Navigation: Goldenrod layout is tricky with fences. Need to find the gap to reach the Center at (14, 21).
- Navigation Discovery: Access to Pokemon Center (14, 21) is blocked from East (NPC) and South-Central (Walls at Col 13/14). 
- Valid Path: Go South to Main St (Row 29), West to Col 8 (Open Corridor), North to Row 22, then East to Center.
- Navigation Strategy: Enclosed walls around PokeCenter (Row 21) require access from South (Row 22). 
- Blockage: NPCs at (16,23) and (17,22) block direct path.
- Workaround 1: Fly to Goldenrod City (should land in front of Center).
- Workaround 2: Go East to Col 19, South to Main St (Row 29), West to Col 8, North to Row 22, East to Center.
- West Coast Access: From Main St, go East to Col 18, North to Row 17, West to Col 3 (Water).
- Navigation Update: Path at (16, 23) definitely blocked by Grunt.
- Reroute: Going East to Col 18, South to Row 29, then West to reach Center from the South.
- Navigation Error: Previous attempt to Fly failed because I entered the Bag/Item menu instead of Pokemon. "Use on which PkMn?" is an item prompt.
- Correction: Resetting to Overworld, syncing Start Menu cursor, and entering Pokemon -> Topaz -> Fly.
- Next Step: Verify Fly Map is open, then navigate to Goldenrod.
- Current State: Resetting menus.