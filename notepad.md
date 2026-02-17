Location: Warehouse (11, 5) - Gate 2 Closed.
Objective: Toggle Switch 3 to OFF (Target: 0-1-0).
Current State: 0-1-1 (S1 OFF, S2 ON, S3 ON).
- Verified: Gate 2 (10, 6) is CLOSED.
- Verified: Secret Door (11, 6) is CLOSED.
- Inferred: Gate 3 (16, 6) is CLOSED (S1 OFF).
- Conclusion: State 0-1-1 blocks the middle path.

Plan:
1. Move to Switch 3 (2, 1).
   - Route: Up to Row 2, then Left.
   - Note: (10, 4) might be a warp. If so, it takes me closer to S3 anyway.
2. Toggle Switch 3 OFF (State becomes 0-1-0).
3. Check Gate 1 and Gate 2/Wall.
4. If 0-1-0 fails, maybe try 1-1-0 (S1 ON, S2 ON, S3 OFF).

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