# Rocket Hideout - Floor Mapping & Exploration

## B1F Layout & Mapping
- **Stairs to Game Corner & DOWN to B2F:** (23, 2) - Warps the player UP to the Game Corner (17, 5) or DOWN to B2F (27, 8).
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
- **Trainers on B1F:**
  - Rocket Grunt at (12, 6) facing Right. Defeated on Turn 13944.
  - Rocket Grunt at (26, 8) facing Left. Defeated on Turn 14001.
- **Items on B1F:**
  - Pokéé Ball at (11, 14). Escape Rope obtained on Turn 13977.


## B2F Layout & Mapping
- **Stairs to B1F:** (27, 8)
- **Stairs to B3F:** (5, 15) (Warp trigger on B2F at (4, 15), (5, 15), (6, 15) going Down) - Spawns player at (5, 15) facing Up on B3F.
- **Walkable Area:**
  - Columns 25-28 on Rows 8-12 (completely clear pink floor around stairs)
  - Rows 13-15 on Columns 23-28 (pocket leading to spinner entrance at (12, 13))
  - Row 10 on Columns 14-20, Row 11 on Columns 14-16, Row 12 on Columns 14-15
  - Columns 1-3 on Rows 7-9 (area around far-left spinner landing at (2, 9))
  - Row 7 on Columns 1-5 (top corridor on the far left)
  - Row 11 on Columns 5-7 (area near the Poké Ball at (6, 12))
  - Row 13-15 on Columns 1-4 (bottom-left area)
- **Trainers on B2F:**
  - Rocket Grunt at (20, 13) facing Down. Defeated on Turn 14038.
- **Spinners / Maze Mechanics:**
  - UP spinner at (12, 13) -> UP spinner at (12, 11) -> LEFT spinner at (12, 9) -> LEFT spinner at (4, 9) -> Stopper at (2, 9).
  - LEFT spinner at (17, 10) -> DOWN spinner at (13, 10) -> RIGHT spinner at (13, 12) -> Wall at (15, 12) (stops player at (14, 12)).
- **Items on B2F:**
  - Poké Ball at (16, 8) (blocked by wall at (16, 9), accessible from row 7 at (16, 7))
  - Poké Ball at (1, 11) (Moon Stone, Obtained on Turn 14079)
  - Poké Ball at (6, 12) (TM07 - Horn Drill, Obtained on Turn 14097)

## B3F Layout & Mapping
- **Stairs UP to B2F (Left):** (5, 15) - Warps and spawns the player at B2F (2, 9) facing Right (empirically verified on Turn 15297).
- **Stairs UP to B2F (Right):** (27, 8) - Connects UP to B2F (27, 8) -> B1F (23, 2).
- **Stairs DOWN to B4F:** Located at (21, 22) or (21, 21) in B3F. Takes the player to B4F at (21, 25) (empirically verified on Turn 14770).
- **Entry Landing Position:** (8, 11) (player automatically spins and lands here after coming down the stairs from B2F (5, 15)).
- **Reachable Walkable Areas:**
  - Left Room / Maze: Rows 7-25, Columns 1-16 (completely explored).
  - Right Room: Rows 10-15, Columns 18-28.
- **Major Barriers & Obstacles:**
  - Column 15: Blocked by solid green-edged wall tiles from Row 18 to Row 24 (empirically verified on Turn 14753 that (15, 20) is impassable).
  - Column 18: Solid vertical wall from Row 6 to Row 19, with gaps only at (18, 10) and (18, 11).
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
- **Column 23 Wall:** Empirically verified to be completely solid and impassable from Row 17 to Row 26 on B4F, completely walling off the elevator area (Columns 24-28).
- **Stairs UP to B3F:** (21, 25) - Takes the player back UP to B3F (21, 22).
- **Elevator Doors:** (24, 16) and (25, 16). Access to the elevator is from (24, 17) or (25, 17) going UP.
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