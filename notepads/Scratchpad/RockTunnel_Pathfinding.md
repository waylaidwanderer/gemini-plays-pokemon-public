# RockTunnel_Pathfinding (Updated Turn 24783)
- Current Turn: 24783
- Current Position: (17, 13) on Rock Tunnel B1F
- Active Exploration Duration: 3292 turns (Started B1F backtracking on Turn 21491)

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

## Standard Escape Milestones & Upcoming Route:
- [x] Return from (17, 13) to Ladder C at B1F (23, 11)
- [ ] Take Ladder C up to 1F (17, 11)
- [ ] Walk Left to Column 14 on 1F (14, 11)
- [ ] Physically test if we can walk Down Column 14 on 1F to reach the south exit area, completely bypassing B1F!
- [ ] If blocked, return to B1F and determine a valid detour bypassing (15, 22).