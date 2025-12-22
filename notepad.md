# Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: Dynamic collision. (2,6), (3,6), (10,6), (16,6), (17,6), (16,7), (17,7), (6,8), (12,8), (10,10), (10,11), (11,10), (11,11).
- Switch: Background object. Interact from adjacent tile.
- LADDER: Warp tile. Traversable.
- WARP_CARPET_DOWN: Warp tile.

# Underground Warehouse Puzzle
- Sequence: 3 (ON) -> 2 (ON) -> 1 (ON). (Sequence Complete).
- Result: Gaps opened at x=2,3 (Row 6,7), x=6 (Row 8), x=10,11 (Row 10,11), x=16,17 (Row 10,11), x=18 (Row 12,13).

# Current Strategy: Enter Warehouse
- Search Started: Turn 10940
- Goal: Activate the Emergency Switch at (20, 11).
- Status: Rocket Grunt at (19, 13) defeated. Moving to Emergency Switch. (Turn 10995)
- Step 1: Activate the Emergency Switch at (20, 11) from (20, 12). (Turn 10998: Turning it ON).
- Step 3: Explore the southern area (Rows 22-29) for the Warehouse entrance (Map 3_55).

# Shutter Observation
- Sequence 3-2-1 complete.
- Emergency Switch (20, 11): Interacted from (20, 12) facing UP.
- Shutter (12, 8) is CLOSED.
- Shutter (6, 12-13) is WALL.

# Training & Party
- Calcifer (Lv43 Typhlosion): FLAME WHEEL, HEADBUTT. (Strong vs Grass).
- GNEISS (Lv40 Graveler): STRENGTH, MAGNITUDE, ROLLOUT. (4x weak to Grass).
- KIMCHI (Lv21 Gloom): CUT.
- Ravioli (Lv10 Krabby): SURF.

# Findings
- Found Full Heal at (14, 9). (Turn 10981)