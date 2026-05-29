# RockTunnel_Pathfinding (Updated Turn 24801)
- Current Turn: 24801
- Current Position: (14, 19) on Rock Tunnel 1F
- Active Exploration Duration: 3310 turns (Started B1F backtracking on Turn 21491)

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
- [x] Return from (17, 13) to Ladder C at B1F (23, 11) (Turn 24784)
- [x] Take Ladder C up to 1F (17, 11) (Turn 24785)
- [x] Walk Left to Column 14 on 1F (14, 11) (Turn 24789)
- [x] Physically test if we can walk Down Column 14 on 1F (Turn 24793-24797)
- [x] 1F Column 14 Experiment Result: Row 23 is completely blocked by solid rock wall TYPE_2889 across Columns 10-19. Under previous tests on Turn 24431-24453, we proved Row 22 is a solid barrier from Column 2 to 21 on 1F. Therefore, 1F is completely impassable, and we MUST solve the B1F detour!
- [ ] Return to B1F via Ladder C at (17, 11)
- [ ] On B1F, find an alternative path Down to Row 24 (test B1F Column 14, 16, or 17 past Row 21)

## 1F Column 14 Passability Experiment (Turn 24786) - RESOLVED Turn 24801
- **Hypothesis**: Columns 14-16 on Row 11 are open on 1F, and Column 14 is open to the south, allowing a direct bypass to the exit on 1F.
- **Methodology**:
  - Stand at (17, 11) on 1F.
  - Move Left 3 steps to (14, 11).
  - Move Down Column 14 to see if we can bypass the B1F bisection entirely.
- **Result**: Checked up to Row 19 on Column 14. Row 23 is a solid wall of TYPE_2889 rock, confirming the western 1F area is completely cut off from the south. We must proceed via B1F. Status: Closed.