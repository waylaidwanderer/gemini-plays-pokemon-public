# Persistent Knowledge
## Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- LADDER: Floor change.
- COUNTER: Face and press A to interact.
- LEDGE: Semi-traversable (jump down).

## Active Quest: Find Granddaughter
- Status: Investigating B1F. Sailor at (30, 6) is blocking the corridor.
- Strategy: Stun sailor at (30, 6) and bypass via (31, 6) -> (31, 5).
- Clues: energetic girl (1F); "lazy bum" buddy goofing off (B1F).

## Kanto Strategy
- Goal: Collect 8 Kanto badges.
- Target 1: Lt. Surge (Vermilion City). MVP: GNEISS (Graveler) Lv 51.

## Lessons Learned
- S.S. Aqua sailors swap positions to block corridors; use `stun_npc`.
- Super Nerd (26, 9) blocks the x=26 corridor.
- Verify object positions in Game State Information before pathing.
- Pathing around (30, 6) must go through (31, 6).