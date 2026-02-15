# Underground Warehouse
- **Goal:** Rescue Director.
- **Puzzle Solved:** Switch Combination [1,1,0] (Sw1 ON, Sw2 ON, Sw3 OFF).
  - Opens Gate 1 (2,6), Gate 3 (16,6).
  - Gate 2 (10,6) is CLOSED.
  - Traps at (2,8) and (3,8) are disabled.
- **Traps Identified:**
  - (16,8), (12,9), (10,9).
- **Trap Check:** (16,8) is ACTIVE (Trap). Warps to (16,5).
- **Immediate Plan:**
  1. Navigate to Gate 1 (2,6).
  2. Bypass Silver by walking South to Row 9.
  3. Navigate to Duncan (9,12) and East side.
- **Warp Connection:** (23,3) in Warehouse (3_54) leads to (22,27) in Underground Path (3_53).
- **Current Location:** Small room in 3_53, blocked by Rocket Grunt at (22,24).
- **RESET ALERT:** Switches reset upon re-entering. Current State: likely [0,0,0].
- **New Plan:** Turn Sw2 ON -> Check Gate 2 -> Reach Sw1 -> Turn Sw1 ON -> Open Gate 1 & 3.
- Switches RESET. Current State: likely [1,1,1] (All ON).
  - Evidence: Sw2 found ON. Gate 1 closed.
- **New Plan:**
  1. Leave Sw2 ON (Done).
  2. Go to Sw1 (16,1). Check if ON. Leave ON.
  3. Go to Sw3 (2,1). Turn OFF.
  4. Verify Gate 1 (2,6) opens.
- Gate 1 (2,6) confirmed OPEN.
- Blocked at (12,9) [Wall] and (11,10) [Wall].
- Tile Change Detected at (16,10)/(16,11) [Opened!].
- New Route: Backtrack through Gate 1 -> Row 5 -> Gate 3 (16,6) -> South to Duncan.
- Toggled Switch 2 OFF. State: [0, 0, 0] (All OFF).
- Checking Gate 2 (10,6).
- If Gate 2 is CLOSED, check Gate 3 (16,6).
- If both CLOSED, will try [0, 0, 1] (Toggle Sw3 ON).