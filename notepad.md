Location: Warehouse (2, 1) - At Switch 3.
Objective: Toggle Switch 3 to ON (Target: 0-1-1).
Current State: 0-1-0 (S1 OFF, S2 ON, S3 OFF) -> Changing to 0-1-1.
- CRITICAL CORRECTION: Switch 3 was found OFF.
- This means my previous test (Gate 2 Closed) was done in State 0-1-0.
- State 0-1-0 is a DEAD END (Gate 2 Closed, Gate 3 Closed).
- Now testing State 0-1-1 (S1 OFF, S2 ON, S3 ON).

Plan:
1. Confirm turning S3 ON.
2. Check Gate 1 (2, 6).
3. Check Gate 2 (10, 6) and Wall (11, 10).

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