# Underground Warehouse
- **Goal:** Rescue Director.
- **Hypothesis:** Order matters ("Switch on the end first").
- **Tested Sequences (Order Matters Hypothesis):**
  - `3 -> 2 -> 1`: Gate 3 CLOSED.
  - `1 -> 2 -> 3`: Gate 1 & 2 & 3 CLOSED.
  - `[1, 0, 1]`: Gate 3 CLOSED.
- **Confirmed States:**
  - `[1, 1, 0]`: Gate 1 OPEN (Re-verifying).
  - `[0, 1, 0]`: Gate 2 CLOSED (Confirmed).
- **Current Status:**
  - State: [0, 0, 1] (Sw1 OFF, Sw2 OFF, Sw3 ON).
  - Action: Turn Sw3 OFF -> [0, 0, 0].
  - Next: Go to Sw1.
- **Hazards:**
  - Trap suspected on Row 3 (between x=3 and x=8). Warps to (8, 2).
  - Row 4 confirmed safe in past turns.
- **Immediate Plan:**
  1. Move via Row 4 to Switch 3 (2, 1).
  2. Turn Switch 3 OFF.
  3. Verify State [0, 0, 0].
  4. Test "Left End First" (Sw3 -> Sw2 -> Sw1?).
- **Plan:**
  1. Go to Gate 1 (2, 6).
  2. Check if open.
  3. Enter and traverse Row 9 to check wall at (11, 10).
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
  - [0, 1, 0]: Gate 2 CLOSED.
  - [1, 0, 0]: Gate 3 CLOSED. Gate 1 CLOSED.
  - [0, 0, 0]: All Closed.
  - [0, 1, 1]: Gate 1, 2, & 3 CLOSED.
  - [0, 0, 1]: Gate 2 CLOSED. Gate 3 CLOSED.
  - [1, 0, 1]: Gate 2 & 3 CLOSED.
- **Reflection (Turn 45388):**
  - Progress: Systematically tested `[1,1,0]` (Gate 1) and `[1,0,1]` (Gate 3). Both led to dead ends or loops.
  - Current Goal: Test `[0,1,0]` (Switch 2 ON only) to open Gate 2.
  - Hypothesis: `[0,1,0]` will open Gate 2 and disable the trap at (10,9).
  - Map Hygiene: Cleaned up conflicting markers on Switch 3.
  - Mental Check: Switch 3 is confirmed OFF. Switch 1 is assumed OFF. Heading to Switch 2.
- **Correction (Turn 45392):**
  - Switch 1 interaction was incomplete. It is likely still ON.
  - Current Real State: [1, 0, 0] (Sw1 ON, Sw2 OFF, Sw3 OFF).
- **Revised Plan:**
  1. Turn Switch 2 ON (Interacting now).
  2. Go to Switch 1. Verify/Turn OFF -> State [0, 1, 0].
  3. Check Gate 2 (10, 6).
- Visual Confirm: Gate 3 (16, 6) is CLOSED (Type 2889).
- Visual Confirm: Gate 2 (10, 6) is CLOSED (Type 2889).
- Checking Switch 1 Status...
- Visual Confirm: Gate 3 (16, 6) is CLOSED (Type 2889) with State [1, 0, 0].
- Plan: Change state to [1, 0, 1] (Sw1 ON, Sw2 OFF, Sw3 ON).
  - Move to Switch 3 (2, 1). Turn ON.
  - Check Gate 3.
- Movement: Navigating to Switch 3 (2, 1) from (10, 4).
- Testing Trap at (16, 8) with Sw3 ON...
- Exploring South of Gate 3:
  - (16, 9) is accessible.
  - checking (16, 10) (Wall?).
  - checking West path towards (12, 9).
- Dead End Check:
  - (12, 9) is Wall.
  - (13, 10) is Wall.
  - Checking (16, 10) and (17, 9).
- Gate 3 with [1, 0, 1] leads to a small room (Rows 6-9, Cols 13-17).
  - No obvious exit found yet.
  - Investigating (16, 10) for hidden door.
- Correction: I only checked West from (16, 9). I need to check East towards the Grunt at (19, 12).
- Plan: Go South to (16, 9), then East.
- Encountered Rocket Grunt at (17, 2). He seems to just loop dialogue without battling. Ignoring him.
- Plan: Turn Switch 1 (16, 1) OFF.
- Then: Check Gate 2 (10, 6).
- Checking (11, 10) and (12, 9) for hidden paths.
- Hypothesis: [0, 1, 1] might keep Gate 2 open AND open the wall at (11, 10).
- **Movement:** Moving to Switch 2 (10, 1) via Row 5 to avoid Grunts.
- **Next Action:** Turn Switch 2 OFF.
- **Current Status:**
  - State: [0, 0, 1] (Sw1 OFF, Sw2 OFF, Sw3 ON).
  - Next Action: Turn Switch 3 OFF -> [0, 0, 0].
  - Plan: Test Sequence Sw3 -> Sw2 -> Sw1.
Turn 45785: Manually moving to Switch 3 (2, 2) to turn OFF.
Turn 45786: Turned Switch 3 OFF. State: [0, 0, 0] (All OFF). Starting Sequence Test: 3 -> 2 -> 1.
Turn 45787: Confirmed Switch 3 OFF. Reset Complete: [0, 0, 0].
Turn 45788: Sequence Step 1: Turned Switch 3 ON. State: [0, 0, 1]. Moving to Switch 2.
Turn 45791: Sequence Step 2: Moving to Switch 2 to turn ON.
Turn 45792: Sequence Step 2: Turned Switch 2 ON. State: [0, 1, 1]. Moving to Switch 1.
Turn 45793: Confirmed Switch 2 ON. Moving to Switch 1.
Turn 45795: Sequence Step 3: Turned Switch 1 ON. State: [1, 1, 1]. Order: 3->2->1. Checking Gate 3.
Turn 45796: Kept Switch 1 ON. Checking Gate 3.
Turn 45797: Gate 3 CLOSED. Sequence 3->2->1 failed. Turning Switch 1 OFF to reset. Next Plan: 1->2->3.
Turn 45797: Turned Switch 1 OFF. State: [0, 1, 1]. Moving to Switch 2 to turn OFF.
Turn 45799: Turned Switch 2 OFF. State: [0, 0, 1]. Moving to Switch 3 to turn OFF.
Turn 45800: Confirmed Switch 2 OFF. Moving to Switch 3.
Turn 45802: Continuing to Switch 3.
Turn 45803: Arriving at Switch 3 (2, 2).
Turn 45805: Confirmed Switch 3 OFF. Reset Complete [0, 0, 0]. Moving to Switch 1 to start Sequence 1->2->3.
Turn 45806: Correction - Likely cancelled Switch 3 toggle with 'B'. Returning to Switch 3 (2, 2) to verify and turn OFF properly.
Turn 45807: Moving to (2, 2) to inspect Switch 3.
Turn 45808: Interacting with Switch 3 to turn OFF. State -> [0, 0, 0].
Turn 45809: Confirmed Switch 3 OFF. Reset Complete. Moving to Switch 1.
Turn 45813: Moving to Switch 1 (16, 1). Sequence Plan: 1 -> 2 -> 3.
Turn 45814: Sequence Step 1: Turned Switch 1 ON. State: [1, 0, 0]. Moving to Switch 2.
Turn 45815: Confirmed Switch 1 ON. Moving to Switch 2.
Turn 45817: Moving to Switch 2 to turn ON (Step 2 of Sequence 1->2->3).
Turn 45818: Arriving at Switch 2 (10, 2) to turn ON.
Turn 45819: Sequence Step 2: Turned Switch 2 ON. State: [1, 1, 0]. Moving to Switch 3.
Turn 45820: Confirmed Switch 2 ON. State: [1, 1, 0]. Moving to Switch 3.
Turn 45821: Moving to Switch 3 to turn ON (Step 3/3).
Turn 45822: Arriving at Switch 3 (2, 2).
Turn 45823: Moving to Switch 3 (2, 2) from (6, 4).
Turn 45824: Moving around grunt to Switch 3 (2, 2).
Turn 45825: Sequence Step 3: Turned Switch 3 ON. State: [1, 1, 1]. Order: 1->2->3. Checking Gate 1.
Turn 45826: Confirmed Switch 3 ON. Sequence 1->2->3 Complete. Checking Gate 1.
Turn 45835: Turned Switch 2 OFF. State: [1, 0, 1]. Checking Gate 3.
Turn 45839: Turned Switch 2 ON. State: [1, 1, 1]. Moving to Switch 3 to turn OFF -> Target [1, 1, 0].
Turn 45843: Turned Switch 2 ON. State: [1, 1, 1] (assuming Sw3 is ON). Heading to Switch 3 to turn OFF.
Turn 45844: Turned Switch 2 ON. State: [1, 1, 0]. Checking Gate 1.