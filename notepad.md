# Warehouse Strategy
- Objective: Find the Director in Underground Warehouse.
- Constraint: Team Rocket barriers block South Goldenrod. Must access South Underground Entrance via West Route 34.

- Navigation Strategy Change: Overworld interaction failed multiple times. Retrying Menu interaction to trigger Whirlpool.
- Action:
  1. Open Menu (Start).
  2. Select Pokémon (Down, A).
  3. Select Headache (Down x3, A).
  4. Select Whirlpool.
- Target: Clear Whirlpool at (3, 8).

# Route 34 Exploration Plan
1. Fly to Goldenrod City.
2. Heal at Pokémon Center.
3. Go to Harbor (North of Center).
4. Surf South along the coast to bypass trees.
5. Enter West Route 34.

# Known Locations (Warehouse)
- Stairs: (23, 3) Silver Room <-> (22, 27) Warehouse.
- Switch 1 (Silver Room): Toggles Traps (21,31)-(22,31) and Grunt (22,24).
- Obstacles: Locked Shutter (6, 20), Frozen Grunt (22, 24), Burglar (19, 6).

# Reflection (Turn 41177)
- Progress: Cleared major gyms, now tackling Rocket arc. Stuck at Route 34 Whirlpool.
- Issues: Menu inputs failing or desyncing. 'IntermediateStates' showing wrong turn data.
- Plan: Slowing down inputs. Verifying Party Menu entry before selecting move.