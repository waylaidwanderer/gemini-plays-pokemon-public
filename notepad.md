# Persistent Knowledge
## Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- LADDER: Floor change.
- COUNTER: Face and press A to interact.
- LEDGE: Semi-traversable (jump down).

## Active Quest: Find Granddaughter
- Status: Investigating B1F. Sailor at (30, 6) is blocking the corridor.
- Strategy: Bypass sailor via (31, 6) -> (31, 5).
- Clues: energetic girl (1F); "lazy bum" buddy goofing off (B1F).

## Kanto Strategy
- Goal: Collect 8 Kanto badges.
- Target 1: Lt. Surge (Vermilion City). MVP: GNEISS (Graveler) Lv 51.

## Lessons Learned
- S.S. Aqua sailors block corridors dynamically; use alternate routes.
- Super Nerd (26, 9) blocks the x=26 corridor on B1F.
- Verify object positions in Game State Information before pathing.
- Map transitions reset NPC positions.
- Sailor (ID 1) is at (30, 6), blocking the path north. (Verified Turn 37969).