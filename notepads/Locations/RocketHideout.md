# Rocket Hideout - Floor Mapping & Exploration

## B1F Layout & Mapping
- **Stairs DOWN to B2F:** Located at B1F (23, 2). Warps the player DOWN to B2F, spawning them at (27, 8) facing Down (verified on Turn 15948).

- **Stairs UP to Celadon Game Corner:** Located at B1F (21, 2). Warps the player UP to Celadon Game Corner, spawning them at (17, 4) (verified on Turn 15914).
- **Walkable Area:**
  - Row 1: Columns 19-24
  - Row 2: Columns 19-22
  - Row 3: Columns 19-24
  - Row 4: Columns 20-23
  - Row 5: Columns 13-26 (leading Left and Right)
  - Column 11: Rows 5-10
  - Column 12: Rows 5-10
  - Row 10: Columns 11-14
  - Column 14: Rows 10-14
  - Row 14: Columns 12-14
  - Column 26: Rows 5-7
  - Row 7: Columns 25-26
  - Column 25: Rows 7-9 and 11-15
  - Row 11: Columns 25-28
  - Column 28: Rows 11-15
  - Row 15: Columns 24-28
  - Column 24: Rows 14-15
  - Row 14: Columns 24-28 (walkable horizontal corridor connecting to Column 28)
  - Column 23 (Vertical Corridor): Rows 9-13 is a narrow 1-column wide vertical strip bounded by a solid wall at the north (Row 8) and a solid hedge/wall at the south (Row 14), making it a dead end.
- **Trainers on B1F:**
  - Rocket Grunt at (12, 6) facing Right. Defeated on Turn 13944.
  - Rocket Grunt at (26, 8) facing Left. Defeated on Turn 14001.
- **Items on B1F:**
  - Pokéé Ball at (11, 14). Escape Rope obtained on Turn 13977.


## B2F Layout & Mapping
- **Stairs to B1F:** (27, 8)
- **Stairs to B3F:** (21, 8) (verified on Turn 15897).
- **Walkable Area:**
  - Columns 25-28 on Rows 8-12 (completely clear pink floor around stairs)
  - Rows 13-15 on Columns 23-28 (pocket leading to spinner entrance at (12, 13))
  - Row 10 on Columns 14-20, Row 11 on Columns 14-16, Row 12 on Columns 14-15
  - Columns 1-3 on Rows 7-9 (area around far-left spinner landing at (2, 9))
  - Row 7 on Columns 1-5 (top corridor on the far left)
  - Row 11 on Columns 5-7 (area near the Poké Ball at (6, 12))
  - Row 13-15 on Columns 1-4 (bottom-left area)
- **B2F (17, 12) Wall:** Verified solid wall block (empirically hit on Turn 16975).
- **Trainers on B2F:**
  - Rocket Grunt at (20, 13) facing Down. Defeated on Turn 14038.
- **Spinners / Maze Mechanics:**
  - LEFT spinner at (17, 11) -> slides all the way to (2, 9) (stopper). (Verified on Turn 16828)
- **Items on B2F:**
  - Poké Ball at (16, 8) (blocked by wall at (16, 9), accessible from row 7 at (16, 7))
  - Poké Ball at (1, 11) (Moon Stone, Obtained on Turn 14079)
  - Poké Ball at (6, 12) (TM07 - Horn Drill, Obtained on Turn 14097)


- **Elevator Location & Interaction (Verified on Turn 17280):**
  - The B2F elevator doorway is located at (25, 13) (Row 13 Column 25).
  - Column 24 Row 13 is a solid decorative pillar, which blocks it.
  - To use the elevator on B2F, you must stand at B2F (25, 14) facing UP, and press "A" (with the Lift Key in your bag). This will open the doors, allowing you to walk UP to (25, 13) to warp inside the elevator cabin.

## B3F Layout & Mapping

- **Stairs UP to B2F (Left Room):** Located at B3F (5, 15). Warps the player UP, spawning them at B2F (2, 9) facing Right (verified on Turn 15297).
- **Stairs UP to B2F (Right Room):** Located at B3F (25, 6). Warps the player UP, spawning them at B2F (21, 8) (verified on Turn 15541).
- **Stairs DOWN to B4F (Western Room):** Located at B3F (19, 18). Takes the player to B4F at (19, 10) (verified on Turn 15679).
- **Stairs DOWN to B4F (Eastern Room):** Located at B3F (21, 22). Takes the player to B4F at (21, 24) (verified on Turn 17035).
- **Major Barriers & Obstacles:**
  - Column 15: Blocked by solid green-edged wall tiles from Row 18 to Row 24 (empirically verified on Turn 14753 that (15, 20) is impassable).
  - Column 18: Solid vertical wall from Row 6 to Row 19, with walkable gaps at (18, 10), (18, 11), (18, 12), and (18, 13).
  - Row 16: Solid horizontal wall from Column 18 to Column 28, making the bottom-right corridor (rows 17-19) inaccessible from the Right Room.
  - Column 24: Decorative columns/pillars at (24, 11) and (24, 13) are impassable.
- **Walkable Row 25 Crossing Method (Burden of Proof Verified):**
  - Land at (9, 24) stopper on B3F (Turn 14758).
  - Walk Right 1 step to (10, 24) (Turn 14759).
  - Walk Down 1 step onto (10, 25) RIGHT spinner -> slides us through (11, 25), (12, 25), (13, 25) to (14, 25) stopper (Turn 14760). This is the only physical route that successfully bypasses the Column 15 blockage!
- **Spinner Pathways:**
  - (12, 13) (UP spinner) -> spins UP to (12, 9) (LEFT spinner) -> spins Left to (2, 9) (stopper).
  - (9, 14) (DOWN spinner) -> spins DOWN to (9, 16) (stopper).
  - (11, 16) (RIGHT spinner) -> spins RIGHT to (15, 17) (stopper).
  - (14, 17) (UP spinner) -> spins UP to (14, 15) (stopper).
  - (16, 14) (UP spinner) -> spins UP to (16, 13) (stopper).
- **Items on B3F:**
  - Poké Ball at (16, 8) (TM30 - Teleport, obtained on Turn 14196)
  - Poké Ball at (3, 21) (Super Potion, obtained on Turn 14439)

## B4F Layout & Mapping
### Verified Barriers & Obstacles:
- **Row 16 Railing/Wall:** Empirically verified to be completely solid and impassable from Column 10 to Column 22 on B4F.
- **Column 23 Wall:** Column 23 has a walkable horizontal gap on Row 16, allowing passage between the western and eastern chambers on B4F.
- **Stairs UP to B3F (Western Room):** Located at B4F (19, 10). Takes the player back UP to B3F (19, 18) (verified on Turn 15679).
- **Stairs UP to B3F (Eastern Room):** Located at B4F (21, 24). Takes the player back UP to B3F (21, 22) (verified on Turn 17035).
- **Elevator**: Located in the eastern chamber. The western stairs land at B4F (19, 10). While the Column 23 wall is solid on most rows, Row 16 is completely walkable, allowing the player to walk on foot from the western stairs to the eastern chamber and the Lift Key gate. The Lift Key is obtained on B4F at (10, 2) on Turn 15797.
- **Walkable Areas:**
  - Row 25: Column 10 to Column 22 is a clear, walkable horizontal pink floor corridor.
  - Columns 10-11: Walkable vertical corridor from Row 17 to Row 25.
  - Row 17: Walkable from Column 10 to Column 22 (east room).
  - Row 17 Column 9: Location of the Hyper Potion Pokéball (obtained on Turn 14865, now walkable).
- **Trainers on B4F:**
  - Rocket Grunt at (17, 25). Defeated on Turn 14805. Tells the player to take the elevator to see his boss.
  - Rocket Grunt at (18, 17). Defeated on Turn 14902. He says "SILPH SCOPE? I don't know where it is!".
- **Items on B4F:**
  - Poké Ball at (19, 17) (Nugget, obtained on Turn 14992).
  - Poké Ball at (9, 17) (Hyper Potion, obtained on Turn 14865).
  - Poké Ball at (10, 12) (HP UP, obtained on Turn 15709).
  - Poké Ball at (10, 2) (LIFT KEY, dropped by elevator-guard grunt at (11, 2) on Turn 15778).
- **B3F Grid Obstacles & Boundaries (Burden of Proof Verified):**
  - B3F (20, 7) to (20, 11) is a clear, walkable vertical corridor (verified on Turn 16950).
  - B3F (20, 12) is a solid green-edged plant wall block (completely impassable, verified on Turn 16950).
  - B3F Column 21 is a solid vertical grey wall from Row 6 to Row 13 (verified on Turn 16950).
  - B3F Column 19 is blocked by solid wall blocks from Row 10 to Row 14 (verified on Turn 16952).
  - B3F Column 18 is blocked by solid wall blocks from Row 10 to Row 14 (verified on Turn 16952).
  - B3F Column 8 is blocked by a solid vertical wall on Row 5-7 (verified on Turn 16958).
  - B3F Column 9 has a solid vertical wall at Row 20-21 (verified on Turn 17019).