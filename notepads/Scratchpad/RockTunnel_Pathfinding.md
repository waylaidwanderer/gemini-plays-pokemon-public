# Rock Tunnel Escape Route to Lavender Town - Master Plan (Turn 24062)

We have discovered that standard Pokemon Red/Blue Rock Tunnel has 4 ladders on B1F/1F:
- Ladder 1: B1F (33, 25) <-> 1F (37, 3) (Ladder A)
- Ladder 2: B1F (27, 3) <-> 1F (5, 3) (Ladder B)
- Ladder 3: B1F (23, 11) <-> 1F (17, 11) (Ladder C)
- Ladder 4: Unverified location, suspected to be in western chambers (Columns 2-13, Rows 10-23) (Ladder D)

The final exit of Rock Tunnel is on 1F at (15, 33), which connects to Route 10 South (Lavender Town).
To reach the exit, we must:
1. Locate the true Ladder 4 (Ladder D) in the unexplored western chambers of B1F.
2. Take Ladder 4 up to 1F.
3. Walk to the exit at 1F (15, 33).

## Current Position & Phase 1: Return to Western Connecting Passage
We are currently at B1F (23, 18). We must walk north to Column 23, Row 11 (Ladder C), and then systematically explore Row 11 going West to verify passability and find the entrance to the western chambers (Columns 2-13).

Step-by-step coordinates:
- Start: B1F (32, 13)
- Go Down 3 steps to (32, 16)
- Go Left 12 steps to (20, 16)
- Go Up 5 steps to (20, 11)
- Go Right 3 steps to (23, 11) (Ladder C)
- Go Left systematically along Row 11 to (3, 11) to locate the true Ladder D.

## Phase 4: Final Exit to Route 10 South
- Take Ladder 4 up to 1F and exit to Route 10 South.

  - Active Exploration Duration:
    - Started B1F southern backtracking on Turn 21491.
    - Current Turn: 24121.
    - Elapsed Time: 2630 turns.
  - Verified Constraints:
    - 1F (16, 8) is impassable, blocking direct north-south movement on those columns.
    - B1F (3, 31) was tested thoroughly (Turns 23832-23873) by stepping from East, South, and pressing A. Warp did not trigger.
    - B1F (33, 31) was tested thoroughly (Turns 23890-23903) by stepping from West (Left) and performing step-off-and-on. Warp did not trigger.
  - Latest Strategy:
    - Southwest corner room coordinates (3, 31), (3, 32), and (3, 33) are fully proven inert. There is no physical ladder here.
    - True Ladder D must be in the unexplored western chambers (Rows 10-23, Columns 2-13). We will head to Ladder C (23, 11) and systematically test the passability of the Row 11 corridor to find the entry.
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
    - Turn 24022: Attempted to move Up to (15, 28) from (15, 33). Aborted at step 3 due to wild Geodude encounter at (15, 30). Escaped safely.
    - Turn 24035: Reached (15, 24) on overworld.
    - Turn 24042: Moved Right 5 steps along Row 24 to reach (20, 24).
    - Turn 24049: Attempted to walk Up 4 steps along Column 20. Collided with the defeated Pokémaniac sprite at (20, 21), halting at (20, 22).
    - Turn 24052: Stepped Right to (21, 22) to bypass the Pokémaniac sprite.
    - Turn 24054: Walked Up 4 steps along Column 21 to reach (21, 18).
    - Turn 24057: Walked Right 2 steps along Row 18 to reach (23, 18).
    - Turn 24059: Attempted to walk Up 2 steps to (23, 16). Aborted at step 1 due to wild Geodude encounter at (23, 18).

## Southwest Warp Systematic Testing Protocol (Completed Turn 24006):
All candidate coordinates tested and confirmed inert:
- Candidate 1: (3, 31) - Inert (Tested Turn 23958)
- Candidate 2: (3, 32) - Inert (Tested Turn 23983)
- Candidate 3: (3, 33) - Inert (Tested Turn 23993)
- Turn 24069: Escaped Geodude battle. Walked Up 2 steps along Column 23 to reach (23, 16).
- Turn 24070: Walked Right 5 steps along Row 16. Aborted at step 1 due to wild Zubat encounter at (24, 16). Escaped safely.
- Turn 24074: Walked Right 5 steps along Row 16 to reach (29, 16).
- Turn 24076: Walked Right 3 steps to reach the eastern bypass connector at (32, 16).
- Turn 24077: Walked Up 3 steps along Column 32 to reach (32, 13).
- Turn 24081: Walked Down 3 steps along Column 32 to return to (32, 16).
- Turn 24084: Walked Left 6 steps along Row 16 to reach (26, 16).
- Turn 24086: Walked Left 6 steps along Row 16. Aborted at step 4 due to wild Machop encounter at (22, 16).