# Pokémon Crystal Playthrough
- Started: Friday, January 16, 2026 (Turn #12392)

### Immediate Goals
1. **Traverse National Park**: Enter via Gatehouse, exit East to reach Route 36.
2. **Find Floria**: Look for her near Sudowoodo on Route 36.
3. **Get SquirtBottle**: Return to Goldenrod Flower Shop after finding Floria.
4. **Move Sudowoodo**: Use SquirtBottle on the tree to clear the path to Ecruteak.

### Quest Log
- **Badges**: Zephyr, Hive, Plain.
- **Party**: All Healthy.
- **Mail Quest**: Active.

### Strategic Notes
- **Navigation**: Search the area around the Sudowoodo (35, 9) for Floria.
- **SquirtBottle**: Requires finding Floria first.
- **Floria**: Last seen/rumored near the "wiggly tree" (Sudowoodo).

### Tile Types
- **TYPE_3fe2**: Walkable Ground/Grass (Safe)
- **TYPE_2889**: Obstacle (Wall/Tree)
- **TYPE_fed7**: Mixed (Benches/Obstacles & Gaps).
- Checked Berry Tree at (21, 4). It is just an Ice Berry tree. Floria is not here.
- **Navigation Constraint**: Route 35 East is separated from Goldenrod Gatehouse by a fence. Must use the West side (via National Park) to reach the Gatehouse from the North.
- Navigation Update: The right side of the Route 35 Gatehouse (approx x=13) appears to be an exit-only or blocked path. The main entrance is likely on the left side (approx x=10).
- Tool: `type_text` active. Layout verified (9 cols). Row 4: UPPER (0-2), DEL (3-5), END (6-8).
- Status Update: Currently out of Poké Balls. Need to restock at next opportunity.
- Navigation Update: Tree at (11, 5) is NOT cuttable (just a wall).
- Active Navigation Plan: Reach National Park Gate (6, 4).
- Solved Maze Path (South to North):
  1. Current: (16, 40).
  2. Navigate to (13, 35) [Bypass wall at (13, 36)].
  3. West to (10, 35) -> North to (10, 33).
  4. West to (6, 33) -> North to (6, 31).
  5. West to (4, 31) -> North to (4, 29).
  6. West to (2, 29) -> North to (2, 27).
  7. West to (1, 27) [Service Lane Access].
  8. North on Col 0 to (0, 10) -> Gate.
- Immediate Action: Navigate to (13, 35).