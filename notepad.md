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
- Toggled Switch 1 ON. State: [1, 0, 0].
- Gate 2 (10,6) confirmed CLOSED with [1,0,0].
- AUDIT COMPLETE: Sw2 is ON.
- Confirmed State: [1, 1, 1] (All ON).
- Sw1 found ON. Kept it ON.
- Current State: [1, 1, 0] (Sw3 turned OFF).
- Gate 1 (2,6) confirmed OPEN.
- Wall at x=6 blocks East. Gate 1 area appears to be a dead end with Silver.
- Action: Talk to Silver (4,8).
- Then: Backtrack North through Gate 1 to Row 5, head East to Gate 3 (16,6).
- Spoke to Silver at (4,8). He said "There's nothing down there." and did not battle.
- Gate 1 (2,6) confirmed OPEN with [1, 1, 0].
- Gate (2,10) confirmed CLOSED (Dead End).
- Plan: Go to Switch 1 (16,1). Turn OFF.
- Goal State: [0, 1, 0] (Sw1 OFF, Sw2 ON, Sw3 OFF).
- Hypothesis: Sw1 OFF opens Gate 3.
- Stuck in menu at Switch 3.
- Action: Press B to cancel (Keep Sw3 ON).
- Move to Switch 2 (10,1).
- Plan: Turn Sw2 OFF -> Go to Sw1 -> Turn Sw1 ON.
- Target: [1, 0, 1].
- Gate 2 (10,6) reported OPEN in past logs with this state.
- **Puzzle Update:** State [0, 1, 1] Failed.
  - Gate 2 (10, 6) CLOSED.
  - Gate 3 (16, 6) CLOSED.
  - (12, 8) OPEN (Unreachable).
- **Tested Combinations (Sw1, Sw2, Sw3):**
  - [1, 1, 0]: Gate 1 OPEN, Gate 3 CLOSED. (Trap 2,8 disabled).
  - [0, 1, 0]: Gate 2 OPEN, Gate 3 CLOSED.
  - [1, 0, 0]: Gate 3 CLOSED. Gate 1 CLOSED.
  - [0, 0, 0]: All Closed.
  - [0, 1, 1]: Gate 3 CLOSED.
  - [0, 0, 1]: Gate 3 CLOSED.
  - [1, 0, 1]: Gate 3 OPEN. Gate 1 & 2 CLOSED. (Current).
- **Current Status:**
  - Switches: [1, 0, 1] (Sw1 ON, Sw2 OFF, Sw3 ON).
  - Gate 3 (16, 6): OPEN!
- **Plan:**
  1. Enter Gate 3 (16, 6).
  2. Cross (16, 8). **Hypothesis:** Trap is disabled by [1, 0, 1].
  3. Explore south.
- Visual Confirm: Gate 3 (16, 6) is CLOSED (Type 2889).
- Visual Confirm: Gate 2 (10, 6) is CLOSED (Type 2889).
- Checking Switch 1 Status...
- Visual Confirm: Gate 3 (16, 6) is CLOSED (Type 2889) with State [1, 0, 0].
- Plan: Change state to [1, 0, 1] (Sw1 ON, Sw2 OFF, Sw3 ON).
  - Move to Switch 3 (2, 1). Turn ON.
  - Check Gate 3.
- Movement: Navigating to Switch 3 (2, 1) from (10, 4).
- Testing Trap at (16, 8) with Sw3 ON...