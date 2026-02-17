Location: Warehouse (10, 2) - At Switch 2.
Objective: Enable State 1-1-1 (All ON).
Current State: 1-1-0 (S1 ON, S2 ON, S3 OFF).
- Verified: Gate 3 OPEN, Wall CLOSED in 1-1-0.
- Previous move to S3 apparently failed or reset. Retrying.

Plan:
1. Move to Switch 3 (2, 1).
   - Path: (10, 2) -> (10, 5) -> (2, 5) -> (2, 1).
   - Taking Row 5 to avoid potential traps on Row 4.
2. Turn Switch 3 ON (State -> 1-1-1).
3. Use code to check Gate 3 and Wall (11, 10).

Switch Locations:
- S3: (2, 1)
- S2: (10, 1)
- S1: (16, 1)

History:
- 1-0-0: G1 Open, G3 Open, Wall Closed.
- 0-1-0: Secret Door Open.
- X-1-1: Gate 1 Open, Secret Door Open (from summary).
Anomaly: Attempted to walk East along Row 2 to (16, 2) but was warped back to (2, 2). Possible hidden Trap Warp near (16, 2) or triggered by Grunt at (17, 2).
Action: Checking Gate 1 first.
Observation: In 1-0-1, Wall (11, 10) appears to be TYPE_2889 (Closed).
Action: Walking South to confirm blockage and test for traps on Row 9.
Anomaly: Warped to (6, 4) during navigation to Switch 3.
- Path taken: (10, 2) -> (4, 2) -> (4, 4) -> (2, 4) -> (2, 2).
- Suspect trap at (4, 4), (3, 4), (2, 4), or (2, 2) in State 0-0-1.
Action: Retrying access to Switch 3 from (6, 4).
Plan Update:
- Trapped in NW corner (0-0-0). Gate 1 Closed.
- Hypothesis: There is a Trap Warp in this room (likely Row 4) that allows escape while keeping S3 OFF.
- Action: Trigger the trap at (2, 4) or (3, 4) to warp out.
- Goal: Explore map in State 0-0-0 (S1 OFF, S2 OFF, S3 OFF).