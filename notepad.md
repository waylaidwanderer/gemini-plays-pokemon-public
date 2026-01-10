# Persistent Knowledge
## Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- LADDER: Floor change.
- COUNTER: Face and press A to interact.
- LEDGE: Semi-traversable (jump down).

## Active Quest: Find Granddaughter
- Status: Investigating B1F. Sailors (ID 1 and 2) swap positions between (30, 6) and (31, 6) to block the corridor.
- Clues: energetic girl (1F); "lazy bum" buddy goofing off (B1F).
- Buddy Quest: Talked to sailor at (30, 6) who returned to post. Now talking to the other sailor at (31, 6).
- Strategy: Clear the sailors to explore western B1F.

## Kanto Strategy
- Goal: Collect 8 Kanto badges.
- Target 1: Lt. Surge (Vermilion City). MVP: GNEISS (Graveler) Lv 51.

## Lessons Learned
- S.S. Aqua sailors block corridors dynamically; talk to both to progress the quest.
- Super Nerd (26, 9) blocks the x=26 corridor on B1F.
- Verify object positions in Game State Information before pathing.
- Map transitions reset NPC positions.
- Sailor (ID 2) is at (31, 6), blocking the path north. (Verified Turn 37970).