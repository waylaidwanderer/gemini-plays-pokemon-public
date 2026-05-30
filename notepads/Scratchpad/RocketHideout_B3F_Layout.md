# Rocket Hideout B3F Scratchpad Layout & Routing

## Stairs and Key Transitions

## Defeated Trainers & Landmarks
- Rocket Grunt 2: Defeated at (18, 17) (Verified Turn 31867).

## Key Room Layout & Passability
- Southeast Starting Area: (18, 21) to (22, 26) is an open rectangular room containing the stairs up to B2F.
- Row 25 & 26 Corridor: Extends west past Column 17, providing access to the western side of B3F.
- Western Corridor: Columns 10 and 11 form a completely open vertical path from row 26 up to row 17 (Verified Turn 32114).
- Column 23 Wall: Solid and impassable wall at (23, 18), verified by direct collision test on Turn 32105.
- Barriers: Column 9 (rows 22-25) is blocked by plants/statues. Columns 12 and 13 (rows 22-24) are blocked by building walls (Verified Turn 32048).
- Row 17 Tile-by-Tile Search (Turns 32187-32192):
  - (22, 17): Physically stood on and verified on Turn 32188. No warp triggered. Normal walkable floor.
  - (21, 17): Physically stood on and verified on Turn 32189. No warp triggered. Normal walkable floor.
- Western Corridor Systematic Verification (Turn 32232 - 32235):
  - Stood on and walked along column 11 (rows 18 to 26) on Turn 32232. No warp. All normal floor.
  - Stood on (10, 26) and (9, 26) on Turn 32235. No warp. Normal floor.
  - Stood on and verified (10, 22) on B3F on Turn 32299, and verified no warp occurred when stepping off on Turn 32304.
  - Conclusion: Columns 9, 10, and 11 on B3F (rows 17 to 26) do NOT contain any stairs or warps.
- Row 17 Central Verification (Turns 32193-32194):
  - Stood on (20, 17) on Turn 32193. No warp triggered. Normal walkable floor.
  - Stood on (19, 17) on Turn 32194. No warp triggered. Normal walkable floor.
- Row 25 & 26 Central Corridor Systematic Verification (Turns 32256 - 32258):
  - Walked along row 26 from (19, 26) to (11, 26) on Turn 32256. No warp triggered. Normal floor.
  - Walked along row 25 in columns 12-18 on Turn 32258 (bypassing the Grunt at (15, 25)). No warp triggered. Normal floor.
  - Conclusion: No stairs to B4F exist on row 25 or row 26 in columns 12-18 of B3F.
- Turn 32480: Empirically tested the passability of (23, 18) by trying to walk Right from (22, 18). Result: Collided, player remained at (22, 18). Confirmed (23, 18) is solid wall TYPE_2889 and impassable.

# B3F B4F Stairs Systematic Exploration Plan (Turn 32713):
- **Premise**: In unmodded Red/Blue Rocket Hideout B3F, the staircase to B4F is located at (19, 17). However, our previous B3F notes indicate we stood on (19, 17) and (20, 17) without triggering any warp. 
- **Plan**: Since the Map ID '0_199' is shared with B1F, and the northern partition of Map '0_199' is physically inaccessible from the south on B3F, we must systematically inspect the unexplored area of rows 18-24 on columns 12-18 on B3F to find the stairs DOWN to B4F. This will provide a rigorous empirical search of the center-west of B3F.
  - [ ] Inspect column 12 (rows 18 to 21) - Tested (12, 24) on Turn 32788 (Collided). Tested (12, 19) on Turn 32791 (Collided). Confirmed solid.
  - [ ] Inspect column 13 (rows 18 to 21) - Tested (13, 24) on Turn 32786 (Collided).
  - [ ] Inspect column 14 (rows 18 to 21) - Tested (14, 24) on Turn 32784 (Collided).
  - [ ] Inspect column 15 (rows 18 to 21) - Bypassed via row 26.
  - [ ] Inspect column 16 (rows 18 to 21) - Tested (16, 24) on Turn 32780 (Collided).
  - [ ] Inspect column 17 (rows 18 to 21) - Tested (17, 24) on Turn 32779 (Collided).
  - [x] Inspect column 18 (rows 18 to 21) - Confirmed open vertical corridor (traversed frequently).

## Column 23 Partition Wall Systematic Tests (Turn 32765):
- Tested (23, 17) on Turn 32765: Attempted to step Right from (22, 17) and collided. Confirmed solid.
- Tested (23, 19) on Turn 32773: Attempted to step Right from (22, 19) and collided. Confirmed solid.
- Tested (23, 25) on Turn 32777: Attempted to step Right from (22, 25) and collided. Confirmed solid.
- Conclusion: Column 23 is a solid, continuous, and impassable wall dividing the west and east of B3F.