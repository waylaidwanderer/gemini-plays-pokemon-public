# PC Storage (Box 1)
- DAPXWW (LARVITAR): Lv20
- GLAIVE (SCYTHER): Lv14
- SELKIE (SEEL): Lv24
- DELTA (MANTINE): Lv20
- RANGOON (KRABBY): Lv22
- NOMURA (TENTACOOL): Lv17
- Ravioli (KRABBY): Lv10 (Surf, Whirlpool)
- Ouroboros (DRATINI): Lv15
- AAAAAAAAAA (SPINARAK): Lv13
- LAPIS (POLIWAG): Lv12 (Waterfall, Surf, Whirlpool)

# Tile Mechanics
- WATER: Traversable only via Surf.
- BUOY: Impassable water obstacle.
- FLOOR: Standard walkable ground.
- WALL: Impassable obstacle.
- FLOOR_UP_WALL: Represents a ledge face. Impassable from ALL directions.
- LEDGE_HOP_DOWN: One-way jump from NORTH to SOUTH.
- (11, 14): Dead End Pocket. Wall at (11, 13) and (12, 14) blocks access to the north plateau.
- (11, 15): Gap in the city wall (Y=15). Accesses the beach area but not the plateau.

# Quest Strategies
## Suicune: 'The Great Spiral' (The Only Real Path)
- Fact: The northern plateau is walled off from the south and west. The buoy maze is the only intended entrance.
- Route:
    1. Walk to (19, 30) (East Coast Surf Point).
    2. Use SUPER REPEL.
    3. Use Surf and sail East to (27, 30) (Channel Entrance).
    4. Lane 1 (X=27-29): Sail North to (27, 10).
    5. Gap 1: Move West through (26, 10) into Lane 2.
    6. Lane 2 (X=23-25): Sail South to (23, 16).
    7. Gap 2: Move West through (22, 16) into Lane 3.
    8. Lane 3 (X=19-21): Sail South to (19, 26).
    9. Gap 3: Move West through (18, 26) into Lane 4.
    10. Lane 4 (X=17-18): Sail North to (17, 20).
    11. Gap 4: Move West through (16, 20) into Lane 5.
    12. Lane 5 (X=14-16): Sail North to (14, 10) and land.
    13. Walk to Suicune at (7, 4).
- Preparation: Lead with XENON (Haunter). Use SUPER REPEL.
- Start Turn: 47680 (Suicune North Beach Quest)
- Start Time: Wednesday, Jan 14, 2026, 4:00 AM PST

# Strategy Lessons
- Buoy Maze: The buoy spiral is the only intended path.
- Menu Memory: Items in the pack stay selected. Use the pocket-switch trick to reset cursor.
- Efficiency: Use (19, 30) for launching into the spiral.

# Fly Navigation
- The Fly menu in Johto (Crystal) is a 2D Town Map cursor navigation.
- Cursor Grid (X, Y):
  - New Bark: (14, 10)
  - Cherrygrove: (12, 10)
  - Violet: (12, 6)
  - Azalea: (10, 12)
  - Goldenrod: (6, 9)
  - Ecruteak: (6, 5)
  - Olivine: (2, 6)
  - Cianwood: (0, 9)
  - Mahogany: (10, 5)
  - Lake of Rage: (10, 3)
  - Blackthorn: (14, 5)
- Navigation from Cherrygrove (12, 10) to Cianwood (0, 9): 12 Lefts, 1 Up.
- Failed Fly attempts: 10 (Reason: Fly move not activating or immediately landing in current city).
- Status: Moving to (29, 5) and re-attempting Fly to Cianwood.

# Hypotheses
## Land Route to Suicune (The 'Gem Shortcut')
- Hypothesis: Suicune (7, 4) is reachable by walking North along the West beach (X=2).
- Discovery: There is a gap in the internal city walls. Path: City -> (10, 33) -> (9, 33) -> (8, 33) -> (7, 33) -> (6, 33) -> (6, 35) -> (5, 35) -> Beach (X=2).
- Test: Fly to Cianwood, walk the path above to X=2, then walk North to Y=4.
- Success Condition: Reaching (7, 4) and triggering the Suicune sighting.
- Failed Attempts: 0
- Status: Testing. Path to beach confirmed via wall gaps at Y=33 and Y=35.

# General Lessons
- Wild Encounters & Pathing: A "Movement Blocked" error during navigation often indicates a wild encounter triggered on that step. It doesn't necessarily mean the tile is impassable.
- Buoy Maze Navigation: When surfing in narrow channels, wild encounters are frequent. Maintain Super Repel and be prepared to resume the path after running.