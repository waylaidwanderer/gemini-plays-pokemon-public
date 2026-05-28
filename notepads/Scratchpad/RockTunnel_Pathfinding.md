# Rock Tunnel Escape Route to Lavender Town - Master Plan (Turn 23666)

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
  - Go Right 12 steps along Row 33 to (15, 33)
  - Go Down 1 step to exit!

## Active Exploration Duration:
- Started B1F southern backtracking on Turn 21491.
- Current Turn: 23667.
- Elapsed Time: 2176 turns.