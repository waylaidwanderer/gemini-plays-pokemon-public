# PC Storage (Box 1)
- Ravioli (KRABBY): Lv10 (Surf, Whirlpool)
- LAPIS (POLIWAG): Lv12 (Waterfall, Surf, Whirlpool)

# Tile Mechanics
- WATER: Traversable only via Surf.
- BUOY: Impassable water obstacle.
- FLOOR: Standard walkable ground.
- WALL: Impassable obstacle.
- FLOOR_UP_WALL: Represents a ledge face. Impassable from the SOUTH (cannot walk north). Behaves as FLOOR from other directions.
- LEDGE_HOP_DOWN: One-way jump from NORTH to SOUTH.
- (11, 14): Dead End Pocket. Wall at (11, 13) and (12, 14) blocks access to the north plateau.
- (11, 15): Gap in the city wall (Y=15). Accesses the beach area but not the plateau.

# Quest Strategies
## Suicune: 'The Great Spiral'
- Fact: The buoy spiral is a clockwise maze starting from the east. The land route is blocked by ledge faces.
- The solution is to navigate the lanes:
    1. Lane 1 (East of X=26): Sail North to (27, 10).
    2. Transition: Move West through Gap 1 at (26, 10) into Lane 2.
    3. Lane 2 (Between X=22 and X=26): Sail South to (23, 16).
    4. Transition: Move West through Gap 2 at (22, 16) into Lane 3.
    5. Lane 3 (Between X=19 and X=22): Sail South to (21, 21).
    6. Transition: Move West through Gap 3 at (19, 21) into Lane 4.
    7. Lane 4 (X=19): Sail South to (19, 26).
    8. Transition: Move West through Gap 4 at (18, 26) into Lane 5.
    9. Lane 5 (West of X=18): Navigate the remaining zigs to (14, 10) and land.
    10. Walk to Suicune at (7, 4).
- Preparation: Lead with XENON (Haunter). Use SUPER REPEL.
- Start Turn: 47680 (Suicune North Beach Quest)
- Start Time: Wednesday, Jan 14, 2026, 4:00 AM PST

# Strategy Lessons
- Buoy Maze: The buoy spiral is the only intended path.
- Menu Memory: Items in the pack stay selected. Use the pocket-switch trick to reset cursor.
- Efficiency: Use (19, 30) for launching into the spiral.