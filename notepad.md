# Persistent Knowledge
## Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- LADDER: Floor change (e.g. 1F to B1F).
- COUNTER: Face and press A to interact.
- LEDGE: Semi-traversable (jump down).
- WATER: Requires SURF.
- WHIRLPOOL: Requires WHIRLPOOL.
- WATERFALL: Requires WATERFALL.

## Active Quest: Find Granddaughter
- Status: Investigating B1F. Passage north at (30, 6) is blocked by a sailor.
- Clues: Energetic girl (1F); "lazy bum" buddy goofing off (B1F).
- Strategy: Use the ladder at (30, 14) to reach B1F, then bypass the sailor at (30, 6) using the empty tile at (31, 6). Explore western B1F.

## Kanto Strategy
- Goal: Collect 8 Kanto badges.
- Target 1: Lt. Surge (Vermilion City).
- MVP: GNEISS (Graveler) Lv 51. Ground-type immunity to Electric.

## Lessons Learned
- S.S. Aqua sailors block corridors; check Game State for exact positions.
- Super Nerd (26, 9) blocks the x=26 corridor on B1F.
- Map transitions reset NPC positions and can progress scripted events.
- Path to western 1F is likely via B1F (East 1F -> East B1F -> West B1F -> West 1F).