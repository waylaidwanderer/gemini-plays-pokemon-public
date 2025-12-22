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
- Step 1: Defeat Burglar Duncan at (9, 12). COMPLETED.
- Step 2: Navigate to (14, 9) to collect the item ball.
  - Route: (14, 5) -> (2, 5) -> (2, 9) -> (10, 9) -> (10, 12) -> (16, 12) -> (16, 9) -> (14, 9).
- Step 3: Explore the southern area (Rows 22-29) for the Warehouse entrance (Map 3_55).
- Step 4: Activate the Emergency Switch at (20, 11).

# Shutter Observation (Turn 10976)
- Sequence 3-2-1 complete. Gaps opened at:
  - x=2,3 (Rows 6, 7)
  - x=6 (Row 8) - Wait, re-verify this.
  - x=10,11 (Rows 10, 11)
  - x=16,17 (Rows 10, 11)
- Shutter (12, 8) is CLOSED.
- Shutter (6, 12-13) is WALL.
- Gap at (2, 6-7) is the only way to reach Row 8/9 from Row 4/5.
- East section (x >= 20) seems separated from the center by walls at x=18/19. Need to find a gap.
- Plan: Collect item at (14, 9), then explore south for x=15 gap.
- Failed Attempt: Tried to path through (14, 6) (WALL). Row 6 is blocked at x=14.
- Turn Mismatch Fixed: Current Turn is 10976. (Error on 10975).

# Training & Party
- Gneiss (Lv40 Graveler) is highly effective against Poison-types in this area.
- Typhlosion (Lv43) is the backup heavy hitter.
- Icarus (Lv16 Pidgey) is used for Fly.
- Kimchi (Lv21 Gloom) is used for Cut.
- Ravioli (Lv10 Krabby) is used for Surf.

# Shutter Observation (Turn 10968)
- Row 10/11 at x=16: OPEN (Turn 10967).
- Row 14 wall: Solid from x=6 to x=16. Need to check x<6 or x>16.
- Reachable Unseen: (22, 13), (21, 14), (0-5, 14).
- Plan: Explore row 13 to find a path to the southern sections.