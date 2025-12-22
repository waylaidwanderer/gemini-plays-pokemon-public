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
- Step 2: Navigate to (20, 11) to activate the Emergency Switch.
  - Route: Row 8 -> Row 9 -> x=2 -> Row 4 -> x=20 -> Row 11.
- Step 3: Explore the southern area (Rows 22-29) for the Warehouse entrance (Map 3_55).
- Step 4: Locate the real Director in the Warehouse.

# Shutter Observation (Turn 10971)
- East/West separation: Wall at x=18 blocks row 8-17.
- Row 4/5: Clear passage across the entire map.
- Emergency Switch (20, 11) is likely the next trigger.
- Gap at (2, 6-7) is the only known way to reach Row 4 from the central area.
- Pharmacist (ID 2) at (4, 8) blocks row 8; must go around via Row 9.
- Shutter (12, 8) is CLOSED with S1, S2, S3 all ON. Row 8 is blocked.
- Plan: (5, 8) -> (5, 9) -> (2, 9) -> (2, 4) -> (22, 4) -> (22, 12) -> (20, 12) -> (20, 11).

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