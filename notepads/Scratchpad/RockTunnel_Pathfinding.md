# Rock Tunnel Escape Route to Lavender Town - Master Plan (Turn 24006)

We have discovered that standard Pokemon Red/Blue Rock Tunnel has 4 ladders on B1F/1F:
- Ladder 1: B1F (33, 25) <-> 1F (37, 3) (Ladder A)
- Ladder 2: B1F (27, 3) <-> 1F (5, 3) (Ladder B)
- Ladder 3: B1F (23, 11) <-> 1F (17, 11) (Ladder C)
- Ladder 4: B1F (3, 13) or similar west-middle coordinate <-> 1F (3, 13) or similar (Ladder D)

The final exit of Rock Tunnel is on 1F at (15, 33), which connects to Route 10 South (Lavender Town).
To reach the exit, we must:
1. Locate the true Ladder 4 (Ladder D) in the unexplored western chambers of B1F (likely around Column 3, Row 13).
2. Take Ladder 4 up to 1F.
3. Walk to the exit at 1F (15, 33).

## Current Position & Phase 1: Return to Western Connecting Passage
We are currently at B1F (3, 33) in the southwest corner. We must walk east along the southern corridor to Column 15, then move north through the Western Connecting Passage (Rows 24-29) to explore the western region (Columns 2-13, Rows 10-23).

Step-by-step coordinates:
- Start: B1F (3, 33)
- Go Right 12 steps to (15, 33)
- Go Up 9 steps to (15, 24)
- Go Left to explore the western chamber (Columns 2-13) to find the true Ladder D.

## Phase 4: Final Exit to Route 10 South
- Take Ladder 4 up to 1F and exit to Route 10 South.

- Active Exploration Duration:
  - Started B1F southern backtracking on Turn 21491.
  - Current Turn: 24006.
  - Elapsed Time: 2515 turns.
  - Verified Constraints:
    - 1F (16, 8) is impassable, blocking direct north-south movement on those columns.
    - B1F (3, 31) was tested thoroughly (Turns 23832-23873) by stepping from East, South, and pressing A. Warp did not trigger.
    - B1F (33, 31) was tested thoroughly (Turns 23890-23903) by stepping from West (Left) and performing step-off-and-on. Warp did not trigger.
  - Latest Strategy:
    - Southwest corner room coordinates (3, 31), (3, 32), and (3, 33) are fully proven inert. There is no physical ladder here.
    - True Ladder D must be in the unexplored western chambers (Rows 10-23, Columns 2-13).
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

## Southwest Warp Systematic Testing Protocol (Completed Turn 24006):
All candidate coordinates tested and confirmed inert:
- Candidate 1: (3, 31) - Inert (Tested Turn 23958)
- Candidate 2: (3, 32) - Inert (Tested Turn 23983)
- Candidate 3: (3, 33) - Inert (Tested Turn 23993)