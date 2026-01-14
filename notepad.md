# PC Storage (Box 1)
- Ravioli (KRABBY): Lv10 (Surf, Whirlpool)
- LAPIS (POLIWAG): Lv12 (Waterfall, Surf, Whirlpool)

# Tile Mechanics (Global)
- FLOOR: Standard walkable ground.
- WATER: Traversable only via Surf.
- BUOY: Impassable water obstacle.
- WALL: Impassable obstacle.
- HEADBUTT_TREE: Special tree for Headbutt.
- DOOR: Warp point.
- FLOOR_UP_WALL: Ledge face. Impassable.
- LEDGE_HOP_DOWN: One-way jump (North to South).

# Fly Navigation (Grid Math)
- Map: Town Map (Fly).
- Rule: 7 directional taps = 1 coordinate unit. (Verified: 14 taps = 2 units from New Bark to Cherrygrove).
- Target: Cianwood (0, 9) from New Bark (14, 10).
- Progress: 0/98 Lefts.
- Strategy: Move cursor in chunks of 14 taps (2 units) with 250ms sleeps.

# Suicune Capture Strategy
- Lead: XENON (Haunter).
- Move 1: Hypnosis (Sleep status).
- Move 2: Night Shade (Fixed 44 dmg; Suicune has ~120 HP). Use 2 times to reach red zone.
- Item: Ultra Balls.

# Strategic Plans
## Fly to Cianwood
- Current Step: Moving cursor 14 taps West to reach Cherrygrove City.

## Verify 'Gem Shortcut' in Cianwood
- Task: Once in Cianwood, verify if the wall gap at (11, 15) allows access to the north beach plateau (Y < 16).