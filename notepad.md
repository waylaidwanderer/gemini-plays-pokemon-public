Location: Warehouse (7, 5) - Moving to Switch 3.
Objective: Enable State 1-1-1 (All ON).
Current State: 1-0-0 (S1 ON, S2 OFF, S3 OFF).

Switch Logic Summary (Hypothesis):
- S1 ON: Opens Gate 3 (16, 6).
- S2 OFF: Opens Gate 2 (10, 6) & Disables Row 4 Traps.
- S3 ON: Opens Gate 1 (2, 6).
- Wall (11, 10): Logic unknown. Maybe requires specific combo (e.g., 1-1-1 or 0-1-0)?

Tested States & Wall Status:
- 0-0-0: Wall Closed (All Gates Closed).
- 0-0-1: Wall Closed (G1, G2 Open).
- 0-1-1: Wall Closed (G1 Open).
- 1-0-0: Wall Closed (G3 Open).
- 1-1-0: Wall Closed (G3 Open).
- 1-0-1: Wall Closed (G1, G2, G3 Open - Verified previously).

Missing/Untested States for Wall:
- 1-1-1: (All ON). To be tested now.
- 0-1-0: (S2 ON only). Was briefly tested, seemed blocked?

Plan:
1. Move to Switch 3 (2, 1).
2. Turn Switch 3 ON (State -> 1-0-1).
3. Move to Switch 2 (10, 1).
4. Turn Switch 2 ON (State -> 1-1-1).
5. Use code to check Wall (11, 10).

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