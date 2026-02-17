Location: Warehouse (2, 1) - At Switch 3.
Objective: Toggle Switch 3 to OFF (Target: 0-1-0).
Current State: 0-1-1 (S1 OFF, S2 ON, S3 ON) -> Changing to 0-1-0.
- S3 is currently ON.
- Action: Turning S3 OFF.
- Goal: Check if State 0-1-0 opens Wall (11, 10) or Gate 1.

Plan:
1. Turn Switch 3 OFF.
2. Check Gate 1 (2, 6).
3. If Gate 1 Open, go check Gate 2/Wall.
4. If Gate 1 Closed, check other gates.

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