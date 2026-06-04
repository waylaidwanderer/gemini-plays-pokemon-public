# Safari Zone West Exploration Scratchpad (Run 24 Planning & Execution)
- **Objective**: Retrieve Gold Teeth and HM03 Surf from the Secret House in Safari Zone West (Map 0_219).
- **Current Status**: Standing at (3, 4) inside Safari Zone Gatehouse (Map 0_156), facing LEFT.
- **Next Step**: Speak to the Gatekeeper at (1, 4), pay ¥500, and enter Safari Zone Center to start Run 24.

## Socratic Question Answers (Turn 55568 Update)

### Socratic Question 1: Exact Overworld Route in Safari Zone Center to Safari Zone East
- Spawn at (15, 25) in Safari Zone Center (Map 0_220).
- Exact horizontal/vertical route to reach eastern transition:
  1. Walk Left 1 step to (14, 25) [1 step] (align with the open gate).
  2. Walk Up 1 step to (14, 24) [1 step] (cross the open gate).
  3. Walk Up 2 steps to (14, 22) [2 steps].
  4. Walk Right 15 steps along Row 22 to (29, 22) [15 steps] (transitions to (0, 22) in Safari Zone East).
  - Total step cost: 19 steps.

### Socratic Question 2: Strict Routine for Map Transitions and Step-Budget Synchronization
- To guarantee that we always operate with 100% accurate, live step budget and coordinates:
  1. Immediately upon map transition (the very first turn inside the new map), call `safari_navigator_agent` to compute the step delta.
  2. Immediately call `notepad_edit` to synchronize the active scratchpad's status block (turn, position, step budget) with the empirical reality of the new map.
  3. Call `update_objectives` to synchronize navigation goals.
  4. Only proceed with further overworld movement after these files are updated.

### Socratic Question 3: Standard File I/O vs. Official Notepad Tools
- **Why standard open() fails**: Standard Python file operations in `run_code` read and write stale, static cached files from the workspace disk. They do NOT interact with the live, in-memory updates managed dynamically by the harness. Using file I/O causes severe temporal and spatial reasoning distortions because we read outdated data.
- **Enforced Principle**: We will rely EXCLUSIVELY on the official harness tools (`read_notepad`, `search_notepads`, and `notepad_edit`) for all notepad reads, searches, and writes. Standard file I/O operations (like open()) are completely banned in our raw Python blocks.

### Socratic Question 3: Standard File I/O vs. Official Notepad Tools
- **Why standard open() fails**: Standard Python file operations in `run_code` read and write stale, static cached files from the workspace disk. They do NOT interact with the live, in-memory updates managed dynamically by the harness. Using file I/O causes severe temporal and spatial reasoning distortions because we read outdated data.
- **Enforced Principle**: We will rely EXCLUSIVELY on the official harness tools (`read_notepad`, `search_notepads`, and `notepad_edit`) for all notepad reads, searches, and writes. Standard file I/O operations (like open()) are completely banned in our raw Python blocks.

## Run 24 Route Plan (Fuchsia City to Secret House)
1. Walk from (24, 28) to (18, 20) via Column 24 and Row 20.
2. Cut the first bush at (18, 19).
3. Walk to (16, 12) and cut the second bush at (16, 11).
4. Enter the Safari Zone Gatehouse at (18, 3).
5. Start Run 24 with a fresh 500-step budget.
6. Traverse directly to the Secret House at (3, 3) in Safari Zone West (~220 steps).
7. Retrieve HM03 Surf!