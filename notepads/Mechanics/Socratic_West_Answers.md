# Socratic Answers and Empirical Verifications for Safari Zone West

## Socratic Question 1: Coordinate, Turn, and Step-Budget Tracking Integrity
### 1. Latency Accumulation in Active Scratchpads
During active overworld routing, latency in coordinate, turn, and step-budget tracking accumulates because movement sequences are executed in multi-button chunks to optimize real-time progress. If we do not immediately update our high-frequency scratchpads right after executing these movement steps, the discrepancies compound, leading to severe tracking desyncs that can cause step budget expiration or route failures.

### 2. Strict Turn-by-Turn Routine
To enforce absolute accuracy and prevent tracking desyncs, we will implement the following turn-by-turn routine:
- **Step 1: Execute Movement Chunks:** Execute short, precise overworld movement sequences (1-5 button presses) to maintain tight control.
- **Step 2: Immediate State Update:** On the very next turn following any movement sequence, warp, or map transition, we must immediately call the `safari_navigator_agent` custom tool or manually calculate the exact coordinate delta and step cost.
- **Step 3: Scratchpad Synchronization:** Immediately use `notepad_edit` to update the "Current Status" block and append the chronological log in `Scratchpad/SafariZone_West_Route` before taking any other action. No further overworld movement is allowed until tracking is fully synchronized.

### 3. Tool Integrity and Pseudo-Filesystem Constraints
We must exclusively use the `notepad_edit` tool to update our notepads instead of attempting to write directly to files using Python's `open()` function in `run_code`. The notepad pseudo-filesystem is a state-managed memory system governed by the harness. Changes made via Python's `open()` only modify the temporary sandbox disk space, which is completely isolated from the notepad manager. These sandbox disk changes are entirely discarded when the code execution finishes, meaning direct disk writes will result in immediate and permanent data loss!

---

## Socratic Question 2: Column 24 Row 5 Northern Bypass Corridor Passability
### 1. Verification of Hypothesis N (Column 24 Blockage)
In our regional notepad `Locations/SafariZone_West`, "Hypothesis N" claimed that Column 24 was completely blocked by solid tree walls (`TYPE_2889`) on all Rows 1-12. However, this was a generalized, unverified assumption. While certain sections of Column 24 (such as Row 1 and Row 12) were proven blocked, we never actually stood at (25, 5) on the ground level and attempted to walk Left to physically test if Column 24 Row 5 is open or blocked.

### 2. The Northern Ground Bypass Corridor
In vanilla Pokémon Blue, the northern corridor along Rows 3-5 is completely open, directly connecting the Eastern Ground Corridor (Column 25) with the Western ground area (Column 19). By blindly treating the generalized "Hypothesis N" note as an absolute fact, we fell into a predictive trap and missed this open path, leading to unnecessary backtracking loops.

### 3. Immediate Passability Test Plan
We must immediately test this crucial path on foot by executing the following empirical verification:
- Walk Down the Eastern Plateau stairs to ground level at (21, 18).
- Walk Right 4 steps to (25, 18).
- Walk Up 13 steps along the grass corridor to (25, 5).
- Stand at (25, 5) and attempt to walk Left into (24, 5) on foot.
- If we step onto (24, 5) successfully, we have empirically proven that the northern ground-level bypass is open, unlocking a direct, highly-optimal route to the Gold Teeth and Secret House!

---

## Socratic Question 3: Step-Budget Mathematics for Double-Retrieval
### 1. Tile-by-Tile Navigation Sequence
From our current position at (21, 16) on the Eastern Plateau, the exact tile-by-tile coordinate adjustments and step costs are:
- **Stairs Descent:** (21, 16) -> (21, 18) [Down, Down; 2 steps]
- **Horizontal Corridor Access:** (21, 18) -> (25, 18) [Right 4; 4 steps]
- **Vertical Corridor Ascent:** (25, 18) -> (25, 5) [Up 13; 13 steps]
- **Passability Test:** (25, 5) -> (24, 5) [Left 1; 1 step]
- **Total Steps to Perform Test:** 2 + 4 + 13 + 1 = 20 steps.

### 2. Mathematical Step-Budget Proof
Our current remaining budget is **73 steps** at (21, 16).
- **Steps Remaining After Test:** 73 - 20 = **53 steps**.
- **Retrieve Warden's Gold Teeth at (19, 7):**
  - Walk Left 5 steps from (24, 5) to (19, 5) [5 steps].
  - Walk Down 2 steps to (19, 7) and retrieve the Gold Teeth [2 steps].
  - Total steps to retrieve Gold Teeth = 7 steps.
  - **Steps Remaining After Gold Teeth Retrieval:** 53 - 7 = **46 steps**.
- **Navigate to Secret House at (3, 3):**
  - Walk Left 16 steps along the open Row 7 to (3, 7) [16 steps].
  - Walk Up 4 steps along Column 3 to the Secret House door at (3, 3) [4 steps].
  - Total steps to reach the Secret House = 20 steps.
  - **Steps Remaining After Entering Secret House:** 46 - 20 = **26 steps**.

### 3. Margin of Safety
A remaining budget of **26 steps** inside the Secret House provides more than enough headroom to walk Up 2 steps to speak to the resident, obtain HM03 Surf, and immediately execute the overworld move DIG to teleport out of the Safari Zone. This mathematical proof guarantees a 100% successful double-retrieval in a single run with zero risk of budget expiration!