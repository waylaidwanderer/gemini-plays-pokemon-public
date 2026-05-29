# RockTunnel_Pathfinding (Updated Turn 25525)
- Current Turn: 25525
- Active Exploration Duration: 4034 turns (Started B1F backtracking on Turn 21491, synchronized Turn 25525)

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
- B1F Column 17/23 Active Detour Physical Verification (Turns 25180-25310): Verified that Column 17 is fully passable from Row 13 to Row 20. Verified that Column 23 Row 14 and Column 21-22 Row 14 are blocked by solid rock walls (TYPE_2889).
- Turn 25322: Verified B1F Row 22 and Row 23 are blocked on Columns 13-19, and Columns 18-19 are blocked on Rows 14-23. This isolates the southwest quadrant of B1F from Column 17, requiring backtracking to Ladder C at (23, 11) and crossing via 1F.
- B1F Passage Verification: Physically verified that B1F Column 17 is open from Row 13 down to Row 20. Specifically, Rows 13-20 on Column 17 are 100% passable.
- 1F West Column 13 Bypass (Verified Turn 25360): Column 13 has a solid rock wall on Rows 2-13, preventing direct Left movement. To bypass this wall, we walked Left from (17, 11) to (14, 11), walked Down to Row 14, and then walked Left past Column 13 on Row 14.
- 1F Columns 6-7 Blockage (Verified Turn 25363): Attempted to navigate west on Row 14 to Column 5, but collided with solid rock walls on Columns 6 and 7 on Row 14. This forced us to head North along Column 8, reaching Row 8.
- 1F Rows 8-9 Column 6-7 Passable Opening (Verified Turn 25371): Proved that Columns 6 and 7 are open and passable on Row 8, providing a direct horizontal corridor from Column 8 to Column 5 (the western vertical bypass hallway).
- 1F Column 5 Western Hallway (Verified Turn 25452): Column 5 is 100% open and passable from Row 8 to Row 3, leading directly to Ladder B at (5, 3).
- B1F Eastern Corridor Row 3 Passability (Verified Turn 25485): Row 3 is completely open and passable from Column 27 (Ladder B) to Column 33.
16. B1F Column 33 Row 6/7 Blockage (Verified Turn 25505): Column 33 is blocked on Row 6 and Row 7 by solid rock walls (TYPE_2889). Bypassed by detouring to Column 34/35.