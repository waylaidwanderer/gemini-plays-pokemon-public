# Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: Dynamic collision. (2,6), (3,6), (10,6), (16,6), (17,6), (16,7), (17,7), (6,8), (12,8), (10,10), (10,11), (11,10), (11,11).
- Switch: Background object. Interact from adjacent tile.
- LADDER: Warp tile. Traversable.
- WARP_CARPET_DOWN: Warp tile.

# Underground Warehouse Puzzle
- Sequence: 3 (ON) -> 2 (ON) -> 1 (ON). (Sequence Complete).
- Result: Gaps opened at x=2,3 (Row 6,7), x=6 (Row 8), and x=10,11 (Row 10,11).

# Current Strategy: Enter Warehouse
- Started Warehouse search: Turn 10940
- Step 1: Defeat Rocket Girl at (19, 12).
- Step 2: Activate the Emergency Switch at (20, 11).
- Step 3: Explore the southern area (Rows 22-29) for the Warehouse entrance (Map 3_55).
- Step 4: Locate the real Director in the Warehouse.

# Shutter Observation (Turn 10978)
- Sequence 3-2-1 complete. Gaps opened at:
  - x=2,3 (Rows 6, 7)
  - x=6 (Row 8)
  - x=10,11 (Rows 10, 11)
  - x=16,17 (Rows 10, 11)
  - x=18 (Rows 12, 13) - New gap!
- Emergency Switch (20, 11): Interacted from (20, 12) facing UP.
- Rocket Girl (ID 6) at (19, 12) blocks the direct path; must loop around via Row 13.
- Shutter (12, 8) is CLOSED.
- Shutter (6, 12-13) is WALL.

# Training & Party
- GNEISS (Lv40 Graveler): STRENGTH, MAGNITUDE, ROLLOUT.
- Calcifer (Lv43 Typhlosion): FLAME WHEEL, HEADBUTT.
- KIMCHI (Lv21 Gloom): CUT.
- Ravioli (Lv10 Krabby): SURF.

# Findings
- Found Full Heal at (14, 9). (Turn 10981)