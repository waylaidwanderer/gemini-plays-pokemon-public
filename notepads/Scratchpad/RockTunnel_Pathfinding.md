# RockTunnel_Pathfinding (Updated Turn 24907)
- Current Turn: 24907
- Current Position: (17, 16) on Rock Tunnel B1F
- Active Exploration Duration: 3416 turns (Started B1F backtracking on Turn 21491, synchronized Turn 24907)

## Verified Structural Layout Discoveries:
1. Column 17 on 1F: Solid blockage at (17, 15) prevents direct north passage along Column 17.
2. Column 16 on 1F: Fully passable at Rows 14 and 15, allowing us to successfully reach Ladder C at (17, 11).
3. Ladder C (1F 17, 11 <-> B1F 23, 11): Taken down on Turn 24525.
4. B1F Northern Passage: Fully open from Column 23 via Column 17 north to Row 4, but blocked at Columns 24 and 25 on Rows 2-4 (verified Turn 24546).
5. B1F East-West crossing at Row 20: Physically verified to be BLOCKED on Turn 24686. Columns 18 and 19 on Row 20 are solid rock walls (TYPE_2889).
6. B1F Column 20 Row 14/15 Blockage: Physically verified to be BLOCKED on Turn 24708. Row 14 Column 20 is a solid rock wall (TYPE_2889).
7. B1F East-West crossing via starting chamber: Fully open on Rows 10-13, Columns 14-23.
8. B1F East-West bypass highway: Row 16 has Columns 20-37 open, connecting directly to Column 37 (Ladder D).
9. Column 15 on B1F at Row 22 is solid rock blockage (verified Turn 24763).
10. Column 12 on B1F is a solid vertical wall (TYPE_2889) on Rows 18-25, isolating Columns 10-11.
11. Column 11 on B1F: Blocked at Row 29 by solid rock wall TYPE_2889 (verified Turn 24878, map marker placed).

## Active Detour Plan:
- [x] Backtrack north up Column 11 to Row 17 on Turn 24881
- [x] Walk East to (17, 17) on Turn 24887
- [x] Walk south down Column 17 to (17, 21) on Turn 24890
- [x] Backtrack Up Column 17 to (17, 16) on Turn 24896 (re-evaluating to perform physical collision test on Column 17 Row 22)
- [x] Physical Collision Test on Column 17 Row 22 (Turn 24911):
  - [x] Walked Down to (17, 21) on Turn 24910.
  - [x] Pressed Down to step onto (17, 22) (labeled TYPE_2770) on Turn 24910.
  - [x] Result: Collided (player remained at (17, 21), visited 0 tiles on Turn 24911), physically and mathematically proving that B1F Column 17 Row 22 is solid and impassable.
- [x] Conclusion: Column 17 is impassable past Row 21 on B1F. Backtracking all the way to Row 11 is mathematically/mechanically necessary!
- [ ] Implement Backtrack Detour Plan:
  - [ ] Walk Up Column 17 from (17, 21) to (17, 11) (10 steps Up)
  - [ ] Walk Right on Row 11 to Column 23 (Ladder C) (6 steps Right)
  - [ ] Walk Down Column 23 to Row 16 (5 steps Down)
  - [ ] Walk Left on Row 16 across Columns 24-25 to Column 20 (3 steps Left)
  - [ ] Walk Down Column 20 to Row 24 (8 steps Down)
  - [ ] Walk Left on Row 24 to Column 15 (5 steps Left)
  - [ ] Walk Down Column 15 to Row 31 (7 steps Down)
  - [ ] Walk East along Southern Corridor (Row 31) to Column 37 (22 steps East)
  - [ ] Walk Up Column 37 to Row 15 (16 steps Up)
  - [ ] Take Ladder D up to 1F (37, 15) to exit Rock Tunnel!