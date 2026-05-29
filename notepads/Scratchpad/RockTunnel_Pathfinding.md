# RockTunnel_Pathfinding (Updated Turn 25441)
- Current Turn: 25441
- Active Exploration Duration: 3950 turns (Started B1F backtracking on Turn 21491, synchronized Turn 25441)

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
14. Columns 18-19 on B1F are solid rock walls on Rows 14 to 23 (verified Turn 25322).
15. Columns 13 to 19 are solid rock walls on Rows 22 and 23 (verified Turn 25322).

## Physical Verification Logs for Active Route:
- Turn 25158: Reached (22, 5). Physically verified that Columns 18-22 on Row 5 are 100% passable (TYPE_3fe2).
- Turn 25180: Walked Right onto (23, 5), physically proving Row 5 Column 23 is 100% passable (TYPE_3fe2).
- Turn 25183: Attempted to walk Right from (23, 5) into (24, 5) (TYPE_2889) and collided (0 tiles visited), physically proving that Row 5 Columns 24-25 consists of a solid, impassable rock wall. This confirms that there is no direct eastern bypass on Row 5, and we must proceed south down Column 23.
- Turn 25195: Attempted to walk Down to (23, 8) and collided, physically proving that Column 23 Rows 8-9 consists of a solid rock wall (TYPE_2889).
- Turn 25217: Reached (19, 5) and got interrupted by a wild Geodude battle.
- Turn 25218: Escaped the Geodude battle safely.
- Turn 25224: Reached (22, 10) and got interrupted by a wild Machop battle.
- Turn 25226: Escaped the Machop battle safely.
- Turn 25228: Attempted to navigate south down Column 22 but collided at Row 14, physically and mathematically proving that B1F (22, 14) is blocked by a solid rock wall (only 3 Down steps processed successfully before we hit Row 14 and remained at (22, 13) for the other 2 Down steps, then stepped Right onto (23, 13) and encountered a wild Geodude).
- Turn 25236: Currently in wild Geodude battle at (23, 13).
- Turn 25244: Detoured through Column 21 on Row 14 but collided, physically and mathematically proving that B1F (21, 14) is blocked by a solid rock wall (only 2 Left steps processed successfully to (21, 13) before the 2 Down steps collided, then stepped Right back to (23, 13) and collided Down on (23, 14), triggering a wild Zubat encounter).
- Turn 25258: Walked Left 6 steps along Row 13 to (17, 13) without collision, proving Row 13 is fully passable from Column 23 to Column 17. Attempted to step Down to (17, 14) and triggered a wild Zubat battle, proving that Column 17 is accessible on B1F.
- Turn 25287: Escaped from wild Zubat battle safely at (17, 13).
- Turn 25305: Walked Down Column 17 from (17, 13) to (17, 16) without collision, proving Column 17 is open on Rows 14 to 16.
- Turn 25310: Walked Down Column 17 from (17, 16) to (17, 20) without collision, proving Column 17 is open on Rows 17 to 20.
- Turn 25322: Verified B1F Row 22 and Row 23 are blocked on Columns 13-19, and Columns 18-19 are blocked on Rows 14-23. This isolates the southwest quadrant of B1F from Column 17, requiring backtracking to Ladder C at (23, 11) and crossing via 1F.
- B1F Passage Verification: Physically verified that B1F Column 17 is open from Row 13 down to Row 20. Specifically, Rows 13-20 on Column 17 are 100% passable.
- 1F West Column 13 Bypass (Verified Turn 25360): Column 13 has a solid rock wall on Rows 2-13, preventing direct Left movement. To bypass this wall, we walked Left from (17, 11) to (14, 11), walked Down to Row 14, and then walked Left past Column 13 on Row 14.
- 1F Columns 6-7 Blockage (Verified Turn 25363): Attempted to navigate west on Row 14 to Column 5, but collided with solid rock walls on Columns 6 and 7 on Row 14. This forced us to head North along Column 8, reaching Row 8.
- 1F Rows 8-9 Column 6-7 Passable Opening (Verified Turn 25371): Proved that Columns 6 and 7 are open and passable on Row 8, providing a direct horizontal corridor from Column 8 to Column 5 (the western vertical bypass hallway).
- Turn 25416: Located at (8, 11) on Rock Tunnel 1F. Planning path to Ladder B at (5, 3) on 1F: walk Up 3 steps to (8, 8), Left 3 steps to (5, 8), and Up 5 steps to (5, 3).
- Turn 25418: Walked Up from (8, 11) to (8, 8) on Rock Tunnel 1F.
- Turn 25425: Walked Left from (8, 8) to (5, 8) on Rock Tunnel 1F, interrupted by wild Zubat Lv 17.
- Turn 25431: Fled the wild Zubat battle successfully, standing at (5, 8).