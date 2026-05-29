# Rock Tunnel Escape Route to Lavender Town - Master Plan (Turn 24319)

We have discovered that standard Pokemon Red/Blue Rock Tunnel has 4 ladders on B1F/1F:
- Ladder 1: B1F (33, 25) <-> 1F (37, 3) (Ladder A)
- Ladder 2: B1F (27, 3) <-> 1F (5, 3) (Ladder B)
- Ladder 3: B1F (23, 11) <-> 1F (17, 11) (Ladder C)
- Ladder 4: Unverified location (Ladder D)

The final exit of Rock Tunnel is on 1F at (15, 33), which connects to Route 10 South (Lavender Town).
To reach the exit, we must:
1. Walk from our current position (20, 16) on B1F up Column 37 into the northern corridor.
2. Walk west along the northern corridor to Ladder B at B1F (27, 3).
3. Take Ladder B up to 1F (5, 3).
4. Walk south along the 1F western/southern corridors to the final exit at 1F (15, 33).

## Current Position & Phase 1: Return to Western Connecting Passage
We are currently at B1F (5, 30). We must walk west to Column 4, and systematically check Columns 4 down to 2 on Row 29 to find a passable vertical path.

Step-by-step coordinates:
- Start: B1F (5, 30)
- Walk Left to Column 4.
- For each column X from 4 down to 2:
  - Walk to (X, 30).
  - Attempt to walk Up to (X, 29).
  - Log results to confirm passability of Column X.

## Phase 4: Final Exit to Route 10 South
- Take Ladder 4 up to 1F and exit to Route 10 South.

  - Active Exploration Duration:
    - Started B1F southern backtracking on Turn 21491.
    - Current Turn: 24319.
    - Elapsed Time: 2828 turns.
  - Verified Constraints:
    - 1F (16, 8) is impassable, blocking direct north-south movement on those columns.
    - B1F (3, 31) was tested thoroughly (Turns 23832-23873) by stepping from East, South, and pressing A. Warp did not trigger.
    - B1F (33, 31) was tested thoroughly (Turns 23890-23903) by stepping from West (Left) and performing step-off-and-on. Warp did not trigger.
    - B1F Row 15 is a solid rock wall across Columns 20-27, preventing direct vertical traversal between Row 16 and Row 13 on these columns.
  - Latest Strategy:
    - Southwest corner room coordinates (3, 31), (3, 32), and (3, 33) are fully proven inert. There is no physical ladder here.
    - The bisection of B1F means we cannot reach (23, 11) directly from our current area via overworld traversal on B1F. Instead, we must use the Southern Corridor (Rows 30-33) to access the western side of the map, and trace the path from there. We will walk down to (5, 30), then left to Column 4, and systematically test columns 4 down to 2 on Row 29 to find a passable vertical path.
    - Contingency Plan: If ALL columns (9 down to 2) on Row 29 prove to be impassable rock walls, the Western Chamber is completely sealed from the south. In that case, we must backtrack up to 1F and systematically re-explore the northern areas of 1F (such as finding if there is a vertical connector we missed, or testing if Columns 14-17 have a different passable coordinate).
  - Recent Events:
    - Turn 23955: Stepped onto B1F (3, 31) from (4, 31); warp did not trigger.
    - Turn 23956: Stepped off to (4, 31) due to wild Zubat encounter. Escaped safely.
    - Turn 23958: Stepped onto (3, 31) again; confirmed inert.
    - Turn 23978: Moved down to (4, 32).
    - Turn 23983: Stepped Left to (3, 32) to test; confirmed inert.
    - Turn 23986: Stepped off to (4, 32) due to wild Geodude encounter. Escaped safely.
    - Turn 23992: Moved down to (4, 33).
    - Turn 23993: Stepped Left to (3, 33) to test; confirmed inert.
    - Turn 24006: Deleted the incorrect (3, 31) ladder map marker. Concluded the southwest room contains no exit. Commenced backtracking to explore the western chambers.
    - Turn 24021: Backtracked east through the southern corridor and reached (15, 33).
    - Turn 24035: Reached (15, 24) on overworld.
    - Turn 24042: Moved Right 5 steps along Row 24 to reach (20, 24).
    - Turn 24049: Attempted to walk Up 4 steps along Column 20. Collided with the defeated Pokémaniac sprite at (20, 21), halting at (20, 22).
    - Turn 24052: Stepped Right to (21, 22) to bypass the Pokémaniac sprite.
    - Turn 24054: Walked Up 4 steps along Column 21 to reach (21, 18).
    - Turn 24057: Walked Right 2 steps along Row 18 to reach (23, 18).
    - Turn 24059: Attempted to walk Up 2 steps to (23, 16). Aborted at step 1 due to wild Geodude encounter at (23, 18).
    - Turn 24069: Escaped Geodude battle. Walked Up 2 steps along Column 23 to reach (23, 16).
    - Turn 24120: Stood at (22, 16), analyzed the blockages and recognized that Row 15 is solid. We will now head back to (15, 24) to traverse the western side.
    - Turn 24130: Walked Down from (22, 16) towards (22, 20); interrupted by wild ONIX at (22, 19). Escaped safely.
    - Turn 24139: Walked Down 4 steps from (22, 19) to (22, 23) successfully.
    - Turn 24144: Walked Down 1 step and Left 3 steps from (22, 23) to (19, 24) successfully.
    - Turn 24231: Wild Machop encounter at (11, 30). Escaped safely.
    - Turn 24238: Arrived at (15, 30). Realized that backtracking east is a dead-end loop that returns to the solid Row 15 bisection. Commenced heading back west along Row 30 to systematically test Columns 8 to 2 on Row 29.
    - Turn 24281: Attempted to walk Up to (8, 29) from (8, 30). Resulted in a direct collision (0 tiles visited), proving that (8, 29) is solid and impassable!
    - Turn 24287: Attempted to walk Up to (7, 29) from (7, 30). Resulted in a direct collision (0 tiles visited), proving that (7, 29) is solid and impassable!
    - Turn 24292: Attempted to walk Up to (6, 29) from (6, 30). Resulted in a direct collision (0 tiles visited), proving that (6, 29) is solid and impassable!
    - Turn 24297: Attempted to walk Up to (5, 29) from (5, 30). Resulted in a direct collision (0 tiles visited), proving that (5, 29) is solid and impassable!

## Southwest Warp Systematic Testing Protocol (Completed Turn 24006):
All candidate coordinates tested and confirmed inert:
- Candidate 1: (3, 31) - Inert (Tested Turn 23958)
- Candidate 2: (3, 32) - Inert (Tested Turn 23983)
- Candidate 3: (3, 33) - Inert (Tested Turn 23993)

## Column 11 Passability Testing Protocol (Started Turn 24172):
- Hypothesis: Column 11 on Row 29 is a passable vertical connector, linking the Southern Corridor (Row 30) to the Western Chamber (Row 28 and above).
- Method:
  1. Walk Left 2 steps from (13, 30) to (11, 30).
  2. Attempt to walk Up 1 step to (11, 29) (visually labeled TYPE_2889).
  3. Log whether we collide or successfully step onto (11, 29).
- Log:
  - Turn 24149: Walked Left 4 steps to (15, 24).
  - Turn 24164: Walked Down 4 steps along Column 15 to (15, 28).
  - Turn 24168: Walked Down 2 steps to (15, 30) and Left 2 steps to (13, 30).
  - Turn 24175: Walked Left 2 steps from (13, 30) to (11, 30).
  - Turn 24176: Attempted to walk Up to (11, 29); interrupted by wild Geodude. Escaped safely.
  - Turn 24184: Re-attempted the Up move to test Column 11 passability on Row 29. Resulted in a direct collision (0 tiles visited), proving that (11, 29) is indeed solid and impassable!
  - Turn 24191: Walked Left 1 step from (11, 30) to (10, 30).
  - Turn 24200: Attempted to walk Up to (10, 29) from (10, 30). Resulted in a direct collision (0 tiles visited), proving that (10, 29) is solid and impassable!
  - Turn 24214: Preparing to walk Left 1 step to (9, 30) to test Column 9.
  - Turn 24223: Stood at (9, 30). Now attempting to walk Up to (9, 29) to verify passability of Column 9.
  - Turn 24224: Attempted to walk Up to (9, 29). Resulted in a direct collision (0 tiles visited), proving that (9, 29) is solid and impassable. Concluded that Columns 9, 10, and 11 on Row 29 are all completely solid rock walls. Commenced moving east towards Column 15 to traverse up the Western vertical bypass.
  - Turn 24340: Attempted to walk Up to (3, 29) from (3, 30). Resulted in a direct collision (0 tiles visited), proving that (3, 29) is solid and impassable!