# Rock Tunnel Escape Route to Lavender Town - Master Plan (Turn 23792)

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
  - Current Turn: 23886.
  - Elapsed Time: 2395 turns.
  - Turn 23683: Logged arrival at Rock Tunnel 1F (37, 3) from Ladder A.
  - Turn 23706: Visually mapped the western corridor on 1F, proving that TYPE_2770 at (16, 8) has solid, impassable collision. Therefore, Columns 14-17 are completely blocked at Rows 8 and 9, meaning there is no way to walk directly Down from the upper corridor (Rows 4-7) to the middle area (Rows 10-11) on these columns.
  - Turn 23725: Encountered a wild Zubat at (20, 7) during the backtrack sequence. Escaped safely on Turn 23729.
  - Turn 23734: Commenced backtrack sequence from (20, 7) to Ladder A at (37, 3).
  - Turn 23743: Successfully reached 1F (37, 3) (Ladder A).
  - Turn 23752: Descended back to B1F starting chamber at (33, 25).
  - Turn 23758: Walked Down 7 steps to B1F (33, 32) in the Southern Corridor.
  - Turn 23764: Encountered a wild Machop at (30, 32). Escaped safely on Turn 23767.
  - Turn 23774: Walked Left 3 steps from (30, 32) to (27, 32).
  - Turn 23775: Encountered a wild Onix at (27, 32). Escaped safely on Turn 23777.
  - Turn 23778: Standing at (27, 32). Resumed western corridor detour.
  - Turn 23780: Bypassed Sofia by walking Left 3 to (24, 32) and Up 1 to (24, 31).
  - Turn 23782: Walked Left 10 steps to (14, 31) in the Southern Corridor.
  - Turn 23784: Walked Left 8 steps to (6, 31) in the Southern Corridor.
  - Turn 23795: Standing at B1F (6, 31). Preparing to walk Left 2 steps to (4, 31) adjacent to the exit ladder, and then execute the Step-Off-and-On protocol to enter Lavender Town.
  - B1F Exit Ladder (3, 31) Step-Off-and-On Testing Protocol:
    1. Stand at (4, 31).
    2. Step Left onto (3, 31).
    3. If the warp to 1F does not trigger instantly, step Right back to (4, 31).
    4. Step Left back onto (3, 31) to re-verify and trigger the warp.
- Turn 23832: Stepped Left onto B1F (3, 31).
- Turn 23834: Escaped wild Geodude battle.
- Turn 23835: Cleared the textbox.
- Turn 23836: Stepped off to (4, 31).
- Turn 23837: Stepped back onto (3, 31).
- Turn 23871-23872: Tested stepping onto (3, 31) from (3, 32) (South) after moving Down, Down, Up, Up. Warp still did not trigger, confirming that (3, 31) is NOT an active warp on B1F.
- Turn 23873: Pressed A on (3, 31) to test manual interaction. Result was 0 effect, no text or menu appeared.
- Turn 23886: Concluded that (3, 31) is completely inert on Rock Tunnel B1F. This matches the standard Pokered game structure, which contains only 4 warps on B1F: (33, 25) (Ladder A), (27, 3) (Ladder B), (23, 11) (Ladder C), and (33, 31) (Ladder D). The previous assumption that a fifth ladder existed at (3, 31) was a coordinate misconception. we must navigate back to the east side of B1F and exit via the true Ladder D at (33, 31).