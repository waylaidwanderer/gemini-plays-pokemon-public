# Warehouse Switch Puzzle - Recovery
- **Target State:** [Sw3 OFF, Sw2 ON, Sw1 ON].
- **Current Task:** Verification Tour.
- **Switch 2:** Verified ON (Turn 42189).
- **Next:** Verify Switch 3 (Left), then Switch 1 (Right).

## Plan
1. Navigate to Switch 3 (2, 2) using BFS.
2. Verify/Set Sw3 to **OFF**.
3. Navigate to Switch 1 (16, 2).
4. Verify/Set Sw1 to **ON**.
5. Go to (12, 8) and execute route.