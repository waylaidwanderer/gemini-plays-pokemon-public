# RockTunnel_Pathfinding (Updated Turn 24858)
- Current Turn: 24858
- Current Position: (14, 21) on Rock Tunnel B1F
- Active Exploration Duration: 3363 turns (Started B1F backtracking on Turn 21491)

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
11. Column 11 on B1F is completely open and passable down to the Southern B1F Corridor!

## Standard Escape Milestones & Upcoming Route:
- [x] Return from (17, 13) to Ladder C at B1F (23, 11) (Turn 24784)
- [x] Take Ladder C up to 1F (17, 11) (Turn 24785)
- [x] Walk Left to Column 14 on 1F (14, 11) (Turn 24789)
- [x] Physically test if we can walk Down Column 14 on 1F (Turn 24793-24797)
- [x] 1F Column 14 Experiment Result: Row 23 is completely blocked by solid rock wall TYPE_2889 across Columns 10-19. Under previous tests on Turn 24431-24453, we proved Row 22 is a solid barrier from Column 2 to 21 on 1F. Therefore, 1F is completely impassable, and we MUST solve the B1F detour!
- [x] Return to B1F via Ladder C: Walked north on 1F on Turn 24807, and warped back to B1F (23, 11) on Turn 24808.
- [x] Walk Left 6 steps to (17, 11): Interrupted on Turn 24809 by a wild Machop at (21, 11).
- [x] Escaped wild Machop on Turn 24821.
- [x] Resumed B1F western detour and reached (17, 15) on Turn 24828.
- [x] Walk south down Column 17: Interrupted on Turn 24840 by a wild Zubat at (17, 17) (escaped Turn 24843).
- [x] Walked south to (17, 21) on Turn 24856.
- [x] Walked Left to (14, 21) on Turn 24858.
- [x] Walk north up Column 14 to Row 17 (Turn 24870)
- [x] Walk Left on Row 17 to Column 11 (Turn 24871)
- [x] Walk Down Column 11 to (11, 25) (Turn 24878)
- [ ] Column 11 Blockage Discovery (Turn 24878): Row 29 is blocked at Column 11 by solid rock wall TYPE_2889. We must backtrack to Row 17 and use Column 17 -> Row 24 -> Column 15.
- [ ] Backtrack: Walk Up Column 11 to Row 17:
  - [ ] Walk Up 8 steps from (11, 25) to (11, 17)
- [ ] Walk Right on Row 17 to Column 17:
  - [ ] Walk Right 6 steps from (11, 17) to (17, 17)
- [ ] Walk Down Column 17 to Row 24:
  - [ ] Walk Down 7 steps from (17, 17) to (17, 24)
- [ ] Walk Left on Row 24 to Column 15:
  - [ ] Walk Left 2 steps from (17, 24) to (15, 24)
- [ ] Walk Down Column 15 to Southern B1F Corridor (Row 31):
  - [ ] Walk Down 7 steps from (15, 24) to (15, 31)
- [ ] Walk East along Southern B1F Corridor to Column 37:
  - [ ] Walk East 22 steps from (15, 31) to (37, 31)
- [ ] Walk Up Column 37 to B1F Ladder D:
  - [ ] Walk Up 16 steps to (37, 15)
- [ ] Take Ladder D up to 1F (37, 15) to exit Rock Tunnel!

## 1F Column 14 Passability Experiment (Turn 24786) - RESOLVED Turn 24801
- **Hypothesis**: Columns 14-16 on Row 11 are open on 1F, and Column 14 is open to the south, allowing a direct bypass to the exit on 1F.
- **Methodology**:
  - Stand at (17, 11) on 1F.
  - Move Left 3 steps to (14, 11).
  - Move Down Column 14 to see if we can bypass the B1F bisection entirely.
- **Result**: Checked up to Row 19 on Column 14. Row 23 is a solid wall of TYPE_2889 rock, confirming the western 1F area is completely cut off from the south. We must proceed via B1F. Status: Closed.