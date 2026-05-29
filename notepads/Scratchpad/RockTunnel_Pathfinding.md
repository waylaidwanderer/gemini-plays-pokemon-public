# Rock Tunnel Escape Route to Lavender Town - Master Plan (Turn 23941)

We have discovered that standard Pokemon Red/Blue Rock Tunnel has 4 ladders on B1F/1F:
- Ladder 1: B1F (33, 25) <-> 1F (37, 3) (Ladder A)
- Ladder 2: B1F (27, 3) <-> 1F (5, 3) (Ladder B)
- Ladder 3: B1F (23, 11) <-> 1F (17, 11) (Ladder C)
- Ladder 4: B1F (3, 31) <-> 1F (3, 31) (Ladder D)

The final exit of Rock Tunnel is on 1F at (15, 33), which connects to Route 10 South (Lavender Town).
To reach the exit, we must:
1. Reach Ladder 4 at B1F (3, 31).
2. Take Ladder 4 up to 1F (3, 31).
3. Walk south on Column 3 to Row 33 (or whatever Row 33 is on 1F), east to Column 15, and south to exit at (15, 33).

## Current Position & Phase 1: Return to Starting Chamber (Ladder A)
We are currently at B1F (29, 19). We must return to the Starting Chamber to reach Ladder A at (33, 25).

Step-by-step coordinates for Phase 1:
- Start: B1F (29, 19)
- Go Down 6 steps to (29, 25)
- Go Right 4 steps to (33, 25) (Ladder A)

## Phase 2: Traverse to Ladder 3
- Take Ladder A up to 1F at (37, 3)
- From 1F (37, 3), walk to Ladder C at (17, 11):
  - Go Down 8 steps to (37, 11)
  - Go Left 20 steps to (17, 11)
- Take Ladder C down to B1F at (23, 11)

## Phase 3: Reach Ladder 4 (Exit Ladder)
- From B1F (23, 11), walk to Ladder 4 at (3, 31):
  - Go Left 20 steps along Row 11 to (3, 11)
  - Go Down 20 steps along Column 3 to (3, 31)
- Execute a strict Step-Off-and-On protocol at (3, 31) to ensure the warp triggers:
  - Step onto (3, 31) from (4, 31) or (3, 32).
  - Stop and check if warp triggers. If not, step off to (4, 31).
  - Step back onto (3, 31) and stop to trigger warp.
- Take Ladder 4 up to 1F at (3, 31)

## Phase 4: Final Exit to Route 10 South
- From 1F (3, 31), go to (15, 33):
  - Go Down 2 steps along Column 3 to (3, 33)
- Active Exploration Duration:
  - Started B1F southern backtracking on Turn 21491.
  - Current Turn: 23946.
  - Elapsed Time: 2455 turns.
  - Verified Constraints:
    - 1F (16, 8) is impassable, blocking direct north-south movement on those columns.
    - B1F (3, 31) was tested thoroughly (Turns 23832-23873) by stepping from East, South, and pressing A. Warp did not trigger.
    - B1F (33, 31) was tested thoroughly (Turns 23890-23903) by stepping from West (Left) and performing step-off-and-on. Warp did not trigger.
  - Latest Strategy:
    - Returning to the southwest room on B1F to systematically test all adjacent coordinates (3, 31), (3, 32), (3, 33), etc. with a strict Step-Off-and-On protocol to isolate variables and find where the exit warp triggers.
  - Recent Events:
    - Turn 23890: Traveled back east to the inert (33, 31) coordinate.
    - Turn 23897: Escaped wild Zubat encounter at (33, 31).
    - Turn 23902: Conducted strict step-off-and-on protocol at (33, 31), confirming it is completely inert.
    - Turn 23922: Commenced backtrack west; encountered wild Geodude at (29, 31). Escaped safely.
    - Turn 23928: Reached (29, 31) on overworld; resumed walking west.
    - Turn 23938: Resumed backtracking west; encountered wild Geodude at (19, 31).

## Southwest Warp Systematic Testing Protocol (Turn 23951):
We are standing at (4, 31). We will test three candidate coordinates: (3, 31), (3, 32), and (3, 33) with a strict Step-Off-and-On protocol.
For each coordinate (X, Y):
1. Step onto (X, Y) from (4, Y).
2. If the warp triggers, the test is successful and we warp.
3. If the warp does not trigger, step back onto (4, Y), then step back onto (X, Y) again to re-verify.
4. If it still does not trigger, press A on (X, Y) to test manual interaction.
5. Log the exact result (Warped / Bounded / Inert) and move to the next coordinate.

- Candidate 1: (3, 31)
- Candidate 2: (3, 32)
- Candidate 3: (3, 33)