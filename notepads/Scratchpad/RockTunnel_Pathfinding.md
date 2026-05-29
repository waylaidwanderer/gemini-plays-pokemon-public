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
    - Current Turn: 24391.
    - Elapsed Time: 2900 turns.
  - Recent Milestones:
    - Turn 24346: Completed the systematic collision sweep of Columns 2-11 on Row 29. Verified that the entire southern boundary on Row 29 from Column 2 to Column 11 is completely solid, impassable wall.
    - Turn 24381: Discovered that Row 12 & 13 are completely passable on Columns 16-23, providing a direct connection to the northern corridors.
    - Turn 24385: Updated the rock_tunnel_navigator map database to include the northern B1F corridor, enabling flawless pathfinding to Ladder B (27, 3).

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