# RockTunnel_Pathfinding (Updated Turn 25023)
- Current Turn: 25023
- Current Position: (17, 11) on Rock Tunnel 1F
- Active Exploration Duration: 3532 turns (Started B1F backtracking on Turn 21491, synchronized Turn 25023)

## Verified Structural Layout Discoveries:
1. Column 17 on 1F: Solid blockage at (17, 15) prevents direct north passage along Column 17.
2. Column 16 on 1F: Fully passable at Rows 14 and 15, allowing us to successfully reach Ladder C at (17, 11).
3. Ladder C (1F 17, 11 <-> B1F 23, 11): Taken down on Turn 24525, taken up on Turn 25009.
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

## Active Escape Route via B1F Row 7 Northern Bypass:
- **Verified Route**: From (23, 13), walk West along Row 13 to Column 18, walk Up Column 18 to Row 7, walk East along Row 7 to Column 37, and walk Down Column 37 to reach Ladder D at (37, 15).
- [ ] Step 1: Walk West along Row 13 to Column 18:
  - [ ] Walk Left 4 steps from (23, 13) to (19, 13)
  - [ ] Walk Left 1 step from (19, 13) to (18, 13)
- [ ] Step 2: Walk Up Column 18 to Row 7:
  - [ ] Walk Up 6 steps from (18, 13) to (18, 7)
- [ ] Step 3: Walk East along Row 7 to Column 37:
  - [ ] Walk Right 19 steps from (18, 7) to (37, 7)
- [ ] Step 4: Walk Down Column 37 to Ladder D (37, 15):
  - [ ] Walk Down 8 steps from (37, 7) to (37, 15)
- [ ] Step 5: Take Ladder D to exit!

## Physical Verification Logs for Active Route:
- Turn 24951: Attempted to walk Left on Row 13 from (23, 13) but triggered wild Geodude battle at (23, 13) (escaped Turn 24956). Current position is at (23, 13).
- Turn 24994: Resumed walking Left on Row 13 from (23, 13) to Column 20.
- Turn 24995: Reached (20, 13) and encountered wild Onix.
- Turn 24997: Escaped from wild Onix at (20, 13).
- Turn 25009: Backtracked to Ladder C at (23, 11) and ascended to Rock Tunnel 1F at (17, 11).
- Turn 25023: Returning down Ladder C to resume physical verification of the B1F Column 18 and Row 7 bypass.
- **Burden of Proof Required**: We must systematically verify that B1F Row 7 (Columns 18-37) and Column 18 (Rows 7-13) are passable, logging physical collision results as we proceed.