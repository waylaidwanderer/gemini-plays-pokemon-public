# Pokémon Crystal Playthrough
- Started: Friday, January 16, 2026 (Turn #12392)

### Current Task
- **Fix Glitch**: Enter Route 35 Gatehouse (3, 5) to reset the map and move the glitched girl blocking the Flower Shop.

### Quest Log
- **Badges**: Zephyr, Hive, Plain.
- **Party**: All Healthy.
- **Mail Quest**: Active.
- **Sudowoodo**: Inspected at Turn 12797.

### Strategic Notes
- **Navigation**: Currently in Goldenrod City near the Flower Shop.
- **SquirtBottle**: Need to get this to move Sudowoodo.
- **Floria**: Likely the girl outside or inside the shop.

### Tile Types
- **TYPE_3fe2**: Walkable Ground/Grass (Safe)
- **TYPE_2889**: Obstacle (Wall/Tree)
- **TYPE_fed7**: Mixed (Benches/Obstacles & Gaps).
- **Navigation Constraint**: Route 35 East is separated from Goldenrod Gatehouse by a fence.
- Tool: `type_text` active. Layout verified (9 cols).
- Status Update: Currently out of Poké Balls.
- Glitch Encounter: The girl at (16, 7) triggered Arnie's phone battle script. She is now blocking the door and repeating Arnie's text.
- Fix Plan: Exit South to Goldenrod City and check the Flower Shop (16, 7). If the door is blocked, use the back entrance via Route 35 Alley (requires navigating to the secret exit in this Gatehouse at 4, 0).