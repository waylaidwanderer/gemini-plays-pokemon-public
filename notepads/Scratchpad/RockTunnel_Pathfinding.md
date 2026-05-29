# RockTunnel_Pathfinding (Updated Turn 25264)
- Current Turn: 25264
- Current Position: (17, 13) on Rock Tunnel B1F
- Active Exploration Duration: 3773 turns (Started B1F backtracking on Turn 21491, synchronized Turn 25264)

## Verified Structural Layout Discoveries:
1. Column 17 on 1F: Solid blockage at (17, 15) prevents direct north passage along Column 17.
2. Column 16 on 1F: Fully passable at Rows 14 and 15, allowing us to successfully reach Ladder C at (17, 11).
3. Ladder C (1F 17, 11 <-> B1F 23, 11): Taken down on Turn 24525, taken up on Turn 25009, and down again on Turn 25025.
4. B1F Northern Passage: Fully open from Column 23 via Column 17 north to Row 4, but blocked at Columns 24 and 25 on Rows 2-4 (verified Turn 24546).
5. B1F East-West crossing at Row 20: Physically verified to be BLOCKED on Turn 24686. Columns 18 and 19 on Row 20 are solid rock walls (TYPE_2889).
6. B1F Column 20 Row 14/15 Blockage: Physically verified to be BLOCKED on Turn 24708. Row 14 Column 20 is a solid rock wall (TYPE_2889).
7. B1F East-West crossing via starting chamber: Fully open on Rows 10-13, Columns 14-23.
8. B1F East-West bypass highway: Row 16 has Columns 20-37 open, connecting directly to Column 37 (Ladder D).
9. Column 15 on B1F at Row 22 is solid rock blockage (verified Turn 24763).
10. Column 12 on B1F is a solid vertical wall (TYPE_2889) on Rows 18-25, isolating Columns 10-11.
11. Column 11 on B1F: Blocked at Row 29 by solid rock wall TYPE_2889 (verified Turn 24878, map marker placed).
12. B1F Column 23 Row 14 Blockage: Physically verified to be BLOCKED on Turn 24946. Column 23 Row 14 is a solid rock wall (TYPE_2889).
13. B1F Row 12 Columns 24-25 Blockage: Physically verified to be BLOCKED on Turn 24928. Row 12 Columns 24-25 are solid rock walls (TYPE_2889).

## Mathematical Detour Route (Updated Turn 25248):
- Since Columns 20, 21, 22, and 23 are blocked on Row 14, the shorter detour routes are blocked.
- **Detour Route (Column 19 Bypass)**:
  1. Walk Left 4 steps along Row 13 to Column 19: From (23, 13), move Left to (19, 13).
  2. Walk Down 2 steps along Column 19 to Row 15: From (19, 13), move Down to (19, 15).
  3. Walk Right 4 steps along Row 15 to Column 23: From (19, 15), move Right to (23, 15).
  4. Walk Down 1 step to Row 16: From (23, 15), move Down to (23, 16).
  5. Walk East 14 steps along Row 16 to Column 37: From (23, 16), move Right to (37, 16).
  6. Walk Up 1 step to Ladder D at (37, 15).

## Physical Verification Logs for Active Route:
- Turn 25158: Reached (22, 5). Physically verified that Columns 18-22 on Row 5 are 100% passable (TYPE_3fe2).
- Turn 25180: Walked Right onto (23, 5), physically proving Row 5 Column 23 is 100% passable (TYPE_3fe2).
- Turn 25183: Attempted to walk Right from (23, 5) into (24, 5) (TYPE_2889) and collided (0 tiles visited), physically proving that Row 5 Columns 24-25 consists of a solid, impassable rock wall. This confirms that there is no direct eastern bypass on Row 5, and we must proceed south down Column 23.
- Turn 25195: Attempted to walk Down to (23, 8) and collided, physically proving that Column 23 Rows 8-9 consists of a solid rock wall (TYPE_2889).
- **Burden of Proof Required**: We must systematically verify that B1F Row 7 (Columns 18-37) and Column 18 (Rows 7-13) are passable, logging physical collision results as we proceed.
- Turn 25217: Reached (19, 5) and got interrupted by a wild Geodude battle.
- Turn 25218: Escaped the Geodude battle safely.
- Turn 25224: Reached (22, 10) and got interrupted by a wild Machop battle.
- Turn 25226: Escaped the Machop battle safely.
- Turn 25228: Attempted to navigate south down Column 22 but collided at Row 14, physically and mathematically proving that B1F (22, 14) is blocked by a solid rock wall (only 3 Down steps processed successfully before we hit Row 14 and remained at (22, 13) for the other 2 Down steps, then stepped Right onto (23, 13) and encountered a wild Geodude).
- Turn 25236: Currently in wild Geodude battle at (23, 13).