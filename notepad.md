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
  - Route: Need to find a gap in the x=18/19 wall. Row 4/5 is clear across, but row 6-11 is blocked on the east side.
- Step 3: Explore the southern area (Rows 22-29) for the Warehouse entrance (Map 3_55).
- Step 4: Locate the real Director in the Warehouse.

# Shutter Observation (Turn 10973)
- Row 4/5: Clear passage across the entire map.
- Emergency Switch (20, 11): Interacted from (20, 12) facing UP.
- East/West separation: Wall at x=18/19 blocks row 6-11 on the east.
- Path to East Section: Must find a way to (20, 12).
- Gap at (10, 10-11) is OPEN.
- Shutter (12, 8) is CLOSED (S2=ON, S1 doesn't flip it back).
- Shutter (6, 12) is WALL.
- Plan: Backtrack to Row 4, go to x=10, south through gap to Row 13, then explore east/west for gaps in row 14 or column 18.
- Hypothesis: The Warehouse entrance is likely one of the warps in the south (e.g., (5, 25) or (21, 25)).

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